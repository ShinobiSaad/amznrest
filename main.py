from api.app import create_app
from api.models import *

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)