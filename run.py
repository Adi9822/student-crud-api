from flask_migrate import Migrate

from app import create_app
from app import db
import logging

app = create_app()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)