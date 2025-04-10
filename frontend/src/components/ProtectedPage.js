import React, { useEffect, useState } from 'react';
import apiClient from '../apiClient';

const ProtectedPage = () => {
  const [message, setMessage] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await apiClient.get('/protected-endpoint/');
        setMessage(response.data.message);
      } catch (err) {
        console.error('Error fetching protected data:', err);
      }
    };

    fetchData();
  }, []);

  return <div>{message}</div>;
};

export default ProtectedPage;
