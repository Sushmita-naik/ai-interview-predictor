import axios from "axios";

const API_URL = "http://127.0.0.1:8000/auth";

// Register User
export const registerUser = async (userData) => {
  const response = await axios.post(`${API_URL}/register`, userData);
  return response.data;
};

// Login User
export const loginUser = async (userData) => {
  const response = await axios.post(`${API_URL}/login`, userData);

  // Save JWT Token
  localStorage.setItem("token", response.data.access_token);

  // Save User Details
  localStorage.setItem("user", JSON.stringify(response.data.user));

  return response.data;
};

// Logout
export const logoutUser = () => {
  localStorage.removeItem("token");
  localStorage.removeItem("user");
};

// Get Token
export const getToken = () => {
  return localStorage.getItem("token");
};