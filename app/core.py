from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

debug_toolbar = DebugToolbarExtension()

db = SQLAlchemy()

ma = Marshmallow()

migrate = Migrate()
