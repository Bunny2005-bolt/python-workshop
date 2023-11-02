player_stats={
    "name":"player 1",
    "score": 100,
    "level":5
}
def display_player_info():
    print(f"Name: {player_stats['name']}")
    print(f"Score: {player_stats['score']}")
    print(f"Level: {player_stats['level']}")

display_player_info()