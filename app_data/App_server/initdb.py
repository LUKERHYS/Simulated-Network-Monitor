import os 

from utils.app_factory import create_app
from utils.db import db

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

print("Database initialized...")
