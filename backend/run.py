# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from app import create_app, db
from app.models import User, Task  # Necessary for Flask-Migrate & db.create_all()

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables in db according to models
    app.run(debug=True)