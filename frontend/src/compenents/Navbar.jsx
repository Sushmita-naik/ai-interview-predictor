import React from "react";

function Navbar() {
  return (
    <nav style={styles.navbar}>
      <div style={styles.logo}>
        AI Interview Predictor
      </div>

      <ul style={styles.navLinks}>
        <li>
          <a href="/" style={styles.link}>
            Dashboard
          </a>
        </li>

        <li>
          <a href="/uploadresume" style={styles.link}>
            Upload Resume
          </a>
        </li>

        <li>
          <a href="/resume" style={styles.link}>
            Resume Analysis
          </a>
        </li>

        <li>
          <a href="/interview" style={styles.link}>
            Interview
          </a>
        </li>

        <li>
          <a href="/login" style={styles.link}>
            Logout
          </a>
        </li>
      </ul>
    </nav>
  );
}

const styles = {
  navbar: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    backgroundColor: "#2563eb",
    padding: "15px 30px",
    color: "white",
  },

  logo: {
    fontSize: "22px",
    fontWeight: "bold",
  },

  navLinks: {
    listStyle: "none",
    display: "flex",
    gap: "20px",
    margin: 0,
    padding: 0,
  },

  link: {
    textDecoration: "none",
    color: "white",
    fontWeight: "500",
  },
};

export default Navbar;