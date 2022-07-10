from .models import Team,Region,Player,Transfer,Matches

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

def getPlayer_ByPseudo_resolver(obj, info, pseudo):
    try:
        player = Player.query.filter_by(pseudo=pseudo).first()
        payload = {
            "success": True,
            "player": player.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Player item matching {pseudo} not found"]
        }
    return payload

def listTransfert_resolver(obj, info):
    try:
        transferts = [transfert.to_dict() for transfert in Transfer.query.all()]
        payload = {
            "success": True,
            "transfert": transferts
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

def listMatches_resolver(obj, info):
    try:
        matches = [matche.to_dict() for matche in Matches.query.all()]
        payload = {
            "success": True,
            "matche": matches
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
