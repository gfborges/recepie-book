from flask import Flask
from flask_injector import FlaskInjector
from recepies.dependencies import configure
from recepies.config import Config

app = Flask(__name__)
 
def setup_config(app, test_config):
    if test_config is None:
        app.config.from_object(Config)
    else:
        app.config.update(test_config)
    return app

def create_app(test_config=None):
    setup_config(app, test_config)

    from recepies.database import init_db
    init_db(app)

    @app.route('/health')
    def health():
        return "", 200
    
    from recepies.recepie.routers import ingredient_router, recepie_router
    app.register_blueprint(recepie_router)
    app.register_blueprint(ingredient_router)
    
    from recepies.index import router as index_router
    app.register_blueprint(index_router)

    FlaskInjector(app=app, modules=[configure])
    return app
