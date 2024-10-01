use mednotedatabase;

INSERT INTO `users`(`userEmail`, `userKey`, `salt`) VALUES ('test1@gmail.com', 'a', 'z');

INSERT INTO `users`(`userEmail`, `userKey`, `salt`) VALUES ('test2@gmail.com', '---', '---');

INSERT INTO `patients`(`patientName`, `userID`) VALUES ('u1 patient1','1');
INSERT INTO `patients`(`patientName`, `userID`) VALUES ('u1 patient2','1');
INSERT INTO `patients`(`patientName`, `userID`) VALUES ('u2 patient1','2');

INSERT INTO `meds`(`medName`, `qty`, `qtyUnit`, `notes`, `patientID`) VALUES ('Crocin', 200, 'mg', 'Before eating', 1);
INSERT INTO `meds`(`medName`, `qty`, `qtyUnit`, `notes`, `patientID`) VALUES ('Calpol', 2, 'pills', 'after eating 2 biscuits',1);
INSERT INTO `meds`(`medName`, `qty`, `qtyUnit`, `notes`, `patientID`) VALUES ('Paracetamol', 50, 'ml', 'mixed in water',2);