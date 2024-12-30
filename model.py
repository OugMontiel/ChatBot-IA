from transformers import pipeline
from config import MODEL_NAME

def load_model():
    # Carga el modelo de preguntas y respuestas
    qa_pipeline = pipeline("question-answering", model=MODEL_NAME)
    return qa_pipeline