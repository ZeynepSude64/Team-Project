from flask import Flask, render_template_string, request

app = Flask(__name__)

study_tasks = []

HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Smart Study Planner</title>

    <style>
        body {
            font-family: Arial;
            background-color: #f4f4f4;
            margin: 40px;
        }

        .container {
            background: white;
            padding: 20px;
            border-radius: 10px;
            max-width: 600px;
        }

        h1 {
            color: #333;
        }

        input {
            padding: 10px;
            width: 70%;
        }

        button {
            padding: 10px;
        }

        ul {
            margin-top: 20px;
        }

        li {
            padding: 8px;
            background: #e9e9e9;
            margin-bottom: 10px;
            border-radius: 5px;
        }
    </style>
</head>

<body>

<div class="container">

    <h1>Smart Study Planner</h1>

    <form method="POST">
        <input type="text" name="task" placeholder="Enter study task" required>
        <button type="submit">Add Task</button>
    </form>

    <ul>
        {% for task in tasks %}
            <li>{{ task }}</li>
        {% endfor %}
    </ul>

</div>

</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        task = request.form.get('task')
        study_tasks.append(task)

    return render_template_string(HTML, tasks=study_tasks)

if __name__ == '__main__':
    app.run(debug=True)
    
print("Project Running")
