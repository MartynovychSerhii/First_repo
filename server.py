from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

print(__name__)


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/index.html")
def my_home_index():
    return render_template("index.html")


@app.route("/generic.html")
def genetic():
    return render_template("generic.html")


@app.route("/elements.html")
def elements():
    return render_template(url_for("/elements.html"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/blog/2020/dogs")
def blog2():
    return "<p>My dogs!</p>"


def write_to_file(data):
    with open("database.txt", mode="a") as database:
        email = data["email"]
        subject = data['name']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open("database.csv", mode="a", newline='') as database2:
        email = data["email"]
        subject = data['name']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=",", quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            print(data)
            return render_template('/ty.html')
        except:
            return "did not save to database"
    else:
        return "something went wrong!"
