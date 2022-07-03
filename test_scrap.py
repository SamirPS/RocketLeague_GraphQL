import requests
import re
import time

def Get_The_Team(LinkOfActiveTeams):
    List_Of_Teams=[]
    headers = {'User-Agent': 'RocketLeague_GraphQL On Github (https://github.com/SamirPS/RocketLeague_GraphQL,samirakarioh1@gmail.com)', 'Accept-Encoding': 'gzip'}
    for i in LinkOfActiveTeams:
        i=i.replace("/rocketleague/","")
        Players_Of_The_Team={
            "name":"",
            "1":"",
            "2":"",
            "3":"",
            "sub":"",
            "coach":""
        }

        time.sleep(30)
        Team_In_Progress=requests.get(f"https://liquipedia.net/rocketleague/api.php?action=parse&page={i}&format=json",headers=headers).json()["parse"]["text"]["*"]
        start = '<span class="mw-headline" id="Player_Roster">Player Roster</span>'
        end = '<span class="mw-headline" id="Former">Former</span>'
        Roster=Team_In_Progress[Team_In_Progress.find(start)+len(start):Team_In_Progress.rfind(end)]
        Player_Team=re.findall(r'<tr class="Player">(.*?)</tr>',Roster)
        count=1
        for j in Player_Team:
            if "Substitute" in j:
                
                Player_Name=re.findall(r'<span style="white-space:pre"><a href="/rocketleague/(.*?)"',j)
                Players_Of_The_Team["sub"]=Player_Name[0]
            else:
                Player_Name=re.findall(r'<span style="white-space:pre"><a href="/rocketleague/(.*?)"',j)
                Players_Of_The_Team[str(count)]=Player_Name[0]
            count+=1
        Coach_Name=re.findall(r'<tr class="Player coach"(.*?)</tr>',Roster)
        for j in Coach_Name:
            Coach_Name=re.findall(r'<span style="white-space:pre"><a href="/rocketleague/(.*?)"',j)
            Players_Of_The_Team["coach"]=Coach_Name[0]
        
        List_Of_Teams.append(Players_Of_The_Team)
        i=i.replace("_"," ")
        Players_Of_The_Team["name"]=i
    return List_Of_Teams

def Get_EU_Teams():

    time.sleep(30)
    headers = {'User-Agent': 'RocketLeague_GraphQL On Github (https://github.com/SamirPS/RocketLeague_GraphQL,samirakarioh1@gmail.com)', 'Accept-Encoding': 'gzip'}
    EuropeNotableTeams=requests.get("https://liquipedia.net/rocketleague/api.php?action=parse&page=Portal:Teams/Europe&format=json",headers=headers).json()["parse"]["text"]["*"]
    
    
    start = '<span class="mw-headline" id="Active_teams">Active teams</span>'
    end = '<span class="mw-headline" id="Disbanded_teams">Disbanded teams</span>'
    Active_Team=EuropeNotableTeams[EuropeNotableTeams.find(start)+len(start):EuropeNotableTeams.rfind(end)]

    LinkOfActiveTeamEU=re.findall(r'<span class="team-template-text"><a href="(.*?)"',Active_Team)

    return Get_The_Team(LinkOfActiveTeamEU)

def Get_NA_Teams():

    time.sleep(30)
    headers = {'User-Agent': 'RocketLeague_GraphQL On Github (https://github.com/SamirPS/RocketLeague_GraphQL,samirakarioh1@gmail.com)', 'Accept-Encoding': 'gzip'}
    NANotableTeams=requests.get("https://liquipedia.net/rocketleague/api.php?action=parse&page=Portal:Teams/North_America&format=json",headers=headers).json()["parse"]["text"]["*"]

    start = '<span class="mw-headline" id="Active_teams">Active teams</span>'
    end = '<span class="mw-headline" id="Disbanded_teams">Disbanded teams</span>'
    Active_Team=NANotableTeams[NANotableTeams.find(start)+len(start):NANotableTeams.rfind(end)]

    LinkOfActiveTeamNA=re.findall(r'<span class="team-template-text"><a href="(.*?)"',Active_Team)
    return Get_The_Team(LinkOfActiveTeamNA)
    
def Get_OCE_Teams():
    time.sleep(30)
    headers = {'User-Agent': 'RocketLeague_GraphQL On Github (https://github.com/SamirPS/RocketLeague_GraphQL,samirakarioh1@gmail.com)', 'Accept-Encoding': 'gzip'}
    OCENotableTeams=requests.get("https://liquipedia.net/rocketleague/api.php?action=parse&page=Portal:Teams/Oceania&format=json",headers=headers).json()["parse"]["text"]["*"]
    start = '<span class="mw-headline" id="Active_teams">Active teams</span>'
    end = '<span class="mw-headline" id="Disbanded_teams">Disbanded teams</span>'
    Active_Team=OCENotableTeams[OCENotableTeams.find(start)+len(start):OCENotableTeams.rfind(end)]

    LinkOfActiveTeamOCE=re.findall(r'<span class="team-template-text"><a href="(.*?)"',Active_Team)

    return Get_The_Team(LinkOfActiveTeamOCE)    

