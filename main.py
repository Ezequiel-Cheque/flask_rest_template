
from src.application.app import app

app = app

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=3000)