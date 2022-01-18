from logging import error
import re
import os
from flask import Flask, render_template, request, make_response, session
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from Reviewsmodel import ReviewModel
from ViewClasses import User
from UserModel import UserModel

UPLOAD_FOLDER_VEHICLE = "static/Uploads/vehicle"
UPLOAD_FOLDER_TOUR = "static/Uploads/tour"
UPLOAD_FOLDER_EXP = "static/Uploads/exp"
ALLOWED_EXTENSIONS = set(["txt", "pdf", "png", "jpg", "jpeg", "gif"])

app = Flask(__name__)
app.secret_key = "sessions"
app.config.from_object("config")
app.config["UPLOAD_FOLDER_TOUR"] = UPLOAD_FOLDER_TOUR
app.config["UPLOAD_FOLDER_VEHICLE"] = UPLOAD_FOLDER_VEHICLE
app.config["UPLOAD_FOLDER_EXP"] = UPLOAD_FOLDER_EXP

# you can also pass the key here if you prefer
GoogleMaps(app, key="8JZ7i18MjFuM35dJHq70n3Hx4")


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def logup():
    session.clear()
    return render_template("signup.html", notsame=False, already=None)


@app.route("/map")
def mapview():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)],
    )
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
            {
                "icon": "http://maps.google.com/mapfiles/ms/icons/green-dot.png",
                "lat": 37.4419,
                "lng": -122.1419,
                "infobox": "<b>Hello World</b>",
            },
            {
                "icon": "http://maps.google.com/mapfiles/ms/icons/blue-dot.png",
                "lat": 37.4300,
                "lng": -122.1400,
                "infobox": "<b>Hello World from other place</b>",
            },
        ],
    )
    return render_template("maps.html", mymap=mymap, sndmap=sndmap)


@app.route("/dosignup", methods=["POST", "GET"])
def completesignip():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["pass"]
    repassword = request.form["re_pass"]
    if password != repassword:
        return render_template("signup.html", notsame=True)
    else:
        user = User(name, email, password)
        usermodel = UserModel(
            app.config["DB_IP"],
            app.config["DB_USER"],
            app.config["DB_PASSWORD"],
            app.config["DATABASE"],
        )
        if usermodel.check_user_exist(user):
            return render_template("signup.html", already=True)
        else:
            usermodel.add_user(user)
            return render_template("signin.html", error=None)


@app.route("/homepage")
def homepage():
    username = session.get("username")
    if username != None:
        return render_template("index.html")
    else:
        return render_template("signin.html", error=None)


@app.route("/explainhost")
def explainhost():
    username = session.get("username")
    if username != None:
        return render_template("explainHost.html")
    else:
        return render_template("signin.html", error=None)


@app.route("/explaintour")
def explaintour():
    username = session.get("username")
    if username != None:
        return render_template("explaintour.html")
    else:
        return render_template("signin.html", error=None)


@app.route("/explainvehicle")
def explainvehicle():
    username = session.get("username")
    if username != None:
        return render_template("explainvehicle.html")
    else:
        return render_template("signin.html", error=None)


@app.route("/optionhost")
def hostingoption():
    username = session.get("username")
    if username != None:
        return render_template("option.html")
    else:
        return render_template("signin.html", error=None)


@app.route("/tourslist")
def tourslist():
    return render_template("cards.html")


@app.route("/gohomepage", methods=["POST", "GET"])
def completesignin():
    name = request.form["your_name"]
    password = request.form["your_pass"]
    user = User(name, "none", password)
    usermodel = UserModel(
        app.config["DB_IP"],
        app.config["DB_USER"],
        app.config["DB_PASSWORD"],
        app.config["DATABASE"],
    )
    if usermodel.login_user(user):
        resp = make_response(render_template("index.html"))
        resp.set_cookie("username", user.name)
        session["username"] = request.form.get("your_name")
        return resp
    else:
        return render_template("signin.html", error=True)


@app.route("/hosting")
def hosting():
    username = session.get("username")
    if username != None:
        return render_template("underconstruction.html")
    else:
        return render_template("signin.html", error=None)


@app.route("/sigin")
def hello_world():

    return render_template("signin.html", error=False, errormsg=None)


