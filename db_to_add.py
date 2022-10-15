from app import db
from test_scrap import *

with app.app_context():
    db.drop_all()
    db.session.commit()

    db.create_all()


    from api.models import Region

    EU=Region(name="EU")
    NA=Region(name="NA")
    OCE=Region(name="OCE")
    SAM=Region(name="SAM")
    MENA=Region(name="MENA")
    APAC=Region(name="APAC")
    SSA=Region(name="SSA")

    db.session.add(EU)
    db.session.add(NA)
    db.session.add(OCE)
    db.session.add(SAM)
    db.session.add(MENA)
    db.session.add(APAC)
    db.session.add(SSA)


    db.session.commit()

    from api.models import Team

    EU_Team=Get_Teams("Portal:Teams/Europe")
    NA_Team=Get_Teams("Portal:Teams/North_America")
    OCE_Team=Get_Teams("Portal:Teams/Oceania")
    SAM_Team=Get_Teams("Portal:Teams/South_America")
    MENA_Team=Get_Teams("Portal:Teams/Middle_East_and_North_Africa")
    APAC_Team=Get_Teams("Portal:Teams/Asia-Pacific")
    SSA_Team=Get_Teams("Portal:Teams/Sub-Saharan_Africa")


    for i in EU_Team:
        x=Team(region="EU",name=i["name"],player_one=i["1"],player_two=i["2"],player_three=i["3"],player_sub=i["sub"],coach=i["coach"])
        db.session.add(x)
        db.session.commit()

    for i in NA_Team:
        x=Team(region="NA",name=i["name"],player_one=i["1"],player_two=i["2"],player_three=i["3"],player_sub=i["sub"],coach=i["coach"])
        db.session.add(x)
        db.session.commit()

    for i in OCE_Team:
        x=Team(region="OCE",name=i["name"],player_one=i["1"],player_two=i["2"],player_three=i["3"],player_sub=i["sub"],coach=i["coach"])
        db.session.add(x)
        db.session.commit()
    for i in SAM_Team:
        x=Team(region="SAM",name=i["name"],player_one=i["1"],player_two=i["2"],player_three=i["3"],player_sub=i["sub"],coach=i["coach"])
        db.session.add(x)
        db.session.commit()
    for i in MENA_Team:
        x=Team(region="MENA",name=i["name"],player_one=i["1"],player_two=i["2"],player_three=i["3"],player_sub=i["sub"],coach=i["coach"])
        db.session.add(x)
        db.session.commit()
    for i in APAC_Team:
        x=Team(region="APAC",name=i["name"],player_one=i["1"],player_two=i["2"],player_three=i["3"],player_sub=i["sub"],coach=i["coach"])
        db.session.add(x)
        db.session.commit()
    for i in SSA_Team:
        x=Team(region="SSA",name=i["name"],player_one=i["1"],player_two=i["2"],player_three=i["3"],player_sub=i["sub"],coach=i["coach"])
        db.session.add(x)
        db.session.commit()


    from api.models import Player

    all_player=get_players("Portal:Players/Europe",10)+get_players("Portal:Players/Americas",10)+get_players("Portal:Players/Oceania",10)+get_players("Portal:Players/Asia",10)+get_players("Portal:Players/Africa",10)

    for i in all_player:
        x=Player(name=i["name"],pseudo=i["pseudo"],nationality=i["nationality"],born=i["born"],status=i["status"],team=i["team"],otherpseudo=i["otherpseudo"],winningmonney=i["winningmonney"])
        db.session.add(x)
        db.session.commit()

    from api.models import Transfer

    for i in Get_Transfer():
        x=Transfer(date=i["date"],players=i["players"],oldteam=i["oldteam"],newteam=i["newteam"])
        db.session.add(x)
        db.session.commit()

    from api.models import Matches

    for i in Get_Ongoing_And_Upcoming_Matches():
        x=Matches(countdown=i["countdown"],team_un=i["team_un"],team_deux=i["team_deux"],score=i["score"])
        db.session.add(x)
        db.session.commit()

