from app import db


class Region(db.Model):
    __tablename__ = "region"

    name = db.Column(db.String,primary_key=True)
    def to_dict(self):
        return {
            "name": self.name
        }

class Transfer(db.Model):
    __tablename__ = "transfert"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    players = db.Column(db.String)
    oldteam = db.Column(db.String)
    newteam = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "players" : self.players,
            "oldteam" : self.oldteam,
            "newteam": self.newteam
        }


class Team(db.Model):
    __tablename__ = "team"

    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String)
    name = db.Column(db.String)
    player_one = db.Column(db.String)
    player_two = db.Column(db.String)
    player_three = db.Column(db.String)
    player_sub = db.Column(db.String)
    coach = db.Column(db.String)
    


    def to_dict(self):
        return {
            "id": self.id,
            "region": self.region,
            "name": self.name,
            "player_one": self.player_one,
            "player_two": self.player_two,
            "player_three": self.player_three,
            "player_sub": self.player_sub,
            "coach": self.coach
        }

class Player(db.Model):
    __tablename__ = 'player'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    nationality = db.Column(db.String)
    born = db.Column(db.String)
    status = db.Column(db.String)
    team = db.Column(db.String)
    otherpseudo = db.Column(db.String)
    winningmonney = db.Column(db.String)
    pseudo = db.Column(db.String)
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "nationality": self.nationality,
            "born": self.born,
            "status": self.status,
            "team": self.team,
            "otherpseudo": self.otherpseudo,
            "winningmonney": self.winningmonney,
            "pseudo": self.pseudo
        }






