import React from "react";

function Dashboard() {
  const user = {
    name: "Sushmita",
    resumeScore: 82,
    interviewScore: 76,
    interviewsTaken: 5,
  };

  return (
    <div style={styles.container}>
      <h1>Dashboard</h1>

      <h2>Welcome, {user.name} 👋</h2>

      <div style={styles.cardContainer}>
        <div style={styles.card}>
          <h3>Resume Score</h3>
          <p>{user.resumeScore}/100</p>
        </div>

        <div style={styles.card}>
          <h3>Interview Score</h3>
          <p>{user.interviewScore}/100</p>
        </div>

        <div style={styles.card}>
          <h3>Interviews Taken</h3>
          <p>{user.interviewsTaken}</p>
        </div>
      </div>

      <div style={styles.actions}>
        <h2>Quick Actions</h2>

        <button style={styles.button}>
          Upload Resume
        </button>

        <button style={styles.button}>
          Start Interview
        </button>

        <button style={styles.button}>
          View Reports
        </button>
      </div>

      <div style={styles.activity}>
        <h2>Recent Activity</h2>

        <ul>
          <li>Resume Uploaded</li>
          <li>Technical Interview Completed</li>
          <li>Report Generated</li>
        </ul>
      </div>
    </div>
  );
}

const styles = {
  container: {
    padding: "30px",
    fontFamily: "Arial",
  },

  cardContainer: {
    display: "flex",
    gap: "20px",
    marginTop: "20px",
    marginBottom: "30px",
  },

  card: {
    border: "1px solid #ddd",
    borderRadius: "10px",
    padding: "20px",
    width: "220px",
    textAlign: "center",
    boxShadow: "0 2px 5px rgba(0,0,0,0.1)",
  },

  actions: {
    marginTop: "20px",
  },

  button: {
    padding: "10px 20px",
    marginRight: "10px",
    cursor: "pointer",
    borderRadius: "5px",
    border: "none",
    backgroundColor: "#2563eb",
    color: "white",
  },

  activity: {
    marginTop: "40px",
  },
};

export default Dashboard;