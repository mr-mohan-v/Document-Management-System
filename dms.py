from app import create_app, db, cli
from app.models import User, Post, Message, Notification, Task

app = create_app()
with app.app_context():
    db.create_all()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message,
            'Notification': Notification, 'Task': Task}


if __name__ == '__main__':
    app.run(host='0.0.0.0')
