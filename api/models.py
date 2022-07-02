from app import db

class Team(db.Model):
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

