from flask import render_template, request, redirect, url_for

from app import app


posts =[]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        city = request.form.get("city")
        hobby = request.form.get("hobby")
        age = request.form.get("age")
        if name and city and hobby and age:
            posts.append({"name": name, "city": city, "hobby": hobby, "age": age})
            return redirect(url_for("index"))

    return render_template("Formasayta.html", posts=posts)