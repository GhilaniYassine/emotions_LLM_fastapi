def is_safe_content(text):
    sensitive_words = ['suicide', 'kill', 'die', 'hurt']
    return not any(word in text.lower() for word in sensitive_words)

def process_text_safely(text):
    try:
        if not is_safe_content(text):
            return {"status": "error", "message": "Content contains sensitive topics, please seek professional help"}
            
        # Set default safety limits
        max_length = 10000
        if len(text) > max_length:
            text = text[:max_length]
            
        return {"status": "success", "text": text}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def process_emotions_response(response_text):
    emotions = [
        "Anxiety", "Stress", "Anger", "Sadness", "Fear", "Shame", "Disgust",
        "Hopelessness", "Confusion", "Deep emotional pain", "Self-criticism",
        "Joy", "Hope", "Gratitude", "Pride", "Relief", "Love", "Surprise",
        "Curiosity", "Acceptance", "Ambivalence"
    ]
    
    emotion_dict = {}

    for emotion in emotions:
        try:
            if emotion in response_text:
                pos = response_text.find(emotion)
                value = response_text[pos:].split('"')[2].strip()
                emotion_dict[emotion] = value
        except Exception:
            emotion_dict[emotion] = "-"
            
    return emotion_dict