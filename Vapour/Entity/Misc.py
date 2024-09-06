from Entity.DatabaseConnection import DatabaseConnection

class account:
    def __init__(self, dbconn):
        self.dbconn = dbconn

    # getters and setters for each attribute 

    def setacc_id(self, id):
        self.acc_id = id
    def getacc_id(self):
        return self.acc_id
    
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    
    def setLevel(self, level):
        self.level = level
    def getLevel(self):
        return self.level
    
    def insert(self):   
        tempconn = self.dbconn.getConnection()  # get the database connection
        mysqlcursor = tempconn.cursor()    # get a cursor
        sql = 'insert into Accounts (name, level) values (%s, 0)'
        val = [self.name]
        mysqlcursor.execute(sql, val)
        tempconn.commit()
    
    def delete(self):
        # this delete assumes that the water_systems object to be deleted has been found
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()
        sql = 'delete from Accounts where acc_id = %s'
        val = [self.acc_id]
        mysqlcursor.execute(sql, val)
        tempconn.commit()

    def findByID(self, ID):
        # get the connection
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # here is the sql
        sql = "select name, level from accounts where acc_id = %s"
        # it only need one value, the ID, but val needs to be a list, so I put [ ] around it
        val = [ID]
        mysqlcursor.execute(sql, val)
        myresults = mysqlcursor.fetchone()
        # once the record is found, load the values into the objects attributes (I could do it this way or use the setters methods)
        self.acc_id = ID
        self.name = myresults[0]
        self.level = myresults[1]
   
    def findAll(self):
        # this method will return a list of account objects
        ACCList = list()  # create empty list

        # get database connection
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # create the sql
        sql = "select acc_id, name, level from Accounts order by acc_id"
        mysqlcursor.execute(sql)
        # get all of the results
        myresults = mysqlcursor.fetchall()
        # loop through each result
        for myrow in myresults:
            # create a new water_systems object
            tempacc = account(self.dbconn)
            # load the values into the attributes of the object using the setter methods
            tempacc.setacc_id(int(myrow[0]))
            tempacc.setName(myrow[1])
            tempacc.setLevel(int(myrow[2]))
            
            ACCList.append(tempacc)
        # return the list of water_systems objects
        return ACCList

