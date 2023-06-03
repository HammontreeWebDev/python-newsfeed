from flask import Flask
from .routes import home, dashboard

def create_app(test_config=None):
    # !Set up app configuration
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes=False
    app.config.from_mapping(
        SECRET_KEY='super_secret_key'
    )

    @app.route('/hello')
    def hello():
        return 'Hello World, I am Thor!'
    
    # !register the routes
    app.register_blueprint(home)
    app.register_blueprint(dashboard)

    return app