import React from "react";

function ScoreCard({
  title,
  score,
  total = 100,
}) {
  const percentage = (score / total) * 100;

  return (
    <div style={styles.card}>
      <h3>{title}</h3>

      <div style={styles.score}>
        {score}/{total}
      </div>

      <div style={styles.progressBar}>
        <div
          style={{
            ...styles.progress,
            width: `${percentage}%`,
          }}
        />
      </div>

      <p>{percentage.toFixed(0)}% Score</p>
    </div>
  );
}

const styles = {
  card: {
    backgroundColor: "#ffffff",
    padding: "20px",
    borderRadius: "12px",
    boxShadow:
      "0 2px 8px rgba(0,0,0,0.1)",
    width: "250px",
    textAlign: "center",
  },

  score: {
    fontSize: "32px",
    fontWeight: "bold",
    margin: "15px 0",
  },

  progressBar: {
    width: "100%",
    height: "10px",
    backgroundColor: "#e5e7eb",
    borderRadius: "10px",
    overflow: "hidden",
  },

  progress: {
    height: "100%",
    backgroundColor: "#2563eb",
  },
};

export default ScoreCard;