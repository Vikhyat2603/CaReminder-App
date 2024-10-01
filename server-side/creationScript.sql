-- -----------------------------------------------------
-- Schema mednotedatabase
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mednotedatabase` DEFAULT CHARACTER SET utf8mb4 ;
USE `mednotedatabase` ;

-- -----------------------------------------------------
-- Table `mednotedatabase`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mednotedatabase`.`users` (
  `userID` INT(11) NOT NULL AUTO_INCREMENT,
  `userEmail` VARCHAR(50) NOT NULL,
  `userKey` VARCHAR(100) NULL DEFAULT NULL,
  `salt` VARCHAR(64) NULL DEFAULT NULL,
  PRIMARY KEY (`userID`),
  UNIQUE INDEX `userEmail` (`userEmail` ASC)
);

-- -----------------------------------------------------
-- Table `mednotedatabase`.`patients`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mednotedatabase`.`patients` (
  `patientID` INT(11) NOT NULL AUTO_INCREMENT,
  `patientName` TINYTEXT NOT NULL,
  `userID` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`patientID`),
  INDEX `userID` (`userID` ASC),
  CONSTRAINT `patients_ibfk_1`
    FOREIGN KEY (`userID`)
    REFERENCES `mednotedatabase`.`users` (`userID`)
    ON DELETE CASCADE
);

-- -----------------------------------------------------
-- Table `mednotedatabase`.`meds`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mednotedatabase`.`meds` (
  `medID` INT(11) NOT NULL AUTO_INCREMENT,
  `medName` TINYTEXT NULL DEFAULT NULL,
  `qty` SMALLINT NULL DEFAULT 0,
  `qtyUnit` TINYTEXT NULL DEFAULT "",
  `notes` TEXT NULL,
  `medTime1` TIME NOT NULL,
  `medTime2` TIME NULL,
  `medTime3` TIME NULL,
  `wasTaken1` TINYINT(1) NOT NULL DEFAULT 0,
  `wasTaken2` TINYINT(1) NOT NULL DEFAULT 0,
  `wasTaken3` TINYINT(1) NOT NULL DEFAULT 0,
  `patientID` INT(11) NOT NULL,
  PRIMARY KEY (`medID`),
  INDEX `patientID` (`patientID` ASC),
  CONSTRAINT `meds_ibfk_1`
    FOREIGN KEY (`patientID`)
    REFERENCES `mednotedatabase`.`patients` (`patientID`)
    ON DELETE CASCADE
);