from flask import request, session, make_response, jsonify, abort
from flask_restful import Resource

from models import User, Game
from config import app, db, api
from chess.chess_logic import Chess
from chess.pgn_to_fen import pgn_to_fen

class Users(Resource):
    def get(self):
        return make_response(
            [u.to_dict() for u in User.query.all()],
            200
        )
api.add_resource(Users, '/users')

class UserById(Resource):
    def get(self, id):
        try:
            user = User.query.filter_by(id=id).first()
            return make_response(user.to_dict(), 200)
        except Exception as e:
            return make_response({'error': str(e)}, 400)
api.add_resource(UserById, '/users/<int:id>')

class Games(Resource):
    def get(self):
        return make_response(
            [g.to_dict() for g in Game.query.all()],
            200
        )
api.add_resource(Games, '/games')

class GameById(Resource):
    def get(self, id):
        try:
            game = Game.query.filter_by(id=id).first()
            return make_response(game.to_dict(), 200)
        except Exception as e:
            return make_response({'error': str(e)}, 404)
        
    def patch(self, id):
        request_data = request.json
        from_index = request_data['fromIndex']
        to_index = request_data['toIndex']

        game = Game.query.filter_by(id=id).first()
        chess = Chess(game.fen)

        move = chess.move(from_index, to_index)
        print('move', move)
        
        if move:
            new_pgn = game.pgn[:-1] + move + ' ' + game.pgn[-1]
            game.pgn = new_pgn
            game.fen = pgn_to_fen(new_pgn)
            db.session.add(game)
            db.session.commit()
        
        return make_response(jsonify(game.fen), 200)

api.add_resource(GameById, '/games/<int:id>')

class Login(Resource):
    def post(self):
        data = request.json
        try:
            user = User.query.filter_by(email=data['email']).first()
            if user.authenticate(data['password']):
                session['user_id'] = user.id
                return make_response(user.to_dict(), 200)
        except Exception as e:
            return make_response({'error': str(e)}, 400)
api.add_resource(Login, '/login')

class SignUp(Resource):
    def post(self):
        data = request.json
        try:
            user = User(
                full_name=data['fullName'],
                username=data['username'],
                email=data['email'],
                profile_image='https://github.com/kschneider0/chess/blob/main/server/assets/default.png?raw=true',
                password_hash=data['password']
            )
            db.session.add(user)
            db.session.commit()
            return make_response(user.to_dict(), 201)
        except Exception as e:
            return make_response({'error': str(e)}, 400)
api.add_resource(SignUp, '/signup')

class Logout(Resource):
    def delete(self):
        session['user_id'] = None
        return make_response({}, 204)
api.add_resource(Logout, '/logout')

class AuthorizedSession(Resource):
    def get(self):
        try:
            user = User.query.filter_by(id=session['user_id']).first()
            return make_response(user.to_dict(), 200)
        except Exception as e:
            return make_response({'error': str(e)}, 400)
api.add_resource(AuthorizedSession, '/authorized-session')

if __name__ == '__main__':
    app.run(port=5555, debug=True)