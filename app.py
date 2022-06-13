from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv()

DB_PASSWORD = os.getenv('DB_PASSWORD')
DOMAIN = os.getenv('DOMAIN')
MAX_CODE_LENGTH = int(os.getenv('MAX_CODE_LENGTH'))

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug = True) 