import React, { useState } from 'react';
import { TextField, Button, Typography } from '@mui/material';
import api from '../../services/api';

function DataSourceForm() {
  const [name, setName] = useState('');
  const [type, setType] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post('/data/ingest', { name, type });
      // Show success message or redirect
    } catch (error) {
      console.error('Data ingestion failed:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <Typography variant="h5">Add Data Source</Typography>
      <TextField
        label="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <TextField
        label="Type"
        value={type}
        onChange={(e) => setType(e.target.value)}
      />
      <Button type="submit" variant="contained" color="primary">
        Add Data Source
      </Button>
    </form>
  );
}

export default DataSourceForm;