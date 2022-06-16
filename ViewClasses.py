class User:
    def __init__(self) -> None:
        self.user_id = 0
        self.email = ""
        self.password = "Not set"
        self.name = None

    def __init__(self, name, a_password) -> None:
        self.user_id = id
        self.email = "none"
        self.password = a_password
        self.name = name

    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        self.password = password


class Reviews:
    def __init__(self, profession, desc, rev_id) -> None:
        self.review_id = rev_id
        self.profession = profession
        self.description = desc


class Tours:
    def __init__(self, t_id, h_id,  img, t_title, t_description,
                 t_location, t_days, t_capacity, t_price_default, t_price_delux, t_describe_default,
                 t_decribe_delux, t_start_date, t_end_date) -> None:
        self.tour_id = t_id
        self.hostId = h_id
        self.tour_img1 = img[0]
        self.tour_img2 = img[1]
        self.tour_img3 = img[2]
        self.tour_title = t_title
        self.tour_description = t_description
        self.tour_location = t_location
        self.tour_days = t_days
        self.tour_capacity = t_capacity
        self.tour_price_default = t_price_default
        self.tour_price_delux = t_price_delux
        self.tour_describe_default = t_describe_default
        self.tour_describe_delux = t_decribe_delux
        self.tour_start_date = t_start_date
        self.tour_end_date = t_end_date

    def addinit(self, tour_img1, tour_title, tour_location, tour_days, tour_price_default, tour_capacity) -> None:
        self.tour_img1 = tour_img1
        self.tour_title = tour_title
        self.tour_location = tour_location
        self.tour_days = tour_days
        self.tour_price_default = tour_price_default
        self.tour_capacity = tour_capacity


class Hosts:
    def __init__(self) -> None:
        self.user_id = 0
        self.host_id = 0
        self.email = ""
        self.name = None
        self.phone = None

    def __init__(self, userid, name, email, phone, img) -> None:
        self.user_id = userid
        self.email = "none"
        self.host_img = img
        self.name = name
        self.email = email
        self.phone = phone
        self.describe = "Hello I am One of the Host"

    def settter(self, h_des, h_name):
        self.name = h_name
        self.describe = h_des


class Experiences:
    def __init__(self) -> None:
        pass

    def __init__(self, h_id,  img, t_title, t_description,
                 t_location, t_days, t_capacity, t_price_default, t_describe_default,
                 t_start_date, t_end_date) -> None:
        self.experience_id = 0
        self.hostId = h_id
        self.experience_img1 = img[0]
        self.experience_img2 = img[1]
        self.experience_age = 0
        self.experience_img3 = img[2]
        self.experience_title = t_title
        self.experience_description = t_description
        self.experience_location = t_location
        self.experience_days = t_days
        self.experience_capacity = t_capacity
        self.experience_price_default = t_price_default
        self.experience_price_delux = 0
        self.experience_describe_default = t_describe_default
        self.experience_describe_delux = ''
        self.experience_start_date = t_start_date
        self.experience_end_date = t_end_date

    def addinit(self, experience_img1, experience_title, experience_location, experience_days, experience_price_default, experience_capacity) -> None:
        self.experience_img1 = experience_img1
        self.experience_title = experience_title
        self.experience_location = experience_location
        self.experience_days = experience_days
        self.experience_price_default = experience_price_default
        self.experience_capacity = experience_capacity


class Vehicles:
    def __init__(self) -> None:
        pass

    def __init__(self, h_id,  img, t_title, t_description,
                 t_location, t_days, t_capacity, t_price_default, t_describe_default,
                 t_start_date, t_end_date) -> None:
        self.vehicle_id = 0
        self.hostId = h_id
        self.vehicle_img1 = img[0]
        self.vehicle_img2 = img[1]
        self.vehicle_age = 0
        self.vehicle_img3 = img[2]
        self.vehicle_title = t_title
        self.vehicle_description = t_description
        self.vehicle_location = t_location
        self.vehicle_days = t_days
        self.vehicle_capacity = t_capacity
        self.vehicle_price_default = t_price_default
        self.vehicle_price_delux = 0
        self.vehicle_describe_default = t_describe_default
        self.vehicle_describe_delux = ''
        self.vehicle_start_date = t_start_date
        self.vehicle_end_date = t_end_date

    def addinit(self, vehicle_img1, vehicle_title, vehicle_location, vehicle_days, vehicle_price_default, vehicle_capacity) -> None:
        self.vehicle_img1 = vehicle_img1
        self.vehicle_title = vehicle_title
        self.vehicle_location = vehicle_location
        self.vehicle_days = vehicle_days
        self.vehicle_price_default = vehicle_price_default
        self.vehicle_capacity = vehicle_capacity
