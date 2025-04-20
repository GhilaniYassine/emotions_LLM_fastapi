import google.generativeai as genai

def configure_api(api_key: str):
    genai.configure(api_key="AIzaSyBHXlI__9P7hHKzV5mSdXGYc0HKV55_tFM")

def is_safe_content(text: str) -> bool:
    sensitive_words = ['suicide', 'kill', 'die', 'hurt']
    return not any(word in text.lower() for word in sensitive_words)

def process_text_safely(text: str) -> dict:
    if not is_safe_content(text):
        return {"status": "error", "message": "Content contains sensitive topics, please seek professional help"}
    
    max_length = 10000
    if len(text) > max_length:
        text = text[:max_length]
    
    return {"status": "success", "text": text}

def analyze_text_with_gemini(prompt: str) -> str:
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error occurred: {str(e)}"

def process_emotions_response(response_text: str) -> dict:
    emotions = [
        "Anxiety", "Stress", "Anger", "Sadness", "Fear", "Shame", "Disgust",
        "Hopelessness", "Confusion", "Deep emotional pain", "Self-criticism",
        "Joy", "Hope", "Gratitude", "Pride", "Relief", "Love", "Surprise",
        "Curiosity", "Acceptance", "Ambivalence"
    ]
    
    emotion_dict = {emotion: "-" for emotion in emotions}

    for emotion in emotions:
        if emotion in response_text:
            pos = response_text.find(emotion)
            value = response_text[pos:].split('"')[2].strip()
            emotion_dict[emotion] = value
            
    return emotion_dict