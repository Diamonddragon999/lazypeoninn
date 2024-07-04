PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE chef (
	id INTEGER NOT NULL, 
	employee_code VARCHAR(255) NOT NULL, 
	name VARCHAR(255) NOT NULL, 
	motto VARCHAR(255) NOT NULL, 
	speciality VARCHAR(255) NOT NULL, 
	description TEXT NOT NULL, 
	avatar VARCHAR(255) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (employee_code), 
	UNIQUE (name), 
	UNIQUE (motto), 
	UNIQUE (speciality), 
	UNIQUE (avatar)
);
INSERT INTO chef VALUES(1,'23fa3629c5a04107a11fa86e3021e582','Mr. Green','Me busy, leave me alone!','Salad','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.         Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.         Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','images/chef1.jpg');
INSERT INTO chef VALUES(2,'cd51107ac1f6427d92ece22c7b3e66e6','Mr. Red','Me not that kind of orc!','Barbeque','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.         Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.         Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','images/chef2.jpg');
INSERT INTO chef VALUES(3,'05388cab0d964427ae46d98031c6050d','Mr. Blue','What...?','Ice Cream','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.         Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.         Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','images/chef3.png');
CREATE TABLE dish (
	id INTEGER NOT NULL, 
	name VARCHAR(255) NOT NULL, 
	price INTEGER NOT NULL, 
	ingredients TEXT NOT NULL, 
	avatar VARCHAR(255) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (name), 
	UNIQUE (avatar)
);
INSERT INTO dish VALUES(1,'Snapjaw roll',14,'snapjaw fillet, fish crust, lemon','images/dish1.jpeg');
INSERT INTO dish VALUES(2,'Pain au pork',10,'pork minced meat, bread, snake oil','images/dish2.png');
INSERT INTO dish VALUES(3,'Spicy squid',15,'squid, hot spices, tomato sauce','images/dish3.png');
INSERT INTO dish VALUES(4,'South sea stew',25,'medalion, tomato, pepper','images/dish4.jpeg');
INSERT INTO dish VALUES(5,'Savory deviate delight',30,'deviate fish, secret chef ingredients','images/dish5.jpg');
INSERT INTO dish VALUES(6,'Grilled Zangar trout',18,'zangar trout, oranges','images/dish6.jpg');
INSERT INTO dish VALUES(7,'Sweet secret',1000,'e1bd444d8bbd53fafeb84020de615b22dee7fcd9a213a0827701d72c4f99f478','images/dish7.png');
CREATE TABLE media (
	id INTEGER NOT NULL, 
	name VARCHAR(255) NOT NULL, 
	path VARCHAR(255) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (name), 
	UNIQUE (path)
);
INSERT INTO media VALUES(1,'Mr. Green slicing','./static/files/mr_green_slice.jpg');
INSERT INTO media VALUES(2,'Mr. Blue smiling','./static/files/mr_blue_smiling.webp');
INSERT INTO media VALUES(3,'Mr. Green cooking','./static/files/mr_green_cooking.jpeg');
INSERT INTO media VALUES(4,'Sweet secret recipe','./static/files/sweet_secret_recipe.txt');
CREATE TABLE user (
	id INTEGER NOT NULL, 
	email VARCHAR(150) NOT NULL, 
	password VARCHAR(150) NOT NULL, 
	name VARCHAR(150) NOT NULL, 
	user_code TEXT NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (email), 
	UNIQUE (user_code)
);
INSERT INTO user VALUES(2,'admin@lazypeon.com','scrypt:32768:8:1$21Yqrx6s8Lxjn1fa$fc3bf6f7a9b04633600c14f2a07c10b1ca278abdc92bb2905e0dfdf0c339dd37c81b7595a3fd96e10fec009befc1bbfda9b59edfd96f4eba0b66d163ef923691','Administrator','4111dc6e4d07768994259d82dbffb5a75b79c61920749949b4976a73e7ccc1a4');
INSERT INTO user VALUES(3,'mrsecret@lazypeon.com','scrypt:32768:8:1$tVGgdagn2bJxlyrs$456cb4c8af0fb0dd1bf0a4ea80b68660ada7a287738448d801726142b505424973e20d2b1e01a1c6873746d3f4394f0f83576ce0edb6c81100949d49d8455690','Mr. Secret','bae03e6165637a3d93ca05b2fdebb4ef3981d7a6d685dee4e1bbc72e22422d2f');
CREATE TABLE review (
	id INTEGER NOT NULL, 
	author INTEGER, 
	review_title VARCHAR(255) NOT NULL, 
	review_text TEXT NOT NULL, 
	review_code VARCHAR(255) NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(author) REFERENCES user (id), 
	UNIQUE (review_code)
);
INSERT INTO review VALUES(1,2,'Best place for a refill','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','6ec002511fc443d0827769577cf7fc80');
INSERT INTO review VALUES(2,3,'Can''t wait to get sick here again!','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','5962bd92e79140e3814e874785465845');
COMMIT;
