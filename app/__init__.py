"""
Flask Application Factory
"""
import os
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'),
        static_folder=os.path.join(os.path.dirname(__file__), '..', 'static')
    )

    # ── Config ──
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'ayurparam-dev-key-change-in-prod')
    app.config['DATABASE'] = os.path.join(os.path.dirname(__file__), '..', 'data', 'ayurparam.db')
    app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB upload limit

    CORS(app)

    # ── Database ──
    from app.models.database import init_db
    init_db(app)

    # ── Model Loader (background) ──
    # Removed here to prevent Gunicorn fork() thread dying. Loaded lazily in /api/status.


    # ── Register Blueprints ──
    from app.routes.main import main_bp
    from app.routes.chat import chat_bp
    from app.routes.history import history_bp
    from app.routes.settings import settings_bp
    from app.routes.admin import admin_bp
    from app.routes.herbs import herbs_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(chat_bp, url_prefix='/api')
    app.register_blueprint(history_bp, url_prefix='/api')
    app.register_blueprint(settings_bp, url_prefix='/api')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    app.register_blueprint(herbs_bp, url_prefix='/api')

    return app
