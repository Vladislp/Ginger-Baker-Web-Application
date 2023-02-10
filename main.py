from Website import create_app

# create the Flask application object
app = create_app()

# check if this script is run as the main program
if __name__ == '__main__':
    # run the application with debug mode on
    app.run(debug=True)
