import datetime
from faker import Faker

fake = Faker()
start_date = datetime.date(2005, 1, 1)
end_date = datetime.date(2015, 12, 31)

user_data = [
    {
        'full_name': 'Kyle Schneider',
        'username': 'Kye_Schnei',
        'email': 'kyle@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/woody.jpg?raw=true',
        'date_joined': datetime.date(2020, 11, 23),
        'password_hash': 'password'
    },
    {
        'full_name': 'Topher Ludlow',
        'username': 'topherLud',
        'email': 'toper@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/topher.jpg?raw=true',
        'date_joined': datetime.date(2020, 11, 10),
        'password_hash': 'password'
    },
    {
        'full_name': 'Magnus Carlsen',
        'username': 'DrDrunkenstein',
        'email': 'magnus@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/magnus.jpg?raw=true',
        'date_joined': fake.date_between(start_date=start_date, end_date=end_date),
        'password_hash': 'password'
    },
    {
        'full_name': 'Bobby Fischer',
        'username': 'BobbyBlitzBoy',
        'email': 'bobby@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/bobby.jpg?raw=true',
        'date_joined': fake.date_between(start_date=start_date, end_date=end_date),
        'password_hash': 'password'
    },
    {
        'full_name': 'Garry Kasparov',
        'username': 'KasparovKingKiller',
        'email': 'garry@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/garry.jpg?raw=true',
        'date_joined': fake.date_between(start_date=start_date, end_date=end_date),
        'password_hash': 'password'
    },
    {
        'full_name': 'Hans Niemann',
        'username': 'Hans Solo',
        'email': 'hand@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/hans.jpg?raw=true',
        'date_joined': fake.date_between(start_date=start_date, end_date=end_date),
        'password_hash': 'password'
    },
    {
        'full_name': 'Hikaru Nakamura',
        'username': 'Hikaru',
        'email': 'hikaru@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/hikaru.png?raw=true',
        'date_joined': fake.date_between(start_date=start_date, end_date=end_date),
        'password_hash': 'password'
    },
    {
        'full_name': 'Levy Rozman',
        'username': 'Gotham Chess',
        'email': 'levy@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/levy.png?raw=true',
        'date_joined': fake.date_between(start_date=start_date, end_date=end_date),
        'password_hash': 'password'
    },
    {
        'full_name': 'Fabiano Caruana',
        'username': 'FabulousFabiano',
        'email': 'fabiano@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/fabiano.png?raw=true',
        'date_joined': fake.date_between(start_date=start_date, end_date=end_date),
        'password_hash': 'password'
    },
    {
        'full_name': 'Maxime Vachier-Lagrave',
        'username': 'MVLchess',
        'email': 'maxime@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/maxime.jpg?raw=true',
        'date_joined': fake.date_between(start_date=start_date, end_date=end_date),
        'password_hash': 'password'
    },
    {
        'full_name': 'Wesley So',
        'username': 'SoSneaky',
        'email': 'wesley@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/wesley.png?raw=true',
        'date_joined': fake.date_between(start_date=start_date, end_date=end_date),
        'password_hash': 'password'
    },
    {
        'full_name': 'Viswanathan Anand',
        'username': 'Vishy',
        'email': 'vishy@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/viswanathan.jpg?raw=true',
        'date_joined': fake.date_between(start_date=start_date, end_date=end_date),
        'password_hash': 'password'
    },
    {
        'full_name': 'Levon Aronian',
        'username': 'The Levonator',
        'email': 'levon@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/levon.jpg?raw=true',
        'date_joined': fake.date_between(start_date=start_date, end_date=end_date),
        'password_hash': 'password'
    },
    {
        'full_name': 'Anish Giri',
        'username': 'GiriGiri',
        'email': 'anish@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/anish.jpg?raw=true',
        'date_joined': fake.date_between(start_date=start_date, end_date=end_date),
        'password_hash': 'password'
    },
    {
        'full_name': 'Ian Nepomniachtchi',
        'username': 'Nepo',
        'email': 'ian@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/ian.jpeg?raw=true',
        'date_joined': fake.date_between(start_date=start_date, end_date=end_date),
        'password_hash': 'password'
    }
]