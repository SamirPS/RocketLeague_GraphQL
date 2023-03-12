import requests
import re
import time

def Get_Information_About_Team(LinkOfActiveTeams):
    List_Of_Teams=[]
    headers = {'User-Agent': 'RocketLeague_GraphQL On Github (https://github.com/SamirPS/RocketLeague_GraphQL,samirakarioh1@gmail.com)', 'Accept-Encoding': 'gzip'}
    for i in LinkOfActiveTeams:
        try:
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
            Team_In_Progress=requests.get(f"https://liquipedia.net/rocketleague/api.php?action=parse&page={i}&format=json",headers=headers).json()["parse"]
            Team_In_Progress_text_html=Team_In_Progress["text"]["*"]

            start = '<span class="mw-headline" id="Player_Roster">Player Roster</span>'
            end = '<span class="mw-headline" id="Former">Former</span>'
            Roster=Team_In_Progress_text_html[Team_In_Progress_text_html.find(start)+len(start):Team_In_Progress_text_html.rfind(end)]
            Player_Team=re.findall(r'<tr class="Player">(.*?)</tr>',Roster)
            count=1
            for j in Player_Team:
                Player_Name=re.findall(r'<span style="white-space:pre"><a href="/rocketleague/(.*?)"',j)
                Player_Name[0]=Player_Name[0].replace("index.php?title=","")
                Player_Name[0]=Player_Name[0].replace("&amp;action=edit&amp;redlink=1","")
                if "Substitute" in j:
                    Players_Of_The_Team["sub"]=Player_Name[0].replace("_"," ")
                else:
                    Players_Of_The_Team[str(count)]=Player_Name[0].replace("_"," ")
                count+=1
            Coach_Name=re.findall(r'<tr class="Player coach"(.*?)</tr>',Roster)
            for j in Coach_Name:
                Coach_Name=re.findall(r'<span style="white-space:pre"><a href="/rocketleague/(.*?)"',j)
                Coach_Name[0]=Coach_Name[0].replace("index.php?title=","")
                Coach_Name[0]=Coach_Name[0].replace("&amp;action=edit&amp;redlink=1","")
                Players_Of_The_Team["coach"]=Coach_Name[0]

            
            Players_Of_The_Team["name"]=Team_In_Progress["title"]
            List_Of_Teams.append(Players_Of_The_Team)
        except:
            continue
        
       
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

def get_players(page,number=None):
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
    
    if number!=None:
        link_players=link_players[0:number]
        
    for player in link_players:
        info_about_player={}
        time.sleep(30) 
        player=player.replace("/rocketleague/","")
        Player_in_Progress=requests.get(f"https://liquipedia.net/rocketleague/api.php?action=parse&page={player}&format=json",headers=headers).json()["parse"]
        Player_in_Progress_html=Player_in_Progress["text"]["*"]
       
        
        start = '<div class="fo-nttax-infobox wiki-bordercolor-light">'
        end = '<div class="fo-nttax-infobox-adbox wiki-bordercolor-light">'
        Information_Player_In_Progress=Player_in_Progress_html[Player_in_Progress_html.find(start)+len(start):Player_in_Progress_html.rfind(end)]

        if '<div class="infobox-cell-2">Player</div>' not in Information_Player_In_Progress:
            continue

        Information_Player_In_Progress_all_div={i[0]:i[1] for i in re.findall(r'<div class="infobox-cell-2 infobox-description">(.*?)</div><div class="infobox-cell-2">(.*?)</div>', Information_Player_In_Progress) }
        
        try:
            info_about_player["name"]=Information_Player_In_Progress_all_div["Name:"]
        except:
            info_about_player["name"]=""

        try:
            info_about_player["born"]=Information_Player_In_Progress_all_div["Born:"]
        except:
            info_about_player["born"]=""
        
        try:
            info_about_player["status"]=Information_Player_In_Progress_all_div["Status:"]
        except:
            info_about_player["status"]=""
        
        try:
            info_about_player["winningmonney"]=Information_Player_In_Progress_all_div["Approx. Total Winnings:"]
        except:
            info_about_player["winningmonney"]=""

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
        
        try:
            nationality=re.findall(r'<span class="flag"><a href="/rocketleague/Category:(.*?)"', Information_Player_In_Progress_all_div["Nationality:"])
            info_about_player["nationality"]=",".join(nationality)
        except:
            info_about_player["nationality"]=""

        
        info_about_player["pseudo"]=Player_in_Progress["title"]
        info_all_player.append(info_about_player)
    return info_all_player

