## Overview
The Mental Health Assistant Chatbot is designed to provide support for individuals seeking mental health assistance. It can engage users in empathetic conversations, offer mindfulness exercises, provide resources for mental wellness, and track mood over time. The chatbot is powered by OpenAI's GPT-3 to generate responses based on user input, allowing for natural and sensitive interactions.

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python)
- **AI Model:** OpenAI's GPT-3
- **Containerization:** Docker

## Features
1. **Empathetic Conversations:**
   - Engages in supportive conversations to help users manage stress, anxiety, and other mental health issues.
   - Uses natural language processing to understand and respond sensitively to user input.

2. **Mindfulness Exercises:**
   - Provides guided mindfulness exercises and techniques to help users relax and focus.
   - Offers suggestions for meditation, breathing exercises, and other relaxation techniques.

3. **Resource Provision:**
   - Offers information on mental health resources, including articles, videos, and contacts for professional help.
   - Can escalate critical issues by providing emergency contact information.

4. **Mood Tracking:**
   - Allows users to log their mood and track changes over time.
   - Provides insights and suggestions based on mood patterns.

5. **Ease of Deployment:**
   - Containerized using Docker for easy deployment and scalability.
   - Can be integrated into existing mental health support infrastructure.

## Project Structure
```plaintext
mental_health_assistant/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── index.html
│   └── main.js
