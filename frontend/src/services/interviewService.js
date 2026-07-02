import API_BASE_URL from "./api";

// Generate Interview Questions

export const generateQuestions = async (
  skills,
  projects
) => {
  const response = await fetch(
    `${API_BASE_URL}/generate-questions`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        skills,
        projects,
      }),
    }
  );

  return await response.json();
};

// Submit Interview Answers

export const submitInterview = async (
  candidateName,
  answers
) => {
  const response = await fetch(
    `${API_BASE_URL}/submit-interview`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        candidate_name: candidateName,
        answers,
      }),
    }
  );

  return await response.json();
};

// Calculate Interview Score

export const getInterviewScore = async (
  technicalScore,
  communicationScore,
  projectScore,
  confidenceScore
) => {
  const response = await fetch(
    `${API_BASE_URL}/interview-score`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        technical_score: technicalScore,
        communication_score: communicationScore,
        project_score: projectScore,
        confidence_score: confidenceScore,
      }),
    }
  );

  return await response.json();
};