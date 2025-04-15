## MAIN APPs
from config import create_app, db
from routes import routes

app = create_app()
app.register_blueprint(routes)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(debug=True)  # Run the Flask application in debug mode