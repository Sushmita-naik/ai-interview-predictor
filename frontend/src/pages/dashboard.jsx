import { useNavigate } from "react-router-dom";
import { logoutUser } from "../services/authService";
import "./dashboard.css";

function Dashboard() {

    const navigate = useNavigate();

    const user = JSON.parse(localStorage.getItem("user"));

    const logout = () => {
        logoutUser();
        navigate("/");
    };

    return (

        <div className="dashboard">

            <div className="navbar">

                <h2>AI Interview Predictor</h2>

                <button
                    className="logout-btn"
                    onClick={logout}
                >
                    Logout
                </button>

            </div>

            <div className="welcome">

                <h1>
                    Welcome,
                    {user ? ` ${user.name}` : ""}
                    👋
                </h1>

                <p>
                    Let's prepare for your dream job today.
                </p>

            </div>

            <div className="cards">

                <div className="card">

                    <h2>📄 Upload Resume</h2>

                    <p>
                        Upload your latest resume.
                    </p>

                    <button
                        onClick={() =>
                            navigate("/uploadresume")
                        }
                    >
                        Upload
                    </button>

                </div>

                <div className="card">

                    <h2>🤖 AI Interview</h2>

                    <p>
                        Practice AI Interview Questions.
                    </p>

                    <button
                        onClick={() =>
                            navigate("/interview")
                        }
                    >
                        Start
                    </button>

                </div>

                <div className="card">

                    <h2>📊 Resume Analysis</h2>

                    <p>
                        Analyze Resume & Skills.
                    </p>

                    <button>
                        Analyze
                    </button>

                </div>

                <div className="card">

                    <h2>💼 Placement Prediction</h2>

                    <p>
                        Predict your placement chances.
                    </p>

                    <button>
                        Predict
                    </button>

                </div>

                <div className="card">

                    <h2>💰 Salary Prediction</h2>

                    <p>
                        Predict your expected salary.
                    </p>

                    <button>
                        View
                    </button>

                </div>

                <div className="card">

                    <h2>📈 Reports</h2>

                    <p>
                        View your complete report.
                    </p>

                    <button>
                        Reports
                    </button>

                </div>

            </div>

        </div>

    );

}

export default Dashboard;