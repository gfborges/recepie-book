from flask import Flask

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

    from recepies import index
    app.register_blueprint(index.bp)
    return app
