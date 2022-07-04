import requests
import re
import time

def Get_Information_About_Team(LinkOfActiveTeams):
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
            Player_Name=re.findall(r'<span style="white-space:pre"><a href="/rocketleague/(.*?)"',j)
            Player_Name[0]=Player_Name[0].replace("index.php?title=","")
            Player_Name[0]=Player_Name[0].replace("&amp;action=edit&amp;redlink=1","")
            if "Substitute" in j:
                Players_Of_The_Team["sub"]=Player_Name[0]
            else:
                Players_Of_The_Team[str(count)]=Player_Name[0]
            count+=1
        Coach_Name=re.findall(r'<tr class="Player coach"(.*?)</tr>',Roster)
        for j in Coach_Name:
            Coach_Name=re.findall(r'<span style="white-space:pre"><a href="/rocketleague/(.*?)"',j)
            Coach_Name[0]=Coach_Name[0].replace("index.php?title=","")
            Coach_Name[0]=Coach_Name[0].replace("&amp;action=edit&amp;redlink=1","")
            Players_Of_The_Team["coach"]=Coach_Name[0]

        i=i.replace("_"," ")
        Players_Of_The_Team["name"]=i
        List_Of_Teams.append(Players_Of_The_Team)
        print(Players_Of_The_Team)
       
    return List_Of_Teams

def Get_Teams(page):

    time.sleep(30)
    headers = {'User-Agent': 'RocketLeague_GraphQL On Github (https://github.com/SamirPS/RocketLeague_GraphQL,samirakarioh1@gmail.com)', 'Accept-Encoding': 'gzip'}
    Notable_Teams=requests.get(f"https://liquipedia.net/rocketleague/api.php?action=parse&page={page}&format=json",headers=headers).json()["parse"]["text"]["*"]
    
    
    start = '<span class="mw-headline" id="Active_teams">Active teams</span>'
    end = '<span class="mw-headline" id="Disbanded_teams">Disbanded teams</span>'
    Active_Team=Notable_Teams[Notable_Teams.find(start)+len(start):Notable_Teams.rfind(end)]

    LinkOfActiveTeam=re.findall(r'<span class="team-template-text"><a href="(.*?)"',Active_Team)

    return Get_Information_About_Team(LinkOfActiveTeam)

def get_players(page):
    time.sleep(30)
    headers = {'User-Agent': 'RocketLeague_GraphQL On Github (https://github.com/SamirPS/RocketLeague_GraphQL,samirakarioh1@gmail.com)', 'Accept-Encoding': 'gzip'}
    Region_Player=requests.get(f"https://liquipedia.net/rocketleague/api.php?action=parse&page={page}&format=json",headers=headers).json()["parse"]["text"]["*"]
    link_players = []
    info_all_player=[]
    rows = re.findall(r'<tr><td style="text-align:left">(.*?)</td>',Region_Player)
    for row in rows:
        link_of_user=re.findall(r'<a href="(.*?)" title="(.*?)">',row)[-1][0]
        if "&amp;action=edit&amp;redlink=1" not in link_of_user:
            link_players.append(link_of_user)
    i=1
    for player in link_players:
        info_about_player={}
        time.sleep(30) 
        player=player.replace("/rocketleague/","")
        Player_in_Progress=requests.get(f"https://liquipedia.net/rocketleague/api.php?action=parse&page={player}&format=json",headers=headers).json()["parse"]["text"]["*"]
       
        
        start = '<div class="fo-nttax-infobox wiki-bordercolor-light">'
        end = '<div class="fo-nttax-infobox-adbox wiki-bordercolor-light">'
        Information_Player_In_Progress=Player_in_Progress[Player_in_Progress.find(start)+len(start):Player_in_Progress.rfind(end)]

        if '<div class="infobox-cell-2">Player</div>' not in Information_Player_In_Progress:
            continue

        Information_Player_In_Progress_all_div={i[0]:i[1] for i in re.findall(r'<div class="infobox-cell-2 infobox-description">(.*?)</div><div class="infobox-cell-2">(.*?)</div>', Information_Player_In_Progress) }
        info_about_player["name"]=Information_Player_In_Progress_all_div["Name:"]
        try:
            info_about_player["born"]=Information_Player_In_Progress_all_div["Born:"]
        except:
            info_about_player["born"]=""
        

        info_about_player["status"]=Information_Player_In_Progress_all_div["Status:"]
        
        info_about_player["winningmonney"]=Information_Player_In_Progress_all_div["Approx. Total Winnings:"]
        try:
            info_about_player["otherpseudo"]=Information_Player_In_Progress_all_div["Alternate IDs:"]
        except:
            info_about_player["otherpseudo"]=""
        try:
            team=re.findall(r'>(.*?)</a>', Information_Player_In_Progress_all_div["Team:"])
            if "&amp;action=edit&amp;redlink=1" in team[-1]:
                info_about_player["team"]=""
            else:
                info_about_player["team"]=team[-1]
        except:
            info_about_player["team"]=""
        
        nationality=re.findall(r'<span class="flag"><a href="/rocketleague/Category:(.*?)"', Information_Player_In_Progress_all_div["Nationality:"])
        info_about_player["nationality"]=",".join(nationality)
        info_all_player.append(info_about_player)
    return info_all_player


