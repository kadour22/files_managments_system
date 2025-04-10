import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api', // Update with your backend URL
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add a request interceptor to include the token
apiClient.interceptors.request.use(config => {
  const token = localStorage.getItem('authToken'); // Retrieve the token
  if (token) {
    config.headers['Authorization'] = `Bearer ${token}`;
  }
  return config;
}, error => {
  return Promise.reject(error);
});

export default apiClient;
