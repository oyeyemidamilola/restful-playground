from flask import url_for


def make_public_task(task):
    new_task = dict()

    for feild in task:
        if feild == 'id':
            new_task['uri'] = url_for('get_task', task_id = task['id'], _external= True)
        else:
            new_task[feild] = task[feild]
    
    return new_task


