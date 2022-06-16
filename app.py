from logging import error
import re
import os
from turtle import Vec2D
from flask import Flask, render_template, request, make_response, session
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import datetime
from HostModel import HostModel
from Reviewsmodel import ReviewModel
from ExperinceModel import ExperienceModel
from TourModel import TourModel
from VehicleModel import VehicleModel
from ViewClasses import Vehicles
from ViewClasses import User
from ViewClasses import Tours
from ViewClasses import Hosts
from ViewClasses import Experiences
from UserModel import UserModel


UPLOAD_FOLDER_VEHICLE = "static/Uploads/vehicle/"
UPLOAD_FOLDER_TOUR = "static/Uploads/tour/"
UPLOAD_FOLDER_EXP = "static/Uploads/exp/"
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
    tourmodel = TourModel(
        app.config["DB_IP"],
        app.config["DB_USER"],
        app.config["DB_PASSWORD"],
        app.config["DATABASE"],
    )
    tourlist = tourmodel.get_alloftours()
    return render_template("cards.html", tourslist=tourlist)


@app.route("/vehiclelist")
def vehicleslist():
    vemodel = VehicleModel(
        app.config["DB_IP"],
        app.config["DB_USER"],
        app.config["DB_PASSWORD"],
        app.config["DATABASE"],
    )
    velist = vemodel.get_allofVehicle()
    print("Im list")
    print(velist[0])
    print("Im list End")
    return render_template("vehiclecards.html", vehiclelist=velist)


@app.route("/experiencelist")
def experienceslist():
    expmodel = ExperienceModel(
        app.config["DB_IP"],
        app.config["DB_USER"],
        app.config["DB_PASSWORD"],
        app.config["DATABASE"],
    )
    explist = expmodel.get_allofexps()
    print(explist[0].experience_id)
    return render_template("experiencecard.html", experiencelist=explist)


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
        description = request.form["description"]
        vstartdate = request.form["startDate"]
        print(vstartdate)
        tstartdate = datetime.datetime.strptime(
            request.form['startDate'], '%Y-%m-%d')
        venddate = request.form["endDate"]
        tenddate = datetime.datetime.strptime(
            request.form['endDate'], '%Y-%m-%d')
        firstpic = request.files["my-file1"]
        secondpic = request.files["my-file2"]
        thirdpic = request.files["my-file3"]
        print(tname)
        print(temail)
        # return render_template("message.html", hosting="Tour")
        username = request.cookies.get('username')
        usermodel = UserModel(
            app.config["DB_IP"],
            app.config["DB_USER"],
            app.config["DB_PASSWORD"],
            app.config["DATABASE"],
        )
        tuserid = usermodel.getuserid(username)
        path1 = os.path.join(
            app.config["UPLOAD_FOLDER_TOUR"], firstpic.filename)
        path2 = os.path.join(
            app.config["UPLOAD_FOLDER_TOUR"], secondpic.filename)
        path3 = os.path.join(
            app.config["UPLOAD_FOLDER_TOUR"], thirdpic.filename)
        firstpic.save(path1)
        secondpic.save(path2)
        thirdpic.save(path3)
        tourmodel = TourModel(
            app.config["DB_IP"],
            app.config["DB_USER"],
            app.config["DB_PASSWORD"],
            app.config["DATABASE"],
        )
        hostmodel = HostModel(
            app.config["DB_IP"],
            app.config["DB_USER"],
            app.config["DB_PASSWORD"],
            app.config["DATABASE"],
        )
        host = Hosts(tuserid, tname, temail, tphone, "account.png")

        if(hostmodel.check_host_exist(host) == False):
            hostmodel.add_host(host)
        t_host_id = hostmodel.gethostid(tname)
        t_default_price = int(tprice) * (0.1 * int(tprice))
        t_delux_price = int(tprice) * (0.2 * int(tprice))
        picture = [firstpic.filename, secondpic.filename, thirdpic.filename]
        tour = Tours(0, t_host_id,  picture,
                     ttitle, description, tlocation, tdays, tcapacity, t_default_price, t_delux_price,
                     description, description, tstartdate, tenddate)
        print(t_host_id)
        tourmodel.insert_tour(tour)
        return render_template("message.html", hosting="Tour")


