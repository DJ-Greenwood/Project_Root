import React, { useState, useEffect } from 'react';
import { List, ListItem, ListItemText, Typography } from '@mui/material';
import api from '../../services/api';

function ETLProcessList() {
  const [etlProcesses, setEtlProcesses] = useState([]);

  useEffect(() => {
    const fetchETLProcesses = async () => {
      try {
        const response = await api.get('/etl');
        setEtlProcesses(response.data);
      } catch (error) {
        console.error('Failed to fetch ETL processes:', error);
      }
    };
    fetchETLProcesses();
  }, []);

  return (
    <div>
      <Typography variant="h5">ETL Processes</Typography>
      <List>
        {etlProcesses.map((process) => (
          <ListItem key={process.id}>
            <ListItemText
              primary={process.name}
              secondary={`Description: ${process.description}`}
            />
          </ListItem>
        ))}
      </List>
    </div>
  );
}

export default ETLProcessList;