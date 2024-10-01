from flask import Flask
from route import room_type_blueprint, availability_room_blueprint

app = Flask(__name__)

app.register_blueprint(room_type_blueprint)
app.register_blueprint(availability_room_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
