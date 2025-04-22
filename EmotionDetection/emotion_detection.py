import requests
import json  # To handle JSON data

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send the POST request to the API
    response = requests.post(url, headers=headers, json=input_json)

    # Parse the JSON response
    response_data = response.json()  # Parse the response into a Python dictionary

    # Extract emotions from the API response
    emotions = response_data.get("emotionPredictions", [{}])[0].get("emotion", {})

    # Extract the individual emotion scores
    anger_score = emotions.get("anger", 0)
    disgust_score = emotions.get("disgust", 0)
    fear_score = emotions.get("fear", 0)
    joy_score = emotions.get("joy", 0)
    sadness_score = emotions.get("sadness", 0)

    # Determine the dominant emotion (the one with the highest score)
    emotion_scores = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Return the results in the required dictionary format
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
