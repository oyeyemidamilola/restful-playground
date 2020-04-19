from flask import jsonify, abort, make_response, request
from api import app, db, auth
from .utils import make_public_task
from .models import Task

@app.route('/todo/api/v1.0/tasks', methods = ['GET'])
@auth.login_required
def get_tasks():
    
    """
    gets all the task resource
    """
    tasks = Task.query.all()
    if tasks:
        return jsonify(dict( tasks = [make_public_task(task.to_dict()) for task in tasks] ))
    
    abort(404)


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['GET'])
@auth.login_required
def get_task(task_id):

    task = Task.query.get(task_id)
    if task:    
        return jsonify(dict( task = make_public_task( task.to_dict() ) ) )
    
    abort(404)


@app.route('/todo/api/v1.0/tasks', methods = ['POST'])
@auth.login_required
def create_task():

    """
    create a new task resource
    """
    if not request.json or not 'title' in request.json:
        abort(400)

    task = Task()
    task.title = request.json.get('title')
    task.description = request.json.get('description')
    task.done = request.json.get('done')
    db.session.add(task)
    db.session.commit()


    return jsonify(dict(task = make_public_task(task.to_dict()))) , 201

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['PUT'])
@auth.login_required
def update_task(task_id):

    task = Task.query.get(task_id)
    if not Task:
        abort(400)

    if not request.json:
        abort(400)

    if 'title' in request.json and isinstance(request.json.get('title'), bytes):
        abort(400)
    
    if 'description' in request.json and isinstance(request.json.get('description'), bytes):
        abort(400)
    
    if 'done' in request.json and isinstance(request.json.get('done'), bytes):
        abort(400)

    task.title = request.json.get('title')
    task.description = request.json.get('description')
    task.done = request.json.get('done')
    db.session.add(task)
    db.session.commit()

    return jsonify(dict(task = make_public_task(task.to_dict())))


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['DELETE'])
@auth.login_required
def delete_task(task_id):
    
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify(dict(result = True)) 

    return abort(404)   




@app.errorhandler(404)
def not_found(error):

    return make_response(jsonify({'error' : "Not Found"}))

@app.errorhandler(400)
def bad_request(error):

    return make_response(jsonify({'error' : "Bad Request"}))