@app.route("/submitvehicle", methods=["POST", "GET"])
def submitvechicle():
    if request.method == "POST":
        ename = request.form["fname"]
        eemail = request.form["email"]
        ephone = request.form["ph_no"]
        etitle = request.form["title"]
        elocation = request.form["location"]
        edays = request.form["days"]
        ecapacity = request.form["capacity"]
        eprice = request.form["price"]
        description = request.form["description"]
        vstartdate = request.form["startDate"]
        print(vstartdate)
        estartdate = datetime.datetime.strptime(
            request.form['startDate'], '%Y-%m-%d')
        venddate = request.form["endDate"]
        eenddate = datetime.datetime.strptime(
            request.form['endDate'], '%Y-%m-%d')
        firstpic = request.files["my-file1"]
        secondpic = request.files["my-file2"]
        thirdpic = request.files["my-file3"]
        print(ename)
        print(eemail)
        # return render_template("message.html", hosting="Tour")
        username = request.cookies.get('username')
        usermodel = UserModel(
            app.config["DB_IP"],
            app.config["DB_USER"],
            app.config["DB_PASSWORD"],
            app.config["DATABASE"],
        )
        tuserid = usermodel.getuserid(username)
        path1 = os.path.join(
            app.config["UPLOAD_FOLDER_VEHICLE"], firstpic.filename)
        path2 = os.path.join(
            app.config["UPLOAD_FOLDER_VEHICLE"], secondpic.filename)
        path3 = os.path.join(
            app.config["UPLOAD_FOLDER_VEHICLE"], thirdpic.filename)
        firstpic.save(path1)
        secondpic.save(path2)
        thirdpic.save(path3)
        Vehiclemodel = VehicleModel(
            app.config["DB_IP"],
            app.config["DB_USER"],
            app.config["DB_PASSWORD"],
            app.config["DATABASE"],
        )
        hostmodel = HostModel(
            app.config["DB_IP"],
            app.config["DB_USER"],
            app.config["DB_PASSWORD"],
            app.config["DATABASE"],
        )
        host = Hosts(tuserid, ename, eemail, ephone, "account.png")

        if(hostmodel.check_host_exist(host) == False):
            hostmodel.add_host(host)
        t_host_id = hostmodel.gethostid(ename)
        t_default_price = int(eprice) * (0.1 * int(eprice))
        t_delux_price = int(eprice) * (0.2 * int(eprice))
        picture = [firstpic.filename, secondpic.filename, thirdpic.filename]
        vehicle = Vehicles(t_host_id, picture,
                           etitle, description, elocation, edays, ecapacity, t_default_price, t_delux_price,
                           description, description, estartdate, eenddate)

        vehicle.vehicle_age = int(request.form["age"])
        Vehiclemodel.insert_Vehicle(vehicle)
        return render_template("message.html", hosting=" Vehicle")


@app.route("/submitexp", methods=["POST", "GET"])
def submitexp():
    if request.method == "POST":
        ename = request.form["fname"]
        eemail = request.form["email"]
        ephone = request.form["ph_no"]
        etitle = request.form["title"]
        elocation = request.form["location"]
        edays = request.form["days"]
        ecapacity = request.form["capacity"]
        eprice = request.form["price"]
        description = request.form["description"]
        vstartdate = request.form["startDate"]
        print(vstartdate)
        estartdate = datetime.datetime.strptime(
            request.form['startDate'], '%Y-%m-%d')
        venddate = request.form["endDate"]
        eenddate = datetime.datetime.strptime(
            request.form['endDate'], '%Y-%m-%d')
        firstpic = request.files["my-file1"]
        secondpic = request.files["my-file2"]
        thirdpic = request.files["my-file3"]
        print(ename)
        print(eemail)
        # return render_template("message.html", hosting="Tour")
        username = request.cookies.get('username')
        usermodel = UserModel(
            app.config["DB_IP"],
            app.config["DB_USER"],
            app.config["DB_PASSWORD"],
            app.config["DATABASE"],
        )
        tuserid = usermodel.getuserid(username)
        path1 = os.path.join(
            app.config["UPLOAD_FOLDER_EXP"], firstpic.filename)
        path2 = os.path.join(
            app.config["UPLOAD_FOLDER_EXP"], secondpic.filename)
        path3 = os.path.join(
            app.config["UPLOAD_FOLDER_EXP"], thirdpic.filename)
        firstpic.save(path1)
        secondpic.save(path2)
        thirdpic.save(path3)
        experiencemodel = ExperienceModel(
            app.config["DB_IP"],
            app.config["DB_USER"],
            app.config["DB_PASSWORD"],
            app.config["DATABASE"],
        )
        hostmodel = HostModel(
            app.config["DB_IP"],
            app.config["DB_USER"],
            app.config["DB_PASSWORD"],
            app.config["DATABASE"],
        )
        host = Hosts(tuserid, ename, eemail, ephone, "account.png")
        t_host_id = hostmodel.gethostid(ename)
        t_default_price = int(eprice) * (0.1 * int(eprice))
        t_delux_price = int(eprice) * (0.2 * int(eprice))
        picture = [firstpic.filename, secondpic.filename, thirdpic.filename]
        expern = Experiences(t_host_id, picture,
                             etitle, description, elocation, edays, ecapacity, t_default_price, t_delux_price,
                             description, description, estartdate, eenddate)

        expern.experience_age = int(request.form["ages"])
        experiencemodel.insert_experience(expern)
        return render_template("message.html", hosting="In-Person Experience")


