from flask_marshmallow import Marshmallow
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow.exceptions import ValidationError

db = SQLAlchemy()
ma = Marshmallow()

def create_app():

    app = Flask(__name__)
    app.config.from_object("config.app_config")

    #db = SQLAlchemy(app)
    db.init_app(app)
    ma.init_app(app)

    from commands import db_commands
    app.register_blueprint(db_commands)

    #db.create_all()
    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)
    
    @app.errorhandler(ValidationError)
    def handle_bad_request(error):
        return (jsonify(error.messages), 400)

    return app
    #app.run(debug=True)