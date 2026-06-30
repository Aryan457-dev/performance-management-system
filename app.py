from flask import Flask

from config import Config
from extensions import db, login_manager, migrate
from routes.review import review_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager.init_app(app)
migrate.init_app(app, db)

import models

from routes.auth import auth
from routes.dashboard import dashboard_bp

app.register_blueprint(auth)
app.register_blueprint(dashboard_bp)
app.register_blueprint(review_bp)


@app.route("/")
def home():
    return "<h2>Performance Management System is Running 🚀</h2>"


if __name__ == "__main__":
    app.run(debug=True)