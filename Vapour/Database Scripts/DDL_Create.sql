create database SDB;

create table SDB.Developers
(
	dev_id int auto_increment primary key,
	name varchar(100)
);

create table SDB.Publishers
(
	pub_id int auto_increment primary key,
	name varchar(100)
);

create table SDB.Ratings
(
    rating_id int auto_increment primary key,
    name varchar(30)
	/*
	Ratings:
	Overwhelmingly Positive,
	Very Positive,
	Mostly Positive,
	Mixed,
	Mostly Negative,
	Very Negative,
	Overwhelmingly Negative
	*/
);

create table SDB.Genre
(
    genre_id int auto_increment primary key,
    name varchar(100) NOT NULL
);

create table SDB.Accounts
(
    acc_id int auto_increment primary key,
    name varchar(32) NOT NULL,
    level int
);

create table SDB.Games
(
    game_id int auto_increment primary key,
    name varchar(200) NOT NULL,
	cost decimal(7, 2),
	developer int,
	publisher int,
	rating int,
	genre_one int,
    genre_two int,
    genre_three int,
	total_achivements int,
	description varchar(400),

    foreign key (rating) references SDB.Ratings(rating_id),
    foreign key (genre_one) references SDB.Genre(Genre_id),
    foreign key (genre_two) references SDB.Genre(Genre_id),
    foreign key (genre_three) references SDB.Genre(Genre_id),
	foreign key (developer) references SDB.Developers(dev_id),
	foreign key (publisher) references SDB.Publishers(pub_id)
);

create table SDB.AGJunction
(
	-- Acts as a junction between accounts and games
    id int auto_increment primary key,
    acc_id int NOT NULL,
    game_id int NOT NULL,
    hours_played int,
    achievements_unlocked int, -- AGJunction.achievements_unlocked <= Games.total_achivements

	foreign key (acc_id) references SDB.Accounts(acc_id),
    foreign key (game_id) references SDB.Games(game_id)
);
