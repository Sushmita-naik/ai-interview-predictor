import React from "react";

function ReportCard({
  resumeScore,
  technicalScore,
  communicationScore,
  projectScore,
  recommendation,
}) {
  return (
    <div style={styles.card}>
      <h2>Interview Report</h2>

      <div style={styles.scoreBox}>
        <p>
          <strong>Resume Score:</strong> {resumeScore}/100
        </p>

        <p>
          <strong>Technical Score:</strong> {technicalScore}/100
        </p>

        <p>
          <strong>Communication Score:</strong> {communicationScore}/100
        </p>

        <p>
          <strong>Project Understanding:</strong> {projectScore}/100
        </p>
      </div>

      <div style={styles.recommendation}>
        <h3>Recommendation</h3>
        <p>{recommendation}</p>
      </div>
    </div>
  );
}

const styles = {
  card: {
    backgroundColor: "#ffffff",
    padding: "25px",
    borderRadius: "12px",
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
    maxWidth: "700px",
    margin: "20px auto",
  },

  scoreBox: {
    marginTop: "20px",
    lineHeight: "2",
  },

  recommendation: {
    marginTop: "25px",
    padding: "15px",
    backgroundColor: "#f5f7fa",
    borderRadius: "8px",
  },
};

export default ReportCard;