// src/components/Navbar.js
import React from 'react';
import { AppBar, Toolbar, Button, Typography, Box } from '@mui/material';
import { Link as RouterLink, useNavigate } from 'react-router-dom';
import { logout } from '../services/api';

function Navbar() {
  const navigate = useNavigate();
  const token = localStorage.getItem('token');

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          Data Lineage Tracker
        </Typography>
        <Box>
          {!token ? (
            <>
              <Button color="inherit" component={RouterLink} to="/login">Login</Button>
              <Button color="inherit" component={RouterLink} to="/register">Register</Button>
            </>
          ) : (
            <>
              <Button color="inherit" component={RouterLink} to="/data-ingestion">Data Ingestion</Button>
              <Button color="inherit" component={RouterLink} to="/etl">ETL Processes</Button>
              <Button color="inherit" component={RouterLink} to="/models">ML Models</Button>
              <Button color="inherit" component={RouterLink} to="/outputs">Outputs</Button>
              <Button color="inherit" component={RouterLink} to="/lineage">Lineage Graph</Button>
              <Button color="inherit" onClick={handleLogout}>Logout</Button>
            </>
          )}
        </Box>
      </Toolbar>
    </AppBar>
  );
}

export default Navbar;