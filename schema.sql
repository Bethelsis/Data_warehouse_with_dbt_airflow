CREATE TABLE IF NOT EXISTS `stations` 
(

    `ID`  INT PRIMARY KEY,
    `Fwy` VARCHAR(10),
    `Dir` VARCHAR(2),
    `District` VARCHAR(10),
    `County` VARCHAR(10),
    `City` VARCHAR(10),
    `State_PM` VARCHAR(10),
    `Abs_PM` VARCHAR(20),
    `Latitude` VARCHAR(20),
    `Longitude` VARCHAR(20),
    `Length`VARCHAR(20),
    `Type` VARCHAR(3),
    `Lanes`VARCHAR(10),
    `Name` VARCHAR(50),
    `User_ID_1` VARCHAR(6),
    `User_ID_2` VARCHAR(20),
    `User_ID_3` VARCHAR(10),
    `User_ID_4` VARCHAR(10)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;