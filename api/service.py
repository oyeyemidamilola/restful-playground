from flask import jsonify, abort, make_response, request
from api import app

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods = ['GET'])
def get_tasks():
    
    """
    gets all the task resource
    """
    return jsonify(dict(tasks = tasks))


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['GET'])
def get_task(task_id):

    task = [task for task in tasks if task.get('id') == task_id]
    if len(task) == 0:
        abort(404)
    
    return jsonify(dict(task = task))


@app.route('/todo/api/v1.0/tasks', methods = ['POST'])
def create_task():

    """
    create a new task resource
    """

    if not request.json or not 'title' in request.json:
        print(request.json)
        abort(400)

    task = dict(
                    id = tasks[-1].get('id') + 1,
                    title = request.json.get('title'),
                    description = request.json.get('description'),
                    done = False
                )
    tasks.append(task)
    return jsonify(dict(task = task)) , 201

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task.get('id') == task_id]

    if len(task) == 0:
        abort(400)

    if not request.json:
        abort(400)

    if 'title' in request.json and type(request.json.get('title')) is not unicode:
        abort(400)
    
    if 'description' in request.json and type(request.json.get('description')) != unicode:
        abort(400)
    
    if 'done' in request.json and type(request.json.get('done')) is not bool:
        abort(400)

    task[0]['title'] = request.json.get('title')
    task[0]['description'] = request.json.get('description')
    task[0]['done'] = request.json.get('done')

    return jsonify(dict(task = task[0]))
    








@app.errorhandler(404)
def not_found(error):

    return make_response(jsonify({'error' : "Not Found"}))

@app.errorhandler(400)
def bad_request(error):

    return make_response(jsonify({'error' : "Bad Request"}))
