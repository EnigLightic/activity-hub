class Config:
    SECRET_KEY = "dev-secret-key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///activity_hub.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False