def Get_Transfer(number_of_transfert=None):
    time.sleep(30)
    headers = {'User-Agent': 'RocketLeague_GraphQL On Github (https://github.com/SamirPS/RocketLeague_GraphQL,samirakarioh1@gmail.com)', 'Accept-Encoding': 'gzip'}
    Last_Transfer=requests.get(f"https://liquipedia.net/rocketleague/api.php?action=parse&page=Transfers&format=json",headers=headers).json()["parse"]["text"]["*"]
    
    start = '<div class="divTable mainpage-transfer Ref" style="text-align: center; width:100%;">'
    end = '<div class="content-ad navigation-not-searchable">'

    Last_Transfer_Information=Last_Transfer[Last_Transfer.find(start)+len(start):Last_Transfer.rfind(end)]
    Last_Transfer_Information=re.findall(r'<div class="divCell Date">(.*?)</div><div class="divCell Name">(.*?)</div><div class="divCell Team OldTeam">(.*?)</div>(.*?)<div class="divCell Team NewTeam">(.*?)</div>', Last_Transfer_Information)

    if number_of_transfert!=None:
        Last_Transfer_Information=Last_Transfer_Information[0:number_of_transfert]
       
    Transfer_List=[]
    for transfert in Last_Transfer_Information:
        transfert_in_progress={
            "date":"",
            "players":"",
            "oldteam":"",
            "newteam":""
        }
        
        transfert_in_progress["date"]=transfert[0]
        Name_Of_Players=re.findall(r'</span> <a href="/rocketleague/(.*?) title="(.*?)">(.*?)</a>', transfert[1])
        transfert_in_progress["players"]=",".join(i[-1] for i in Name_Of_Players)

        if "<i>None</i>" in transfert[2]:
            transfert_in_progress["oldteam"]="None"
        elif "<i>Retired</i>" in transfert[2]:
            transfert_in_progress["oldteam"]="Retired"
        elif '<abbr title="">TBD</abbr>' in transfert[2]:
            transfert_in_progress["oldteam"]="TBD"
        else:
            transfert_in_progress["oldteam"]=re.findall(r'<a href="/rocketleague/(.*?) title="(.*?)">(.*?)</a>', transfert[2])[-1][-1]
        
        if "<i>None</i>" in transfert[4]:
            transfert_in_progress["newteam"]="None"
        elif "<i>Retired</i>" in transfert[4]:
            transfert_in_progress["newteam"]="Retired"
        elif '<i>Inactive</i>' in transfert[4]:
            transfert_in_progress["newteam"]="Inactive"
        elif '<abbr title="">TBD</abbr>' in transfert[4]:
            transfert_in_progress["newteam"]="TBD"
        else:
            transfert_in_progress["newteam"]=re.findall(r'<a href="/rocketleague/(.*?) title="(.*?)">(.*?)</a>', transfert[4])[-1][-1]
        
        Transfer_List.append(transfert_in_progress)

    return Transfer_List

def Get_Ongoing_And_Upcoming_Matches():
    time.sleep(30)
    headers = {'User-Agent': 'RocketLeague_GraphQL On Github (https://github.com/SamirPS/RocketLeague_GraphQL,samirakarioh1@gmail.com)', 'Accept-Encoding': 'gzip'}
    Matches_Page=requests.get(f"https://liquipedia.net/rocketleague/api.php?action=parse&page=Liquipedia:Matches&format=json",headers=headers).json()["parse"]["text"]["*"]

    start = '<div data-toggle-area-content="1">'
    end = '<div data-toggle-area-content="2">'
    Matches_Page_Information=Matches_Page[Matches_Page.find(start)+len(start):Matches_Page.rfind(end)].replace("\n","")
    Matches_Page_Information=re.findall(r'<tbody>(.*?)</tbody>', Matches_Page_Information)

    All_Matches=[]

    for match in Matches_Page_Information:
        match_in_progress={
            "countdown":"",
            "team_un":"",
            "team_deux":"",
            "score":"None",
        } 
        try:
            match_in_progress["team_un"]=re.findall(r'<td class="team-left"><span data-highlightingclass="(.*?)"', match)[0]
        except:
            continue
        try:
            match_in_progress["team_deux"]=re.findall(r'<td class="team-right"><span data-highlightingclass="(.*?)"', match)[0]
        except:
            continue
        try:
            match_in_progress["score"]=re.findall(r'<td class="versus">(.*?)</td>', match)[0]
            if "vs" in match_in_progress["score"].lower():
                match_in_progress["score"]="None"
        except:
            continue

        try:
            match_in_progress["countdown"]=re.findall(r'<span class="timer-object timer-object-countdown-only" (.*?)>(.*?)<', match)[0][1]
        except:
            continue
        
        All_Matches.append(match_in_progress)
    return All_Matches

