# API Football Endpoint Dokümantasyonu

**Oluşturulma Tarihi:** 2025-06-19 22:36:11  
**Toplam Dosya Sayısı:** 26  
**Kaynak Dizin:** C:\Users\Mazzel\Desktop\api-football\api-enpoint-list  

## İçindekiler

- [countries](#countries)
- [fixture-events](#fixture-events)
- [fixture-h2h](#fixture-h2h)
- [fixture-lineups](#fixture-lineups)
- [fixture-playerstatistics](#fixture-playerstatistics)
- [fixture-statistics](#fixture-statistics)
- [fixtures](#fixtures)
- [fixtures-round](#fixtures-round)
- [injures](#injures)
- [leagues.txt](#leaguestxt)
- [odds-live](#odds-live)
- [odds-live-bets](#odds-live-bets)
- [player-profiles](#player-profiles)
- [player-squads](#player-squads)
- [player-statistics](#player-statistics)
- [prematch-bets](#prematch-bets)
- [prematch-bookmakers](#prematch-bookmakers)
- [prematch-mapping](#prematch-mapping)
- [prematch-odds](#prematch-odds)
- [seasons](#seasons)
- [standings](#standings)
- [team-countries](#team-countries)
- [team-statistics](#team-statistics)
- [teamsinfo](#teamsinfo)
- [temp_memory.md](#temp_memorymd)
- [Timezone.txt](#timezonetxt)

---


## countries

**Dosya Boyutu:** 2790 bytes  
**Son Değişiklik:** 2025-06-18 19:05:18  

```text
Countries
Get the list of available countries for the leagues endpoint.

The name and code fields can be used in other endpoints as filters.

To get the flag of a country you have to call the following url: https://media.api-sports.io/flags/{country_code}.svg

Examples available in Request samples "Use Cases".

All the parameters of this endpoint can be used together.

Update Frequency : This endpoint is updated each time a new league from a country not covered by the API is added.

Recommended Calls : 1 call per day.

query Parameters
name	
string
The name of the country

code	
string [ 2 .. 6 ] characters FR, GB-ENG, IT…
The Alpha code of the country

search	
string = 3 characters
The name of the country

header Parameters
x-rapidapi-key
required
string
Your Api-Key

import http.client

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "XxXxXxXxXxXxXxXxXxXxXxXx"
    }

conn.request("GET", "/countries", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))







##################################################
Responses;
200 OK:
Response Schema: application/json
| Field | Type |
|-------|------|
| get | string |
| parameters | Array of objects |
| errors | Array of objects |
| results | integer |
| response | Array of objects |
{
  "get": "countries",
  "parameters": {
    "name": "england"
  },
  "errors": [],
  "results": 1,
  "paging": {
    "current": 1,
    "total": 1
  },
  "response": [
    {
      "name": "England",
      "code": "GB",
      "flag": "https://media.api-sports.io/flags/gb.svg"
    }
  ]
}
###############################################
204 No Content:
Response Schema: application/json
| Field | Type |
|-------|------|
| get | string |
| parameters | Array of objects |
| errors | Array of objects |
| results | integer |
| response | Array of strings |
{
  "get": "countries",
  "parameters": [],
  "errors": {
    "time": "2019-11-26T00:00:00+00:00",
    "bug": "This is on our side, please report us this bug on https://dashboard.api-football.com",
    "report": "countries"
  },
  "results": 0,
  "paging": {
    "current": 1,
    "total": 1
  },
  "response": []
}
#################################################
499 Time Out:
Response Schema: application/json
message	
string
{
  "message": "Something went wrong while fetching details. Try again later."
}
################################################
500 Internal Server Error:
Response Schema: application/json
message	
string
{
  "message": "Something went wrong while fetching details. Try again later."
}
```

---


## fixture-events

**Dosya Boyutu:** 10056 bytes  
**Son Değişiklik:** 2025-06-19 21:58:30  

```text
Events
Get the events from a fixture.

Available events

TYPE				
Goal	Normal Goal	Own Goal	Penalty	Missed Penalty
Card	Yellow Card	Red card		
Subst	Substitution [1, 2, 3...]			
Var	Goal cancelled	Penalty confirmed		
VAR events are available from the 2020-2021 season.
Update Frequency : This endpoint is updated every 15 seconds.

Recommended Calls : 1 call per minute for the fixtures in progress otherwise 1 call per day.

You can also retrieve all the events of the fixtures in progress with to the endpoint fixtures?live=all

Here is an example of what can be achieved

demo-events

query Parameters
fixture
required
integer
The id of the fixture

team	
integer
The id of the team

player	
integer
The id of the player

type	
string
The type

header Parameters
x-rapidapi-key
required
string
Your Api-Key
#####################################
Responses;
200 OK:
Response Schema: application/json

| Field | Type | Description |
|-------|------|-------------|
| get | string | Endpoint name |
| parameters | Array of objects | Query parameters used |
| errors | Array of objects | Error information if any |
| results | integer | Number of results returned |
| response | Array of any | Response data array |
{
  "get": "fixtures/events",
  "parameters": {
    "fixture": "215662"
  },
  "errors": [],
  "results": 18,
  "paging": {
    "current": 1,
    "total": 1
  },
  "response": [
    {
      "time": {
        "elapsed": 25,
        "extra": null
      },
      "team": {
        "id": 463,
        "name": "Aldosivi",
        "logo": "https://media.api-sports.io/football/teams/463.png"
      },
      "player": {
        "id": 6126,
        "name": "F. Andrada"
      },
      "assist": {
        "id": null,
        "name": null
      },
      "type": "Goal",
      "detail": "Normal Goal",
      "comments": null
    },
    {
      "time": {
        "elapsed": 33,
        "extra": null
      },
      "team": {
        "id": 442,
        "name": "Defensa Y Justicia",
        "logo": "https://media.api-sports.io/football/teams/442.png"
      },
      "player": {
        "id": 5936,
        "name": "Julio González"
      },
      "assist": {
        "id": null,
        "name": null
      },
      "type": "Card",
      "detail": "Yellow Card",
      "comments": null
    },
    {
      "time": {
        "elapsed": 33,
        "extra": null
      },
      "team": {
        "id": 463,
        "name": "Aldosivi",
        "logo": "https://media.api-sports.io/football/teams/463.png"
      },
      "player": {
        "id": 6126,
        "name": "Federico Andrada"
      },
      "assist": {
        "id": null,
        "name": null
      },
      "type": "Card",
      "detail": "Yellow Card",
      "comments": null
    },
    {
      "time": {
        "elapsed": 36,
        "extra": null
      },
      "team": {
        "id": 442,
        "name": "Defensa Y Justicia",
        "logo": "https://media.api-sports.io/football/teams/442.png"
      },
      "player": {
        "id": 5931,
        "name": "Diego Rodríguez"
      },
      "assist": {
        "id": null,
        "name": null
      },
      "type": "Card",
      "detail": "Yellow Card",
      "comments": null
    },
    {
      "time": {
        "elapsed": 39,
        "extra": null
      },
      "team": {
        "id": 442,
        "name": "Defensa Y Justicia",
        "logo": "https://media.api-sports.io/football/teams/442.png"
      },
      "player": {
        "id": 5954,
        "name": "Fernando Márquez"
      },
      "assist": {
        "id": null,
        "name": null
      },
      "type": "Card",
      "detail": "Yellow Card",
      "comments": null
    },
    {
      "time": {
        "elapsed": 44,
        "extra": null
      },
      "team": {
        "id": 463,
        "name": "Aldosivi",
        "logo": "https://media.api-sports.io/football/teams/463.png"
      },
      "player": {
        "id": 6262,
        "name": "Emanuel Iñiguez"
      },
      "assist": {
        "id": null,
        "name": null
      },
      "type": "Card",
      "detail": "Yellow Card",
      "comments": null
    },
    {
      "time": {
        "elapsed": 46,
        "extra": null
      },
      "team": {
        "id": 442,
        "name": "Defensa Y Justicia",
        "logo": "https://media.api-sports.io/football/teams/442.png"
      },
      "player": {
        "id": 35695,
        "name": "D. Rodríguez"
      },
      "assist": {
        "id": 5947,
        "name": "B. Merlini"
      },
      "type": "subst",
      "detail": "Substitution 1",
      "comments": null
    },
    {
      "time": {
        "elapsed": 62,
        "extra": null
      },
      "team": {
        "id": 463,
        "name": "Aldosivi",
        "logo": "https://media.api-sports.io/football/teams/463.png"
      },
      "player": {
        "id": 6093,
        "name": "Gonzalo Verón"
      },
      "assist": {
        "id": null,
        "name": null
      },
      "type": "Card",
      "detail": "Yellow Card",
      "comments": null
    },
    {
      "time": {
        "elapsed": 73,
        "extra": null
      },
      "team": {
        "id": 442,
        "name": "Defensa Y Justicia",
        "logo": "https://media.api-sports.io/football/teams/442.png"
      },
      "player": {
        "id": 5942,
        "name": "A. Castro"
      },
      "assist": {
        "id": 6059,
        "name": "G. Mainero"
      },
      "type": "subst",
      "detail": "Substitution 2",
      "comments": null
    },
    {
      "time": {
        "elapsed": 74,
        "extra": null
      },
      "team": {
        "id": 463,
        "name": "Aldosivi",
        "logo": "https://media.api-sports.io/football/teams/463.png"
      },
      "player": {
        "id": 6561,
        "name": "N. Solís"
      },
      "assist": {
        "id": 35845,
        "name": "H. Burbano"
      },
      "type": "subst",
      "detail": "Substitution 1",
      "comments": null
    },
    {
      "time": {
        "elapsed": 75,
        "extra": null
      },
      "team": {
        "id": 463,
        "name": "Aldosivi",
        "logo": "https://media.api-sports.io/football/teams/463.png"
      },
      "player": {
        "id": 6093,
        "name": "G. Verón"
      },
      "assist": {
        "id": 6396,
        "name": "N. Bazzana"
      },
      "type": "subst",
      "detail": "Substitution 2",
      "comments": null
    },
    {
      "time": {
        "elapsed": 79,
        "extra": null
      },
      "team": {
        "id": 463,
        "name": "Aldosivi",
        "logo": "https://media.api-sports.io/football/teams/463.png"
      },
      "player": {
        "id": 6474,
        "name": "G. Gil"
      },
      "assist": {
        "id": 6550,
        "name": "F. Grahl"
      },
      "type": "subst",
      "detail": "Substitution 3",
      "comments": null
    },
    {
      "time": {
        "elapsed": 79,
        "extra": null
      },
      "team": {
        "id": 442,
        "name": "Defensa Y Justicia",
        "logo": "https://media.api-sports.io/football/teams/442.png"
      },
      "player": {
        "id": 5936,
        "name": "J. González"
      },
      "assist": {
        "id": 70767,
        "name": "B. Ojeda"
      },
      "type": "subst",
      "detail": "Substitution 3",
      "comments": null
    },
    {
      "time": {
        "elapsed": 84,
        "extra": null
      },
      "team": {
        "id": 442,
        "name": "Defensa Y Justicia",
        "logo": "https://media.api-sports.io/football/teams/442.png"
      },
      "player": {
        "id": 6540,
        "name": "Juan Rodriguez"
      },
      "assist": {
        "id": null,
        "name": null
      },
      "type": "Card",
      "detail": "Yellow Card",
      "comments": null
    },
    {
      "time": {
        "elapsed": 85,
        "extra": null
      },
      "team": {
        "id": 463,
        "name": "Aldosivi",
        "logo": "https://media.api-sports.io/football/teams/463.png"
      },
      "player": {
        "id": 35845,
        "name": "Hernán Burbano"
      },
      "assist": {
        "id": null,
        "name": null
      },
      "type": "Card",
      "detail": "Yellow Card",
      "comments": null
    },
    {
      "time": {
        "elapsed": 90,
        "extra": null
      },
      "team": {
        "id": 442,
        "name": "Defensa Y Justicia",
        "logo": "https://media.api-sports.io/football/teams/442.png"
      },
      "player": {
        "id": 5912,
        "name": "Neri Cardozo"
      },
      "assist": {
        "id": null,
        "name": null
      },
      "type": "Card",
      "detail": "Yellow Card",
      "comments": null
    },
    {
      "time": {
        "elapsed": 90,
        "extra": null
      },
      "team": {
        "id": 463,
        "name": "Aldosivi",
        "logo": "https://media.api-sports.io/football/teams/463.png"
      },
      "player": {
        "id": 35845,
        "name": "Hernán Burbano"
      },
      "assist": {
        "id": null,
        "name": null
      },
      "type": "Card",
      "detail": "Red Card",
      "comments": null
    },
    {
      "time": {
        "elapsed": 90,
        "extra": null
      },
      "team": {
        "id": 463,
        "name": "Aldosivi",
        "logo": "https://media.api-sports.io/football/teams/463.png"
      },
      "player": {
        "id": 35845,
        "name": "Hernán Burbano"
      },
      "assist": {
        "id": null,
        "name": null
      },
      "type": "Card",
      "detail": "Yellow Card",
      "comments": null
    }
  ]
}
```

---


## fixture-h2h

**Dosya Boyutu:** 3105 bytes  
**Son Değişiklik:** 2025-06-19 21:58:57  

```text
Head To Head
Get heads to heads between two teams.

Update Frequency : This endpoint is updated every 15 seconds.

Recommended Calls : 1 call per minute for the leagues, teams, fixtures who have at least one fixture in progress otherwise 1 call per day.

Here is an example of what can be achieved

demo-h2h

query Parameters
h2h
required
stringID-ID
The ids of the teams

date	
stringYYYY-MM-DD
league	
integer
The id of the league

season	
integer = 4 characters YYYY
The season of the league

last	
integer
For the X last fixtures

next	
integer
For the X next fixtures

from	
stringYYYY-MM-DD
to	
stringYYYY-MM-DD
status	
string
Enum: "NS" "NS-PST-FT"
One or more fixture status short

venue	
integer
The venue id of the fixture

timezone	
string
A valid timezone from the endpoint Timezone

header Parameters
x-rapidapi-key
required
string
Your Api-Key


##########################################
Responses;
200 OK:
Response Schema: application/json
get	
string
parameters	
Array of objects
errors	
Array of objects
results	
integer
response	
Array of any
{
  "get": "fixtures/headtohead",
  "parameters": {
    "h2h": "33-34",
    "last": "1"
  },
  "errors": [],
  "results": 1,
  "paging": {
    "current": 1,
    "total": 1
  },
  "response": [
    {
      "fixture": {
        "id": 157201,
        "referee": "Kevin Friend, England",
        "timezone": "UTC",
        "date": "2019-12-26T17:30:00+00:00",
        "timestamp": 1577381400,
        "periods": {
          "first": 1577381400,
          "second": 1577385000
        },
        "venue": {
          "id": 556,
          "name": "Old Trafford",
          "city": "Manchester"
        },
        "status": {
          "long": "Match Finished",
          "short": "FT",
          "elapsed": 90,
          "extra": null
        }
      },
      "league": {
        "id": 39,
        "name": "Premier League",
        "country": "England",
        "logo": "https://media.api-sports.io/football/leagues/2.png",
        "flag": "https://media.api-sports.io/flags/gb.svg",
        "season": 2019,
        "round": "Regular Season - 19"
      },
      "teams": {
        "home": {
          "id": 33,
          "name": "Manchester United",
          "logo": "https://media.api-sports.io/football/teams/33.png",
          "winner": true
        },
        "away": {
          "id": 34,
          "name": "Newcastle",
          "logo": "https://media.api-sports.io/football/teams/34.png",
          "winner": false
        }
      },
      "goals": {
        "home": 4,
        "away": 1
      },
      "score": {
        "halftime": {
          "home": 3,
          "away": 1
        },
        "fulltime": {
          "home": 4,
          "away": 1
        },
        "extratime": {
          "home": null,
          "away": null
        },
        "penalty": {
          "home": null,
          "away": null
        }
      }
    }
  ]
}
#########################################
```

---


## fixture-lineups

**Dosya Boyutu:** 10894 bytes  
**Son Değişiklik:** 2025-06-19 21:59:28  

```text
Lineups
Get the lineups for a fixture.

Lineups are available between 20 and 40 minutes before the fixture when the competition covers this feature. You can check this with the endpoint leagues and the coverage field.

It's possible that for some competitions the lineups are not available before the fixture, this can be the case for minor competitions

Available datas

Formation
Coach
Start XI
Substitutes
Players' positions on the grid *

X = row and Y = column (X:Y)

Line 1 X being the one of the goal and then for each line this number is incremented. The column Y will go from left to right, and incremented for each player of the line.

* As a new feature, some irregularities may occur, do not hesitate to report them on our public Roadmap

Update Frequency : This endpoint is updated every 15 minutes.

Recommended Calls : 1 call every 15 minutes for the fixtures in progress otherwise 1 call per day.

Here are several examples of what can be done

demo-lineups

demo-lineups

query Parameters
fixture
required
integer
The id of the fixture

team	
integer
The id of the team

player	
integer
The id of the player

type	
string
The type

header Parameters
x-rapidapi-key
required
string
Your Api-Key


###############################################
Responses;
200 OK:
Response Schema: application/json
get	
string
parameters	
Array of objects
errors	
Array of objects
results	
integer
response	
Array of any
{
  "get": "fixtures/lineups",
  "parameters": {
    "fixture": "592872"
  },
  "errors": [],
  "results": 2,
  "paging": {
    "current": 1,
    "total": 1
  },
  "response": [
    {
      "team": {
        "id": 50,
        "name": "Manchester City",
        "logo": "https://media.api-sports.io/football/teams/50.png",
        "colors": {
          "player": {
            "primary": "5badff",
            "number": "ffffff",
            "border": "99ff99"
          },
          "goalkeeper": {
            "primary": "99ff99",
            "number": "000000",
            "border": "99ff99"
          }
        }
      },
      "formation": "4-3-3",
      "startXI": [
        {
          "player": {
            "id": 617,
            "name": "Ederson",
            "number": 31,
            "pos": "G",
            "grid": "1:1"
          }
        },
        {
          "player": {
            "id": 627,
            "name": "Kyle Walker",
            "number": 2,
            "pos": "D",
            "grid": "2:4"
          }
        },
        {
          "player": {
            "id": 626,
            "name": "John Stones",
            "number": 5,
            "pos": "D",
            "grid": "2:3"
          }
        },
        {
          "player": {
            "id": 567,
            "name": "Rúben Dias",
            "number": 3,
            "pos": "D",
            "grid": "2:2"
          }
        },
        {
          "player": {
            "id": 641,
            "name": "Oleksandr Zinchenko",
            "number": 11,
            "pos": "D",
            "grid": "2:1"
          }
        },
        {
          "player": {
            "id": 629,
            "name": "Kevin De Bruyne",
            "number": 17,
            "pos": "M",
            "grid": "3:3"
          }
        },
        {
          "player": {
            "id": 640,
            "name": "Fernandinho",
            "number": 25,
            "pos": "M",
            "grid": "3:2"
          }
        },
        {
          "player": {
            "id": 631,
            "name": "Phil Foden",
            "number": 47,
            "pos": "M",
            "grid": "3:1"
          }
        },
        {
          "player": {
            "id": 635,
            "name": "Riyad Mahrez",
            "number": 26,
            "pos": "F",
            "grid": "4:3"
          }
        },
        {
          "player": {
            "id": 643,
            "name": "Gabriel Jesus",
            "number": 9,
            "pos": "F",
            "grid": "4:2"
          }
        },
        {
          "player": {
            "id": 645,
            "name": "Raheem Sterling",
            "number": 7,
            "pos": "F",
            "grid": "4:1"
          }
        }
      ],
      "substitutes": [
        {
          "player": {
            "id": 50828,
            "name": "Zack Steffen",
            "number": 13,
            "pos": "G",
            "grid": null
          }
        },
        {
          "player": {
            "id": 623,
            "name": "Benjamin Mendy",
            "number": 22,
            "pos": "D",
            "grid": null
          }
        },
        {
          "player": {
            "id": 18861,
            "name": "Nathan Aké",
            "number": 6,
            "pos": "D",
            "grid": null
          }
        },
        {
          "player": {
            "id": 622,
            "name": "Aymeric Laporte",
            "number": 14,
            "pos": "D",
            "grid": null
          }
        },
        {
          "player": {
            "id": 633,
            "name": "İlkay Gündoğan",
            "number": 8,
            "pos": "M",
            "grid": null
          }
        },
        {
          "player": {
            "id": 44,
            "name": "Rodri",
            "number": 16,
            "pos": "M",
            "grid": null
          }
        },
        {
          "player": {
            "id": 931,
            "name": "Ferrán Torres",
            "number": 21,
            "pos": "F",
            "grid": null
          }
        },
        {
          "player": {
            "id": 636,
            "name": "Bernardo Silva",
            "number": 20,
            "pos": "M",
            "grid": null
          }
        },
        {
          "player": {
            "id": 642,
            "name": "Sergio Agüero",
            "number": 10,
            "pos": "F",
            "grid": null
          }
        }
      ],
      "coach": {
        "id": 4,
        "name": "Guardiola",
        "photo": "https://media.api-sports.io/football/coachs/4.png"
      }
    },
    {
      "team": {
        "id": 45,
        "name": "Everton",
        "logo": "https://media.api-sports.io/football/teams/45.png",
        "colors": {
          "player": {
            "primary": "070707",
            "number": "ffffff",
            "border": "66ff00"
          },
          "goalkeeper": {
            "primary": "66ff00",
            "number": "000000",
            "border": "66ff00"
          }
        }
      },
      "formation": "4-3-1-2",
      "startXI": [
        {
          "player": {
            "id": 2932,
            "name": "Jordan Pickford",
            "number": 1,
            "pos": "G",
            "grid": "1:1"
          }
        },
        {
          "player": {
            "id": 19150,
            "name": "Mason Holgate",
            "number": 4,
            "pos": "D",
            "grid": "2:4"
          }
        },
        {
          "player": {
            "id": 2934,
            "name": "Michael Keane",
            "number": 5,
            "pos": "D",
            "grid": "2:3"
          }
        },
        {
          "player": {
            "id": 19073,
            "name": "Ben Godfrey",
            "number": 22,
            "pos": "D",
            "grid": "2:2"
          }
        },
        {
          "player": {
            "id": 2724,
            "name": "Lucas Digne",
            "number": 12,
            "pos": "D",
            "grid": "2:1"
          }
        },
        {
          "player": {
            "id": 18805,
            "name": "Abdoulaye Doucouré",
            "number": 16,
            "pos": "M",
            "grid": "3:3"
          }
        },
        {
          "player": {
            "id": 326,
            "name": "Allan",
            "number": 6,
            "pos": "M",
            "grid": "3:2"
          }
        },
        {
          "player": {
            "id": 18762,
            "name": "Tom Davies",
            "number": 26,
            "pos": "M",
            "grid": "3:1"
          }
        },
        {
          "player": {
            "id": 2795,
            "name": "Gylfi Sigurðsson",
            "number": 10,
            "pos": "M",
            "grid": "4:1"
          }
        },
        {
          "player": {
            "id": 18766,
            "name": "Dominic Calvert-Lewin",
            "number": 9,
            "pos": "F",
            "grid": "5:2"
          }
        },
        {
          "player": {
            "id": 2413,
            "name": "Richarlison",
            "number": 7,
            "pos": "F",
            "grid": "5:1"
          }
        }
      ],
      "substitutes": [
        {
          "player": {
            "id": 18755,
            "name": "João Virgínia",
            "number": 31,
            "pos": "G",
            "grid": null
          }
        },
        {
          "player": {
            "id": 766,
            "name": "Robin Olsen",
            "number": 33,
            "pos": "G",
            "grid": null
          }
        },
        {
          "player": {
            "id": 156490,
            "name": "Niels Nkounkou",
            "number": 18,
            "pos": "D",
            "grid": null
          }
        },
        {
          "player": {
            "id": 18758,
            "name": "Séamus Coleman",
            "number": 23,
            "pos": "D",
            "grid": null
          }
        },
        {
          "player": {
            "id": 138849,
            "name": "Kyle John",
            "number": 48,
            "pos": "D",
            "grid": null
          }
        },
        {
          "player": {
            "id": 18765,
            "name": "André Gomes",
            "number": 21,
            "pos": "M",
            "grid": null
          }
        },
        {
          "player": {
            "id": 1455,
            "name": "Alex Iwobi",
            "number": 17,
            "pos": "F",
            "grid": null
          }
        },
        {
          "player": {
            "id": 18761,
            "name": "Bernard",
            "number": 20,
            "pos": "F",
            "grid": null
          }
        }
      ],
      "coach": {
        "id": 2407,
        "name": "C. Ancelotti",
        "photo": "https://media.api-sports.io/football/coachs/2407.png"
      }
    }
  ]
}
```

---


## fixture-playerstatistics

**Dosya Boyutu:** 2813 bytes  
**Son Değişiklik:** 2025-06-19 22:14:39  

```text
Players statistics
Get the players statistics from one fixture.

Update Frequency : This endpoint is updated every minute.

Recommended Calls : 1 call every minute for the fixtures in progress otherwise 1 call per day.

query Parameters
fixture
required
integer
The id of the fixture

team	
integer
The id of the team

header Parameters
x-rapidapi-key
required
string
Your Api-Key


##############################################
Responses;
200 OK:
Response Schema: application/json
get	
string
parameters	
Array of objects
errors	
Array of objects
results	
integer
response	
Array of any
{
  "get": "fixtures/players",
  "parameters": {
    "fixture": "169080"
  },
  "errors": [],
  "results": 2,
  "paging": {
    "current": 1,
    "total": 1
  },
  "response": [
    {
      "team": {
        "id": 2284,
        "name": "Monarcas",
        "logo": "https://media.api-sports.io/football/teams/2284.png",
        "update": "2020-01-13T16:12:12+00:00"
      },
      "players": [
        {
          "player": {
            "id": 35931,
            "name": "Sebastián Sosa",
            "photo": "https://media.api-sports.io/football/players/35931.png"
          },
          "statistics": [
            {
              "games": {
                "minutes": 90,
                "number": 13,
                "position": "G",
                "rating": "6.3",
                "captain": false,
                "substitute": false
              },
              "offsides": null,
              "shots": {
                "total": 0,
                "on": 0
              },
              "goals": {
                "total": null,
                "conceded": 1,
                "assists": null,
                "saves": 0
              },
              "passes": {
                "total": 17,
                "key": 0,
                "accuracy": "68%"
              },
              "tackles": {
                "total": null,
                "blocks": 0,
                "interceptions": 0
              },
              "duels": {
                "total": null,
                "won": null
              },
              "dribbles": {
                "attempts": 0,
                "success": 0,
                "past": null
              },
              "fouls": {
                "drawn": 0,
                "committed": 0
              },
              "cards": {
                "yellow": 0,
                "red": 0
              },
              "penalty": {
                "won": null,
                "commited": null,
                "scored": 0,
                "missed": 0,
                "saved": 0
              }
            }
          ]
        }
      ]
    }
  ]
}
```

---


## fixture-statistics

**Dosya Boyutu:** 2788 bytes  
**Son Değişiklik:** 2025-06-19 22:16:12  

```text
Statistics
Get the statistics for one fixture.

Available statistics

Shots on Goal
Shots off Goal
Shots insidebox
Shots outsidebox
Total Shots
Blocked Shots
Fouls
Corner Kicks
Offsides
Ball Possession
Yellow Cards
Red Cards
Goalkeeper Saves
Total passes
Passes accurate
Passes %
Update Frequency : This endpoint is updated every minute.

Recommended Calls : 1 call every minute for the teams or fixtures who have at least one fixture in progress otherwise 1 call per day.

Here is an example of what can be achieved

demo-statistics

query Parameters
fixture
required
integer
The id of the fixture

team	
integer
The id of the team

type	
string
The type of statistics

half	
boolean
Default: false
Enum: "true" "false"
Add the halftime statistics in the response Data start from 2024 season for half parameter


###########################################
Responses;
200 OK:
Response Schema: application/json
get	
string
parameters	
Array of objects
errors	
Array of objects
results	
integer
response	
Array of any
{
  "get": "fixtures/statistics",
  "parameters": {
    "team": "463",
    "fixture": "215662"
  },
  "errors": [],
  "results": 1,
  "paging": {
    "current": 1,
    "total": 1
  },
  "response": [
    {
      "team": {
        "id": 463,
        "name": "Aldosivi",
        "logo": "https://media.api-sports.io/football/teams/463.png"
      },
      "statistics": [
        {
          "type": "Shots on Goal",
          "value": 3
        },
        {
          "type": "Shots off Goal",
          "value": 2
        },
        {
          "type": "Total Shots",
          "value": 9
        },
        {
          "type": "Blocked Shots",
          "value": 4
        },
        {
          "type": "Shots insidebox",
          "value": 4
        },
        {
          "type": "Shots outsidebox",
          "value": 5
        },
        {
          "type": "Fouls",
          "value": 22
        },
        {
          "type": "Corner Kicks",
          "value": 3
        },
        {
          "type": "Offsides",
          "value": 1
        },
        {
          "type": "Ball Possession",
          "value": "32%"
        },
        {
          "type": "Yellow Cards",
          "value": 5
        },
        {
          "type": "Red Cards",
          "value": 1
        },
        {
          "type": "Goalkeeper Saves",
          "value": null
        },
        {
          "type": "Total passes",
          "value": 242
        },
        {
          "type": "Passes accurate",
          "value": 121
        },
        {
          "type": "Passes %",
          "value": null
        }
      ]
    }
  ]
}
```

---


## fixtures

**Dosya Boyutu:** 5829 bytes  
**Son Değişiklik:** 2025-06-19 22:16:41  

```text
Fixtures
For all requests to fixtures you can add the query parameter timezone to your request in order to retrieve the list of matches in the time zone of your choice like “Europe/London“

To know the list of available time zones you have to use the endpoint timezone.

Available fixtures status

SHORT	LONG	TYPE	DESCRIPTION
TBD	Time To Be Defined	Scheduled	Scheduled but date and time are not known
NS	Not Started	Scheduled	
1H	First Half, Kick Off	In Play	First half in play
HT	Halftime	In Play	Finished in the regular time
2H	Second Half, 2nd Half Started	In Play	Second half in play
ET	Extra Time	In Play	Extra time in play
BT	Break Time	In Play	Break during extra time
P	Penalty In Progress	In Play	Penaly played after extra time
SUSP	Match Suspended	In Play	Suspended by referee's decision, may be rescheduled another day
INT	Match Interrupted	In Play	Interrupted by referee's decision, should resume in a few minutes
FT	Match Finished	Finished	Finished in the regular time
AET	Match Finished	Finished	Finished after extra time without going to the penalty shootout
PEN	Match Finished	Finished	Finished after the penalty shootout
PST	Match Postponed	Postponed	Postponed to another day, once the new date and time is known the status will change to Not Started
CANC	Match Cancelled	Cancelled	Cancelled, match will not be played
ABD	Match Abandoned	Abandoned	Abandoned for various reasons (Bad Weather, Safety, Floodlights, Playing Staff Or Referees), Can be rescheduled or not, it depends on the competition
AWD	Technical Loss	Not Played	
WO	WalkOver	Not Played	Victory by forfeit or absence of competitor
LIVE	In Progress	In Play	Used in very rare cases. It indicates a fixture in progress but the data indicating the half-time or elapsed time are not available
Fixtures with the status TBD may indicate an incorrect fixture date or time because the fixture date or time is not yet known or final. Fixtures with this status are checked and updated daily. The same applies to fixtures with the status PST, CANC.

The fixtures ids are unique and specific to each fixture. In no case an ID will change.

Not all competitions have livescore available and only have final result. In this case, the status remains in NS and will be updated in the minutes/hours following the match (this can take up to 48 hours, depending on the competition).

Although the data is updated every 15 seconds, depending on the competition there may be a delay between reality and the availability of data in the API.

Update Frequency : This endpoint is updated every 15 seconds.

Recommended Calls : 1 call per minute for the leagues, teams, fixtures who have at least one fixture in progress otherwise 1 call per day.

Here are several examples of what can be achieved

demo-fixtures

query Parameters
id	
integer
Value: "id"
The id of the fixture

ids	
stringMaximum of 20 fixtures ids
Value: "id-id-id"
One or more fixture ids

live	
string
Enum: "all" "id-id"
All or several leagues ids

date	
stringYYYY-MM-DD
A valid date

league	
integer
The id of the league

season	
integer = 4 characters YYYY
The season of the league

team	
integer
The id of the team

last	
integer <= 2 characters
For the X last fixtures

next	
integer <= 2 characters
For the X next fixtures

from	
stringYYYY-MM-DD
A valid date

to	
stringYYYY-MM-DD
A valid date

round	
string
The round of the fixture

status	
string
Enum: "NS" "NS-PST-FT"
One or more fixture status short

venue	
integer
The venue id of the fixture

timezone	
string
A valid timezone from the endpoint Timezone

header Parameters
x-rapidapi-key
required
string
Your Api-Key

########################################################
Responses;
200 OK:
Response Schema: application/json
get	
string
parameters	
Array of objects
errors	
Array of objects
results	
integer
response	
Array of any
{
  "get": "fixtures",
  "parameters": {
    "live": "all"
  },
  "errors": [],
  "results": 4,
  "paging": {
    "current": 1,
    "total": 1
  },
  "response": [
    {
      "fixture": {
        "id": 239625,
        "referee": null,
        "timezone": "UTC",
        "date": "2020-02-06T14:00:00+00:00",
        "timestamp": 1580997600,
        "periods": {
          "first": 1580997600,
          "second": null
        },
        "venue": {
          "id": 1887,
          "name": "Stade Municipal",
          "city": "Oued Zem"
        },
        "status": {
          "long": "Halftime",
          "short": "HT",
          "elapsed": 45,
          "extra": null
        }
      },
      "league": {
        "id": 200,
        "name": "Botola Pro",
        "country": "Morocco",
        "logo": "https://media.api-sports.io/football/leagues/115.png",
        "flag": "https://media.api-sports.io/flags/ma.svg",
        "season": 2019,
        "round": "Regular Season - 14"
      },
      "teams": {
        "home": {
          "id": 967,
          "name": "Rapide Oued ZEM",
          "logo": "https://media.api-sports.io/football/teams/967.png",
          "winner": false
        },
        "away": {
          "id": 968,
          "name": "Wydad AC",
          "logo": "https://media.api-sports.io/football/teams/968.png",
          "winner": true
        }
      },
      "goals": {
        "home": 0,
        "away": 1
      },
      "score": {
        "halftime": {
          "home": 0,
          "away": 1
        },
        "fulltime": {
          "home": null,
          "away": null
        },
        "extratime": {
          "home": null,
          "away": null
        },
        "penalty": {
          "home": null,
          "away": null
        }
      }
    }
  ]
}
```

---


## fixtures-round

**Dosya Boyutu:** 5640 bytes  
**Son Değişiklik:** 2025-06-19 22:17:10  

```text
Rounds
Get the rounds for a league or a cup.

The round can be used in endpoint fixtures as filters

Examples available in Request samples "Use Cases".

Update Frequency : This endpoint is updated every day.

Recommended Calls : 1 call per day.

query Parameters
league
required
integer
The id of the league

season
required
integer = 4 characters YYYY
The season of the league

current	
boolean
Enum: "true" "false"
The current round only

dates	
boolean
Default: false
Enum: "true" "false"
Add the dates of each round in the response

timezone	
string
A valid timezone from the endpoint Timezone

header Parameters
x-rapidapi-key
required
string
Your Api-Key


############################################
Responses;
200 OK:
Response Schema: application/json
get	
string
parameters	
Array of objects
errors	
Array of objects
results	
integer
response	
Array of any
{
  "get": "fixtures/rounds",
  "parameters": {
    "league": "39",
    "season": "2024",
    "dates": "true"
  },
  "errors": [],
  "results": 38,
  "paging": {
    "current": 1,
    "total": 1
  },
  "response": [
    {
      "round": "Regular Season - 1",
      "dates": [
        "2024-08-16",
        "2024-08-17",
        "2024-08-18",
        "2024-08-19"
      ]
    },
    {
      "round": "Regular Season - 2",
      "dates": [
        "2024-08-24",
        "2024-08-25"
      ]
    },
    {
      "round": "Regular Season - 3",
      "dates": [
        "2024-08-31",
        "2024-09-01"
      ]
    },
    {
      "round": "Regular Season - 4",
      "dates": [
        "2024-09-14",
        "2024-09-15"
      ]
    },
    {
      "round": "Regular Season - 5",
      "dates": [
        "2024-09-21",
        "2024-09-22"
      ]
    },
    {
      "round": "Regular Season - 6",
      "dates": [
        "2024-09-28",
        "2024-09-29",
        "2024-09-30"
      ]
    },
    {
      "round": "Regular Season - 7",
      "dates": [
        "2024-10-05",
        "2024-10-06"
      ]
    },
    {
      "round": "Regular Season - 8",
      "dates": [
        "2024-10-19",
        "2024-10-20",
        "2024-10-21"
      ]
    },
    {
      "round": "Regular Season - 9",
      "dates": [
        "2024-10-25",
        "2024-10-26",
        "2024-10-27"
      ]
    },
    {
      "round": "Regular Season - 10",
      "dates": [
        "2024-11-02",
        "2024-11-03",
        "2024-11-04"
      ]
    },
    {
      "round": "Regular Season - 11",
      "dates": [
        "2024-11-09",
        "2024-11-10"
      ]
    },
    {
      "round": "Regular Season - 12",
      "dates": [
        "2024-11-23",
        "2024-11-24",
        "2024-11-25"
      ]
    },
    {
      "round": "Regular Season - 13",
      "dates": [
        "2024-11-29",
        "2024-11-30",
        "2024-12-01"
      ]
    },
    {
      "round": "Regular Season - 14",
      "dates": [
        "2024-12-03",
        "2024-12-04"
      ]
    },
    {
      "round": "Regular Season - 15",
      "dates": [
        "2024-12-07"
      ]
    },
    {
      "round": "Regular Season - 16",
      "dates": [
        "2024-12-14"
      ]
    },
    {
      "round": "Regular Season - 17",
      "dates": [
        "2024-12-21"
      ]
    },
    {
      "round": "Regular Season - 18",
      "dates": [
        "2024-12-26"
      ]
    },
    {
      "round": "Regular Season - 19",
      "dates": [
        "2024-12-29"
      ]
    },
    {
      "round": "Regular Season - 20",
      "dates": [
        "2025-01-04"
      ]
    },
    {
      "round": "Regular Season - 21",
      "dates": [
        "2025-01-14",
        "2025-01-15"
      ]
    },
    {
      "round": "Regular Season - 22",
      "dates": [
        "2025-01-18"
      ]
    },
    {
      "round": "Regular Season - 23",
      "dates": [
        "2025-01-25"
      ]
    },
    {
      "round": "Regular Season - 24",
      "dates": [
        "2025-02-01"
      ]
    },
    {
      "round": "Regular Season - 25",
      "dates": [
        "2025-02-15"
      ]
    },
    {
      "round": "Regular Season - 26",
      "dates": [
        "2025-02-22"
      ]
    },
    {
      "round": "Regular Season - 27",
      "dates": [
        "2025-02-25",
        "2025-02-26"
      ]
    },
    {
      "round": "Regular Season - 28",
      "dates": [
        "2025-03-08"
      ]
    },
    {
      "round": "Regular Season - 29",
      "dates": [
        "2025-03-15"
      ]
    },
    {
      "round": "Regular Season - 30",
      "dates": [
        "2025-04-01",
        "2025-04-02"
      ]
    },
    {
      "round": "Regular Season - 31",
      "dates": [
        "2025-04-05"
      ]
    },
    {
      "round": "Regular Season - 32",
      "dates": [
        "2025-04-12"
      ]
    },
    {
      "round": "Regular Season - 33",
      "dates": [
        "2025-04-19"
      ]
    },
    {
      "round": "Regular Season - 34",
      "dates": [
        "2025-04-26"
      ]
    },
    {
      "round": "Regular Season - 35",
      "dates": [
        "2025-05-03"
      ]
    },
    {
      "round": "Regular Season - 36",
      "dates": [
        "2025-05-10"
      ]
    },
    {
      "round": "Regular Season - 37",
      "dates": [
        "2025-05-18"
      ]
    },
    {
      "round": "Regular Season - 38",
      "dates": [
        "2025-05-25"
      ]
    }
  ]
}
```

---


## injures

**Dosya Boyutu:** 11829 bytes  
**Son Değişiklik:** 2025-06-19 22:17:50  

```text
Injuries
Get the list of players not participating in the fixtures for various reasons such as suspended, injured for example.

Being a new endpoint, the data is only available from April 2021.

There are two types:

Missing Fixture : The player will not play the fixture.
Questionable : The information is not yet 100% sure, the player may eventually play the fixture.
Examples available in Request samples "Use Cases".

All the parameters of this endpoint can be used together.

This endpoint requires at least one parameter.

Update Frequency : This endpoint is updated every 4 hours.

Recommended Calls : 1 call per day.

query Parameters
league	
integer
The id of the league

season	
integer = 4 characters YYYY
The season of the league, required with league, team and player parameters

fixture	
integer
The id of the fixture

team	
integer
The id of the team

player	
integer
The id of the player

date	
stringYYYY-MM-DD
A valid date

ids	
stringMaximum of 20 fixtures ids
Value: "id-id-id"
One or more fixture ids

timezone	
string
A valid timezone from the endpoint Timezone

header Parameters
x-rapidapi-key
required
string
Your Api-Key
####################################################
Responses;
200 OK:
Response Schema: application/json
get	
string
parameters	
Array of objects
errors	
Array of objects
results	
integer
response	
Array of any
{
  "get": "injuries",
  "parameters": {
    "fixture": "686314"
  },
  "errors": [],
  "results": 13,
  "paging": {
    "current": 1,
    "total": 1
  },
  "response": [
    {
      "player": {
        "id": 865,
        "name": "D. Costa",
        "photo": "https://media.api-sports.io/football/players/865.png",
        "type": "Missing Fixture",
        "reason": "Broken ankle"
      },
      "team": {
        "id": 157,
        "name": "Bayern Munich",
        "logo": "https://media.api-sports.io/football/teams/157.png"
      },
      "fixture": {
        "id": 686314,
        "timezone": "UTC",
        "date": "2021-04-07T19:00:00+00:00",
        "timestamp": 1617822000
      },
      "league": {
        "id": 2,
        "season": 2020,
        "name": "UEFA Champions League",
        "country": "World",
        "logo": "https://media.api-sports.io/football/leagues/2.png",
        "flag": null
      }
    },
    {
      "player": {
        "id": 510,
        "name": "S. Gnabry",
        "photo": "https://media.api-sports.io/football/players/510.png",
        "type": "Missing Fixture",
        "reason": "Illness"
      },
      "team": {
        "id": 157,
        "name": "Bayern Munich",
        "logo": "https://media.api-sports.io/football/teams/157.png"
      },
      "fixture": {
        "id": 686314,
        "timezone": "UTC",
        "date": "2021-04-07T19:00:00+00:00",
        "timestamp": 1617822000
      },
      "league": {
        "id": 2,
        "season": 2020,
        "name": "UEFA Champions League",
        "country": "World",
        "logo": "https://media.api-sports.io/football/leagues/2.png",
        "flag": null
      }
    },
    {
      "player": {
        "id": 496,
        "name": "R. Hoffmann",
        "photo": "https://media.api-sports.io/football/players/496.png",
        "type": "Missing Fixture",
        "reason": "Knee Injury"
      },
      "team": {
        "id": 157,
        "name": "Bayern Munich",
        "logo": "https://media.api-sports.io/football/teams/157.png"
      },
      "fixture": {
        "id": 686314,
        "timezone": "UTC",
        "date": "2021-04-07T19:00:00+00:00",
        "timestamp": 1617822000
      },
      "league": {
        "id": 2,
        "season": 2020,
        "name": "UEFA Champions League",
        "country": "World",
        "logo": "https://media.api-sports.io/football/leagues/2.png",
        "flag": null
      }
    },
    {
      "player": {
        "id": 521,
        "name": "R. Lewandowski",
        "photo": "https://media.api-sports.io/football/players/521.png",
        "type": "Missing Fixture",
        "reason": "Knee Injury"
      },
      "team": {
        "id": 157,
        "name": "Bayern Munich",
        "logo": "https://media.api-sports.io/football/teams/157.png"
      },
      "fixture": {
        "id": 686314,
        "timezone": "UTC",
        "date": "2021-04-07T19:00:00+00:00",
        "timestamp": 1617822000
      },
      "league": {
        "id": 2,
        "season": 2020,
        "name": "UEFA Champions League",
        "country": "World",
        "logo": "https://media.api-sports.io/football/leagues/2.png",
        "flag": null
      }
    },
    {
      "player": {
        "id": 514,
        "name": "J. Martinez",
        "photo": "https://media.api-sports.io/football/players/514.png",
        "type": "Missing Fixture",
        "reason": "Knock"
      },
      "team": {
        "id": 157,
        "name": "Bayern Munich",
        "logo": "https://media.api-sports.io/football/teams/157.png"
      },
      "fixture": {
        "id": 686314,
        "timezone": "UTC",
        "date": "2021-04-07T19:00:00+00:00",
        "timestamp": 1617822000
      },
      "league": {
        "id": 2,
        "season": 2020,
        "name": "UEFA Champions League",
        "country": "World",
        "logo": "https://media.api-sports.io/football/leagues/2.png",
        "flag": null
      }
    },
    {
      "player": {
        "id": 162037,
        "name": "M. Tillman",
        "photo": "https://media.api-sports.io/football/players/162037.png",
        "type": "Missing Fixture",
        "reason": "Knee Injury"
      },
      "team": {
        "id": 157,
        "name": "Bayern Munich",
        "logo": "https://media.api-sports.io/football/teams/157.png"
      },
      "fixture": {
        "id": 686314,
        "timezone": "UTC",
        "date": "2021-04-07T19:00:00+00:00",
        "timestamp": 1617822000
      },
      "league": {
        "id": 2,
        "season": 2020,
        "name": "UEFA Champions League",
        "country": "World",
        "logo": "https://media.api-sports.io/football/leagues/2.png",
        "flag": null
      }
    },
    {
      "player": {
        "id": 519,
        "name": "C. Tolisso",
        "photo": "https://media.api-sports.io/football/players/519.png",
        "type": "Missing Fixture",
        "reason": "Tendon Injury"
      },
      "team": {
        "id": 157,
        "name": "Bayern Munich",
        "logo": "https://media.api-sports.io/football/teams/157.png"
      },
      "fixture": {
        "id": 686314,
        "timezone": "UTC",
        "date": "2021-04-07T19:00:00+00:00",
        "timestamp": 1617822000
      },
      "league": {
        "id": 2,
        "season": 2020,
        "name": "UEFA Champions League",
        "country": "World",
        "logo": "https://media.api-sports.io/football/leagues/2.png",
        "flag": null
      }
    },
    {
      "player": {
        "id": 258,
        "name": "J. Bernat",
        "photo": "https://media.api-sports.io/football/players/258.png",
        "type": "Missing Fixture",
        "reason": "Knee Injury"
      },
      "team": {
        "id": 85,
        "name": "Paris Saint Germain",
        "logo": "https://media.api-sports.io/football/teams/85.png"
      },
      "fixture": {
        "id": 686314,
        "timezone": "UTC",
        "date": "2021-04-07T19:00:00+00:00",
        "timestamp": 1617822000
      },
      "league": {
        "id": 2,
        "season": 2020,
        "name": "UEFA Champions League",
        "country": "World",
        "logo": "https://media.api-sports.io/football/leagues/2.png",
        "flag": null
      }
    },
    {
      "player": {
        "id": 769,
        "name": "A. Florenzi",
        "photo": "https://media.api-sports.io/football/players/769.png",
        "type": "Missing Fixture",
        "reason": "Illness"
      },
      "team": {
        "id": 85,
        "name": "Paris Saint Germain",
        "logo": "https://media.api-sports.io/football/teams/85.png"
      },
      "fixture": {
        "id": 686314,
        "timezone": "UTC",
        "date": "2021-04-07T19:00:00+00:00",
        "timestamp": 1617822000
      },
      "league": {
        "id": 2,
        "season": 2020,
        "name": "UEFA Champions League",
        "country": "World",
        "logo": "https://media.api-sports.io/football/leagues/2.png",
        "flag": null
      }
    },
    {
      "player": {
        "id": 216,
        "name": "M. Icardi",
        "photo": "https://media.api-sports.io/football/players/216.png",
        "type": "Missing Fixture",
        "reason": "Muscle Injury"
      },
      "team": {
        "id": 85,
        "name": "Paris Saint Germain",
        "logo": "https://media.api-sports.io/football/teams/85.png"
      },
      "fixture": {
        "id": 686314,
        "timezone": "UTC",
        "date": "2021-04-07T19:00:00+00:00",
        "timestamp": 1617822000
      },
      "league": {
        "id": 2,
        "season": 2020,
        "name": "UEFA Champions League",
        "country": "World",
        "logo": "https://media.api-sports.io/football/leagues/2.png",
        "flag": null
      }
    },
    {
      "player": {
        "id": 263,
        "name": "L. Kurzawa",
        "photo": "https://media.api-sports.io/football/players/263.png",
        "type": "Missing Fixture",
        "reason": "Calf Injury"
      },
      "team": {
        "id": 85,
        "name": "Paris Saint Germain",
        "logo": "https://media.api-sports.io/football/teams/85.png"
      },
      "fixture": {
        "id": 686314,
        "timezone": "UTC",
        "date": "2021-04-07T19:00:00+00:00",
        "timestamp": 1617822000
      },
      "league": {
        "id": 2,
        "season": 2020,
        "name": "UEFA Champions League",
        "country": "World",
        "logo": "https://media.api-sports.io/football/leagues/2.png",
        "flag": null
      }
    },
    {
      "player": {
        "id": 271,
        "name": "L. Paredes",
        "photo": "https://media.api-sports.io/football/players/271.png",
        "type": "Missing Fixture",
        "reason": "Suspended"
      },
      "team": {
        "id": 85,
        "name": "Paris Saint Germain",
        "logo": "https://media.api-sports.io/football/teams/85.png"
      },
      "fixture": {
        "id": 686314,
        "timezone": "UTC",
        "date": "2021-04-07T19:00:00+00:00",
        "timestamp": 1617822000
      },
      "league": {
        "id": 2,
        "season": 2020,
        "name": "UEFA Champions League",
        "country": "World",
        "logo": "https://media.api-sports.io/football/leagues/2.png",
        "flag": null
      }
    },
    {
      "player": {
        "id": 273,
        "name": "M. Verratti",
        "photo": "https://media.api-sports.io/football/players/273.png",
        "type": "Missing Fixture",
        "reason": "Illness"
      },
      "team": {
        "id": 85,
        "name": "Paris Saint Germain",
        "logo": "https://media.api-sports.io/football/teams/85.png"
      },
      "fixture": {
        "id": 686314,
        "timezone": "UTC",
        "date": "2021-04-07T19:00:00+00:00",
        "timestamp": 1617822000
      },
      "league": {
        "id": 2,
        "season": 2020,
        "name": "UEFA Champions League",
        "country": "World",
        "logo": "https://media.api-sports.io/football/leagues/2.png",
        "flag": null
      }
    }
  ]
}
```

---


## leagues.txt

**Dosya Boyutu:** 5056 bytes  
**Son Değişiklik:** 2025-06-19 22:18:19  

```text
Leagues
Get the list of available leagues and cups.

The league id are unique in the API and leagues keep it across all seasons

To get the logo of a competition you have to call the following url: https://media.api-sports.io/football/leagues/{league_id}.png

This endpoint also returns the coverage of each competition, which makes it possible to know what is available for that league or cup.

The values returned by the coverage indicate the data available at the moment you call the API, so for a competition that has not yet started, it is normal to have all the features set to False. This will be updated once the competition has started.

You can find all the leagues ids on our Dashboard.

Example :

"coverage": {
  "fixtures": {
      "events": true,
      "lineups": true,
      "statistics_fixtures": false,
      "statistics_players": false
  },
  "standings": true,
  "players": true,
  "top_scorers": true,
  "top_assists": true,
  "top_cards": true,
  "injuries": true,
  "predictions": true,
  "odds": false
}
In this example we can deduce that the competition does not have the following features: statistics_fixtures, statistics_players, odds because it is set to False.

The coverage of a competition can vary from season to season and values set to True do not guarantee 100% data availability.

Some competitions, such as the friendlies, are exceptions to the coverage indicated in the leagues endpoint, and the data available may differ depending on the match, including livescore, events, lineups, statistics and players.

Competitions are automatically renewed by the API when a new season is available. There may be a delay between the announcement of the official calendar and the availability of data in the API.

For Cup competitions, fixtures are automatically added when the two participating teams are known. For example if the current phase is the 8th final, the quarter final will be added once the teams playing this phase are known.

Examples available in Request samples "Use Cases".

Most of the parameters of this endpoint can be used together.

Update Frequency : This endpoint is updated several times a day.

Recommended Calls : 1 call per hour.

query Parameters
id	
integer
The id of the league

name	
string
The name of the league

country	
string
The country name of the league

code	
string [ 2 .. 6 ] characters FR, GB-ENG, IT…
The Alpha code of the country

season	
integer = 4 characters YYYY
The season of the league

team	
integer
The id of the team

type	
string
Enum: "league" "cup"
The type of the league

current	
string Return the list of active seasons or the las...Show pattern
Enum: "true" "false"
The state of the league

search	
string >= 3 characters
The name or the country of the league

last	
integer <= 2 characters
The X last leagues/cups added in the API

header Parameters
x-rapidapi-key
required
string
Your Api-Key
################################################
200 OK:
Response Schema: application/json
| Field | Type |
|-------|------|
| get | string |
| parameters | Array of objects |
| errors | Array of objects |
| results | integer |
| response | Array of objects |
{
  "get": "leagues",
  "parameters": {
    "id": "39"
  },
  "errors": [],
  "results": 1,
  "paging": {
    "current": 1,
    "total": 1
  },
  "response": [
    {
      "league": {
        "id": 39,
        "name": "Premier League",
        "type": "League",
        "logo": "https://media.api-sports.io/football/leagues/2.png"
      },
      "country": {
        "name": "England",
        "code": "GB",
        "flag": "https://media.api-sports.io/flags/gb.svg"
      },
      "seasons": [
        {
          "year": 2010,
          "start": "2010-08-14",
          "end": "2011-05-17",
          "current": false,
          "coverage": {
            "fixtures": {
              "events": true,
              "lineups": true,
              "statistics_fixtures": false,
              "statistics_players": false
            },
            "standings": true,
            "players": true,
            "top_scorers": true,
            "top_assists": true,
            "top_cards": true,
            "injuries": true,
            "predictions": true,
            "odds": false
          }
        },
        {
          "year": 2011,
          "start": "2011-08-13",
          "end": "2012-05-13",
          "current": false,
          "coverage": {
            "fixtures": {
              "events": true,
              "lineups": true,
              "statistics_fixtures": false,
              "statistics_players": false
            },
            "standings": true,
            "players": true,
            "top_scorers": true,
            "top_assists": true,
            "top_cards": true,
            "injuries": true,
            "predictions": true,
            "odds": false
          }
        }
      ]
    }
  ]
}
```

---


## odds-live

**Dosya Boyutu:** 60107 bytes  
**Son Değişiklik:** 2025-06-19 22:18:57  

```text
odds/live
This endpoint returns in-play odds for fixtures in progress.

Fixtures are added between 15 and 5 minutes before the start of the fixture. Once the fixture is over they are removed from the endpoint between 5 and 20 minutes. No history is stored. So fixtures that are about to start, fixtures in progress and fixtures that have just ended are available in this endpoint.

Update Frequency : This endpoint is updated every 5 seconds.*

* This value can change in the range of 5 to 60 seconds

INFORMATIONS ABOUT STATUS

"status": {
    "stopped": false, // True if the fixture is stopped by the referee for X reason
    "blocked": false, // True if bets on this fixture are temporarily blocked
    "finished": false // True if the fixture has not started or if it is finished
},
INFORMATIONS ABOUT VALUES

When several identical values exist for the same bet the main field is set to True for the bet being considered, the others will have the value False.

The main field will be set to True only if several identical values exist for the same bet.

When a value is unique for a bet the main value will always be False or null.

Example below :

"id": 36,
"name": "Over/Under Line",
"values": [
    {
        "value": "Over",
        "odd": "1.975",
        "handicap": "2",
        "main": true, // Bet to consider
        "suspended": false // True if this bet is temporarily suspended
    },
    {
        "value": "Over",
        "odd": "3.45",
        "handicap": "2",
        "main": false, // Bet to no consider
        "suspended": false
    },
]
query Parameters
fixture	
integer
The id of the fixture

league	
integer (In this endpoint the "season" parameter is ...Show pattern
The id of the league

bet	
integer
The id of the bet

header Parameters
x-rapidapi-key
required
string
Your Api-Key

########################################################
Responses;
200 OK
Response Schema: application/json
get	
string
parameters	
Array of objects
errors	
Array of objects
results	
integer
response	
Array of any
{
    "get": "odds/live",
    "parameters": {
      "fixture": "721238"
    },
    "errors": [],
    "results": 1,
    "paging": {
      "current": 1,
      "total": 1
    },
    "response": [
      {
        "fixture": {
          "id": 721238,
          "status": {
            "long": "Second Half",
            "elapsed": 62,
            "seconds": "62:14"
          }
        },
        "league": {
          "id": 30,
          "season": 2022
        },
        "teams": {
          "home": {
            "id": 1563,
            "goals": 1
          },
          "away": {
            "id": 1565,
            "goals": 0
          }
        },
        "status": {
          "stopped": false,
          "blocked": false,
          "finished": false
        },
        "update": "2022-01-27T16:21:01+00:00",
        "odds": [
          {
            "id": 20,
            "name": "Match Corners",
            "values": [
              {
                "value": "Over",
                "odd": "2.5",
                "handicap": "8",
                "main": null,
                "suspended": false
              },
              {
                "value": "Exactly",
                "odd": "4.333",
                "handicap": "8",
                "main": null,
                "suspended": false
              },
              {
                "value": "Under",
                "odd": "2.2",
                "handicap": "8",
                "main": null,
                "suspended": false
              },
              {
                "value": "Over",
                "odd": "9",
                "handicap": "10",
                "main": null,
                "suspended": false
              },
              {
                "value": "Exactly",
                "odd": "7.5",
                "handicap": "10",
                "main": null,
                "suspended": false
              },
              {
                "value": "Under",
                "odd": "1.181",
                "handicap": "10",
                "main": null,
                "suspended": false
              },
              {
                "value": "Over",
                "odd": "1.615",
                "handicap": "7",
                "main": null,
                "suspended": false
              },
              {
                "value": "Exactly",
                "odd": "4",
                "handicap": "7",
                "main": null,
                "suspended": false
              },
              {
                "value": "Under",
                "odd": "4.333",
                "handicap": "7",
                "main": null,
                "suspended": false
              },
              {
                "value": "Over",
                "odd": "1.2",
                "handicap": "6",
                "main": null,
                "suspended": false
              },
              {
                "value": "Exactly",
                "odd": "5.5",
                "handicap": "6",
                "main": null,
                "suspended": false
              },
              {
                "value": "Under",
                "odd": "15",
                "handicap": "6",
                "main": null,
                "suspended": false
              },
              {
                "value": "Over",
                "odd": "4.5",
                "handicap": "9",
                "main": null,
                "suspended": false
              },
              {
                "value": "Exactly",
                "odd": "5",
                "handicap": "9",
                "main": null,
                "suspended": false
              },
              {
                "value": "Under",
                "odd": "1.5",
                "handicap": "9",
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 33,
            "name": "Asian Handicap",
            "values": [
              {
                "value": "Home",
                "odd": "1.475",
                "handicap": "-1",
                "main": false,
                "suspended": false
              },
              {
                "value": "Away",
                "odd": "2.6",
                "handicap": "1",
                "main": false,
                "suspended": false
              },
              {
                "value": "Home",
                "odd": "2.05",
                "handicap": "-1",
                "main": true,
                "suspended": false
              },
              {
                "value": "Away",
                "odd": "1.8",
                "handicap": "1",
                "main": true,
                "suspended": false
              },
              {
                "value": "Home",
                "odd": "3.8",
                "handicap": "-2",
                "main": false,
                "suspended": false
              },
              {
                "value": "Away",
                "odd": "1.25",
                "handicap": "2",
                "main": false,
                "suspended": false
              },
              {
                "value": "Home",
                "odd": "1.3",
                "handicap": "-1",
                "main": false,
                "suspended": false
              },
              {
                "value": "Away",
                "odd": "3.45",
                "handicap": "1",
                "main": false,
                "suspended": false
              },
              {
                "value": "Home",
                "odd": "2.85",
                "handicap": "-1",
                "main": false,
                "suspended": false
              },
              {
                "value": "Away",
                "odd": "1.4",
                "handicap": "1",
                "main": false,
                "suspended": false
              }
            ]
          },
          {
            "id": 85,
            "name": "Which team will score the 2nd goal?",
            "values": [
              {
                "value": "1",
                "odd": "3.2",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "No goal",
                "odd": "2.2",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "2",
                "odd": "2.875",
                "handicap": null,
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 36,
            "name": "Over/Under Line",
            "values": [
              {
                "value": "Over",
                "odd": "1.625",
                "handicap": "2",
                "main": false,
                "suspended": false
              },
              {
                "value": "Under",
                "odd": "2.25",
                "handicap": "2",
                "main": false,
                "suspended": false
              },
              {
                "value": "Over",
                "odd": "2.675",
                "handicap": "2",
                "main": false,
                "suspended": false
              },
              {
                "value": "Under",
                "odd": "1.45",
                "handicap": "2",
                "main": false,
                "suspended": false
              },
              {
                "value": "Over",
                "odd": "3.45",
                "handicap": "2",
                "main": false,
                "suspended": false
              },
              {
                "value": "Under",
                "odd": "1.3",
                "handicap": "2",
                "main": false,
                "suspended": false
              },
              {
                "value": "Over",
                "odd": "1.975",
                "handicap": "2",
                "main": true,
                "suspended": false
              },
              {
                "value": "Under",
                "odd": "1.875",
                "handicap": "2",
                "main": true,
                "suspended": false
              }
            ]
          },
          {
            "id": 60,
            "name": "To Score 3 or More",
            "values": [
              {
                "value": "Correa Caio Canedo",
                "odd": "67",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Omar Al-Somah",
                "odd": "126",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Omar Khrbin",
                "odd": "151",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Ali Saleh",
                "odd": "401",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Tahnoon Al Zaabi",
                "odd": "501",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Mahmood Al Mawas",
                "odd": "401",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Khalil Ibrahim",
                "odd": "0",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "Abdullah Ramadan",
                "odd": "0",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "Oliver Kass Kawo",
                "odd": "501",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Ali Salmeen",
                "odd": "0",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "Amro Jenyat",
                "odd": "0",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "Fahd Youssef",
                "odd": "0",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "Mouhamad Anez",
                "odd": "0",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "Abdelaziz Sanqour",
                "odd": "0",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "Walid Abbas",
                "odd": "0",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "Mohamad Al Attas",
                "odd": "0",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "Tamer Haj Mohamad",
                "odd": "0",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "Moaiad Al Khouli",
                "odd": "0",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "Omar Midani",
                "odd": "0",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "Mahmoud Al Hammadi",
                "odd": "0",
                "handicap": null,
                "main": null,
                "suspended": true
              }
            ]
          },
          {
            "id": 23,
            "name": "Final Score",
            "values": [
              {
                "value": "1-0",
                "odd": "2.2",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "2-0",
                "odd": "4.5",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "2-1",
                "odd": "9",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "3-0",
                "odd": "19",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "3-1",
                "odd": "34",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "3-2",
                "odd": "67",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "4-0",
                "odd": "67",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "4-1",
                "odd": "101",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "4-2",
                "odd": "301",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "4-3",
                "odd": "351",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "5-0",
                "odd": "301",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "5-1",
                "odd": "301",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "5-2",
                "odd": "351",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "6-0",
                "odd": "351",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "6-1",
                "odd": "401",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "0-0",
                "odd": "3.4",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "1-1",
                "odd": "4.333",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "2-2",
                "odd": "29",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "3-3",
                "odd": "301",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "0-1",
                "odd": "5.5",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "0-2",
                "odd": "17",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "1-2",
                "odd": "17",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "0-3",
                "odd": "51",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "1-3",
                "odd": "51",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "2-3",
                "odd": "81",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "0-4",
                "odd": "201",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "1-4",
                "odd": "201",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "2-4",
                "odd": "351",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "3-4",
                "odd": "351",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "0-5",
                "odd": "351",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "1-5",
                "odd": "401",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "2-5",
                "odd": "401",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "5-3",
                "odd": "401",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "4-4",
                "odd": "401",
                "handicap": null,
                "main": null,
                "suspended": true
              }
            ]
          },
          {
            "id": 29,
            "name": "Result / Both Teams To Score",
            "values": [
              {
                "value": "Home/Yes",
                "odd": "8",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Away/Yes",
                "odd": "17",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Draw/Yes",
                "odd": "4.333",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Home/No",
                "odd": "1.5",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Away/No",
                "odd": "0",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "Draw/No",
                "odd": "0",
                "handicap": null,
                "main": null,
                "suspended": true
              }
            ]
          },
          {
            "id": 27,
            "name": "Home Team Score a Goal (2nd Half)",
            "values": [
              {
                "value": "Yes",
                "odd": "2.625",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "No",
                "odd": "1.444",
                "handicap": null,
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 58,
            "name": "Home Team Goals",
            "values": [
              {
                "value": "Over",
                "odd": "2.625",
                "handicap": "2",
                "main": null,
                "suspended": false
              },
              {
                "value": "Under",
                "odd": "1.444",
                "handicap": "2",
                "main": null,
                "suspended": false
              },
              {
                "value": "Over",
                "odd": "13",
                "handicap": "3",
                "main": null,
                "suspended": false
              },
              {
                "value": "Under",
                "odd": "1.04",
                "handicap": "3",
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 46,
            "name": "Goal Scorer",
            "values": [
              {
                "value": "Omar Al-Somah",
                "odd": "7",
                "handicap": "2",
                "main": null,
                "suspended": false
              },
              {
                "value": "Correa Caio Canedo",
                "odd": "10",
                "handicap": "2",
                "main": null,
                "suspended": false
              },
              {
                "value": "Omar Khrbin",
                "odd": "8.5",
                "handicap": "2",
                "main": null,
                "suspended": false
              },
              {
                "value": "Ali Saleh",
                "odd": "12",
                "handicap": "2",
                "main": null,
                "suspended": false
              },
              {
                "value": "Mahmood Al Mawas",
                "odd": "13",
                "handicap": "2",
                "main": null,
                "suspended": false
              },
              {
                "value": "Tahnoon Al Zaabi",
                "odd": "15",
                "handicap": "2",
                "main": null,
                "suspended": false
              },
              {
                "value": "Khalil Ibrahim",
                "odd": "19",
                "handicap": "2",
                "main": null,
                "suspended": false
              },
              {
                "value": "Oliver Kass Kawo",
                "odd": "17",
                "handicap": "2",
                "main": null,
                "suspended": false
              },
              {
                "value": "Abdullah Ramadan",
                "odd": "23",
                "handicap": "2",
                "main": null,
                "suspended": false
              },
              {
                "value": "Fahd Youssef",
                "odd": "19",
                "handicap": "2",
                "main": null,
                "suspended": false
              },
              {
                "value": "Amro Jenyat",
                "odd": "21",
                "handicap": "2",
                "main": null,
                "suspended": false
              },
              {
                "value": "Ali Salmeen",
                "odd": "23",
                "handicap": "2",
                "main": null,
                "suspended": false
              },
              {
                "value": "Mouhamad Anez",
                "odd": "21",
                "handicap": "2",
                "main": null,
                "suspended": false
              },
              {
                "value": "Tamer Haj Mohamad",
                "odd": "26",
                "handicap": "2",
                "main": null,
                "suspended": false
              },
              {
                "value": "Abdelaziz Sanqour",
                "odd": "41",
                "handicap": "2",
                "main": null,
                "suspended": false
              },
              {
                "value": "Mahmoud Al Hammadi",
                "odd": "41",
                "handicap": "2",
                "main": null,
                "suspended": false
              },
              {
                "value": "Walid Abbas",
                "odd": "41",
                "handicap": "2",
                "main": null,
                "suspended": false
              },
              {
                "value": "Moaiad Al Khouli",
                "odd": "34",
                "handicap": "2",
                "main": null,
                "suspended": false
              },
              {
                "value": "Mohamad Al Attas",
                "odd": "41",
                "handicap": "2",
                "main": null,
                "suspended": false
              },
              {
                "value": "Omar Midani",
                "odd": "41",
                "handicap": "2",
                "main": null,
                "suspended": false
              },
              {
                "value": "No 2nd Goal",
                "odd": "2.2",
                "handicap": "2",
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 21,
            "name": "3-Way Handicap",
            "values": [
              {
                "value": "Home",
                "odd": "1.025",
                "handicap": "1",
                "main": false,
                "suspended": false
              },
              {
                "value": "Draw",
                "odd": "19",
                "handicap": "-1",
                "main": false,
                "suspended": false
              },
              {
                "value": "Away",
                "odd": "51",
                "handicap": "-1",
                "main": false,
                "suspended": false
              },
              {
                "value": "Home",
                "odd": "51",
                "handicap": "-3",
                "main": false,
                "suspended": false
              },
              {
                "value": "Draw",
                "odd": "17",
                "handicap": "3",
                "main": false,
                "suspended": false
              },
              {
                "value": "Away",
                "odd": "1.025",
                "handicap": "3",
                "main": false,
                "suspended": false
              },
              {
                "value": "Home",
                "odd": "15",
                "handicap": "-2",
                "main": false,
                "suspended": false
              },
              {
                "value": "Draw",
                "odd": "4.333",
                "handicap": "2",
                "main": false,
                "suspended": false
              },
              {
                "value": "Away",
                "odd": "1.222",
                "handicap": "2",
                "main": false,
                "suspended": false
              },
              {
                "value": "Home",
                "odd": "3.75",
                "handicap": "-1",
                "main": true,
                "suspended": false
              },
              {
                "value": "Draw",
                "odd": "1.833",
                "handicap": "1",
                "main": true,
                "suspended": false
              },
              {
                "value": "Away",
                "odd": "3.4",
                "handicap": "1",
                "main": true,
                "suspended": false
              }
            ]
          },
          {
            "id": 32,
            "name": "Asian Corners",
            "values": [
              {
                "value": "Over",
                "odd": "2.05",
                "handicap": "8",
                "main": null,
                "suspended": false
              },
              {
                "value": "Under",
                "odd": "1.75",
                "handicap": "8",
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 25,
            "name": "Match Goals",
            "values": [
              {
                "value": "Over",
                "odd": "11",
                "handicap": "4",
                "main": null,
                "suspended": false
              },
              {
                "value": "Under",
                "odd": "1.05",
                "handicap": "4",
                "main": null,
                "suspended": false
              },
              {
                "value": "Over",
                "odd": "1.615",
                "handicap": "2",
                "main": null,
                "suspended": false
              },
              {
                "value": "Under",
                "odd": "2.2",
                "handicap": "2",
                "main": null,
                "suspended": false
              },
              {
                "value": "Over",
                "odd": "3.75",
                "handicap": "3",
                "main": null,
                "suspended": false
              },
              {
                "value": "Under",
                "odd": "1.25",
                "handicap": "3",
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 35,
            "name": "To Win 2nd Half",
            "values": [
              {
                "value": "Home",
                "odd": "3.75",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Draw",
                "odd": "1.833",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Away",
                "odd": "3.4",
                "handicap": null,
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 45,
            "name": "Race to the 7th corner?",
            "values": [
              {
                "value": "1",
                "odd": "81",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "2",
                "odd": "3.4",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Neither",
                "odd": "1.3",
                "handicap": null,
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 16,
            "name": "How many goals will Away Team score?",
            "values": [
              {
                "value": "No goal",
                "odd": "1.5",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "1",
                "odd": "2.75",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "2",
                "odd": "11",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "3 or more",
                "odd": "41",
                "handicap": null,
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 44,
            "name": "Race to the 9th corner?",
            "values": [
              {
                "value": "1",
                "odd": "101",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "2",
                "odd": "15",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Neither",
                "odd": "1.03",
                "handicap": null,
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 59,
            "name": "Fulltime Result",
            "values": [
              {
                "value": "Home",
                "odd": "1.3",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Draw",
                "odd": "4.333",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Away",
                "odd": "17",
                "handicap": null,
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 72,
            "name": "Double Chance",
            "values": [
              {
                "value": "Home or Draw",
                "odd": "1.025",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Away or Draw",
                "odd": "3.4",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Home or Away",
                "odd": "1.2",
                "handicap": null,
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 66,
            "name": "Home Team Clean Sheet",
            "values": [
              {
                "value": "Yes",
                "odd": "1.5",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "No",
                "odd": "2.5",
                "handicap": null,
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 90,
            "name": "2nd Goal in Interval",
            "values": [
              {
                "value": "Yes",
                "odd": "4.5",
                "handicap": "70",
                "main": null,
                "suspended": false
              },
              {
                "value": "No",
                "odd": "1.166",
                "handicap": "70",
                "main": null,
                "suspended": false
              },
              {
                "value": "Yes",
                "odd": "2.5",
                "handicap": "80",
                "main": null,
                "suspended": false
              },
              {
                "value": "No",
                "odd": "1.5",
                "handicap": "80",
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 88,
            "name": "Which team will score the 7th corner? (2 Way)",
            "values": [
              {
                "value": "1",
                "odd": "2.375",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "2",
                "odd": "1.533",
                "handicap": null,
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 68,
            "name": "Goals Odd/Even",
            "values": [
              {
                "value": "Odd",
                "odd": "1.615",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Even",
                "odd": "2.2",
                "handicap": null,
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 39,
            "name": "Away Team Goals",
            "values": [
              {
                "value": "Over",
                "odd": "11",
                "handicap": "2",
                "main": null,
                "suspended": false
              },
              {
                "value": "Under",
                "odd": "1.05",
                "handicap": "2",
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 48,
            "name": "Draw No Bet",
            "values": [
              {
                "value": "Home",
                "odd": "1.05",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Away",
                "odd": "11",
                "handicap": null,
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 65,
            "name": "Next 10 Minutes Total",
            "values": [
              {
                "value": "Goals/Over  0.5",
                "odd": "3.75",
                "handicap": "70",
                "main": null,
                "suspended": false
              },
              {
                "value": "Goals/Under  0.5",
                "odd": "1.25",
                "handicap": "70",
                "main": null,
                "suspended": false
              },
              {
                "value": "Corners/Over  0.5",
                "odd": "1.571",
                "handicap": "70",
                "main": null,
                "suspended": false
              },
              {
                "value": "Corners/Under  0.5",
                "odd": "2.25",
                "handicap": "70",
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 37,
            "name": "Total Corners",
            "values": [
              {
                "value": "Over",
                "odd": "1.615",
                "handicap": "8",
                "main": null,
                "suspended": false
              },
              {
                "value": "Under",
                "odd": "2.2",
                "handicap": "8",
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 52,
            "name": "1x2 - 80 minutes",
            "values": [
              {
                "value": "Home",
                "odd": "1.142",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Draw",
                "odd": "5",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Away",
                "odd": "41",
                "handicap": null,
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 69,
            "name": "Both Teams to Score",
            "values": [
              {
                "value": "Yes",
                "odd": "2.5",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "No",
                "odd": "1.5",
                "handicap": null,
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 43,
            "name": "Both Teams To Score (2nd Half)",
            "values": [
              {
                "value": "Yes",
                "odd": "7",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "No",
                "odd": "1.1",
                "handicap": null,
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 56,
            "name": "1x2 - 70 minutes",
            "values": [
              {
                "value": "Home",
                "odd": "1.055",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Draw",
                "odd": "8.5",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Away",
                "odd": "151",
                "handicap": null,
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 15,
            "name": "Last Corner",
            "values": [
              {
                "value": "1",
                "odd": "2.5",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "2",
                "odd": "1.5",
                "handicap": null,
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 53,
            "name": "To Score 2 or More",
            "values": [
              {
                "value": "Correa Caio Canedo",
                "odd": "6.5",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Omar Al-Somah",
                "odd": "34",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Omar Khrbin",
                "odd": "51",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Ali Saleh",
                "odd": "101",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Tahnoon Al Zaabi",
                "odd": "101",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Mahmood Al Mawas",
                "odd": "101",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Khalil Ibrahim",
                "odd": "126",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Abdullah Ramadan",
                "odd": "151",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Oliver Kass Kawo",
                "odd": "101",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Ali Salmeen",
                "odd": "151",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Amro Jenyat",
                "odd": "126",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Fahd Youssef",
                "odd": "126",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Mouhamad Anez",
                "odd": "126",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Abdelaziz Sanqour",
                "odd": "251",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Walid Abbas",
                "odd": "301",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Mohamad Al Attas",
                "odd": "301",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Tamer Haj Mohamad",
                "odd": "151",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Moaiad Al Khouli",
                "odd": "251",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Omar Midani",
                "odd": "301",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Mahmoud Al Hammadi",
                "odd": "251",
                "handicap": null,
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 62,
            "name": "Last Team to Score (3 way)",
            "values": [
              {
                "value": "1",
                "odd": "1.363",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "No goal",
                "odd": "3.4",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "2",
                "odd": "3",
                "handicap": null,
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 47,
            "name": "Away 1st Goal in Interval",
            "values": [
              {
                "value": "Yes",
                "odd": "7.5",
                "handicap": "70",
                "main": null,
                "suspended": false
              },
              {
                "value": "No",
                "odd": "1.071",
                "handicap": "70",
                "main": null,
                "suspended": false
              },
              {
                "value": "Yes",
                "odd": "4",
                "handicap": "80",
                "main": null,
                "suspended": false
              },
              {
                "value": "No",
                "odd": "1.222",
                "handicap": "80",
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 70,
            "name": "Away Team Score a Goal (2nd Half)",
            "values": [
              {
                "value": "Yes",
                "odd": "2.5",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "No",
                "odd": "1.5",
                "handicap": null,
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 95,
            "name": "Home 2nd Goal in Interval",
            "values": [
              {
                "value": "Yes",
                "odd": "8",
                "handicap": "70",
                "main": null,
                "suspended": false
              },
              {
                "value": "No",
                "odd": "1.062",
                "handicap": "70",
                "main": null,
                "suspended": false
              },
              {
                "value": "Yes",
                "odd": "4.333",
                "handicap": "80",
                "main": null,
                "suspended": false
              },
              {
                "value": "No",
                "odd": "1.2",
                "handicap": "80",
                "main": null,
                "suspended": false
              }
            ]
          },
          {
            "id": 63,
            "name": "Anytime Goal Scorer",
            "values": [
              {
                "value": "Correa Caio Canedo",
                "odd": "0",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "Omar Al-Somah",
                "odd": "5",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Omar Khrbin",
                "odd": "6",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Ali Saleh",
                "odd": "8.5",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Tahnoon Al Zaabi",
                "odd": "11",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Mahmood Al Mawas",
                "odd": "9",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Khalil Ibrahim",
                "odd": "13",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Abdullah Ramadan",
                "odd": "17",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Oliver Kass Kawo",
                "odd": "12",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Ali Salmeen",
                "odd": "17",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Fahd Youssef",
                "odd": "13",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Amro Jenyat",
                "odd": "15",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Mouhamad Anez",
                "odd": "15",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Tamer Haj Mohamad",
                "odd": "19",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Abdelaziz Sanqour",
                "odd": "26",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Walid Abbas",
                "odd": "29",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Mohamad Al Attas",
                "odd": "29",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Moaiad Al Khouli",
                "odd": "26",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "Omar Midani",
                "odd": "29",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "No 1st Goal",
                "odd": "0",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "Mahmoud Al Hammadi",
                "odd": "26",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "No 2nd Goal",
                "odd": "0",
                "handicap": null,
                "main": null,
                "suspended": true
              }
            ]
          },
          {
            "id": 67,
            "name": "How many goals will Home Team score?",
            "values": [
              {
                "value": "No goal",
                "odd": "2",
                "handicap": null,
                "main": null,
                "suspended": true
              },
              {
                "value": "1",
                "odd": "1.444",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "2",
                "odd": "3.25",
                "handicap": null,
                "main": null,
                "suspended": false
              },
              {
                "value": "3 or more",
                "odd": "13",
                "handicap": null,
                "main": null,
                "suspended": false
              }
            ]
          }
        ]
      }
    ]
  }
```

---


## odds-live-bets

**Dosya Boyutu:** 11294 bytes  
**Son Değişiklik:** 2025-06-19 22:19:18  

```text
odds/live/bets
Get all available bets for in-play odds.

All bets id can be used in endpoint odds/live as filters, but are not compatible with endpoint odds for pre-match odds.

Update Frequency : This endpoint is updated every 60 seconds.

query Parameters
id	
string
The id of the bet name

search	
string = 3 characters
The name of the bet

header Parameters
x-rapidapi-key
required
string
Your Api-Key

####################################
Responses;
200 OK:
Response Schema: application/json
get	
string
parameters	
Array of objects
errors	
Array of objects
results	
integer
response	
Array of any
{
  "get": "odds/live/bets",
  "parameters": [],
  "errors": [],
  "results": 137,
  "paging": {
    "current": 1,
    "total": 1
  },
  "response": [
    {
      "id": 1,
      "name": "Over/Under Extra Time"
    },
    {
      "id": 2,
      "name": "1x2 Extra Time"
    },
    {
      "id": 3,
      "name": "Extra Time Asian Corners"
    },
    {
      "id": 4,
      "name": "Extra Time Total Corners (3 Ways) (1st Half)"
    },
    {
      "id": 5,
      "name": "Extra Time Double Result"
    },
    {
      "id": 6,
      "name": "Which team will score the 1st goal in extra time?"
    },
    {
      "id": 7,
      "name": "Extra Time Asian Corners (1st Half)"
    },
    {
      "id": 8,
      "name": "Method of Victory"
    },
    {
      "id": 9,
      "name": "Both Teams To Score (ET)"
    },
    {
      "id": 10,
      "name": "To Qualify"
    },
    {
      "id": 11,
      "name": "Asian Handicap Extra Time"
    },
    {
      "id": 12,
      "name": "1x2 Extra Time (1st Half)"
    },
    {
      "id": 13,
      "name": "Extra Time Total Corners (3 Ways)"
    },
    {
      "id": 14,
      "name": "Over/Under Extra Time (1st Half)"
    },
    {
      "id": 15,
      "name": "Last Corner"
    },
    {
      "id": 16,
      "name": "How many goals will Away Team score?"
    },
    {
      "id": 17,
      "name": "Asian Handicap (1st Half)"
    },
    {
      "id": 18,
      "name": "1st Goal in Interval"
    },
    {
      "id": 19,
      "name": "1x2 (1st Half)"
    },
    {
      "id": 20,
      "name": "Match Corners"
    },
    {
      "id": 21,
      "name": "3-Way Handicap"
    },
    {
      "id": 22,
      "name": "1x2 - 30 minutes"
    },
    {
      "id": 23,
      "name": "Final Score"
    },
    {
      "id": 24,
      "name": "Over/Under Line (1st Half)"
    },
    {
      "id": 25,
      "name": "Match Goals"
    },
    {
      "id": 26,
      "name": "European Handicap (1st Half)"
    },
    {
      "id": 27,
      "name": "Home Team Score a Goal (2nd Half)"
    },
    {
      "id": 28,
      "name": "Home Team  to Score in Both Halves"
    },
    {
      "id": 29,
      "name": "Result / Both Teams To Score"
    },
    {
      "id": 30,
      "name": "Both Teams To Score (1st Half)"
    },
    {
      "id": 31,
      "name": "Total Corners (3way) (2nd Half)"
    },
    {
      "id": 32,
      "name": "Asian Corners"
    },
    {
      "id": 33,
      "name": "Asian Handicap"
    },
    {
      "id": 34,
      "name": "1x2 - 40 minutes"
    },
    {
      "id": 35,
      "name": "To Win 2nd Half"
    },
    {
      "id": 36,
      "name": "Over/Under Line"
    },
    {
      "id": 37,
      "name": "Total Corners"
    },
    {
      "id": 38,
      "name": "Away Team to Score in Both Halves"
    },
    {
      "id": 39,
      "name": "Away Team Goals"
    },
    {
      "id": 40,
      "name": "Total Corners (3 way) (1st Half)"
    },
    {
      "id": 41,
      "name": "1x2 - 50 minutes"
    },
    {
      "id": 42,
      "name": "Race to the 3rd corner?"
    },
    {
      "id": 43,
      "name": "Both Teams To Score (2nd Half)"
    },
    {
      "id": 44,
      "name": "Race to the 9th corner?"
    },
    {
      "id": 45,
      "name": "Race to the 7th corner?"
    },
    {
      "id": 46,
      "name": "Goal Scorer"
    },
    {
      "id": 47,
      "name": "Away 1st Goal in Interval"
    },
    {
      "id": 48,
      "name": "Draw No Bet"
    },
    {
      "id": 49,
      "name": "Over/Under (1st Half)"
    },
    {
      "id": 50,
      "name": "1x2 - 60 minutes"
    },
    {
      "id": 51,
      "name": "Asian Corners (1st Half)"
    },
    {
      "id": 52,
      "name": "1x2 - 80 minutes"
    },
    {
      "id": 53,
      "name": "To Score 2 or More"
    },
    {
      "id": 54,
      "name": "Home 1st Goal in Interval"
    },
    {
      "id": 55,
      "name": "Correct Score (1st Half)"
    },
    {
      "id": 56,
      "name": "1x2 - 70 minutes"
    },
    {
      "id": 57,
      "name": "Away Team Clean Sheet"
    },
    {
      "id": 58,
      "name": "Home Team Goals"
    },
    {
      "id": 59,
      "name": "Fulltime Result"
    },
    {
      "id": 60,
      "name": "To Score 3 or More"
    },
    {
      "id": 61,
      "name": "Race to the 5th corner?"
    },
    {
      "id": 62,
      "name": "Last Team to Score (3 way)"
    },
    {
      "id": 63,
      "name": "Anytime Goal Scorer"
    },
    {
      "id": 64,
      "name": "Half Time/Full Time"
    },
    {
      "id": 65,
      "name": "Next 10 Minutes Total"
    },
    {
      "id": 66,
      "name": "Home Team Clean Sheet"
    },
    {
      "id": 67,
      "name": "How many goals will Home Team score?"
    },
    {
      "id": 68,
      "name": "Goals Odd/Even"
    },
    {
      "id": 69,
      "name": "Both Teams to Score"
    },
    {
      "id": 70,
      "name": "Away Team Score a Goal (2nd Half)"
    },
    {
      "id": 71,
      "name": "Which team will score the 4th corner? (2 Way)"
    },
    {
      "id": 72,
      "name": "Double Chance"
    },
    {
      "id": 73,
      "name": "Which team will score the 1st goal?"
    },
    {
      "id": 74,
      "name": "Which team will score the 3rd corner? (2 Way)"
    },
    {
      "id": 75,
      "name": "Which team will score the 2nd corner? (2 Way)"
    },
    {
      "id": 76,
      "name": "Corners European Handicap"
    },
    {
      "id": 77,
      "name": "1x2 - 10 minutes"
    },
    {
      "id": 78,
      "name": "Corners 1x2"
    },
    {
      "id": 79,
      "name": "1x2 - 20 minutes"
    },
    {
      "id": 80,
      "name": "Method of 1st Goal"
    },
    {
      "id": 81,
      "name": "Method of Qualification"
    },
    {
      "id": 82,
      "name": "Game Won After Penalties Shootout"
    },
    {
      "id": 83,
      "name": "Game Won In Extra Time"
    },
    {
      "id": 84,
      "name": "Which team will score the 2nd goal?"
    },
    {
      "id": 85,
      "name": "Which team will score the 2nd goal?"
    },
    {
      "id": 86,
      "name": "Which team will score the 6th corner? (2 Way)"
    },
    {
      "id": 87,
      "name": "Which team will score the 5th corner? (2 Way)"
    },
    {
      "id": 88,
      "name": "Which team will score the 7th corner? (2 Way)"
    },
    {
      "id": 89,
      "name": "Which team will score the 9th corner? (2 Way)"
    },
    {
      "id": 90,
      "name": "2nd Goal in Interval"
    },
    {
      "id": 91,
      "name": "Away 2nd Goal in Interval"
    },
    {
      "id": 92,
      "name": "Which team will score the 3rd goal?"
    },
    {
      "id": 93,
      "name": "Which team will score the 10th corner? (2 Way)"
    },
    {
      "id": 94,
      "name": "3rd Goal in Interval"
    },
    {
      "id": 95,
      "name": "Home 2nd Goal in Interval"
    },
    {
      "id": 96,
      "name": "Asian Handicap Converted Penalties"
    },
    {
      "id": 97,
      "name": "Sudden Death"
    },
    {
      "id": 98,
      "name": "Away Penalty Shootout"
    },
    {
      "id": 99,
      "name": "Home Penalty Shootout"
    },
    {
      "id": 100,
      "name": "Home Total Converted Penalties"
    },
    {
      "id": 101,
      "name": "Total Penalties in Shootout"
    },
    {
      "id": 102,
      "name": "Last Penalty Score/Miss"
    },
    {
      "id": 103,
      "name": "Correct Score in Shootouts"
    },
    {
      "id": 104,
      "name": "Total Converted Penalties"
    },
    {
      "id": 105,
      "name": "Total Converted Penalties - Goal Line"
    },
    {
      "id": 106,
      "name": "Away Total Converted Penalties"
    },
    {
      "id": 107,
      "name": "Penalties Shootout Winner"
    },
    {
      "id": 108,
      "name": "Which team will score the 11th corner? (2 Way)"
    },
    {
      "id": 109,
      "name": "Which team will score the 4th goal?"
    },
    {
      "id": 110,
      "name": "Which team will score the 8th corner? (2 Way)"
    },
    {
      "id": 111,
      "name": "Last Penalty Scorer in Shootout"
    },
    {
      "id": 112,
      "name": "Which team will score the 5th goal?"
    },
    {
      "id": 113,
      "name": "Method of 2nd Goal"
    },
    {
      "id": 114,
      "name": "Which team will score the 13th corner? (2 Way)"
    },
    {
      "id": 115,
      "name": "Player to be Booked"
    },
    {
      "id": 116,
      "name": "Action In Next 1 Minutes"
    },
    {
      "id": 117,
      "name": "First Action In Next 5 Minutes"
    },
    {
      "id": 118,
      "name": "Player to be Sent Off"
    },
    {
      "id": 119,
      "name": "Total Cards"
    },
    {
      "id": 120,
      "name": "Which team will score the 12th corner? (2 Way)"
    },
    {
      "id": 121,
      "name": "Which team will score the 14th corner? (2 Way)"
    },
    {
      "id": 122,
      "name": "Which team will score the 15th corner? (2 Way)"
    },
    {
      "id": 123,
      "name": "Which team will score the 16th corner? (2 Way)"
    },
    {
      "id": 124,
      "name": "Which team will score the 17th corner? (2 Way)"
    },
    {
      "id": 125,
      "name": "Home 3rd Goal in Interval"
    },
    {
      "id": 126,
      "name": "Which team will score the 18th corner? (2 Way)"
    },
    {
      "id": 127,
      "name": "Which team will score the 6th goal?"
    },
    {
      "id": 128,
      "name": "Away 3rd Goal in Interval"
    },
    {
      "id": 129,
      "name": "Which team will score the 2nd goal in extra time?"
    },
    {
      "id": 130,
      "name": "Method of 3rd Goal"
    },
    {
      "id": 131,
      "name": "4th Goal in Interval"
    },
    {
      "id": 132,
      "name": "Which team will score the 7th goal?"
    },
    {
      "id": 133,
      "name": "Which team will score the 19th corner? (2 Way)"
    },
    {
      "id": 134,
      "name": "Home 4th Goal in Interval"
    },
    {
      "id": 135,
      "name": "Away 4th Goal in Interval"
    },
    {
      "id": 136,
      "name": "5th Goal in Interval"
    },
    {
      "id": 137,
      "name": "Home 5th Goal in Interval"
    }
  ]
}
```

---


## player-profiles

**Dosya Boyutu:** 2147 bytes  
**Son Değişiklik:** 2025-06-19 22:19:34  

```text
Profiles
Returns the list of all available players.

It is possible to call this endpoint without parameters, but you will need to use the pagination to get all available players.

To get the photo of a player you have to call the following url: https://media.api-sports.io/football/players/{player_id}.png

This endpoint uses a pagination system, you can navigate between the different pages with to the page parameter.

Pagination : 250 results per page.

Update Frequency : This endpoint is updated several times a week.

Recommended Calls : 1 call per week.

query Parameters
player	
integer
The id of the player

search	
string >= 3 characters
The lastname of the player

page	
integer
Default: 1
Use for the pagination

header Parameters
x-rapidapi-key
required
string
Your Api-Key
import http.client

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "XxXxXxXxXxXxXxXxXxXxXxXx"
    }

conn.request("GET", "/players/profiles?player=276", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

###################################################
Responses;
200 OK:
Response Schema: application/json
get	
string
parameters	
Array of objects
errors	
Array of objects
results	
integer
response	
Array of any
{
  "get": "players/profiles",
  "parameters": {
    "player": "276"
  },
  "errors": [],
  "results": 1,
  "paging": {
    "current": 1,
    "total": 1
  },
  "response": [
    {
      "player": {
        "id": 276,
        "name": "Neymar",
        "firstname": "Neymar",
        "lastname": "da Silva Santos Júnior",
        "age": 32,
        "birth": {
          "date": "1992-02-05",
          "place": "Mogi das Cruzes",
          "country": "Brazil"
        },
        "nationality": "Brazil",
        "height": "175 cm",
        "weight": "68 kg",
        "number": 10,
        "position": "Attacker",
        "photo": "https://media.api-sports.io/football/players/276.png"
      }
    }
  ]
}
```

---


## player-squads

**Dosya Boyutu:** 10221 bytes  
**Son Değişiklik:** 2025-06-19 22:19:51  

```text
Squads
Return the current squad of a team when the team parameter is used. When the player parameter is used the endpoint returns the set of teams associated with the player.

The response format is the same regardless of the parameter sent.

This endpoint requires at least one parameter.

Update Frequency : This endpoint is updated several times a week.

Recommended Calls : 1 call per week.

query Parameters
team	
integer
The id of the team

player	
integer
The id of the player

header Parameters
x-rapidapi-key
required
string
Your Api-Key

##################################################

Responses;
200 OK:
Response Schema: application/json
get	
string
parameters	
Array of objects
errors	
Array of objects
results	
integer
response	
Array of any
{
  "get": "players/squads",
  "parameters": {
    "team": "33"
  },
  "errors": [],
  "results": 1,
  "paging": {
    "current": 1,
    "total": 1
  },
  "response": [
    {
      "team": {
        "id": 33,
        "name": "Manchester United",
        "logo": "https://media.api-sports.io/football/teams/33.png"
      },
      "players": [
        {
          "id": 20319,
          "name": "N. Bishop",
          "age": 22,
          "number": 30,
          "position": "Goalkeeper",
          "photo": "https://media.api-sports.io/football/players/20319.png"
        },
        {
          "id": 882,
          "name": "David de Gea",
          "age": 31,
          "number": 1,
          "position": "Goalkeeper",
          "photo": "https://media.api-sports.io/football/players/882.png"
        },
        {
          "id": 883,
          "name": "L. Grant",
          "age": 38,
          "number": 13,
          "position": "Goalkeeper",
          "photo": "https://media.api-sports.io/football/players/883.png"
        },
        {
          "id": 2931,
          "name": "T. Heaton",
          "age": 35,
          "number": null,
          "position": "Goalkeeper",
          "photo": "https://media.api-sports.io/football/players/2931.png"
        },
        {
          "id": 19088,
          "name": "D. Henderson",
          "age": 24,
          "number": 26,
          "position": "Goalkeeper",
          "photo": "https://media.api-sports.io/football/players/19088.png"
        },
        {
          "id": 885,
          "name": "E. Bailly",
          "age": 27,
          "number": 3,
          "position": "Defender",
          "photo": "https://media.api-sports.io/football/players/885.png"
        },
        {
          "id": 886,
          "name": "Diogo Dalot",
          "age": 22,
          "number": 20,
          "position": "Defender",
          "photo": "https://media.api-sports.io/football/players/886.png"
        },
        {
          "id": 153434,
          "name": "W. Fish",
          "age": 18,
          "number": 48,
          "position": "Defender",
          "photo": "https://media.api-sports.io/football/players/153434.png"
        },
        {
          "id": 888,
          "name": "P. Jones",
          "age": 29,
          "number": 4,
          "position": "Defender",
          "photo": "https://media.api-sports.io/football/players/888.png"
        },
        {
          "id": 138775,
          "name": "E. Laird",
          "age": 20,
          "number": null,
          "position": "Defender",
          "photo": "https://media.api-sports.io/football/players/138775.png"
        },
        {
          "id": 2935,
          "name": "H. Maguire",
          "age": 28,
          "number": 5,
          "position": "Defender",
          "photo": "https://media.api-sports.io/football/players/2935.png"
        },
        {
          "id": 889,
          "name": "V. Lindelöf",
          "age": 27,
          "number": 2,
          "position": "Defender",
          "photo": "https://media.api-sports.io/football/players/889.png"
        },
        {
          "id": 891,
          "name": "L. Shaw",
          "age": 26,
          "number": 23,
          "position": "Defender",
          "photo": "https://media.api-sports.io/football/players/891.png"
        },
        {
          "id": 378,
          "name": "Alex Telles",
          "age": 29,
          "number": 27,
          "position": "Defender",
          "photo": "https://media.api-sports.io/football/players/378.png"
        },
        {
          "id": 19182,
          "name": "A. Tuanzebe",
          "age": 24,
          "number": 38,
          "position": "Defender",
          "photo": "https://media.api-sports.io/football/players/19182.png"
        },
        {
          "id": 18846,
          "name": "A. Wan-Bissaka",
          "age": 24,
          "number": 29,
          "position": "Defender",
          "photo": "https://media.api-sports.io/football/players/18846.png"
        },
        {
          "id": 138806,
          "name": "B. Williams",
          "age": 21,
          "number": 33,
          "position": "Defender",
          "photo": "https://media.api-sports.io/football/players/138806.png"
        },
        {
          "id": 1485,
          "name": "Bruno Fernandes",
          "age": 27,
          "number": 18,
          "position": "Midfielder",
          "photo": "https://media.api-sports.io/football/players/1485.png"
        },
        {
          "id": 906,
          "name": "T. Chong",
          "age": 22,
          "number": 44,
          "position": "Midfielder",
          "photo": "https://media.api-sports.io/football/players/906.png"
        },
        {
          "id": 895,
          "name": "J. Garner",
          "age": 20,
          "number": null,
          "position": "Midfielder",
          "photo": "https://media.api-sports.io/football/players/895.png"
        },
        {
          "id": 899,
          "name": "Andreas Pereira",
          "age": 25,
          "number": 15,
          "position": "Midfielder",
          "photo": "https://media.api-sports.io/football/players/899.png"
        },
        {
          "id": 900,
          "name": "J. Lingard",
          "age": 29,
          "number": 14,
          "position": "Midfielder",
          "photo": "https://media.api-sports.io/football/players/900.png"
        },
        {
          "id": 901,
          "name": "Mata",
          "age": 33,
          "number": 8,
          "position": "Midfielder",
          "photo": "https://media.api-sports.io/football/players/901.png"
        },
        {
          "id": 902,
          "name": "N. Matić",
          "age": 33,
          "number": 31,
          "position": "Midfielder",
          "photo": "https://media.api-sports.io/football/players/902.png"
        },
        {
          "id": 903,
          "name": "S. McTominay",
          "age": 25,
          "number": 39,
          "position": "Midfielder",
          "photo": "https://media.api-sports.io/football/players/903.png"
        },
        {
          "id": 180560,
          "name": "H. Mejbri",
          "age": 18,
          "number": 46,
          "position": "Midfielder",
          "photo": "https://media.api-sports.io/football/players/180560.png"
        },
        {
          "id": 904,
          "name": "P. Pogba",
          "age": 28,
          "number": 6,
          "position": "Midfielder",
          "photo": "https://media.api-sports.io/football/players/904.png"
        },
        {
          "id": 905,
          "name": "Fred",
          "age": 28,
          "number": 17,
          "position": "Midfielder",
          "photo": "https://media.api-sports.io/football/players/905.png"
        },
        {
          "id": 163054,
          "name": "S. Shoretire",
          "age": 17,
          "number": 74,
          "position": "Midfielder",
          "photo": "https://media.api-sports.io/football/players/163054.png"
        },
        {
          "id": 547,
          "name": "D. van de Beek",
          "age": 24,
          "number": 34,
          "position": "Midfielder",
          "photo": "https://media.api-sports.io/football/players/547.png"
        },
        {
          "id": 138814,
          "name": "E. Galbraith",
          "age": 20,
          "number": null,
          "position": "Midfielder",
          "photo": "https://media.api-sports.io/football/players/138814.png"
        },
        {
          "id": 274,
          "name": "E. Cavani",
          "age": 34,
          "number": 7,
          "position": "Attacker",
          "photo": "https://media.api-sports.io/football/players/274.png"
        },
        {
          "id": 153430,
          "name": "A. Elanga",
          "age": 19,
          "number": 56,
          "position": "Attacker",
          "photo": "https://media.api-sports.io/football/players/153430.png"
        },
        {
          "id": 897,
          "name": "M. Greenwood",
          "age": 20,
          "number": 11,
          "position": "Attacker",
          "photo": "https://media.api-sports.io/football/players/897.png"
        },
        {
          "id": 19329,
          "name": "D. James",
          "age": 24,
          "number": 21,
          "position": "Attacker",
          "photo": "https://media.api-sports.io/football/players/19329.png"
        },
        {
          "id": 908,
          "name": "A. Martial",
          "age": 26,
          "number": 9,
          "position": "Attacker",
          "photo": "https://media.api-sports.io/football/players/908.png"
        },
        {
          "id": 909,
          "name": "M. Rashford",
          "age": 24,
          "number": 10,
          "position": "Attacker",
          "photo": "https://media.api-sports.io/football/players/909.png"
        },
        {
          "id": 157997,
          "name": "A. Diallo",
          "age": 19,
          "number": 19,
          "position": "Attacker",
          "photo": "https://media.api-sports.io/football/players/157997.png"
        }
      ]
    }
  ]
}
```

---


## player-statistics

**Dosya Boyutu:** 5168 bytes  
**Son Değişiklik:** 2025-06-19 22:20:02  

```text
Statistics
Get players statistics.

This endpoint returns the players for whom the profile and statistics data are available. Note that it is possible that a player has statistics for 2 teams in the same season in case of transfers.

The statistics are calculated according to the team id, league id and season.

You can find the available seasons by using the endpoint players/seasons.

To get the squads of the teams it is better to use the endpoint players/squads.

The players id are unique in the API and players keep it among all the teams they have been in.

In this endpoint you have the rating field, which is the rating of the player according to a match or a season. This data is calculated according to the performance of the player in relation to the other players of the game or the season who occupy the same position (Attacker, defender, goal...). There are different algorithms that take into account the position of the player and assign points according to his performance.

To get the photo of a player you have to call the following url: https://media.api-sports.io/football/players/{player_id}.png

This endpoint uses a pagination system, you can navigate between the different pages with to the page parameter.

Pagination : 20 results per page.

Update Frequency : This endpoint is updated several times a week.

Recommended Calls : 1 call per day.

Tutorials :

HOW TO GET ALL TEAMS AND PLAYERS FROM A LEAGUE ID
query Parameters
id	
integer
The id of the player

team	
integer
The id of the team

league	
integer
The id of the league

season	
integer = 4 characters YYYY | Requires the fields Id, League or Team...
The season of the league

search	
string >= 4 characters Requires the fields League or Team
The name of the player

page	
integer
Default: 1
Use for the pagination

header Parameters
x-rapidapi-key
required
string
Your Api-Key
import http.client

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "XxXxXxXxXxXxXxXxXxXxXxXx"
    }

conn.request("GET", "/players?id=276&season=2019", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

###########################################
Responses;
200 OK:
Response Schema: application/json
get	
string
parameters	
Array of objects
errors	
Array of objects
results	
integer
response	
Array of any
{
  "get": "players",
  "parameters": {
    "id": "276",
    "season": "2019"
  },
  "errors": [],
  "results": 1,
  "paging": {
    "current": 1,
    "total": 1
  },
  "response": [
    {
      "player": {
        "id": 276,
        "name": "Neymar",
        "firstname": "Neymar",
        "lastname": "da Silva Santos Júnior",
        "age": 28,
        "birth": {
          "date": "1992-02-05",
          "place": "Mogi das Cruzes",
          "country": "Brazil"
        },
        "nationality": "Brazil",
        "height": "175 cm",
        "weight": "68 kg",
        "injured": false,
        "photo": "https://media.api-sports.io/football/players/276.png"
      },
      "statistics": [
        {
          "team": {
            "id": 85,
            "name": "Paris Saint Germain",
            "logo": "https://media.api-sports.io/football/teams/85.png"
          },
          "league": {
            "id": 61,
            "name": "Ligue 1",
            "country": "France",
            "logo": "https://media.api-sports.io/football/leagues/61.png",
            "flag": "https://media.api-sports.io/flags/fr.svg",
            "season": 2019
          },
          "games": {
            "appearences": 15,
            "lineups": 15,
            "minutes": 1322,
            "number": null,
            "position": "Attacker",
            "rating": "8.053333",
            "captain": false
          },
          "substitutes": {
            "in": 0,
            "out": 3,
            "bench": 0
          },
          "shots": {
            "total": 70,
            "on": 36
          },
          "goals": {
            "total": 13,
            "conceded": null,
            "assists": 6,
            "saves": 0
          },
          "passes": {
            "total": 704,
            "key": 39,
            "accuracy": 79
          },
          "tackles": {
            "total": 13,
            "blocks": 0,
            "interceptions": 4
          },
          "duels": {
            "total": null,
            "won": null
          },
          "dribbles": {
            "attempts": 143,
            "success": 88,
            "past": null
          },
          "fouls": {
            "drawn": 62,
            "committed": 14
          },
          "cards": {
            "yellow": 3,
            "yellowred": 1,
            "red": 0
          },
          "penalty": {
            "won": 1,
            "commited": null,
            "scored": 4,
            "missed": 1,
            "saved": null
          }
        }
      ]
    }
  ]
}
```

---


## prematch-bets

**Dosya Boyutu:** 1361 bytes  
**Son Değişiklik:** 2025-06-19 22:20:12  

```text
Bets
Get all available bets for pre-match odds.

All bets id can be used in endpoint odds as filters, but are not compatible with endpoint odds/live for in-play odds.

Update Frequency : This endpoint is updated several times a week.

Recommended Calls : 1 call per day.

query Parameters
id	
string
The id of the bet name

search	
string = 3 characters
The name of the bet

header Parameters
x-rapidapi-key
required
string
Your Api-Key
###########################################
Responses;
200 OK:
Response Schema: application/json
get	
string
parameters	
Array of objects
errors	
Array of objects
results	
integer
response	
Array of any
{
  "get": "odds/bets",
  "parameters": {
    "search": "under"
  },
  "errors": [],
  "results": 7,
  "paging": {
    "current": 1,
    "total": 1
  },
  "response": [
    {
      "id": 5,
      "name": "Goals Over/Under"
    },
    {
      "id": 6,
      "name": "Goals Over/Under First Half"
    },
    {
      "id": 26,
      "name": "Goals Over/Under - Second Half"
    },
    {
      "id": 45,
      "name": "Corners Over Under"
    },
    {
      "id": 57,
      "name": "Home Corners Over/Under"
    },
    {
      "id": 58,
      "name": "Away Corners Over/Under"
    },
    {
      "id": 74,
      "name": "10 Over/Under"
    }
  ]
}
```

---


## prematch-bookmakers

**Dosya Boyutu:** 1653 bytes  
**Son Değişiklik:** 2025-06-19 22:20:38  

```text
Bookmakers
Get all available bookmakers.

All bookmakers id can be used in endpoint odds as filters.

Update Frequency : This endpoint is updated several times a week.

Recommended Calls : 1 call per day.

query Parameters
id	
integer
The id of the bookmaker

search	
string = 3 characters
The name of the bookmaker

header Parameters
x-rapidapi-key
required
string
Your Api-Key
############################################
Responses;
200 OK:
Response Schema: application/json
get	
string
parameters	
Array of objects
errors	
Array of objects
results	
integer
response	
Array of any
{
  "get": "odds/bookmakers",
  "parameters": [],
  "errors": [],
  "results": 15,
  "paging": {
    "current": 1,
    "total": 1
  },
  "response": [
    {
      "id": 1,
      "name": "10Bet"
    },
    {
      "id": 2,
      "name": "Marathonbet"
    },
    {
      "id": 3,
      "name": "Betfair"
    },
    {
      "id": 4,
      "name": "Pinnacle"
    },
    {
      "id": 5,
      "name": "Sport Betting Online"
    },
    {
      "id": 6,
      "name": "Bwin"
    },
    {
      "id": 7,
      "name": "William Hill"
    },
    {
      "id": 8,
      "name": "Bet365"
    },
    {
      "id": 9,
      "name": "Dafabet"
    },
    {
      "id": 10,
      "name": "Ladbrokes"
    },
    {
      "id": 11,
      "name": "1xBet"
    },
    {
      "id": 12,
      "name": "BetFred"
    },
    {
      "id": 13,
      "name": "188Bet"
    },
    {
      "id": 15,
      "name": "Interwetten"
    },
    {
      "id": 16,
      "name": "Unibet"
    }
  ]
}
```

---


## prematch-mapping

**Dosya Boyutu:** 2333 bytes  
**Son Değişiklik:** 2025-06-19 22:20:50  

```text
Mapping
Get the list of available fixtures id for the endpoint odds.

All fixtures, leagues id and date can be used in endpoint odds as filters.

This endpoint uses a pagination system, you can navigate between the different pages with to the page parameter.

Pagination : 100 results per page.

Update Frequency : This endpoint is updated every day.

Recommended Calls : 1 call per day.

query Parameters
page	
integer
Default: 1
Use for the pagination

header Parameters
x-rapidapi-key
required
string
Your Api-Key
import http.client

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "XxXxXxXxXxXxXxXxXxXxXxXx"
    }

conn.request("GET", "/odds/mapping", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

###########################################
Responses;
200 OK:
Response Schema: application/json
get	
string
parameters	
Array of objects
errors	
Array of objects
results	
integer
response	
Array of any
{
  "get": "odds/mapping",
  "parameters": [],
  "errors": [],
  "results": 129,
  "paging": {
    "current": 1,
    "total": 1
  },
  "response": [
    {
      "league": {
        "id": 106,
        "season": 2019
      },
      "fixture": {
        "id": 154507,
        "date": "2020-05-29T18:30:00+00:00",
        "timestamp": 1590777000
      },
      "update": "2020-05-15T09:52:28+00:00"
    },
    {
      "league": {
        "id": 106,
        "season": 2019
      },
      "fixture": {
        "id": 154508,
        "date": "2020-05-29T16:00:00+00:00",
        "timestamp": 1590768000
      },
      "update": "2020-05-15T09:52:28+00:00"
    },
    {
      "league": {
        "id": 271,
        "season": 2019
      },
      "fixture": {
        "id": 182450,
        "date": "2020-05-23T13:55:00+00:00",
        "timestamp": 1590242100
      },
      "update": "2020-05-15T09:51:45+00:00"
    },
    {
      "league": {
        "id": 271,
        "season": 2019
      },
      "fixture": {
        "id": 182564,
        "date": "2020-05-27T18:00:00+00:00",
        "timestamp": 1590602400
      },
      "update": "2020-05-15T09:52:17+00:00"
    }
  ]
}
```

---


## prematch-odds

**Dosya Boyutu:** 25073 bytes  
**Son Değişiklik:** 2025-06-19 22:21:06  

```text
Odds
Get odds from fixtures, leagues or date.

This endpoint uses a pagination system, you can navigate between the different pages with to the page parameter.

Pagination : 10 results per page.

We provide pre-match odds between 1 and 14 days before the fixture.

We keep a 7-days history (The availability of odds may vary according to the leagues, seasons, fixtures and bookmakers)

Update Frequency : This endpoint is updated every 3 hours.

Recommended Calls : 1 call every 3 hours.

query Parameters
fixture	
integer
The id of the fixture

league	
integer
The id of the league

season	
integer = 4 characters YYYY
The season of the league

date	
stringYYYY-MM-DD
A valid date

timezone	
string
A valid timezone from the endpoint Timezone

page	
integer
Default: 1
Use for the pagination

bookmaker	
integer
The id of the bookmaker

bet	
integer
The id of the bet

header Parameters
x-rapidapi-key
required
string
Your Api-Key
import http.client

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "XxXxXxXxXxXxXxXxXxXxXxXx"
    }

conn.request("GET", "/odds?season=2019&bet=1&bookmaker=6&fixture=157140&league=39", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

########################################################
Responses;
200 OK:
Response Schema: application/json
get	
string
parameters	
Array of objects
errors	
Array of objects
results	
integer
response	
Array of any
{
  "get": "odds",
  "parameters": {
    "fixture": "326090",
    "bookmaker": "6"
  },
  "errors": [],
  "results": 1,
  "paging": {
    "current": 1,
    "total": 1
  },
  "response": [
    {
      "league": {
        "id": 116,
        "name": "Vysshaya Liga",
        "country": "Belarus",
        "logo": "https://media.api-sports.io/football/leagues/116.png",
        "flag": "https://media.api-sports.io/flags/by.svg",
        "season": 2020
      },
      "fixture": {
        "id": 326090,
        "timezone": "UTC",
        "date": "2020-05-15T15:00:00+00:00",
        "timestamp": 1589554800
      },
      "update": "2020-05-15T09:49:32+00:00",
      "bookmakers": [
        {
          "id": 6,
          "name": "Bwin",
          "bets": [
            {
              "id": 38,
              "name": "Exact Goals Number",
              "values": [
                {
                  "value": 4,
                  "odd": "7.00"
                },
                {
                  "value": 3,
                  "odd": "4.40"
                },
                {
                  "value": 2,
                  "odd": "3.40"
                },
                {
                  "value": "more 8",
                  "odd": "251.00"
                },
                {
                  "value": 7,
                  "odd": "101.00"
                },
                {
                  "value": "more 5",
                  "odd": "8.00"
                },
                {
                  "value": 6,
                  "odd": "31.00"
                },
                {
                  "value": 5,
                  "odd": "14.00"
                },
                {
                  "value": 0,
                  "odd": "6.25"
                },
                {
                  "value": 1,
                  "odd": "3.90"
                }
              ]
            },
            {
              "id": 20,
              "name": "Double Chance - First Half",
              "values": [
                {
                  "value": "Home/Draw",
                  "odd": "1.20"
                },
                {
                  "value": "Home/Away",
                  "odd": "1.75"
                },
                {
                  "value": "Draw/Away",
                  "odd": "1.26"
                }
              ]
            },
            {
              "id": 17,
              "name": "Total - Away",
              "values": [
                {
                  "value": "Under 2.5",
                  "odd": "1.06"
                },
                {
                  "value": "Over 2.5",
                  "odd": "7.25"
                },
                {
                  "value": "Under 1.5",
                  "odd": "1.33"
                },
                {
                  "value": "Over 1.5",
                  "odd": "3.10"
                }
              ]
            },
            {
              "id": 16,
              "name": "Total - Home",
              "values": [
                {
                  "value": "Under 2.5",
                  "odd": "1.09"
                },
                {
                  "value": "Over 2.5",
                  "odd": "6.25"
                },
                {
                  "value": "Under 1.5",
                  "odd": "1.40"
                },
                {
                  "value": "Over 1.5",
                  "odd": "2.70"
                }
              ]
            },
            {
              "id": 22,
              "name": "Odd/Even - First Half",
              "values": [
                {
                  "value": "Even",
                  "odd": "1.60"
                },
                {
                  "value": "Odd",
                  "odd": "2.20"
                }
              ]
            },
            {
              "id": 21,
              "name": "Odd/Even",
              "values": [
                {
                  "value": "Even",
                  "odd": "1.80"
                },
                {
                  "value": "Odd",
                  "odd": "1.91"
                }
              ]
            },
            {
              "id": 34,
              "name": "Both Teams Score - First Half",
              "values": [
                {
                  "value": "No",
                  "odd": "1.14"
                },
                {
                  "value": "Yes",
                  "odd": "5.00"
                }
              ]
            },
            {
              "id": 32,
              "name": "Win Both Halves",
              "values": [
                {
                  "value": "Away",
                  "odd": "10.50"
                },
                {
                  "value": "Draw",
                  "odd": "1.13"
                },
                {
                  "value": "Home",
                  "odd": "8.00"
                }
              ]
            },
            {
              "id": 12,
              "name": "Double Chance",
              "values": [
                {
                  "value": "Draw/Away",
                  "odd": "1.50"
                },
                {
                  "value": "Home/Away",
                  "odd": "1.33"
                },
                {
                  "value": "Home/Draw",
                  "odd": "1.36"
                }
              ]
            },
            {
              "id": 10,
              "name": "Exact Score",
              "values": [
                {
                  "value": "3:4",
                  "odd": "126.00"
                },
                {
                  "value": "2:4",
                  "odd": "81.00"
                },
                {
                  "value": "2:3",
                  "odd": "36.00"
                },
                {
                  "value": "1:4",
                  "odd": "67.00"
                },
                {
                  "value": "1:3",
                  "odd": "26.00"
                },
                {
                  "value": "1:2",
                  "odd": "11.50"
                },
                {
                  "value": "0:4",
                  "odd": "67.00"
                },
                {
                  "value": "4:1",
                  "odd": "51.00"
                },
                {
                  "value": "4:0",
                  "odd": "51.00"
                },
                {
                  "value": "3:2",
                  "odd": "34.00"
                },
                {
                  "value": "3:1",
                  "odd": "21.00"
                },
                {
                  "value": "3:0",
                  "odd": "23.00"
                },
                {
                  "value": "2:1",
                  "odd": "10.50"
                },
                {
                  "value": "2:0",
                  "odd": "11.50"
                },
                {
                  "value": "1:0",
                  "odd": "7.25"
                },
                {
                  "value": "4:2",
                  "odd": "81.00"
                },
                {
                  "value": "4:3",
                  "odd": "126.00"
                },
                {
                  "value": "0:3",
                  "odd": "31.00"
                },
                {
                  "value": "0:2",
                  "odd": "14.00"
                },
                {
                  "value": "0:1",
                  "odd": "8.25"
                },
                {
                  "value": "4:4",
                  "odd": "151.00"
                },
                {
                  "value": "3:3",
                  "odd": "67.00"
                },
                {
                  "value": "2:2",
                  "odd": "16.00"
                },
                {
                  "value": "1:1",
                  "odd": "6.25"
                },
                {
                  "value": "0:0",
                  "odd": "6.25"
                }
              ]
            },
            {
              "id": 13,
              "name": "First Half Winner",
              "values": [
                {
                  "value": "Home",
                  "odd": "3.20"
                },
                {
                  "value": "Draw",
                  "odd": "1.90"
                },
                {
                  "value": "Away",
                  "odd": "3.70"
                }
              ]
            },
            {
              "id": 15,
              "name": "Team To Score Last",
              "values": [
                {
                  "value": "No goal",
                  "odd": "6.25"
                },
                {
                  "value": "Away",
                  "odd": "2.15"
                },
                {
                  "value": "Home",
                  "odd": "1.95"
                }
              ]
            },
            {
              "id": 14,
              "name": "Team To Score First",
              "values": [
                {
                  "value": "Away",
                  "odd": "2.15"
                },
                {
                  "value": "Draw",
                  "odd": "6.25"
                },
                {
                  "value": "Home",
                  "odd": "1.95"
                }
              ]
            },
            {
              "id": 46,
              "name": "Exact Goals Number - First Half",
              "values": [
                {
                  "value": "more 3",
                  "odd": "8.25"
                },
                {
                  "value": 0,
                  "odd": "2.35"
                },
                {
                  "value": 1,
                  "odd": "2.60"
                },
                {
                  "value": 2,
                  "odd": "4.75"
                }
              ]
            },
            {
              "id": 25,
              "name": "Result/Total Goals",
              "values": [
                {
                  "value": "Home/Over 2.5",
                  "odd": "4.60"
                },
                {
                  "value": "Away/Under 3.5",
                  "odd": "3.50"
                },
                {
                  "value": "Home/Under 3.5",
                  "odd": "3.00"
                },
                {
                  "value": "Away/Over 3.5",
                  "odd": "12.00"
                },
                {
                  "value": "Home/Over 3.5",
                  "odd": "9.25"
                },
                {
                  "value": "Away/Over 2.5",
                  "odd": "5.50"
                },
                {
                  "value": "Home/Under 2.5",
                  "odd": "4.50"
                },
                {
                  "value": "Away/Under 2.5",
                  "odd": "5.25"
                }
              ]
            },
            {
              "id": 24,
              "name": "Results/Both Teams Score",
              "values": [
                {
                  "value": "Away/No",
                  "odd": "4.40"
                },
                {
                  "value": "Draw/No",
                  "odd": "6.25"
                },
                {
                  "value": "Home/No",
                  "odd": "3.75"
                },
                {
                  "value": "Away/Yes",
                  "odd": "6.50"
                },
                {
                  "value": "Draw/Yes",
                  "odd": "4.50"
                },
                {
                  "value": "Home/Yes",
                  "odd": "5.50"
                }
              ]
            },
            {
              "id": 44,
              "name": "Away Team Score a Goal",
              "values": [
                {
                  "value": "No",
                  "odd": "2.55"
                },
                {
                  "value": "Yes",
                  "odd": "1.45"
                }
              ]
            },
            {
              "id": 43,
              "name": "Home Team Score a Goal",
              "values": [
                {
                  "value": "No",
                  "odd": "2.90"
                },
                {
                  "value": "Yes",
                  "odd": "1.36"
                }
              ]
            },
            {
              "id": 40,
              "name": "Home Team Exact Goals Number",
              "values": [
                {
                  "value": 1,
                  "odd": "2.55"
                },
                {
                  "value": 2,
                  "odd": "4.20"
                },
                {
                  "value": 0,
                  "odd": "2.90"
                },
                {
                  "value": "more 3",
                  "odd": "6.25"
                }
              ]
            },
            {
              "id": 42,
              "name": "Second Half Exact Goals Number",
              "values": [
                {
                  "value": "more 3",
                  "odd": "5.50"
                },
                {
                  "value": 0,
                  "odd": "3.00"
                },
                {
                  "value": 1,
                  "odd": "2.60"
                },
                {
                  "value": 2,
                  "odd": "3.90"
                }
              ]
            },
            {
              "id": 41,
              "name": "Away Team Exact Goals Number",
              "values": [
                {
                  "value": "more 3",
                  "odd": "7.25"
                },
                {
                  "value": 0,
                  "odd": "2.55"
                },
                {
                  "value": 1,
                  "odd": "2.50"
                },
                {
                  "value": 2,
                  "odd": "4.60"
                }
              ]
            },
            {
              "id": 7,
              "name": "HT/FT Double",
              "values": [
                {
                  "value": "Home/Home",
                  "odd": "4.20"
                },
                {
                  "value": "Draw/Draw",
                  "odd": "4.10"
                },
                {
                  "value": "Draw/Away",
                  "odd": "6.75"
                },
                {
                  "value": "Home/Away",
                  "odd": "36.00"
                },
                {
                  "value": "Home/Draw",
                  "odd": "14.50"
                },
                {
                  "value": "Away/Away",
                  "odd": "5.00"
                },
                {
                  "value": "Away/Draw",
                  "odd": "14.50"
                },
                {
                  "value": "Away/Home",
                  "odd": "31.00"
                },
                {
                  "value": "Draw/Home",
                  "odd": "5.75"
                }
              ]
            },
            {
              "id": 26,
              "name": "Goals Over/Under - Second Half",
              "values": [
                {
                  "value": "Under 3.5",
                  "odd": "1.01"
                },
                {
                  "value": "Over 3.5",
                  "odd": "12.00"
                },
                {
                  "value": "Over 1.5",
                  "odd": "2.50"
                },
                {
                  "value": "Under 1.5",
                  "odd": "1.48"
                },
                {
                  "value": "Under 0.5",
                  "odd": "3.00"
                },
                {
                  "value": "Over 0.5",
                  "odd": "1.34"
                },
                {
                  "value": "Under 2.5",
                  "odd": "1.11"
                },
                {
                  "value": "Over 2.5",
                  "odd": "5.50"
                }
              ]
            },
            {
              "id": 6,
              "name": "Goals Over/Under First Half",
              "values": [
                {
                  "value": "Under 0.5",
                  "odd": "2.35"
                },
                {
                  "value": "Over 0.5",
                  "odd": "1.53"
                },
                {
                  "value": "Under 2.5",
                  "odd": "1.04"
                },
                {
                  "value": "Over 2.5",
                  "odd": "8.25"
                },
                {
                  "value": "Under 1.5",
                  "odd": "1.28"
                },
                {
                  "value": "Over 1.5",
                  "odd": "3.30"
                },
                {
                  "value": "Under 3.5",
                  "odd": "1.01"
                },
                {
                  "value": "Over 3.5",
                  "odd": "21.00"
                }
              ]
            },
            {
              "id": 5,
              "name": "Goals Over/Under",
              "values": [
                {
                  "value": "Under 5.5",
                  "odd": "1.01"
                },
                {
                  "value": "Over 3.5",
                  "odd": "4.20"
                },
                {
                  "value": "Under 3.5",
                  "odd": "1.19"
                },
                {
                  "value": "Over 1.5",
                  "odd": "1.44"
                },
                {
                  "value": "Over 5.5",
                  "odd": "15.00"
                },
                {
                  "value": "Under 0.5",
                  "odd": "6.25"
                },
                {
                  "value": "Over 0.5",
                  "odd": "1.09"
                },
                {
                  "value": "Under 2.5",
                  "odd": "1.55"
                },
                {
                  "value": "Over 2.5",
                  "odd": "2.35"
                },
                {
                  "value": "Under 4.5",
                  "odd": "1.05"
                },
                {
                  "value": "Over 4.5",
                  "odd": "8.00"
                },
                {
                  "value": "Under 1.5",
                  "odd": "2.60"
                }
              ]
            },
            {
              "id": 3,
              "name": "Second Half Winner",
              "values": [
                {
                  "value": "Away",
                  "odd": "3.30"
                },
                {
                  "value": "Draw",
                  "odd": "2.20"
                },
                {
                  "value": "Home",
                  "odd": "2.85"
                }
              ]
            },
            {
              "id": 2,
              "name": "Home/Away",
              "values": [
                {
                  "value": "Away",
                  "odd": "2.05"
                },
                {
                  "value": "Home",
                  "odd": "1.70"
                }
              ]
            },
            {
              "id": 1,
              "name": "Match Winner",
              "values": [
                {
                  "value": "Away",
                  "odd": "2.95"
                },
                {
                  "value": "Draw",
                  "odd": "2.95"
                },
                {
                  "value": "Home",
                  "odd": "2.50"
                }
              ]
            },
            {
              "id": 9,
              "name": "Handicap Result",
              "values": [
                {
                  "value": "Away -2",
                  "odd": "1.13"
                },
                {
                  "value": "Draw -2",
                  "odd": "7.00"
                },
                {
                  "value": "Home -2",
                  "odd": "12.00"
                },
                {
                  "value": "Home -1",
                  "odd": "5.25"
                },
                {
                  "value": "Away +2",
                  "odd": "15.00"
                },
                {
                  "value": "Draw +2",
                  "odd": "8.25"
                },
                {
                  "value": "Home +2",
                  "odd": "1.09"
                },
                {
                  "value": "Draw +1",
                  "odd": "4.40"
                },
                {
                  "value": "Away +1",
                  "odd": "6.75"
                },
                {
                  "value": "Home +1",
                  "odd": "1.36"
                },
                {
                  "value": "Draw -1",
                  "odd": "4.00"
                },
                {
                  "value": "Away -1",
                  "odd": "1.50"
                }
              ]
            },
            {
              "id": 30,
              "name": "Win to Nil - Away",
              "values": [
                {
                  "value": "Yes",
                  "odd": "4.40"
                },
                {
                  "value": "No",
                  "odd": "1.17"
                }
              ]
            },
            {
              "id": 29,
              "name": "Win to Nil - Home",
              "values": [
                {
                  "value": "No",
                  "odd": "1.22"
                },
                {
                  "value": "Yes",
                  "odd": "3.75"
                }
              ]
            },
            {
              "id": 8,
              "name": "Both Teams Score",
              "values": [
                {
                  "value": "No",
                  "odd": "1.72"
                },
                {
                  "value": "Yes",
                  "odd": "2.00"
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

---


## seasons

**Dosya Boyutu:** 1504 bytes  
**Son Değişiklik:** 2025-06-19 22:21:25  

```text
Seasons

import http.client

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "XxXxXxXxXxXxXxXxXxXxXxXx"
    }

conn.request("GET", "/leagues/seasons", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

####################################################

Get the list of available seasons.

All seasons are only 4-digit keys, so for a league whose season is 2018-2019 like the English Premier League (EPL), the 2018-2019 season in the API will be 2018.

All seasons can be used in other endpoints as filters.

This endpoint does not require any parameters.

Update Frequency : This endpoint is updated each time a new league is added.

Recommended Calls : 1 call per day.

header Parameters
x-rapidapi-key
required
string
Your Api-Key
####################################################
Responses;

200 OK:
Response Schema: application/json
| Field | Type |
|-------|------|
| response | Array of strings |
| results | integer |
| errors | Array of objects |
| parameters | Array of objects |
| get | string |
{
  "get": "leagues/seasons",
  "parameters": [],
  "errors": [],
  "results": 12,
  "paging": {
    "current": 1,
    "total": 1
  },
  "response": [
    2008,
    2010,
    2011,
    2012,
    2013,
    2014,
    2015,
    2016,
    2017,
    2018,
    2019,
    2020
  ]
}
```

---


## standings

**Dosya Boyutu:** 2961 bytes  
**Son Değişiklik:** 2025-06-19 22:21:34  

```text
Standings
Get the standings for a league or a team.

Return a table of one or more rankings according to the league / cup.

Some competitions have several rankings in a year, group phase, opening ranking, closing ranking etc…

Examples available in Request samples "Use Cases".

Most of the parameters of this endpoint can be used together.

Update Frequency : This endpoint is updated every hour.

Recommended Calls : 1 call per hour for the leagues or teams who have at least one fixture in progress otherwise 1 call per day.

Tutorials :

HOW TO GET STANDINGS FOR ALL CURRENT SEASONS
query Parameters
league	
integer
The id of the league

season
required
integer = 4 characters YYYY
The season of the league

team	
integer
The id of the team

header Parameters
x-rapidapi-key
required
string
Your Api-Key
#################################################
Responses;
200 OK:
Response Schema: application/json
get	
string
parameters	
Array of objects
errors	
Array of objects
results	
integer
response	
Array of any
{
  "get": "standings",
  "parameters": {
    "league": "39",
    "season": "2019"
  },
  "errors": [],
  "results": 1,
  "paging": {
    "current": 1,
    "total": 1
  },
  "response": [
    {
      "league": {
        "id": 39,
        "name": "Premier League",
        "country": "England",
        "logo": "https://media.api-sports.io/football/leagues/2.png",
        "flag": "https://media.api-sports.io/flags/gb.svg",
        "season": 2019,
        "standings": [
          [
            {
              "rank": 1,
              "team": {
                "id": 40,
                "name": "Liverpool",
                "logo": "https://media.api-sports.io/football/teams/40.png"
              },
              "points": 70,
              "goalsDiff": 41,
              "group": "Premier League",
              "form": "WWWWW",
              "status": "same",
              "description": "Promotion - Champions League (Group Stage)",
              "all": {
                "played": 24,
                "win": 23,
                "draw": 1,
                "lose": 0,
                "goals": {
                  "for": 56,
                  "against": 15
                }
              },
              "home": {
                "played": 12,
                "win": 12,
                "draw": 0,
                "lose": 0,
                "goals": {
                  "for": 31,
                  "against": 9
                }
              },
              "away": {
                "played": 12,
                "win": 11,
                "draw": 1,
                "lose": 0,
                "goals": {
                  "for": 25,
                  "against": 6
                }
              },
              "update": "2020-01-29T00:00:00+00:00"
            }
          ]
        ]
      }
    }
  ]
}
```

---


## team-countries

**Dosya Boyutu:** 1150 bytes  
**Son Değişiklik:** 2025-06-19 22:21:45  

```text
Teams countries
Get the list of countries available for the teams endpoint.

Update Frequency : This endpoint is updated several times a week.

Recommended Calls : 1 call per day.

header Parameters
x-rapidapi-key
required
string
Your Api-Key
import http.client

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "XxXxXxXxXxXxXxXxXxXxXxXx"
    }

conn.request("GET", "/teams/countries", headers=headers)

res = conn.getresponse()
data = res.read()

##################################################
Responses;

200 OK:
Response Schema: application/json
| Field | Type |
|-------|------|
| get | string |
| parameters | Array of objects |
| errors | Array of objects |
| results | integer |
| response | Array of arrays |
{
  "get": "teams/countries",
  "parameters": [],
  "errors": [],
  "results": 258,
  "paging": {
    "current": 1,
    "total": 1
  },
  "response": [
    {
      "name": "England",
      "code": "GB",
      "flag": "https://media.api-sports.io/flags/gb.svg"
    }
  ]
}
```

---


## team-statistics

**Dosya Boyutu:** 8291 bytes  
**Son Değişiklik:** 2025-06-19 22:21:58  

```text
Teams statistics
Returns the statistics of a team in relation to a given competition and season.

It is possible to add the date parameter to calculate statistics from the beginning of the season to the given date. By default the API returns the statistics of all games played by the team for the competition and the season.

Update Frequency : This endpoint is updated twice a day.

Recommended Calls : 1 call per day for the teams who have at least one fixture during the day otherwise 1 call per week.

Here is an example of what can be achieved

demo-teams-statistics

query Parameters
league
required
integer
The id of the league

season
required
integer = 4 characters YYYY
The season of the league

team
required
integer
The id of the team

date	
stringYYYY-MM-DD
The limit date

header Parameters
x-rapidapi-key
required
string
Your Api-Key

import http.client

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "XxXxXxXxXxXxXxXxXxXxXxXx"
    }

conn.request("GET", "/teams/statistics?season=2019&team=33&league=39", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



######################################################
Responses;
200 OK:
Response Schema: application/json
| Field | Type |
|-------|------|
| get | string |
| parameters | Array of objects |
| errors | Array of objects |
| results | integer |
| response | object |
{
  "get": "teams/statistics",
  "parameters": {
    "league": "39",
    "season": "2019",
    "team": "33"
  },
  "errors": [],
  "results": 11,
  "paging": {
    "current": 1,
    "total": 1
  },
  "response": {
    "league": {
      "id": 39,
      "name": "Premier League",
      "country": "England",
      "logo": "https://media.api-sports.io/football/leagues/39.png",
      "flag": "https://media.api-sports.io/flags/gb-eng.svg",
      "season": 2019
    },
    "team": {
      "id": 33,
      "name": "Manchester United",
      "logo": "https://media.api-sports.io/football/teams/33.png"
    },
    "form": "WDLDWLDLDWLWDDWWDLWWLWLLDWWDWDWWWWDWDW",
    "fixtures": {
      "played": {
        "home": 19,
        "away": 19,
        "total": 38
      },
      "wins": {
        "home": 10,
        "away": 8,
        "total": 18
      },
      "draws": {
        "home": 7,
        "away": 5,
        "total": 12
      },
      "loses": {
        "home": 2,
        "away": 6,
        "total": 8
      }
    },
    "goals": {
      "for": {
        "total": {
          "home": 40,
          "away": 26,
          "total": 66
        },
        "average": {
          "home": "2.1",
          "away": "1.4",
          "total": "1.7"
        },
        "minute": {
          "0-15": {
            "total": 4,
            "percentage": "6.06%"
          },
          "16-30": {
            "total": 17,
            "percentage": "25.76%"
          },
          "31-45": {
            "total": 11,
            "percentage": "16.67%"
          },
          "46-60": {
            "total": 13,
            "percentage": "19.70%"
          },
          "61-75": {
            "total": 10,
            "percentage": "15.15%"
          },
          "76-90": {
            "total": 8,
            "percentage": "12.12%"
          },
          "91-105": {
            "total": 3,
            "percentage": "4.55%"
          },
          "106-120": {
            "total": null,
            "percentage": null
          }
        },
        "under_over": {
          "0.5": {
            "over": 30,
            "under": 8
          },
          "1.5": {
            "over": 20,
            "under": 18
          },
          "2.5": {
            "over": 11,
            "under": 27
          },
          "3.5": {
            "over": 4,
            "under": 34
          },
          "4.5": {
            "over": 1,
            "under": 37
          }
        }
      },
      "against": {
        "total": {
          "home": 17,
          "away": 19,
          "total": 36
        },
        "average": {
          "home": "0.9",
          "away": "1.0",
          "total": "0.9"
        },
        "minute": {
          "0-15": {
            "total": 6,
            "percentage": "16.67%"
          },
          "16-30": {
            "total": 3,
            "percentage": "8.33%"
          },
          "31-45": {
            "total": 7,
            "percentage": "19.44%"
          },
          "46-60": {
            "total": 9,
            "percentage": "25.00%"
          },
          "61-75": {
            "total": 3,
            "percentage": "8.33%"
          },
          "76-90": {
            "total": 5,
            "percentage": "13.89%"
          },
          "91-105": {
            "total": 3,
            "percentage": "8.33%"
          },
          "106-120": {
            "total": null,
            "percentage": null
          }
        },
        "under_over": {
          "0.5": {
            "over": 25,
            "under": 13
          },
          "1.5": {
            "over": 10,
            "under": 28
          },
          "2.5": {
            "over": 1,
            "under": 37
          },
          "3.5": {
            "over": 0,
            "under": 38
          },
          "4.5": {
            "over": 0,
            "under": 38
          }
        }
      }
    },
    "biggest": {
      "streak": {
        "wins": 4,
        "draws": 2,
        "loses": 2
      },
      "wins": {
        "home": "4-0",
        "away": "0-3"
      },
      "loses": {
        "home": "0-2",
        "away": "2-0"
      },
      "goals": {
        "for": {
          "home": 5,
          "away": 3
        },
        "against": {
          "home": 2,
          "away": 3
        }
      }
    },
    "clean_sheet": {
      "home": 7,
      "away": 6,
      "total": 13
    },
    "failed_to_score": {
      "home": 2,
      "away": 6,
      "total": 8
    },
    "penalty": {
      "scored": {
        "total": 10,
        "percentage": "100.00%"
      },
      "missed": {
        "total": 0,
        "percentage": "0%"
      },
      "total": 10
    },
    "lineups": [
      {
        "formation": "4-2-3-1",
        "played": 32
      },
      {
        "formation": "3-4-1-2",
        "played": 4
      },
      {
        "formation": "3-4-2-1",
        "played": 1
      },
      {
        "formation": "4-3-1-2",
        "played": 1
      }
    ],
    "cards": {
      "yellow": {
        "0-15": {
          "total": 5,
          "percentage": "6.85%"
        },
        "16-30": {
          "total": 5,
          "percentage": "6.85%"
        },
        "31-45": {
          "total": 16,
          "percentage": "21.92%"
        },
        "46-60": {
          "total": 12,
          "percentage": "16.44%"
        },
        "61-75": {
          "total": 14,
          "percentage": "19.18%"
        },
        "76-90": {
          "total": 21,
          "percentage": "28.77%"
        },
        "91-105": {
          "total": null,
          "percentage": null
        },
        "106-120": {
          "total": null,
          "percentage": null
        }
      },
      "red": {
        "0-15": {
          "total": null,
          "percentage": null
        },
        "16-30": {
          "total": null,
          "percentage": null
        },
        "31-45": {
          "total": null,
          "percentage": null
        },
        "46-60": {
          "total": null,
          "percentage": null
        },
        "61-75": {
          "total": null,
          "percentage": null
        },
        "76-90": {
          "total": null,
          "percentage": null
        },
        "91-105": {
          "total": null,
          "percentage": null
        },
        "106-120": {
          "total": null,
          "percentage": null
        }
      }
    }
  }
}
```

---


## teamsinfo

**Dosya Boyutu:** 2504 bytes  
**Son Değişiklik:** 2025-06-19 22:22:09  

```text
Teams information
Get the list of available teams.

The team id are unique in the API and teams keep it among all the leagues/cups in which they participate.

To get the logo of a team you have to call the following url: https://media.api-sports.io/football/teams/{team_id}.png

You can find all the teams ids on our Dashboard.

Examples available in Request samples "Use Cases".

All the parameters of this endpoint can be used together.

This endpoint requires at least one parameter.

Update Frequency : This endpoint is updated several times a week.

Recommended Calls : 1 call per day.

Tutorials :

HOW TO GET ALL TEAMS AND PLAYERS FROM A LEAGUE ID
query Parameters
id	
integer
The id of the team

name	
string
The name of the team

league	
integer
The id of the league

season	
integer = 4 characters YYYY
The season of the league

country	
string
The country name of the team

code	
string = 3 characters
The code of the team

venue	
integer
The id of the venue

search	
string >= 3 characters
The name or the country name of the team

header Parameters
x-rapidapi-key
required
string
Your Api-Key

import http.client

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "XxXxXxXxXxXxXxXxXxXxXxXx"
    }

conn.request("GET", "/teams?id=33", headers=headers)

res = conn.getresponse()
data = res.read()


###########################################
Responses;

200 OK:
Response Schema: application/json
| Field | Type |
|-------|------|
| get | string |
| parameters | Array of objects |
| errors | Array of objects |
| results | integer |
| response | Array of objects |

{
  "get": "teams",
  "parameters": {
    "id": "33"
  },
  "errors": [],
  "results": 1,
  "paging": {
    "current": 1,
    "total": 1
  },
  "response": [
    {
      "team": {
        "id": 33,
        "name": "Manchester United",
        "code": "MUN",
        "country": "England",
        "founded": 1878,
        "national": false,
        "logo": "https://media.api-sports.io/football/teams/33.png"
      },
      "venue": {
        "id": 556,
        "name": "Old Trafford",
        "address": "Sir Matt Busby Way",
        "city": "Manchester",
        "capacity": 76212,
        "surface": "grass",
        "image": "https://media.api-sports.io/football/venues/556.png"
      }
    }
  ]
}
```

---


## temp_memory.md

**Dosya Boyutu:** 2226 bytes  
**Son Değişiklik:** 2025-06-19 22:31:59  

```markdown
# Geçici Hafıza Dosyası - API Football Dokümantasyon Projesi

## Proje Özeti
- **Tarih:** 2025-06-19
- **Konum:** c:\Users\Mazzel\Desktop\api-football\api-enpoint-list
- **Görev:** Tüm API endpoint dosyalarını tek bir Markdown dosyasında birleştiren Python scripti oluşturma

## Tamamlanan İşlemler
1. ✅ Çalışma dizinindeki dosya yapısını analiz ettim
2. ✅ Kapsamlı Python scripti (`create_all_in_one_docs.py`) oluşturdum
3. ✅ Script başarıyla çalıştırıldı ve `all-in-one.md` dosyası oluşturuldu

## Script Özellikleri
- **Dosya Adı:** `create_all_in_one_docs.py`
- **Çıktı Dosyası:** `all-in-one.md`
- **İşlenen Dosya Sayısı:** 26 dosya
- **Toplam Boyut:** 211,940 bytes (yaklaşık 207 KB)

## Script Fonksiyonları
1. **Dosya Tarama:** Tüm alt klasörleri dahil ederek kapsamlı tarama
2. **Filtreleme:** Binary, gizli ve geçici dosyaları otomatik atlama
3. **Hata Yönetimi:** Okunamayan dosyalar için güvenli hata yakalama
4. **Encoding Desteği:** Çoklu encoding desteği (utf-8, latin-1, cp1252)
5. **Syntax Highlighting:** Dosya uzantısına göre otomatik dil tespiti
6. **Metadata:** Her dosya için boyut ve değişiklik tarihi bilgisi
7. **İçindekiler:** Otomatik içindekiler tablosu oluşturma
8. **Progress Tracking:** Terminal çıktısında işlem durumu gösterimi

## Kullanılan Teknolojiler
- Python 3
- pathlib modülü (dosya yolu işlemleri)
- mimetypes modülü (dosya türü tespiti)
- datetime modülü (zaman damgası)
- os modülü (işletim sistemi işlemleri)

## Dosya Yapısı
- Ana dizinde .txt dosyaları (Timezone.txt, leagues.txt)
- Alt klasörler aslında dosya (countries, fixtures, vb.)
- Toplam 26 adet API endpoint dokümantasyon dosyası

## Sonuç
Script başarıyla çalıştı ve tüm API endpoint dokümantasyonunu tek bir dosyada birleştirdi. Hiçbir hata oluşmadı ve tüm dosyalar başarıyla işlendi.

## Kullanım
```bash
python create_all_in_one_docs.py
```

## Önemli Notlar
- Script mevcut dizindeki tüm dosyaları tarar
- Binary dosyaları otomatik olarak atlar
- Hata durumlarında detaylı bilgi verir
- Çıktı dosyası UTF-8 encoding ile oluşturulur
- İçindekiler tablosu otomatik olarak oluşturulur
```

---


## Timezone.txt

**Dosya Boyutu:** 1265 bytes  
**Son Değişiklik:** 2025-06-19 22:22:30  

```text

Timezone


Get the list of available timezone to be used in the fixtures endpoint.

This endpoint does not require any parameters.

Update Frequency : This endpoint contains all the existing timezone, it is not updated.

Recommended Calls : 1 call when you need.

header Parameters
x-rapidapi-key
required
string
Your Api-Key

import http.client

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "XxXxXxXxXxXxXxXxXxXxXxXx"
    }

conn.request("GET", "/timezone", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


Responses;
########################################################
200 OK:
Response Schema: application/json
| Field | Type |
|-------|------|
| get | string |
| parameters | Array of objects |
| errors | Array of objects |
| results | integer |
| response | Array of strings |
{
  "get": "timezone",
  "parameters": [],
  "errors": [],
  "results": 425,
  "paging": {
    "current": 1,
    "total": 1
  },
  "response": [
    "Africa/Abidjan",
    "Africa/Accra",
    "Africa/Addis_Ababa",
    "Africa/Algiers",
    "Africa/Asmara"
  ]
}


```

---


---

**Dokümantasyon Özeti:**  
- İşlenen Dosyalar: 26  
- Atlanan Dosyalar: 1  
- Hatalı Dosyalar: 0  
- Oluşturulma Tarihi: 2025-06-19 22:36:11  
