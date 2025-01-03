from transformers import pipeline

class ModelManager:
    def __init__(self, model_names):
        """
        Inicializa el ModelManager con una lista de nombres de modelos.
        
        :param model_names: Lista de nombres de modelos de Hugging Face.
        """
        self.models = {}
        self.current_model_name = None
        self.load_models(model_names)

    def load_models(self, model_names):
        """
        Carga los modelos especificados y los almacena en un diccionario.
        
        :param model_names: Lista de nombres de modelos de Hugging Face.
        """
        for name in model_names:
            self.models[name] = pipeline("question-answering", model=name)
        self.current_model_name = model_names[0]  # Selecciona el primer modelo por defecto

    def set_current_model(self, model_name):
        """
        Establece el modelo actual a utilizar.
        
        :param model_name: Nombre del modelo a utilizar.
        """
        if model_name in self.models:
            self.current_model_name = model_name
        else:
            raise ValueError(f"Modelo {model_name} no está cargado.")

    def get_current_model(self):
        """
        Devuelve el modelo actual.
        
        :return: Modelo de Hugging Face actual.
        """
        return self.models[self.current_model_name]

    def answer_question(self, question, context):
        """
        Responde a una pregunta utilizando el modelo actual.
        
        :param question: Pregunta a responder.
        :param context: Contexto para la pregunta.
        :return: Respuesta generada por el modelo.
        """
        model = self.get_current_model()
        return model(question=question, context=context)