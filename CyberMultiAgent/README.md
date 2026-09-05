# Multi-Agent Cybersecurity Incident Response System

##  About the Project

A cybersecurity incident usually involves several steps, such as detecting suspicious activity, understanding what happened, assessing the severity of the incident, and deciding what response should be taken.

This project implements a **Multi-Agent Cybersecurity Incident Response System** in which multiple specialized agents work together to analyze a security incident.

Instead of using a single agent for the entire process, the task is divided among different agents. Each agent is responsible for a specific part of the analysis, while **LangGraph manages the workflow and coordinates the agents**.

The project is developed using **Python, LangChain, LangGraph, Google Gemini, and Streamlit**.

---

##  Objective

The main objective of this project is to demonstrate how multiple AI agents can work together to analyze and respond to a cybersecurity incident.

The system can:

- Detect suspicious security activity.
- Analyze the possible type of attack.
- Assess the risk and severity of the incident.
- Recommend appropriate defensive actions.
- Combine the results into a final security assessment.

---

##  How the Multi-Agent System Works

The system consists of four specialized agents. Each agent performs a specific task in the incident response process.

###  1. Threat Detection Agent

The Threat Detection Agent is the first stage of the system.

It receives a security event and checks whether the activity appears suspicious.

For example, it can identify patterns such as repeated failed login attempts followed by a successful login from an unusual location.

**Main responsibilities:**

- Identify suspicious activity.
- Detect unusual security patterns.
- Provide an initial assessment of the event.

---

###  2. Threat Analysis Agent

After suspicious activity is detected, the Threat Analysis Agent examines the event in more detail.

It analyzes the available information to determine:

- What type of attack may have occurred.
- What evidence supports the analysis.
- What may have caused the suspicious activity.

This agent focuses on understanding and analyzing the incident.

---

###  3. Risk Assessment Agent

The Risk Assessment Agent evaluates the seriousness of the detected incident.

It provides:

- A risk score between 0 and 100.
- A severity level such as LOW, MEDIUM, HIGH, or CRITICAL.
- A short explanation for the assigned risk level.

This helps determine which incidents require greater attention.

---

###  4. Response Agent

The Response Agent provides defensive recommendations based on the incident and its assessed risk.

For example, it may recommend:

- Temporarily locking the affected account.
- Terminating active sessions.
- Resetting the account password.
- Enabling multi-factor authentication.
- Reviewing authentication logs.
- Investigating the suspicious login activity.

The system provides recommendations only and does not automatically perform actions on real systems.

---

#  Agent Coordination

The agents work together as part of a single workflow. The result from one stage is passed to the next stage so that the incident can be analyzed step by step.

**LangGraph** is used to manage this workflow and coordinate the execution of the agents.

The workflow is:

```text
Security Event
      ↓
Threat Detection Agent
      ↓
Threat Analysis Agent
      ↓
Risk Assessment Agent
      ↓
Response Agent
      ↓
Final Security Report
