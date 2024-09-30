import requests
import json

def emotion_detector(text_to_analyse):
    """
    Sends post request to server for EmotionPredict ai then parses and returns 
    emotion scores based on the text passed to it.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=myobj, headers=header)
    # Load response into json format
    formatted_response = json.loads(response.text)
    # Extracts emotion and it's corresponding score from nested dictionary
    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
    max_emotion = max(emotion_scores, key=emotion_scores.get) # Gets max score 
    emotion_scores['dominant_emotion'] = max_emotion # Appends max emotion to dict

    return emotion_scores