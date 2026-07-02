import React from "react";

function QuestionCard({
  questionNumber,
  totalQuestions,
  question,
}) {
  return (
    <div style={styles.card}>
      <h3>
        Question {questionNumber} of {totalQuestions}
      </h3>

      <div style={styles.questionBox}>
        <p>{question}</p>
      </div>
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
    marginBottom: "20px",
  },

  questionBox: {
    backgroundColor: "#f5f7fa",
    padding: "15px",
    borderRadius: "8px",
    marginTop: "10px",
    fontSize: "18px",
    fontWeight: "500",
  },
};

export default QuestionCard;