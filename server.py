"""
Flask server for the emotion detection web application.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("emotion_detector")


@app.route("/detect_emotion", methods=["POST"])
def detect_emotion():
    """
    Handle POST request to detect emotions from input text.

    Returns:
        JSON response with emotion scores or error message.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON input"}), 400

    text_to_analyze = data.get("text", "").strip()
    if not text_to_analyze:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    try:
        response = emotion_detector(text_to_analyze)
    except Exception as error:
        return jsonify({"error": f"Processing error: {error}"}), 500

    dominant_emotion = response.get("dominant_emotion")
    if dominant_emotion is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    return jsonify(response)


@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Handle GET request to analyze emotions from query parameter.

    Returns:
        Formatted string with emotion scores or error message.
    """
    text_to_analyze = request.args.get("textToAnalyze", "").strip()
    if not text_to_analyze:
        return "Invalid text! Please try again!", 400

    try:
        response = emotion_detector(text_to_analyze)
    except Exception as error:
        return f"Processing error: {error}", 500

    dominant_emotion = response.get("dominant_emotion")
    if dominant_emotion is None:
        return "Invalid text! Please try again!", 400

    anger = response.get("anger")
    disgust = response.get("disgust")
    fear = response.get("fear")
    joy = response.get("joy")
    sadness = response.get("sadness")

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """
    Render the index page.

    Returns:
        Rendered HTML template.
    """
    return render_template("index.html")


def main():
    """Run the Flask application."""
    app.run(host="0.0.0.0", port=5000, debug=False)


if __name__ == "__main__":
    main()
    