from api import db

class Task(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(30), nullable = False)
    description = db.Column(db.Text,  nullable = False)
    done = db.Column(db.Boolean, nullable = False)
    




    def __repr__(self):
        return f'Task<{self.title}, {self.done}>'

    def to_dict(self):

        task = dict()
        task['id'] = self.id
        task['title'] = self.title
        task['description'] = self.description
        task['done'] = self.done

        return task
        

