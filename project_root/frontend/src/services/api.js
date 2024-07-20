// In your frontend api service (e.g., src/services/api.js)
import axios from 'axios';


const api = axios.create({
  baseURL: 'http://localhost:5000',  // adjust if your backend is on a different port
});

api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers['Authorization'] = 'Bearer ' + token;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export const login = async (username, password) => {
  try {
    const response = await api.post('/auth/login', { username, password });
    localStorage.setItem('token', response.data.access_token);
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const logout = () => {
  localStorage.removeItem('token');
  // Optionally, make a call to the backend to invalidate the token
};

// Use this api instance for all your API calls
export default api;