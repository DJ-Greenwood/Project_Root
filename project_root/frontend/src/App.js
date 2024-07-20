// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { CssBaseline, Container, Box, Typography } from '@mui/material';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import Navbar from './components/Navbar';
import Login from './components/Auth/Login';
import Register from './components/Auth/Register';
import DataSourceForm from './components/DataIngestion/DataSourceForm';
import ETLProcessList from './components/ETL/ETLProcessList';
import ModelList from './components/MLModel/ModelList';
import OutputList from './components/Output/OutputList';
import LineageGraph from './components/Lineage/LineageGraph';

// Create a theme instance.
const theme = createTheme();

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <Box sx={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
          <Navbar />
          <Container component="main" sx={{ mt: 4, mb: 4, flex: 1 }}>
            <Routes>
              <Route path="/login" element={<Login />} />
              <Route path="/register" element={<Register />} />
              <Route path="/data-ingestion" element={<DataSourceForm />} />
              <Route path="/etl" element={<ETLProcessList />} />
              <Route path="/models" element={<ModelList />} />
              <Route path="/outputs" element={<OutputList />} />
              <Route path="/lineage" element={<LineageGraph />} />
              
            </Routes>
          </Container>
          <Box component="footer" sx={{ py: 3, px: 2, mt: 'auto', backgroundColor: (theme) => theme.palette.grey[200] }}>
            <Container maxWidth="sm">
              <Typography variant="body2" color="text.secondary" align="center">
                © {new Date().getFullYear()} Data Lineage Tracking System
              </Typography>
            </Container>
          </Box>
        </Box>
      </Router>
    </ThemeProvider>
  );
}

export default App;