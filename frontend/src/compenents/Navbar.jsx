import { useNavigate } from "react-router-dom";
import { logoutUser } from "../services/authService";

function Navbar() {
  const navigate = useNavigate();

  const user = JSON.parse(localStorage.getItem("user"));

  const handleLogout = () => {
    logoutUser();
    navigate("/");
  };

  return (
    <div className="navbar">

      <button
        className="back-btn"
        onClick={() => navigate(-1)}
      >
        ← Back
      </button>

      <h2 className="logo-title">
        AI Interview Predictor
      </h2>

      <div className="nav-right">

        <span className="username">
          👤 {user?.name}
        </span>

        <button
          className="logout-btn"
          onClick={handleLogout}
        >
          Logout
        </button>

      </div>

    </div>
  );
}

export default Navbar;