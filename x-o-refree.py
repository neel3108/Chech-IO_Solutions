def checkio(game_result: List[str]) -> str:
    
    for i in range(3):
        if (game_result[i][0] in ['O', 'X']) and (game_result[i][0] == game_result[i][1] == game_result[i][2]):
            return game_result[i][0]
        if (game_result[0][i] in ['O', 'X']) and (game_result[0][i] == game_result[1][i] == game_result[2][i]):
            return game_result[0][i]
    if (game_result[1][1] in ['O', 'X']) and ((game_result[0][0] == game_result[1][1] == game_result[2][2]) or (game_result[0][2] == game_result[1][1] == game_result[2][0])):
        return game_result[1][1]
    return "D" 