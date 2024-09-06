
insert into SDB.Developers
(name)
VALUES
('Supergiant Games'),
('Larian Studios'),
('Valve'),
('Rockstar Games'),
('ConcernedApe'),
('Arrowhead Game Studios'),
('CD Projekt Red'),
('Bethesda Game Studios'),
('FromSoftware'),
('Naughty Dog');

insert into SDB.Publishers
(name)
VALUES
('Supergiant Games'),
('Larian Studios'),
('Valve'),
('Rockstar Games'),
('ConcernedApe'),
('Playstation'),
('CD Projekt Red'),
('Bethesda Softworks'),
('Bandai Namco'),
('Sony Interactive Entertainment');

insert into SDB.Ratings
(name)
VALUES
('Overwhelmingly Positive'),
('Very Positive'),
('Mostly Positive'),
('Mixed'),
('Mostly Negative'),
('Very Negative'),
('Overwhelmingly Negative');

insert into SDB.Genre
(name)
VALUES
('Rogue-lite'),
('CRPG'),
('MOBA'),
('Open World'),
('Farming'),
('Shooter'),
('Action'),
('RPG'),
('Platforming'),
('Fighting'),
('Rhythm');

insert into SDB.Accounts
(name, level)
VALUES
('Stromlight Enjoyer', 82),
('gabiru_henchmen', 199),
('Sussy player?', 32),
('Maidenless', 55),
('Gandalf', 30),
('Dragon Slayer', 40),
('Potion Master', 65),
('RogueKnight', 50),
('ShadowWalker', 70);


insert into SDB.Games
(name, cost, developer, publisher, rating, genre_one, genre_two, genre_three, total_achivements, description)
VALUES
('Hades', 24.99, 1, 1, 1, 1, 7, 8, 49, 'Rogue-lite game bout greek mythology'),
('Hades II', 29.99, 1, 1, 2, 1, 7, 8, 4, 'Rogue-lite game bout greek mythology part 2'),
('Divinity Original Sin', 44.99, 2, 2, 1, 2, 8, 7, 97, 'The Divine is dead. The Void approaches'),
('Baldurs Gate 3', 59.99, 2, 2, 1, 2, 8, 7, 90, 'Gather your party and return to the Forgotten Realms'),
('Cyberpunk 2077', 59.99, 7, 7, 4, 7, 4, 8, 45, 'Open world RPG set in Night City'),
('The Witcher 3', 39.99, 7, 7, 1, 7, 8, 2, 78, 'Epic RPG adventure in a fantasy world'),
('Skyrim', 29.99, 8, 8, 2, 4, 7, 8, 75, 'Open world RPG with dragons and magic'),
('Fallout 4', 29.99, 8, 8, 3, 4, 7, 8, 50, 'Post-apocalyptic open world RPG'),
('Monster Hunter World', 49.99, 8, 8, 1, 7, 4, 8, 60, 'Hunt massive monsters in a vibrant world'),
('Stardew Valley', 14.99, 5, 5, 1, 5, 7, 4, 40, 'Farming and life simulation game'),
('Destiny 2', 0.00, 6, 6, 3, 6, 7, 8, 100, 'Shooter game set in a sci-fi universe'),
('Dark Souls III', 49.99, 9, 9, 1, 7, 8, 6, 43, 'Challenging action RPG'),
('Elden Ring', 59.99, 9, 9, 1, 7, 8, 4, 45, 'Open world action RPG'),
('The Last of Us Part II', 59.99, 10, 10, 1, 7, 4, 8, 26, 'Post-apocalyptic action-adventure'),
('Uncharted 4', 39.99, 10, 10, 2, 7, 4, 8, 24, 'Treasure hunting adventure'),
('Bloodborne', 39.99, 9, 9, 1, 7, 8, 6, 34, 'Gothic action RPG'),
('God of War', 49.99, 10, 10, 1, 7, 4, 8, 37, 'Norse mythology action game'),
('Horizon Zero Dawn', 29.99, 10, 10, 2, 7, 4, 8, 50, 'Futuristic open world adventure');


insert into SDB.AGJunction
(acc_id, game_id, hours_played, achievements_unlocked)
VALUES
-- Account 1
(1, 1, 84, 25),
(1, 4, 120, 45),
(1, 3, 60, 40),
(1, 6, 90, 50),
(1, 5, 100, 70),
-- Account 2
(2, 2, 150, 50),
(2, 7, 100, 60),
(2, 5, 130, 70),
-- Account 3
(3, 6, 120, 45),
(3, 11, 90, 50),
(3, 15, 150, 75),
-- Account 4
(4, 16, 180, 60),
(4, 2, 140, 35),
-- Account 5
(5, 12, 170, 100),
(5, 9, 130, 40),
(5, 10, 110, 26),
-- Account 6
(6, 16, 120, 24),
(6, 12, 150, 60),
-- Account 7
(7, 4, 100, 34),
(7, 2, 180, 37),
(7, 12, 150, 45),
-- Account 8
(8, 3, 130, 25),
(8, 12, 110, 30),
(8, 7, 120, 35),
-- Account 9
(9, 9, 140, 40),
(9, 16, 150, 45);



