from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def porreriana():
    return render_template("index.html") # Внутри () пишем название html-файла в кавычках

@app.route("/heroes/")
def heroes():
    return render_template("blog.html") # Внутри () пишем название html-файла в кавычках

@app.route("/contacts/")
def contacts():
    return render_template("contacts.html") # Внутри () пишем название html-файла в кавычках


if __name__ == "__main__":
    app.run()
