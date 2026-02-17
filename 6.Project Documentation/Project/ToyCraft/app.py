import os
from flask import Flask, render_template
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)

# Disable template auto-reload in production and cache static assets.
app.config.setdefault("TEMPLATES_AUTO_RELOAD", False)
app.config.setdefault("SEND_FILE_MAX_AGE_DEFAULT", int(os.getenv("STATIC_CACHE_MAX_AGE", "3600")))

DASHBOARD_URL = "https://public.tableau.com/views/Jitendrakumar/Dashboard1?:showVizHome=no&:embed=yes"
STORY_URL = "https://public.tableau.com/views/Jitendra_17705410008340/Story1?:showVizHome=no&:embed=yes"


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/about")
def about():
    return render_template("about.html")


@app.get("/dashboard")
def dashboard():
    return render_template("dashboard.html", tableau_url=DASHBOARD_URL)


@app.get("/story")
def story():
    return render_template("story.html", tableau_url=STORY_URL)


@app.get("/healthz")
def healthz():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)
