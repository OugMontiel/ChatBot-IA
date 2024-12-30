from flask import Flask, request, jsonify, render_template
from model import load_model

app = Flask(__name__)
qa_pipeline = load_model()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    question = request.form.get('question')
    context = request.form.get('context')

    if not question or not context:
        return jsonify({"error": "Falta pregunta o contexto"}), 400

    result = qa_pipeline(question=question, context=context)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)