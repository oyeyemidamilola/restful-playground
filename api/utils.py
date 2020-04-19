from flask import url_for, make_response, jsonify
from api import auth



def make_public_task(task):
    new_task = dict()

    for feild in task:
        if feild == 'id':
            new_task['uri'] = url_for('get_task', task_id = task['id'], _external= True)
        else:
            new_task[feild] = task[feild]
    
    return new_task


@auth.get_password
def get_password(username):
    if username == 'mcdammy':
        return 'dammyboy'
    
    return None

@auth.error_handler
def unathorized():

    return make_response(jsonify(dict(error = 'Unauthorized access')), 401)

