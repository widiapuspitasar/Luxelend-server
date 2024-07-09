import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from app.routes.men_product_route import men_product_blueprint
from app.routes.women_product_route import women_product_blueprint

load_dotenv()

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
CORS(app, origins=['http://localhost:3000'], supports_credentials=True)

@app.route("/")
def helloWorld():
    return "welcome to Luxelend!"

app.register_blueprint(men_product_blueprint)
app.register_blueprint(women_product_blueprint)

if __name__ == "__main__":
    app.run()