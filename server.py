from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/")
def index_page():
    ''' 
    This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_analyser():
    '''
    Gets text from html page to be analysed, analysis it and returns formatted response
    '''

    text_to_analyse = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyse)

    # Error Checking if value is left blank
    if response['dominant_emotion'] == None:
        return "Invalid text! Please try again!"

    else:
        formatted_response = f"""For the given statement, the system response is 'anger': {response['anger']}, 
        'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 
        'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."""

    return formatted_response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)