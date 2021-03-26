from flask import Flask
from flask_injector import FlaskInjector
from recepies.dependencies import configure

def setup_config(app, test_config):
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.update(test_config)
    return app

def create_app(test_config=None):
    app = Flask(__name__)
    setup_config(app, test_config)
    
    @app.route('/health')
    def health():
        return "", 200

    from recepies.recepie import router as recepie_router
    app.register_blueprint(recepie_router.bp)

    FlaskInjector(app=app, modules=[configure])
    return app
