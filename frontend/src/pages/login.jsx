import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { loginUser } from "../services/authService";
import "../styles/auth.css";

function Login() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();

    setLoading(true);
    setError("");

    try {
      await loginUser({
        email,
        password,
      });

      navigate("/dashboard");
    } catch (err) {
if (err.response) {

    if (err.response.status === 404) {
        setError("This email is not registered. Please create an account.");
    }

    else if (err.response.status === 401) {
        setError("Incorrect password.");
    }

    else {
        setError(err.response.data.detail);
    }

} else {
    setError("Unable to connect to server.");
}
    }

    setLoading(false);
  };

  return (
    <div className="auth-container">

      <div className="auth-card">

        <div className="logo">🎯</div>

        <h1 className="title">
          AI Interview Predictor
        </h1>

        <p className="subtitle">
          Prepare • Practice • Get Hired
        </p>

{error && (
    <div className="error-box">

        <p>{error}</p>

        {error.includes("not registered") && (
            <button
                className="link-btn"
                onClick={() => navigate("/register")}
            >
                Create Account
            </button>
        )}

    </div>
)}

        <form onSubmit={handleLogin}>

          <div className="input-group">

            <label>Email</label>

            <input
              type="email"
              placeholder="Enter your email"
              value={email}
              onChange={(e) =>
                setEmail(e.target.value)
              }
              required
            />

          </div>

          <div className="input-group">

            <label>Password</label>

            <input
              type={showPassword ? "text" : "password"}
              placeholder="Enter your password"
              value={password}
              onChange={(e) =>
                setPassword(e.target.value)
              }
              required
            />

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

          </div>

          <button
            className="btn-primary"
            type="submit"
          >
            {loading ? "Logging In..." : "Login"}
          </button>

        </form>

        <div className="bottom-text">

          Don't have an account?

          <button
            className="link-btn"
            onClick={() =>
              navigate("/register")
            }
          >
            Create Account
          </button>

        </div>

      </div>

    </div>
  );
}

export default Login;