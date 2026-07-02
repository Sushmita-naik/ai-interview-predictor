import { useState } from "react";

function useAuth() {
  const [user, setUser] = useState(null);

  const login = (userData, token) => {
    localStorage.setItem("token", token);
    localStorage.setItem(
      "user",
      JSON.stringify(userData)
    );

    setUser(userData);
  };

  const logout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");

    setUser(null);
  };

  const getCurrentUser = () => {
    const storedUser =
      localStorage.getItem("user");

    if (!storedUser) return null;

    return JSON.parse(storedUser);
  };

  const isAuthenticated = () => {
    return !!localStorage.getItem("token");
  };

  return {
    user,
    login,
    logout,
    getCurrentUser,
    isAuthenticated,
  };
}

export default useAuth;