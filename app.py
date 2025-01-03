from flask import Flask, request, render_template, send_from_directory
from model_manager import ModelManager
import os

app = Flask(__name__)

# Lista de modelos a utilizar
model_names = [
    "distilbert-base-uncased-distilled-squad",
    "bert-large-uncased-whole-word-masking-finetuned-squad",
]

# Inicializa el gestor de modelos
model_manager = ModelManager(model_names)

@app.route('/templates/<path:filename>')
def custom_static(filename):
    return send_from_directory(os.path.join(app.root_path, 'templates'), filename)

@app.route('/', methods=['GET', 'POST'])
def home():
    answer = None
    question = None
    context = None
    selected_model = model_manager.current_model_name

    if request.method == 'POST':
        question = request.form.get('question')
        context = request.form.get('context')
        selected_model = request.form.get('model')

        if selected_model:
            model_manager.set_current_model(selected_model)

        if question and context:
            result = model_manager.answer_question(question, context)
            answer = result['answer']

    return render_template('index.html', question=question, context=context, answer=answer, models=model_names, selected_model=selected_model)

if __name__ == '__main__':
    app.run(debug=True)