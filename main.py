# We can do that, because website is a Python package
from Website import create_app
from flask_babelex import Babel

app = create_app()
babel = Babel(app)

# Only if we run this file, not if we import this file are we going to run this app ?
if __name__ == '__main__':
    # Run Flask application/Run web server with command "debug=True"
    # Whenever we change our code, "debug=True" make sure that changes will be applied and webserver restart
    app.run(debug=True)