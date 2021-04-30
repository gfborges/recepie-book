from flask import Flask
from flask_injector import FlaskInjector
from recepies.dependencies import configure
from recepies.config import Config

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
 
def setup_config(app, test_config):
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.update(test_config)
    return app

def create_app(test_config=None):
    setup_config(app, test_config)
    from recepies.database import init_db
    @app.route('/health')
    def health():
        return "", 200

    from recepies.recepie import router as recepie_router
    app.register_blueprint(recepie_router.bp)

    FlaskInjector(app=app, modules=[configure])
    return app