def Get_SAM_Teams():
    time.sleep(30)
    headers = {'User-Agent': 'RocketLeague_GraphQL On Github (https://github.com/SamirPS/RocketLeague_GraphQL,samirakarioh1@gmail.com)', 'Accept-Encoding': 'gzip'}
    OCENotableTeams=requests.get("https://liquipedia.net/rocketleague/api.php?action=parse&page=Portal:Teams/South_America&format=json",headers=headers).json()["parse"]["text"]["*"]
    start = '<span class="mw-headline" id="Active_teams">Active teams</span>'
    end = '<span class="mw-headline" id="Disbanded_teams">Disbanded teams</span>'
    Active_Team=OCENotableTeams[OCENotableTeams.find(start)+len(start):OCENotableTeams.rfind(end)]

    LinkOfActiveTeamOCE=re.findall(r'<span class="team-template-text"><a href="(.*?)"',Active_Team)

    return Get_The_Team(LinkOfActiveTeamOCE)

def Get_MENA_Teams():
    time.sleep(30)
    headers = {'User-Agent': 'RocketLeague_GraphQL On Github (https://github.com/SamirPS/RocketLeague_GraphQL,samirakarioh1@gmail.com)', 'Accept-Encoding': 'gzip'}
    OCENotableTeams=requests.get("https://liquipedia.net/rocketleague/api.php?action=parse&page=Portal:Teams/Middle_East_and_North_Africa&format=json",headers=headers).json()["parse"]["text"]["*"]
    start = '<span class="mw-headline" id="Active_teams">Active teams</span>'
    end = '<span class="mw-headline" id="Disbanded_teams">Disbanded teams</span>'
    Active_Team=OCENotableTeams[OCENotableTeams.find(start)+len(start):OCENotableTeams.rfind(end)]

    LinkOfActiveTeamOCE=re.findall(r'<span class="team-template-text"><a href="(.*?)"',Active_Team)
    return Get_The_Team(LinkOfActiveTeamOCE)

def Get_APACN_Teams():
    time.sleep(30)
    headers = {'User-Agent': 'RocketLeague_GraphQL On Github (https://github.com/SamirPS/RocketLeague_GraphQL,samirakarioh1@gmail.com)', 'Accept-Encoding': 'gzip'}
    OCENotableTeams=requests.get("https://liquipedia.net/rocketleague/api.php?action=parse&page=Portal:Teams/Asia-Pacific_North&format=json",headers=headers).json()["parse"]["text"]["*"]
    start = '<span class="mw-headline" id="Active_teams">Active teams</span>'
    end = '<span class="mw-headline" id="Disbanded_teams">Disbanded teams</span>'
    Active_Team=OCENotableTeams[OCENotableTeams.find(start)+len(start):OCENotableTeams.rfind(end)]

    LinkOfActiveTeamOCE=re.findall(r'<span class="team-template-text"><a href="(.*?)"',Active_Team)

    return Get_The_Team(LinkOfActiveTeamOCE)

def Get_APACS_Teams():
    time.sleep(30)
    headers = {'User-Agent': 'RocketLeague_GraphQL On Github (https://github.com/SamirPS/RocketLeague_GraphQL,samirakarioh1@gmail.com)', 'Accept-Encoding': 'gzip'}
    OCENotableTeams=requests.get("https://liquipedia.net/rocketleague/api.php?action=parse&page=Portal:Teams/Asia-Pacific_South&format=json",headers=headers).json()["parse"]["text"]["*"]
    start = '<span class="mw-headline" id="Active_teams">Active teams</span>'
    end = '<span class="mw-headline" id="Disbanded_teams">Disbanded teams</span>'
    Active_Team=OCENotableTeams[OCENotableTeams.find(start)+len(start):OCENotableTeams.rfind(end)]

    LinkOfActiveTeamOCE=re.findall(r'<span class="team-template-text"><a href="(.*?)"',Active_Team)
    return Get_The_Team(LinkOfActiveTeamOCE)
    

def Get_SSA_Teams():
    time.sleep(30)
    headers = {'User-Agent': 'RocketLeague_GraphQL On Github (https://github.com/SamirPS/RocketLeague_GraphQL,samirakarioh1@gmail.com)', 'Accept-Encoding': 'gzip'}
    OCENotableTeams=requests.get("https://liquipedia.net/rocketleague/api.php?action=parse&page=Portal:Teams/Sub-Saharan_Africa&format=json",headers=headers).json()["parse"]["text"]["*"]
    start = '<span class="mw-headline" id="Active_teams">Active teams</span>'
    end = '<span class="mw-headline" id="Disbanded_teams">Disbanded teams</span>'
    Active_Team=OCENotableTeams[OCENotableTeams.find(start)+len(start):OCENotableTeams.rfind(end)]

    LinkOfActiveTeamOCE=re.findall(r'<span class="team-template-text"><a href="(.*?)"',Active_Team)

    return Get_The_Team(LinkOfActiveTeamOCE)