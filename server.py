from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')
    print(f"!!! text_to_analyze")

    emotion_response = emotion_detector(text_to_analyze)

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