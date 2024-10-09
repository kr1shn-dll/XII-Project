create database Continental;
use Continental;
CREATE TABLE customers(`UID` INT NOT NULL,`Name` VARCHAR(32) NOT NULL,`Phone` VARCHAR(10) NOT NULL,
  `Email` VARCHAR(45) NOT NULL,`Address` VARCHAR(45) NOT NULL,`Room` VARCHAR(45) NULL,PRIMARY KEY (`UID`));
create table Rooms( `RID` INT NOT NULL,`Name` VARCHAR(10) NOT NULL,`Floor` INT NOT NULL,
  `ac` VARCHAR(6) NOT NULL,`Cost` INT NOT NULL,`Occpuant` VARCHAR(45) NULL,`Checkout` VARCHAR(45) NULL,PRIMARY KEY (`RID`));