@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/inspiration")
def inspire():
    username = session.get("username")
    if username != None:
        reviewmodel = ReviewModel(
            app.config["DB_IP"],
            app.config["DB_USER"],
            app.config["DB_PASSWORD"],
            app.config["DATABASE"],
        )
        reviewlist = reviewmodel.getreviews()
        print(reviewlist)
        print(len(reviewlist))
        return render_template(
            "inspiration.html", reviews=reviewlist, rev_len=len(reviewlist)
        )
    else:
        return render_template("signin.html", error=None)


@app.route("/vehicleform")
def vehicleform():
    return render_template("vehicleform.html")


@app.route("/tourform")
def tourform():
    return render_template("tourform.html")


@app.route("/experienceform")
def experienceform():
    return render_template("experienceform.html")


@app.route("/logout", methods=["POST", "GET"])
def logout():
    session.clear()
    return render_template("signin.html", error=None)


@app.route("/submittour", methods=["POST", "GET"])
def submittour():
    if request.method == "POST":
        tname = request.form["fname"]
        temail = request.form["email"]
        tphone = request.form["ph_no"]
        ttitle = request.form["title"]
        tlocation = request.form["location"]
        tdays = request.form["days"]
        tcapacity = request.form["capacity"]
        tprice = request.form["price"]
        vstartdate = request.form["startDate"]
        venddate = request.form["endDate"]
        firstpic = request.files["my-file1"]
        secondpic = request.files["my-file2"]
        thirdpic = request.files["my-file3"]
        path1 = os.path.join(app.config["UPLOAD_FOLDER_TOUR"], firstpic.filename)
        path2 = os.path.join(app.config["UPLOAD_FOLDER_TOUR"], secondpic.filename)
        path3 = os.path.join(app.config["UPLOAD_FOLDER_TOUR"], thirdpic.filename)
        firstpic.save(path1)
        secondpic.save(path2)
        thirdpic.save(path3)
        return render_template("message.html", hosting="Tour")


@app.route("/submitvehicle", methods=["POST", "GET"])
def submitvechicle():
    if request.method == "POST":
        vname = request.form["fname"]
        vemail = request.form["email"]
        vphone = request.form["ph_no"]
        vaddress = request.form["address"]
        vlocation = request.form["l_name"]
        vtype = request.form["t_shirts"]
        vaddress = request.form["price"]
        vcapacity = request.form["capacity"]
        vstartdate = request.form["startDate"]
        venddate = request.form["endDate"]
        firstpic = request.files["my-file1"]
        secondpic = request.files["my-file2"]
        thirdpic = request.files["my-file3"]
        path1 = os.path.join(app.config["UPLOAD_FOLDER_VEHICLE"], firstpic.filename)
        path2 = os.path.join(app.config["UPLOAD_FOLDER_VEHICLE"], secondpic.filename)
        path3 = os.path.join(app.config["UPLOAD_FOLDER_VEHICLE"], thirdpic.filename)
        firstpic.save(path1)
        secondpic.save(path2)
        thirdpic.save(path3)
        return render_template("message.html", hosting="Vehicle")


@app.route("/submitexp", methods=["POST", "GET"])
def submitexp():
    if request.method == "POST":
        ename = request.form["name"]
        ephone = request.form["ph_no"]
        eage = request.form["age"]
        etitle = request.form["title"]
        elocation = request.form["location"]
        ecatagory = request.form["category"]
        edescription = request.form["requests"]
        firstpic = request.files["my-file1"]
        secondpic = request.files["my-file2"]
        thirdpic = request.files["my-file3"]
        path1 = os.path.join(app.config["UPLOAD_FOLDER_EXP"], firstpic.filename)
        path2 = os.path.join(app.config["UPLOAD_FOLDER_EXP"], secondpic.filename)
        path3 = os.path.join(app.config["UPLOAD_FOLDER_EXP"], thirdpic.filename)
        firstpic.save(path1)
        secondpic.save(path2)
        thirdpic.save(path3)
        return render_template("message.html", hosting="in-person Experience")


if __name__ == "__main__":  # defining main
    app.run(debug=True, port=5000)  # run app on port 5001
