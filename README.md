# Final project

# Final project

## AI-Based Web Application for Emotion Detection

This project is an AI-based web application that detects emotions from customer feedback text. It uses the Watson NLP Emotion Detection service and deploys the application through a Flask web server.

## Project Overview

The application accepts a text statement from the user and analyzes the emotions expressed in the text. It returns scores for five emotions:

* Anger
* Disgust
* Fear
* Joy
* Sadness

The application also identifies the dominant emotion based on the highest emotion score.

## Features

* Emotion detection using Watson NLP API
* JSON response formatting
* Dominant emotion extraction
* Python package structure using `EmotionDetection`
* Unit testing with `unittest`
* Flask-based web deployment
* Error handling for blank or invalid input
* Static code analysis using PyLint

## Project Structure

```text
oaqjp-final-project-emb-ai/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── static/
│   └── mywebscript.js
├── templates/
│   └── index.html
├── server.py
├── test_emotion_detection.py
└── README.md
```

## How to Run the Application

Install the required libraries:

```bash
python3 -m pip install requests flask pylint
```

Run the Flask server:

```bash
python3 server.py
```

Open the application using Skills Network Toolbox and launch the app on port `5000`.

## Example Input

```text
I think I am having fun
```

## Example Output

```text
For the given statement, the system response is 'anger': ..., 'disgust': ..., 'fear': ..., 'joy': ... and 'sadness': .... The dominant emotion is joy.
```

## Unit Testing

Run the unit tests with:

```bash
python3 test_emotion_detection.py
```

## Static Code Analysis

Run PyLint with:

```bash
pylint server.py
```

The target score is:

```text
Your code has been rated at 10.00/10
```

## Technologies Used

* Python
* Flask
* Watson NLP Emotion Detection API
* Requests
* Unittest
* PyLint
* HTML
* JavaScript
