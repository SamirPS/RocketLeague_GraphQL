from .models import Team,Region,Player

def listTeams_resolver(obj, info):
    try:
        teams = [team.to_dict() for team in Team.query.all()]
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


def listRegions_resolver(obj, info):
    try:
        regions = [region.to_dict() for region in Region.query.all()]
        print(regions)
        payload = {
            "success": True,
            "region": regions
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

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