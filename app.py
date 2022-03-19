from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', template_folder='template')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/projects/<int:id>")
def cv(id):
    id = int(id)
    if id == 1:
        return render_template("project1.html")
    if id == 2:
        return render_template("project2.html")
    if id == 3:
        return render_template("project3.html")
    if id == 4:
        return render_template("project4.html")
    #if id == 5:
    #    return render_template("project5.html")
    #if id == 6:
    #    return render_template("project6.html")

if __name__ == "__main__":
    app.run(debug=True)
