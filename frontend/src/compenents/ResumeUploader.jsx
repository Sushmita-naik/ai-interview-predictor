import React, { useState } from "react";

function ResumeUploader() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState("");

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      setUploadStatus("Please select a resume first.");
      return;
    }

    const formData = new FormData();
    formData.append("resume", selectedFile);

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
        setUploadStatus(
          "Resume uploaded successfully!"
        );
        console.log(data);
      } else {
        setUploadStatus(
          "Failed to upload resume."
        );
      }
    } catch (error) {
      console.error(error);
      setUploadStatus(
        "Server error. Please try again."
      );
    }
  };

  return (
    <div style={styles.container}>
      <h2>Upload Your Resume</h2>

      <input
        type="file"
        accept=".pdf"
        onChange={handleFileChange}
      />

      {selectedFile && (
        <p>
          Selected File: {selectedFile.name}
        </p>
      )}

      <button
        onClick={handleUpload}
        style={styles.button}
      >
        Upload Resume
      </button>

      {uploadStatus && (
        <p style={styles.status}>
          {uploadStatus}
        </p>
      )}
    </div>
  );
}

const styles = {
  container: {
    backgroundColor: "#fff",
    padding: "25px",
    borderRadius: "12px",
    boxShadow:
      "0 2px 8px rgba(0,0,0,0.1)",
    textAlign: "center",
    maxWidth: "500px",
    margin: "20px auto",
  },

  button: {
    marginTop: "15px",
    padding: "10px 20px",
    backgroundColor: "#2563eb",
    color: "white",
    border: "none",
    borderRadius: "8px",
    cursor: "pointer",
  },

  status: {
    marginTop: "15px",
    fontWeight: "bold",
  },
};

export default ResumeUploader;