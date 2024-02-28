from flask import Flask, render_template, request

app = Flask(__name__)

notes = []
@app.route('/', methods=["GET","POST"])
def index():
    note = request.form.get("note")
    if note:
        notes.append(note)
    return render_template("project.html", notes=notes)


if __name__ == '__main__':
    app.run(debug=True)