import React, { useState, useEffect } from "react";

function Timer({ initialTime = 60, onTimeUp }) {
  const [timeLeft, setTimeLeft] = useState(initialTime);

  useEffect(() => {
    if (timeLeft <= 0) {
      if (onTimeUp) {
        onTimeUp();
      }
      return;
    }

    const timer = setInterval(() => {
      setTimeLeft((prevTime) => prevTime - 1);
    }, 1000);

    return () => clearInterval(timer);
  }, [timeLeft, onTimeUp]);

  const minutes = Math.floor(timeLeft / 60);
  const seconds = timeLeft % 60;

  return (
    <div style={styles.container}>
      <h3>Time Remaining</h3>

      <div style={styles.timer}>
        {minutes.toString().padStart(2, "0")}:
        {seconds.toString().padStart(2, "0")}
      </div>
    </div>
  );
}

const styles = {
  container: {
    backgroundColor: "#ffffff",
    padding: "15px",
    borderRadius: "10px",
    textAlign: "center",
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
    width: "200px",
  },

  timer: {
    fontSize: "32px",
    fontWeight: "bold",
    color: "#2563eb",
  },
};

export default Timer;