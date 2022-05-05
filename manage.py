
from app import create_app,db
from flask_script import Manager,Server
from app.dbmodels import User,Role
from  flask_migrate import Migrate


app=create_app('development')
manager = Manager(app)
manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Role=Role )


migrate = Migrate(app,db)
# manager.add_command('db',Migrate)

if __name__ == '__main__':
    manager.run()
