import google.generativeai as genai

# Dictionary to store chat history. Key - chat ID. | Словарь для хранения истории чатов. Ключ - ID чата.
chat_sessions = {}

def initialize_gemini_model(api_key: str):
    """
    Configures and initializes the Gemini API model.
    Настраивает и инициализирует модель Gemini API.
    """
    try:
        genai.configure(api_key=api_key)
	# Model name | Название модели
        model = genai.GenerativeModel('gemini-1.5-flash') # https://ai.google.dev/gemini-api/docs/models for models and https://ai.google.dev/gemini-api/docs/rate-limits for rale limits
        print("Gemini model successfully configured.")
        return model
    except Exception as e:
        print(f"Gemini configuration error: {e}")
        return None
