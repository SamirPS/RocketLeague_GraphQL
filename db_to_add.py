from app import db
db.drop_all()
db.session.commit()

db.create_all()

from api.models import Region

EU=Region(name="EU")
NA=Region(name="NA")

db.session.add(EU)
db.session.add(NA)

db.session.commit()

from api.models import Team
Vitality = Team(region="EU",name="Vitality",player_one="Kaydop",player_two="Alpha54",player_three="Radosin",player_sub="FairyPeak",coach="Ferra")
Moist = Team(region="NA",name="Moist Esports",player_one="Joyo",player_two="Vatira",player_three="Rise",player_sub="",coach="Noah")

G2 = Team(region="NA",name="G2 Esports",player_one="JKnaps",player_two="Chicago",player_three="Atomic",player_sub="",coach="Satthew")
NRG = Team(region="NA",name="The General NRG",player_one="GarrettG",player_two="jstn",player_three="SquishyMuffinz",player_sub="Musty",coach="Sizz")

db.session.add(Vitality)
db.session.add(Moist)
db.session.add(G2)
db.session.add(NRG)

db.session.commit()

from api.models import Player
Vatira=Player(name="Axel Touret",nationality="France",born="May 14, 2006",region="EU",status="Active",team="Moist Esports",alternate_IDs="Vati",approx_Total_Winnings="74,978")

Turboplosa=Player(name="Pierre Silfver",nationality="Sweden",born="August 9, 1998",region="NA",status="Active",team="OpTic Gaming",alternate_IDs="Turururu, Turbop0lsa, Turbo",approx_Total_Winnings="446,102")

db.session.add(Vatira)
db.session.add(Turboplosa)


db.session.commit()

