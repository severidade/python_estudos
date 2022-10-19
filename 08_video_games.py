import json

# with open(file="data/video_games/video_games.json") as games_file:
#     print(json.load(games_file)[0]['Title'])


# try:
#     with open(file="data/video_games/video_games.json") as games_file:
#         games_list = json.load(games_file)
#         for game in games_list:
#             print(game["Title"])
# except FileNotFoundError:
#     print("O arquivo não foi encontrado")


try:

    listGamesNames = []

    with open(file="data/video_games/video_games.json") as games_file:
        games_list = json.load(games_file)
        for game in games_list:
            listGamesNames.append(game["Title"] + "\n")

    with open(file="data/video_games/lista.txt", mode="w") as lista:
        listGamesNames.sort()
        lista.writelines(listGamesNames)

except FileNotFoundError:
    print("O arquivo não foi encontrado")


# Super Mario 64 DS é o primeiro jogo
# do arquivo json mas quando eu
# passo na primeira lógica ele nao aprece como primeiro
