import React, { useState, useEffect } from 'react';
import { List, ListItem, ListItemText, Typography } from '@mui/material';
import api from '../../services/api';

function ModelList() {
  const [models, setModels] = useState([]);

  useEffect(() => {
    const fetchModels = async () => {
      try {
        const response = await api.get('/model');
        setModels(response.data);
      } catch (error) {
        console.error('Failed to fetch models:', error);
      }
    };
    fetchModels();
  }, []);

  return (
    <div>
      <Typography variant="h5">ML Models</Typography>
      <List>
        {models.map((model) => (
          <ListItem key={model.id}>
            <ListItemText
              primary={model.name}
              secondary={`Version: ${model.version}, Description: ${model.description}`}
            />
          </ListItem>
        ))}
      </List>
    </div>
  );
}

export default ModelList;