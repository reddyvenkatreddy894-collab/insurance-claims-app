Insurance Claims Processing App (Flask + Docker)
 Overview

This project is a simple insurance claims processing module that enables insurance companies to:

Receive and log customer claims.

Apply rule-based review for claims.

Maintain customer claim history.

Generate claim approval or rejection messages.

 Key Features

Interactive dashboard with sidebar navigation.

Claim submission form (Policy Number, Claim Type, Amount, Description).

Responsive UI with basic CSS styling.

Dockerized Flask backend for easy deployment.

 Project Structure
insurance-claims-app/
│── app.py              # Flask backend application
│── requirements.txt    # Python dependencies
│── Dockerfile          # Docker image configuration
│── README.md           # Project documentation
│
├── templates/
│   ├── dashboard.html  # Dashboard interface
│   └── claim_form.html # Insurance claim form
│
└── static/
    └── style.css       # Stylesheet

 Installation & Setup
1. Clone the Repository
git clone <your-repo-link>
cd insurance-claims-app

2. Build and Run with Docker
docker build -t insurance-claims-app .
docker run -p 5000:5000 insurance-claims-app

3. Access the Application

Open your browser and visit:
👉 http://localhost:5000
<img width="1912" height="995" alt="image" src="https://github.com/user-attachments/assets/78db935b-3815-489c-a3d9-72694801226c" />
