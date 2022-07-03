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

def getTeam_ByName_resolver(obj, info, name):
    try:
        team = Team.query.filter_by(name=name).first()
        payload = {
            "success": True,
            "team": team.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Team item matching {name} not found"]
        }
    return payload

def getTeam_ByRegion_resolver(obj, info, region):
    try:
        teams =  [team.to_dict() for team in Team.query.filter_by(region=region)]
        payload = {
            "success": True,
            "teams": teams
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Region item matching {region} not found"]
        }
    return payload

def listRegions_resolver(obj, info):
    try:
        regions = [region.to_dict() for region in Region.query.all()]
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


def listPlayers_resolver(obj, info):
    try:
        players = [player.to_dict() for player in Player.query.all()]
        payload = {
            "success": True,
            "player": players
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

def getPlayer_ByName_resolver(obj, info, name):
    try:
        player = Player.query.filter_by(name=name).first()
        payload = {
            "success": True,
            "player": player.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Player item matching {name} not found"]
        }
    return payload

def getPlayer_ByRegion_resolver(obj, info, region):
    try:
        players = [player.to_dict() for player in Player.query.filter_by(region=region)]
        payload = {
            "success": True,
            "player": players
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Region item matching {region} not found"]
        }
    return payload
