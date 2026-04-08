# VigiNova 2.0

VigiNova 2.0 is a simulated AI-powered emergency response and safety triage environment built for the OpenEnv Hackathon.

## Overview
This project simulates real-world emergency scenarios where an AI agent must:
- understand the situation
- classify the incident
- decide the severity
- choose the correct response

It is designed to test decision-making in safety-critical situations.

---

## Live Demo
Hugging Face Space:
https://pallavibs0101-viginova-env.hf.space

---

## Tasks

### Easy Task
Identify whether the incident is an emergency or not.

### Medium Task
Classify the type of emergency:
- medical
- fire
- security

### Hard Task
Decide the correct response:
- ignore
- notify trusted contact
- escalate to emergency services

---

## Action Space
The agent can:
- classify incident
- assign severity
- escalate response
- notify contacts

---

## Observation Space
The agent receives:
- incident description (text)
- context clues (keywords like fire, pain, suspicious)
- possible response options

---

## Reward Logic

- Correct classification → +0.4  
- Correct severity → +0.3  
- Correct escalation → +0.3  
- Wrong decisions → penalty  

Final score is between **0.0 to 1.0**

---

## Features
- Real-world emergency simulation
- Simple AI decision-making logic
- Text-based environment
- Offline and reproducible

---

## How to Run

1. Install requirements:
2. Run demo:
---

## Notes
- This is a simulated environment
- No real emergency services are used
- Built for educational and evaluation purposes

---

## License
MIT License
## Tasks
- Easy: Minor incident detection
- Medium: Suspicious activity handling
- Hard: Medical emergency escalation
## Reward
Score is normalized between 0.0 and 1.0
