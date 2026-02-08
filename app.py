from flask import Flask, render_template

app = Flask(__name__)

DASHBOARD_URL = "https://public.tableau.com/views/Jitendrakumar/Dashboard1?:showVizHome=no&:embed=yes"
STORY_URL = "https://public.tableau.com/views/Jitendra_17705410008340/Story1?:showVizHome=no&:embed=yes"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", tableau_url=DASHBOARD_URL)

@app.route("/story")
def story():
    return render_template("story.html", tableau_url=STORY_URL)

if __name__ == "__main__":
    app.run(debug=True)
