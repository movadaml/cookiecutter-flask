"""Create static webpage."""
from flask_frozen import Freezer
from {{cookiecutter.app_name}}.app import create_app

freezer = Freezer(create_app())

if __name__ == '__main__':
    freezer.freeze()
    # freezer.run(debug=True)  # serve static files from default webserver