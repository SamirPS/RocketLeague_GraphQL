from app import db
from test_scrap import *

db.drop_all()
db.session.commit()

db.create_all()

from api.models import Region

EU=Region(name="EU")
NA=Region(name="NA")
OCE=Region(name="OCE")
SAM=Region(name="SAM")
MENA=Region(name="MENA")
APACN=Region(name="APAC N")
APACS=Region(name="APAC S")
SSA=Region(name="SSA")

db.session.add(EU)
db.session.add(NA)
db.session.add(OCE)
db.session.add(SAM)
db.session.add(MENA)
db.session.add(APACN)
db.session.add(APACS)
db.session.add(SSA)


db.session.commit()

from api.models import Team
EU_Team=Get_EU_Teams()

for i in EU_Team:
    x=Team(region="EU",name=i["name"],player_one=i["1"],player_two=i["2"],player_three=i["3"],player_sub=i["sub"],coach=i["coach"])
    db.session.add(x)
    db.session.commit()

G2 = Team(region="NA",name="G2 Esports",player_one="JKnaps",player_two="Chicago",player_three="Atomic",player_sub="",coach="Satthew")
NRG = Team(region="NA",name="The General NRG",player_one="GarrettG",player_two="jstn",player_three="SquishyMuffinz",player_sub="Musty",coach="Sizz")


db.session.add(G2)
db.session.add(NRG)

db.session.commit()

from api.models import Player
Vatira=Player(name="Axel Touret",nationality="France",born="May 14, 2006",region="EU",status="Active",team="Moist Esports",alternate_IDs="Vati",approx_Total_Winnings="74,978")

Turboplosa=Player(name="Pierre Silfver",nationality="Sweden",born="August 9, 1998",region="NA",status="Active",team="OpTic Gaming",alternate_IDs="Turururu, Turbop0lsa, Turbo",approx_Total_Winnings="446,102")

db.session.add(Vatira)
db.session.add(Turboplosa)


db.session.commit()

