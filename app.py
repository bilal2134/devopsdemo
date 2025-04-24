from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metrics = PrometheusMetrics(app)


@app.route("/")
def home():
    return "Hello, DevOps World!"


if __name__ == "__main__":
    app.run(debug=True)
