from flask import Flask, render_template, request

app = Flask(__name__)

study_tasks = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        task = request.form.get('task')
        study_tasks.append(task)

    return render_template('index.html', tasks=study_tasks)

if __name__ == '__main__':
    app.run(debug=True)
