import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Настройки базы данных
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'recipes.db')}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
