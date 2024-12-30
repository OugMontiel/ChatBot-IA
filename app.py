from flask import Flask, request, render_template
from model import load_model

app = Flask(__name__)
qa_pipeline = load_model()

@app.route('/', methods=['GET', 'POST'])
def home():
    answer = None
    question = None
    context = None

    if request.method == 'POST':
        question = request.form.get('question')
        context = request.form.get('context')

        if question and context:
            result = qa_pipeline(question=question, context=context)
            answer = result['answer']

    return render_template('index.html', question=question, context=context, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)