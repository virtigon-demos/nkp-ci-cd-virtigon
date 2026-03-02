from flask import Flask, render_template
import os

app = Flask(__name__, static_url_path="/static")


@app.route("/")
def home():
    # Human-readable app version from Dockerfile or env override
    version = os.getenv("APP_VERSION", "v1.1")

    # CI/CD build version
    build = os.getenv("BUILD_VERSION", "local")
    return render_template("index.html", version=version, build=build)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
