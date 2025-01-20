from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

tasks = []  # This will hold your to-do tasks

@app.route('/')
def index():
    # Render the main page
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    # Add a new task
    task = request.form.get('task')
    if task:
        tasks.append({'task': task, 'done': False})
    return redirect('/')

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    # Mark a task as complete
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = True
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    # Delete a task
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
