import { useState } from 'react';
import { useHistory } from 'react-router-dom';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import CardActionArea from '@mui/material/CardActionArea';
import Button from '@mui/material/Button';

import { ChromePicker } from 'react-color';

import playFriends from '../assets/play-friends.png';
import social from '../assets/social.png';
import about from '../assets/about.png';
import logout from '../assets/logout.png';
import sword from '../assets/sword.png';


function NavBar({ 
    user, 
    movesToMake, 
    numChallenges, 
    onLogout, 
    onClickPlay, 
    selectedColor, 
    onChangeColor, 
    onChangeColorComplete 
}) {
  
    const history = useHistory();

    const [showColorPicker, setShowColorPicker] = useState(false);

    const MenuItem = (text, icon, route) => {
      
        return (
            <CardActionArea>
              <Box 
                onClick={() => {
                  switch (text) {
                    case 'Active Games':
                      onClickPlay(false);
                      break;
                    case 'Challenges':
                      onClickPlay(true);
                      break;
                    case 'Logout':
                      onLogout();
                      break;
                    default:
                      break;
                  };
                  history.push(route);
                }}
                sx={{ 
                  color: '#e1e1e1', 
                  display: 'flex', 
                  alignItems: 'center',
                  pointer: 'cursor', 
              }}
              >
              <Box
                component='img'
                alt=''
                src={icon}
                sx={{
                  width: 50,
                  m: 2,
                }}
              />
                {`${text}`}
                {/* your move */}
                {text === 'Active Games' && movesToMake > 0 ? 
                <Box
                  sx={{ 
                    ml: 2, 
                    bgcolor: 'red',
                    borderRadius: '25%',
                    width: 15,
                    height: 15,
                    display: 'flex',
                    justifyContent: 'center',                
                  }}
                >
                  {movesToMake}
                </Box> : null}
                {/* challenges */}
                {text === 'Challenges' && numChallenges > 0 ? 
                <Box
                  sx={{ 
                    ml: 2, 
                    bgcolor: 'red',
                    borderRadius: '25%',
                    width: 15,
                    height: 15,
                    display: 'flex',
                    justifyContent: 'center',                
                  }}
                >
                  {numChallenges}
                </Box> : null}    
              </Box>
            </CardActionArea>
        );
    };

    return (
        <Box 
        bgcolor='secondary.main'
        >
          <Typography 
            variant='h5' 
            align='center'
            sx={{
              mt: 1,
              mb: 3
            }}
          >
            Chess Is Hard
          </Typography>
          {MenuItem('Active Games', playFriends, '/play')}
          {MenuItem('Challenges', sword, '/play')}
          {MenuItem('Social', social, `/profile/${user.id}`)}
          {MenuItem('About', about, '/about')}
          {MenuItem('Logout', logout, '/login')}
          {selectedColor ? 
            <Box
            sx={{
              position: 'absolute',
              bottom: 0,
              m: '1rem',
              width: 200
            }}
            >
              {showColorPicker ? 
              <ChromePicker 
                color={selectedColor} 
                onChange={onChangeColor} 
                onChangeComplete={onChangeColorComplete}
              /> : null}
              <Box
                sx={{
                  display: 'flex',
                  justifyContent: 'center',
                  m: 2
                }}
              >
                <Button
                  variant='contained'
                  // sx={{ mx: 'auto' }}
                  onClick={() => setShowColorPicker(!showColorPicker)}
                >
                  {showColorPicker ? 'Hide Colors' : 'Show Colors'}
                </Button>
              </Box>
            </Box> : null}
        </Box>
    );
}

export default NavBar;