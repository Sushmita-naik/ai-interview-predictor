import React, { useState } from "react";

function Resume() {
  const [resumeData] = useState({
    name: "John Doe",
    email: "john@example.com",
    skills: ["Python", "React", "Machine Learning"],
    projects: [
      "AI Interview Predictor",
      "Plant Disease Detection"
    ],
    education: "B.E Computer Science",
  });

  return (
    <div style={styles.container}>
      <h1>Resume Analysis</h1>

      <div style={styles.card}>
        <h2>Personal Information</h2>

        <p>
          <strong>Name:</strong> {resumeData.name}
        </p>

        <p>
          <strong>Email:</strong> {resumeData.email}
        </p>

        <p>
          <strong>Education:</strong>{" "}
          {resumeData.education}
        </p>
      </div>

      <div style={styles.card}>
        <h2>Skills</h2>

        <ul>
          {resumeData.skills.map((skill, index) => (
            <li key={index}>{skill}</li>
          ))}
        </ul>
      </div>

      <div style={styles.card}>
        <h2>Projects</h2>

        <ul>
          {resumeData.projects.map((project, index) => (
            <li key={index}>{project}</li>
          ))}
        </ul>
      </div>

      <div style={styles.card}>
        <h2>Resume Score</h2>

        <h3>82 / 100</h3>

        <p>
          Good technical skills and projects.
          Add internships and certifications
          to improve your profile.
        </p>
      </div>
    </div>
  );
}

const styles = {
  container: {
    maxWidth: "900px",
    margin: "40px auto",
    padding: "20px",
    fontFamily: "Arial",
  },

  card: {
    backgroundColor: "#ffffff",
    padding: "20px",
    borderRadius: "10px",
    marginBottom: "20px",
    boxShadow:
      "0px 2px 8px rgba(0,0,0,0.1)",
  },
};

export default Resume;