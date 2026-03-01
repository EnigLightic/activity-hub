import os

class Config:
    SECRET_KEY = "dev-secret-key"
    JWT_SECRET_KEY = "super-secret-jwt-key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///activity_hub.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False