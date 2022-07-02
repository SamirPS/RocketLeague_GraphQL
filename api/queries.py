from .models import Team
from ariadne import convert_kwargs_to_snake_case

def listTeams_resolver(obj, info):
    try:
        teams = [team.to_dict() for team in Team.query.all()]
        print(teams)
        payload = {
            "success": True,
            "teams": teams
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def getTeam_ByName_resolver(obj, info, name):
    try:
        team = Team.query.filter_by(name=name).first()
        payload = {
            "success": True,
            "team": team.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": [f"Team item matching {name} not found"]
        }
    return payload