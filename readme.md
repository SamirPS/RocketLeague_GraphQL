# RocketLeague_GraphQL

[![Run Script](https://github.com/SamirPS/RocketLeague_GraphQL/actions/workflows/main.yml/badge.svg)](https://github.com/SamirPS/RocketLeague_GraphQL/actions/workflows/main.yml)

## Introduction

I created this project to learn how to use GraphQL with python. For this, I used data from the game Rocket League (Team, Region, Player) available via the site: https://liquipedia.net/rocketleague and their api.

## Installation

First you need to install the dependencies:

```python
pip install -r requirements.txt
```

After this, you just need to do the following:

```shell
export FLASK_APP=app.py
flask run
```
And go to http://localhost:5000/

## Scrapping

In order to get the data, i use the api of the Liquipedia Rocket League Website and you can see the limitation and TOS of the API here :

https://liquipedia.net/api-terms-of-use

You can see the function to scrap the teams in the test_scrap.py file. 

## Database

The database is a sqlite3 database.In order to add the data to the database, you can use the script db_to_add.py or with a tool like sqlitebrowser.

## Methods

### Teams

#### Get all teams

If you want to get all the teams in the Sqlite database, you can use the following query:

```graphql
query {
  listAllTeams{
  teams {
    id
    region
    name
    player_one
    player_two
    player_three
    player_sub
    coach
  }
}
}
```

#### Get a team by name

If you want to get information about a team thanks to the name of the team.Use the following query:

```graphql
query {
  getTeam_ByName(name: "NRG"){
  team {
    id
    region
    name
    player_one
    player_two
    player_three
    player_sub
    coach
  }
}
}
```

#### Get a team by region

If you want to get information about all the teams in a region.Use the following query:

```graphql
query {
  getTeam_ByRegion(region: "EU"){
  teams {
    id
    region
    name
    player_one
    player_two
    player_three
    player_sub
    coach
  }
}
}
```

### Region

#### Get all regions

If you want to get all the regions in the Sqlite database, you can use the following query:

```graphql
query {
  listAllRegions {
    region {
      name
    }
  }
}

```

### Player

#### Get all players

If you want to get all the player (Only a few right now ) in the Sqlite database, you can use the following query:

```graphql
query {
  listAllPlayers {
    player {
      id
      name
      nationality
      born
      status
      team
      winningmonney
      otherpseudo
      pseudo
    }
  }
}

```


#### Get a player by name

If you want to get information about a player thanks to the name of the player.Use the following query:

```graphql
query {
  getPlayer_ByName(name: "Axel Touret") {
    player {
      id
      name
      nationality
      born
      status
      team
      winningmonney
      otherpseudo
      pseudo
    }
  }
}

```

#### Get a player by pseudo

If you want to get information about a player thanks to the pseudo of the player.Use the following query:

```graphql
query {
  getPlayer_ByPseudo(pseudo:"FabiDerKrosse"){
    player {
      id
      name
      nationality
      born
      status
      team
      winningmonney
      otherpseudo
      pseudo
    }
  }
}

```



### Transfers

#### Get all transfers

If you want to get all the Transfers listed in the Sqlite database, you can use the following query:

```graphql
query {
  listAlltransferts {
    success
    errors
    transfert {
      id
      players
      oldteam
      newteam
      date
    }
  }
}

```