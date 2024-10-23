create database Continental;

use Continental;

CREATE TABLE customers(
  `UID` INT NOT NULL,
  `Name` VARCHAR(32) NOT NULL,
  `Phone` VARCHAR(10) NOT NULL,
  `Email` VARCHAR(45) NOT NULL,
  `Address` VARCHAR(45) NOT NULL,
  `Room` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`UID`));

create table Rooms(
  `RID` INT NOT NULL,
  `Name` VARCHAR(10) NOT NULL,
  `Floor` INT NOT NULL,
  `ac` VARCHAR(6) NOT NULL,
  `Cost` INT NOT NULL,
  `Occupant` VARCHAR(45) NOT NULL,
  `Checkout` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`RID`));

insert into customers values(1,'Krishn Sharma','8490657869','sharmak69@gmail.com','Assotech','N/A');
insert into customers values(2,'Shivam Sharma','6414004315','ShivamS@gmail.com','Shahberi','N/A');
insert into customers values(3,'Kapish Singh','7071737809','KSingh@gmail.com','Chipiyana','N/A');

insert into rooms values(1,'A011',1,'AC',500,'N/A','N/A');
insert into rooms values(2,'A024',2,'AC',1500,'N/A','N/A');
insert into rooms values(3,'A036',3,'AC',800,'N/A','N/A');