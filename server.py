"""
server to detect emotion
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    operation to display the index page
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_route():
    """
    operation to detect emotion
    """
    text_to_analyze = request.args.get('textToAnalyze')

    emotion_response = emotion_detector(text_to_analyze)

    if emotion_response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response_message = (
        f"For the given statement, the system response is "
        f"'anger': {emotion_response['anger']}, "
        f"'disgust': {emotion_response['disgust']}, "
        f"'fear': {emotion_response['fear']}, "
        f"'joy': {emotion_response['joy']} and "
        f"'sadness': {emotion_response['sadness']}. "
        f"The dominant emotion is <b>{emotion_response['dominant_emotion']}</b>."
    )
    # return jsonify({'message': response_message, 'details': emotion_response})
    return response_message

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
