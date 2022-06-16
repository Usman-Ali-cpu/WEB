create table users (
    user_id int Primary Key auto_increment,
    email varchar(250) UNIQUE,
    password varchar(50)
);
create table hosts(
    host_id int PRIMARY KEY auto_increment,
    user_id int NOT NULL,
    host_name varchar(50),
    host_img  varchar(50),
    host_describe varchar(300),
    CONSTRAINT FK_USER FOREIGN KEY (user_id)
    REFERENCES users(user_id)
);
create table tours(
    tour_id int PRIMARY KEY auto_increment,
    host_id int NOT NULL,
    tour_img1 varchar(50),
    tour_img2 varchar(50),
    tour_img3 varchar(50),
    tour_title varchar(100),
    tour_description varchar(400),
    tour_location varchar(50),
    tour_days int ,
    tour_capacity int,
    tour_price_default int,
    tour_price_delux int,
    tour_describe_default varchar(300),
    tour_describe_delux varchar(300),
    tour_start_date Date, 
    tour_end_date Date,
    CONSTRAINT FK_HOST FOREIGN KEY (host_id)
    REFERENCES hosts(host_id)
);
create table vehicles(
    vehicle_id int PRIMARY KEY auto_increment,
    host_id int NOT NULL,
    vehicle_img1 varchar(50),
    vehicle_img2 varchar(50),
    vehicle_img3 varchar(50),
    vehicle_title varchar(100),
    driver_age int ,
    vehicle_description varchar(400),
    vehicle_location varchar(50),
    vehicle_days int ,
    vehicle_capacity int,
    vehicle_price_default int,
    vehicle_describe_default varchar(300),
    vehicle_start_date Date, 
    vehicle_end_date Date,
    CONSTRAINT FK_VHOST FOREIGN KEY (host_id)
    REFERENCES hosts(host_id)
);

create table experiences(
    experience_id int PRIMARY KEY auto_increment,
    host_id int NOT NULL,
    experience_img1 varchar(50),
    experience_img2 varchar(50),
    experience_img3 varchar(50),
    experience_title varchar(100),
    experience_description varchar(400),
    experience_location varchar(50),
    experience_days int ,
    experience_capacity int,
    experience_price_default int,
    experience_describe_default varchar(300),
    experience_start_date Date, 
    experience_end_date Date,
    CONSTRAINT FK_EHOST FOREIGN KEY (host_id)
    REFERENCES hosts(host_id)
);


CREATE TABLE addressbook (
    contact_id int PRIMARY KEY auto_increment,
    user_id int NOT NULL,
    Contact_name varchar(50),
    Contact_mobile varchar(15),
    Contact_city varchar(50),
    Contact_profession varchar(50),
    CONSTRAINT FK_USERS FOREIGN KEY (user_id)
    REFERENCES users(user_id)
);