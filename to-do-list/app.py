from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_text = request.form.get('task')
    if task_text:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        tasks.append({'text': task_text, 'timestamp': timestamp})
    return redirect(url_for('index'))

@app.route('/remove_task/<int:task_index>', methods=['GET'])
def remove_task(task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
