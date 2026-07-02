import React, { useState } from "react";

function Interview() {
  const questions = [
    "Tell me about yourself.",
    "Explain your main project.",
    "Why did you choose this technology?",
    "What challenges did you face?",
    "Why should we hire you?"
  ];

  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answer, setAnswer] = useState("");
  const [answers, setAnswers] = useState([]);

  const handleNext = () => {
    const updatedAnswers = [
      ...answers,
      {
        question: questions[currentQuestion],
        answer: answer,
      },
    ];

    setAnswers(updatedAnswers);
    setAnswer("");

    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
    } else {
      console.log("Interview Completed");
      console.log(updatedAnswers);
      alert("Interview Submitted Successfully!");
    }
  };

  return (
    <div style={styles.container}>
      <h1>AI Interview</h1>

      <div style={styles.questionCard}>
        <h2>
          Question {currentQuestion + 1} / {questions.length}
        </h2>

        <p>{questions[currentQuestion]}</p>
      </div>

      <textarea
        rows="8"
        placeholder="Type your answer here..."
        value={answer}
        onChange={(e) => setAnswer(e.target.value)}
        style={styles.textarea}
      />

      <div style={styles.buttonContainer}>
        <button onClick={handleNext} style={styles.button}>
          {currentQuestion === questions.length - 1
            ? "Submit Interview"
            : "Next Question"}
        </button>
      </div>
    </div>
  );
}

const styles = {
  container: {
    maxWidth: "900px",
    margin: "50px auto",
    padding: "20px",
    fontFamily: "Arial",
  },

  questionCard: {
    border: "1px solid #ddd",
    borderRadius: "10px",
    padding: "20px",
    marginBottom: "20px",
    backgroundColor: "#f8f9fa",
  },

  textarea: {
    width: "100%",
    padding: "10px",
    borderRadius: "8px",
    border: "1px solid #ccc",
    fontSize: "16px",
  },

  buttonContainer: {
    marginTop: "20px",
    textAlign: "right",
  },

  button: {
    padding: "12px 20px",
    backgroundColor: "#2563eb",
    color: "white",
    border: "none",
    borderRadius: "8px",
    cursor: "pointer",
    fontSize: "16px",
  },
};

export default Interview;