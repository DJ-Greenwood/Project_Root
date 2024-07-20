import React, { useState, useEffect } from 'react';
import { List, ListItem, ListItemText, Typography } from '@mui/material';
import api from '../../services/api';

function OutputList() {
  const [outputs, setOutputs] = useState([]);

  useEffect(() => {
    const fetchOutputs = async () => {
      try {
        const response = await api.get('/output');
        setOutputs(response.data);
      } catch (error) {
        console.error('Failed to fetch outputs:', error);
      }
    };
    fetchOutputs();
  }, []);

  return (
    <div>
      <Typography variant="h5">Outputs</Typography>
      <List>
        {outputs.map((output) => (
          <ListItem key={output.id}>
            <ListItemText
              primary={output.name}
              secondary={`Type: ${output.type}, Description: ${output.description}`}
            />
          </ListItem>
        ))}
      </List>
    </div>
  );
}

export default OutputList;