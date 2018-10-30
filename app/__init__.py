"""

"""
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

#app
app = Flask(__name__)
app.config.from_object('config')

#database
db = SQLAlchemy(app)
migrate = Migrate(app, db)


#manager
manager = Manager(app)
manager.add_command('db', MigrateCommand)


#importar aquivos de controle
from .controllers import default
from .controllers import error