@app.route('/requestlist')
def requestlist():
    return render_template("requestlistADW.html")


@app.route('/adminHostingOption')
def adminoptions():
    return render_template("admin_hosting_option.html")


@app.route('/singleProduct', methods=["POST", "GET"])
def singleproduct():
    print("Request handled ")
    data = [0]
    if request.method == 'POST':
        experience_id = request.form['exp1']
        print("I am")
        print(experience_id)
        exp = ExperienceModel(
            app.config["DB_IP"],
            app.config["DB_USER"],
            app.config["DB_PASSWORD"],
            app.config["DATABASE"],
        )
        print(experience_id)
        result = exp.getdatabyid(experience_id)
        host_id = result.hostId
        hosts = HostModel(
            app.config["DB_IP"],
            app.config["DB_USER"],
            app.config["DB_PASSWORD"],
            app.config["DATABASE"],
        )
        singlehost = hosts.gethostobjbyid(host_id)
        host_name = singlehost.name
        host_describe = singlehost.describe
        print(result)
        return render_template("SingleProduct.html", product=result, hostname=host_name, hostdescribe=host_describe)
    return render_template("underconstruction.html")


@app.route('/tourProduct', methods=["POST", "GET"])
def tourproduct():
    print("Request handled ")
    data = [0]
    if request.method == 'POST':
        tour_id = request.form['tourid1']
        print("I am")
        print(tour_id)
        tour = TourModel(
            app.config["DB_IP"],
            app.config["DB_USER"],
            app.config["DB_PASSWORD"],
            app.config["DATABASE"],
        )
        print(tour_id)
        result = tour.getdatabyid(tour_id)
        host_id = result.hostId
        hosts = HostModel(
            app.config["DB_IP"],
            app.config["DB_USER"],
            app.config["DB_PASSWORD"],
            app.config["DATABASE"],
        )
        singlehost = hosts.gethostobjbyid(host_id)
        host_name = singlehost.name
        host_describe = singlehost.describe
        print(result)
    return render_template("tourproduct.html", product=result, hostname=host_name, hostdescribe=host_describe)


@app.route('/book')
def book():
    return render_template("underconstruction.html")


@app.route('/exptable')
def exptable():
    expmodel = ExperienceModel(
        app.config["DB_IP"],
        app.config["DB_USER"],
        app.config["DB_PASSWORD"],
        app.config["DATABASE"],
    )
    explist = expmodel.get_allofexps()
    # print(explist[0].experience_id)
    #     print(explist[0].experience_title)
    #     print(explist[0].experience_days)
    #     print(explist[0].experience_location)
    #     print(explist[0].experience_capacity)
    #     print("Hellp")
    return render_template("experiencetable.html", experiencelist=explist)
    # return render_template("underconstruction.html")


@app.route('/exptabl', methods=["POST", "GET"])
def exptabl():
    if request.method == 'POST':
        expmodel = ExperienceModel(
            app.config["DB_IP"],
            app.config["DB_USER"],
            app.config["DB_PASSWORD"],
            app.config["DATABASE"],
        )
        expid = request.form["exp1"]
        expmodel.deletedatabyid(expid)
        explist = expmodel.get_allofexps()
        print(explist[0].experience_id)
        print(explist[0].experience_title)
        print(explist[0].experience_days)
        print(explist[0].experience_location)
        print(explist[0].experience_capacity)
        print("Hellp")
        return render_template("experiencetable.html", experiencelist=explist)


@app.route('/tourtable')
def tourtable():
    tourmodel = TourModel(
        app.config["DB_IP"],
        app.config["DB_USER"],
        app.config["DB_PASSWORD"],
        app.config["DATABASE"],
    )
    explist = tourmodel.get_alloftours()
    return render_template("tourstable.html", tourlist=explist)
    # return render_template("underconstruction.html")


if __name__ == "__main__":  # defining main
    app.run(debug=True, port=5000)  # run app on port 5000
