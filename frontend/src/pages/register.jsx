import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { registerUser, loginUser } from "../services/authService";
import "../styles/auth.css";

function Register() {
  const navigate = useNavigate();

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();

    setError("");

    if (password !== confirmPassword) {
      setError("Passwords do not match.");
      return;
    }

    setLoading(true);

    try {
      // Register user
      await registerUser({
        name,
        email,
        password,
      });

      // Automatically login
      await loginUser({
        email,
        password,
      });

      // Go directly to Dashboard
      navigate("/dashboard");

    } catch (err) {
      if (err.response) {
        setError(err.response.data.detail);
      } else {
        setError("Unable to connect to server.");
      }
    }

    setLoading(false);
  };

  return (
    <div className="auth-container">

      <div className="auth-card">

        <div className="logo">🚀</div>

        <h1 className="title">
          Create Account
        </h1>

        <p className="subtitle">
          Start preparing for your dream job
        </p>

        {error && (
          <div className="error-box">
            {error}
          </div>
        )}

        <form onSubmit={handleRegister}>

          <div className="input-group">
            <label>Full Name</label>

            <input
              type="text"
              placeholder="Enter your name"
              value={name}
              onChange={(e)=>setName(e.target.value)}
              required
            />
          </div>

          <div className="input-group">
            <label>Email</label>

            <input
              type="email"
              placeholder="Enter your email"
              value={email}
              onChange={(e)=>setEmail(e.target.value)}
              required
            />
          </div>

          <div className="input-group">
            <label>Password</label>

            <input
              type={showPassword ? "text" : "password"}
              placeholder="Enter password"
              value={password}
              onChange={(e)=>setPassword(e.target.value)}
              required
            />
          </div>

          <div className="input-group">
            <label>Confirm Password</label>

            <input
              type={showPassword ? "text" : "password"}
              placeholder="Confirm password"
              value={confirmPassword}
              onChange={(e)=>setConfirmPassword(e.target.value)}
              required
            />
          </div>

          <div className="show-password">

            <input
              type="checkbox"
              checked={showPassword}
              onChange={() =>
                setShowPassword(!showPassword)
              }
            />

            {" "}Show Password

          </div>

          <br />

          <button
            className="btn-primary"
            type="submit"
          >
            {loading ? "Creating Account..." : "Create Account"}
          </button>

        </form>

        <div className="bottom-text">

          Already have an account?

          <button
            className="link-btn"
            onClick={() => navigate("/")}
          >
            Login
          </button>

        </div>

      </div>

    </div>
  );
}

export default Register;