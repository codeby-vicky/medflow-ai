# MedFlow AI Clinical Command Center

## Complete Implementation and Setup Guide

MedFlow-AI is a clinical workflow platform designed to simulate an intelligent hospital command system. The system performs patient triage, queue prioritization, prescription management, and analytics visualization using a modern full-stack architecture.

The platform integrates a React dashboard, FastAPI backend services, MongoDB data storage, and optional lightweight AI assistance through Ollama.

---

# 1. System Architecture

MedFlow-AI follows a three-layer architecture.

Frontend Layer

React dashboard responsible for:

• Patient registration
• Diagnosis display
• Doctor prescription interface
• Dynamic patient queue
• Clinic analytics visualization

Technologies

React
Axios
Chart.js

---

Backend Layer

FastAPI provides REST APIs for:

• Patient triage
• Severity classification
• Queue prioritization
• Wait time prediction
• Prescription storage
• Analytics generation

Technologies

Python
FastAPI
Scikit-Learn (for models if needed)

---

Database Layer

MongoDB Atlas stores all persistent data.

Collections

patients
prescriptions
analytics

---

# 2. Project Folder Structure

medflow-ai

backend
app
models
routes
services
utils
database.py
main.py

frontend
src
public
package.json

ai_engine
dataset

requirements.txt
README.md
.gitignore

---

# 3. Required Software

Install the following tools before running the system.

Python 3.10 or later
Node.js 18 or later
Git
MongoDB Atlas account
Ollama (optional AI runtime)

---

# 4. Clone the Project

Open terminal

cd D:\

git clone [https://github.com/codeby-vicky/medflow-ai.git](https://github.com/codeby-vicky/medflow-ai.git)

cd medflow-ai

---

# 5. Backend Setup

Navigate to backend directory

cd backend

Create Python virtual environment

python -m venv venv

Activate environment (PowerShell)

venv\Scripts\Activate

Install backend dependencies

pip install fastapi uvicorn pymongo scikit-learn pandas numpy python-dotenv

Generate requirements file

pip freeze > requirements.txt

---

# 6. MongoDB Configuration

Create a MongoDB Atlas cluster and obtain the connection URI.

Example database.py configuration

from pymongo import MongoClient

client = MongoClient("YOUR_MONGODB_URI")

db = client["medflow_ai"]

patients_collection = db["patients"]

prescriptions_collection = db["prescriptions"]

---

# 7. Start Backend Server

cd backend

venv\Scripts\Activate

uvicorn app.main:app --reload

Backend URL

[http://127.0.0.1:8000](http://127.0.0.1:8000)

FastAPI documentation

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

# 8. Frontend Setup

Open another terminal

cd frontend

Install dependencies

npm install

Start frontend

npm start

Frontend URL

[http://localhost:3000](http://localhost:3000)

---

# 9. Install Ollama (Optional AI Feature)

Download Ollama

[https://ollama.com](https://ollama.com)

After installation start the Ollama server

ollama serve

---

# 10. Recommended Ollama Models

These models are chosen because they work on low-end hardware (8GB RAM, 2-4GB GPU).

Recommended Model 1

phi3 mini

Install

ollama pull phi3:mini

Recommended Model 2

llama 3.2 small

Install

ollama pull llama3.2:1b

Recommended Model 3

qwen lightweight model

Install

ollama pull qwen2.5:1.5b

Test model

ollama run phi3:mini

Example prompt

Suggest medicines for symptoms fever cough cold

---

# 11. Running the Complete System

Terminal 1 (Backend)

cd backend

venv\Scripts\Activate

uvicorn app.main:app --reload

Terminal 2 (Frontend)

cd frontend

npm start

Terminal 3 (Optional AI)

ollama serve

---

# 12. System Workflow

Patient enters symptoms

Severity classification performed

Patient inserted into queue

Queue sorted by priority

Wait time predicted

Doctor generates prescription

Prescription stored in MongoDB

Analytics calculated

Dashboard chart updated

---

# 13. Queue Priority Logic

Emergency = 4
High = 3
Medium = 2
Low = 1

Queue sorted using

Severity priority
Arrival time

---

# 14. GitHub Deployment

From project root

cd D:\medflow-ai

Initialize repository

git init

Add files

git add .

Commit

git commit -m "Initial commit - MedFlow AI Clinical Command Center"

Connect GitHub repository

git remote add origin [https://github.com/codeby-vicky/medflow-ai.git](https://github.com/codeby-vicky/medflow-ai.git)

Push code

git branch -M main

git push -u origin main

---

# 15. Running Project After Clone (For New Users)

Clone repository

git clone [https://github.com/codeby-vicky/medflow-ai.git](https://github.com/codeby-vicky/medflow-ai.git)

cd medflow-ai

Backend setup

cd backend

python -m venv venv

venv\Scripts\Activate

pip install -r requirements.txt

uvicorn app.main:app --reload

Frontend setup

cd frontend

npm install

npm start

---

# 16. Features Implemented

Patient triage system

Severity classification

Dynamic patient queue

Wait time prediction

Doctor prescription system

MongoDB patient history storage

Analytics dashboard

Optional AI medicine suggestion

---

# Author

Vignesh M N

Contact

[m.n.vignesh2004@gmail.com](mailto:m.n.vignesh2004@gmail.com)
