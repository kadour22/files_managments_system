import React, { useEffect, useState } from 'react';
import apiClient from '../apiClient';

const CourseList = () => {
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    const fetchCourses = async () => {
      try {
        const response = await apiClient.get('/courses/');
        setCourses(response.data);
      } catch (err) {
        console.error('Error fetching courses:', err);
      }
    };

    fetchCourses();
  }, []);

  return (
    <div>
      <h1>Courses</h1>
      <ul>
        {courses.map(course => (
          <li key={course.id}>
            {course.name} - <a href={course.download_url}>Download</a>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CourseList;