class game:
    def __init__(self, dbconn):
        self.dbconn = dbconn

    def setgame_id(self, id):
        self.game_id = id
    def getgame_id(self):
        return self.game_id 
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setCost(self, cost):
        self.cost = cost
    def getCost(self):
        return self.cost
    def setDev(self, dev):
        self.developer = dev
    def getDev(self):
        return self.developer
    def setPub(self, pub):
        self.publisher = pub
    def getPub(self):
        return self.publisher
    def setRating(self, rating):
        self.rating = rating
    def getRating(self):
        return self.rating
    def setGenreOne(self, genre_one):
        self.genre_one = genre_one
    def getGenreOne(self):
        return self.genre_one
    def setGenreTwo(self, genre_two):
        self.genre_two = genre_two
    def getGenreTwo(self):
        return self.genre_two
    def setGenreThree(self, genre_three):
        self.genre_three = genre_three
    def getGenreThree(self):
        return self.genre_three
    def setTotalAchievements(self, total_achievements):
        self.total_achievements = total_achievements
    def getTotalAchievements(self):
        return self.total_achievements
    def setDescription(self, description):
        self.description = description
    def getDescription(self):
        return self.description
    
    def insert(self):   
        tempconn = self.dbconn.getConnection()  # get the database connection
        mysqlcursor = tempconn.cursor()    # get a cursor
        sql = 'insert into Games (name, cost, developer, publisher, rating, genre_one, genre_two, genre_three, total_achivements, description) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (self.name, self.cost, self.developer, self.publisher, self.rating, self.genre_one, self.genre_two, self.genre_three, self.total_achievements, self.description)
        mysqlcursor.execute(sql, val)
        tempconn.commit()

    def findByID(self, ID):
        # get the connection
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # here is the sql
        sql = "select name, cost, developer, publisher, rating, genre_one, genre_two, genre_three, total_achivements, description from Games where game_id = %s"
        # it only need one value, the ID, but val needs to be a list, so I put [ ] around it
        val = [ID]
        mysqlcursor.execute(sql, val)
        myresults = mysqlcursor.fetchone()
        # once the record is found, load the values into the objects attributes (I could do it this way or use the setters methods)
        self.game_id = ID
        self.name = myresults[0]
        self.cost = myresults[1]
        self.developer = myresults[2]
        self.publisher = myresults[3]
        self.rating = myresults[4]
        self.genre_one = myresults[5]
        self.genre_two = myresults[6]
        self.genre_three = myresults[7]
        self.total_achivements = myresults[8]
        self.description = myresults[9]


    def findAll(self):
        # this method will return a list of water_systems objects
        WSList = list()  # create empty list

        # get database connection
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # create the sql (super long query)
        sql = "SELECT g.game_id, g.name, g.cost, d.name AS developer_name, p.name AS publisher_name, r.name AS rating_name, ge1.name AS genre_one_name, ge2.name AS genre_two_name, ge3.name AS genre_three_name, g.total_achivements, g.description FROM SDB.Games g JOIN SDB.Developers d ON g.developer = d.dev_id JOIN SDB.Publishers p ON g.publisher = p.pub_id LEFT JOIN SDB.Ratings r ON g.rating = r.rating_id LEFT JOIN SDB.Genre ge1 ON g.genre_one = ge1.genre_id LEFT JOIN SDB.Genre ge2 ON g.genre_two = ge2.genre_id LEFT JOIN SDB.Genre ge3 ON g.genre_three = ge3.genre_id ORDER BY g.game_id;"
        mysqlcursor.execute(sql)
        # get all of the results
        myresults = mysqlcursor.fetchall()
        # loop through each result
        for myrow in myresults:
            # create a new water_systems object
            tempws = game(self.dbconn)
            # load the values into the attributes of the object using the setter methods
            tempws.setgame_id(int(myrow[0]))
            tempws.setName(myrow[1])
            tempws.setCost(float(myrow[2]))
            tempws.setDev((myrow[3]))
            tempws.setPub((myrow[4]))
            tempws.setRating((myrow[5]))
            tempws.setGenreOne((myrow[6]))
            tempws.setGenreTwo((myrow[7]))
            tempws.setGenreThree((myrow[8]))
            tempws.setTotalAchievements(int(myrow[9]))
            tempws.setDescription(myrow[10])
            # add that water_systems object to the list
            WSList.append(tempws)
        # return the list of water_systems objects
        return WSList
    
    def printGenre(self):
        # get database connection
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # create the sql (super long query)
        sql = "select genre_id, name from Genre order by genre_id"
        mysqlcursor.execute(sql)

        # get all of the results
        myresults = mysqlcursor.fetchall()
        # loop through each result
        print('Genres:')
        for myrow in myresults:
                print( str(myrow[0]) + '. ' + myrow[1])

    def printDevs(self):
        # get database connection
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # create the sql (super long query)
        sql = "select dev_id, name from Developers order by dev_id"
        mysqlcursor.execute(sql)

        # get all of the results
        myresults = mysqlcursor.fetchall()
        # loop through each result
        print('Developers:')
        for myrow in myresults:
                print( str(myrow[0]) + '. ' + myrow[1])

    def printPubs(self):
        # get database connection
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # create the sql (super long query)
        sql = "select pub_id, name from Publishers order by pub_id"
        mysqlcursor.execute(sql)

        # get all of the results
        myresults = mysqlcursor.fetchall()
        # loop through each result
        print('Publishers:')
        for myrow in myresults:
                print( str(myrow[0]) + '. ' + myrow[1])

    
