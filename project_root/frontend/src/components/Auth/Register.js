import React, { useState } from 'react';
import { TextField, Button, Typography } from '@mui/material';
import api from '../../services/api';

function Register() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  
  const handleSubmit = async (e) => {
    
    e.preventDefault();
    try {
      
      await api.post('/auth/register', { username, email, password });
      // Redirect to login page or show success message
      alert('Registration successful!');
    } catch (error) {
      alert('Registration failed, username or email already exists!');
      console.error('Registration failed:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <Typography variant="h5">Register</Typography>
      <TextField
        label="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <TextField
        type="email"
        label="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <TextField
        type="password"
        label="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <Button type="submit" variant="contained" color="primary">
        Register
      </Button>
    </form>
  );
}

export default Register;