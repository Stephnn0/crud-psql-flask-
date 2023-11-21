from flask import Flask
from routes.NoteRoutes import notes_bp


app = Flask(__name__)
app.register_blueprint(notes_bp)


if __name__ == '__main__':
    app.run(debug=True)