class AGJ:
    def __init__(self, dbconn):
        self.dbconn = dbconn

    # getters and setters for each attribute
    def setacc_id(self, id):
        self.acc_id = id
    def getacc_id(self):
        return self.acc_id
    
    def setgame_id(self, id):
        self.game_id = id
    def getgame_id(self):
        return self.game_id
    
    def setHoursPlayed(self, hours):
        self.hours_played = hours
    def getHoursPlayed(self):
        return self.hours_played

    def setAchievements(self, n):
        self.achievements_unlocked = n
    def getAchievements(self):
        return self.achievements_unlocked
    
    def findByID(self, acc, game):
        # get the connection
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # here is the sql
        sql = "select acc_id, game_id, hours_played, achievements_unlocked from AGJunction where acc_id = %s AND game_id = %s"
        # it only need one value, the ID, but val needs to be a list, so I put [ ] around it
        val = (acc, game)
        mysqlcursor.execute(sql, val)
        myresults = mysqlcursor.fetchone()
        # once the record is found, load the values into the objects attributes (I could do it this way or use the setters methods)
        self.acc_id = myresults[0]
        self.game_id = myresults[1]
        self.hours_played = myresults[2]
        self.achievements_unlocked = myresults[3]
    
    def increaseHour(self, acc, game, hours):
        # this update assumes that the water_systems object already has the values for the attributes that need to be updated

        tempconn = self.dbconn.getConnection()  # get the connection
        mysqlcursor = tempconn.cursor()

        # create the sql and set up the values
        sql = 'update AGJunction set hours_played = hours_played + %s where acc_id = %s AND game_id = %s'
        val = (hours, acc, game)
        # execute the sql
        mysqlcursor.execute(sql, val)
        # commit
        tempconn.commit()

    def buyGame(self, acc, game):

        tempconn = self.dbconn.getConnection()  # get the connection
        mysqlcursor = tempconn.cursor()

        # create the sql and set up the values
        sql = 'insert into AGJunction (acc_id, game_id, hours_played, achievements_unlocked) values (%s, %s, 0, 0)'
        val = (acc, game)
        # execute the sql
        mysqlcursor.execute(sql, val)
        # commit
        tempconn.commit()

    def printLite(self,acc):
        # get database connection
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # create the sql
        sql = 'select g.game_id, g.name, j.hours_played from AGJunction j join games g on j.game_id = g.game_id where j.acc_id = %s' 
        val = [acc]

        mysqlcursor.execute(sql, val)
        # get all of the results
        myresults = mysqlcursor.fetchall()
        # loop through each result
        if(myresults):
            for myrow in myresults:
                print( str(myrow[0]) + '. ' + myrow[1])
        else:
                print('You have no games! Head over to the store to get some.')

    def printOwnedGames(self, acc):
        # get database connection
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # create the sql
        sql = 'select g.game_id, g.name, j.hours_played, j.achievements_unlocked from AGJunction j join games g on j.game_id = g.game_id where j.acc_id = %s' 
        val = [acc]

        mysqlcursor.execute(sql, val)
        # get all of the results
        myresults = mysqlcursor.fetchall()
        # loop through each result
        if(myresults):
            for myrow in myresults:
                print( str(myrow[0]) + '. ' + myrow[1] + ' || ' + str(myrow[2]) + ' Hours' + ' || Achievements Unlocked:' + str(myrow[3]))
        else:
                print('You have no games! Head over to the store to get some.')

    def printStats(self, acc):

        hoursPlayed = 0
        moneySpent = 0
        achievementsEarned = 0
        # get database connection
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Get total hours played
        sql = 'select g.cost, j.hours_played, j.achievements_unlocked from AGJunction j join games g on j.game_id = g.game_id where j.acc_id = %s' 
        val = [acc]
        mysqlcursor.execute(sql, val)
        myresults = mysqlcursor.fetchall()
        for myrow in myresults:
            moneySpent = moneySpent + myrow[0]
            hoursPlayed = hoursPlayed + myrow[1]
            achievementsEarned = achievementsEarned + myrow[2]

        print('Total Hours Spent Playing: ' + str(hoursPlayed))
        print('Total Achievements Earned: ' + str(achievementsEarned))
        print('Total Money Spent: ' + str(moneySpent) + '$')

    def achievementGet(self, acc, game, ach):
        # get database connection
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Get total hours played
        sql = 'update AGJunction set achievements_unlocked = achievements_unlocked + %s where acc_id = %s AND game_id = %s' 
        val = (ach, acc, game)
        mysqlcursor.execute(sql, val)
        # commit
        tempconn.commit()
        print('You unlocked ' + str(ach) + ' achievements this session!')


            

        