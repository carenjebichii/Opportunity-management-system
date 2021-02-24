from flask_script import Shell, Manager
from app import create_app, db
from app.main.models import User
from flask_migrate import Migrate, MigrateCommand

app = create_app("default")

manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User)


manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
