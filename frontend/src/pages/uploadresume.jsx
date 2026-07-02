import React, { useState } from "react";

function UploadResume() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      setMessage("Please select a resume.");
      return;
    }

    const formData = new FormData();
    formData.append("resume", file);

    try {
      const response = await fetch(
        "http://localhost:8000/upload-resume",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      if (response.ok) {
        setMessage("Resume uploaded successfully!");
        console.log(data);
      } else {
        setMessage("Upload failed.");
      }
    } catch (error) {
      console.error(error);
      setMessage("Server error.");
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h1>Upload Resume</h1>

        <p>
          Upload your resume in PDF format for
          AI analysis.
        </p>

        <input
          type="file"
          accept=".pdf"
          onChange={handleFileChange}
          style={styles.input}
        />

        {file && (
          <p>
            Selected File: <b>{file.name}</b>
          </p>
        )}

        <button
          onClick={handleUpload}
          style={styles.button}
        >
          Upload Resume
        </button>

        {message && (
          <p style={styles.message}>
            {message}
          </p>
        )}
      </div>
    </div>
  );
}

const styles = {
  container: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    minHeight: "100vh",
    backgroundColor: "#f4f6f9",
  },

  card: {
    backgroundColor: "#fff",
    padding: "30px",
    borderRadius: "12px",
    width: "500px",
    boxShadow:
      "0 2px 10px rgba(0,0,0,0.1)",
    textAlign: "center",
  },

  input: {
    marginTop: "20px",
    marginBottom: "20px",
  },

  button: {
    width: "100%",
    padding: "12px",
    backgroundColor: "#2563eb",
    color: "#fff",
    border: "none",
    borderRadius: "8px",
    cursor: "pointer",
    fontSize: "16px",
  },

  message: {
    marginTop: "15px",
    fontWeight: "bold",
  },
};

export default UploadResume;