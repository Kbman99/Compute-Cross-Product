from flask import Flask

from app.core import db, debug_toolbar, ma, migrate
from app.helpers import register_blueprints

from app import config
from app import filters


def create_app(package_name, package_path, settings=None):
    app = Flask(package_name,
                template_folder='templates'
                )

    app.config.from_object(config.DevConfig)

    if settings:
        app.config.update(settings)

    db.init_app(app)

    migrate.init_app(app, db)

    ma.init_app(app)

    debug_toolbar.init_app(app)

    register_blueprints(app, package_name, package_path)

    app.jinja_env.filters['time_str'] = filters.gen_time_str

    return app
