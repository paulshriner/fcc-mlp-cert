# The winning moves associated with Rock, Paper, Scissors
winning_moves = {'R': 'P', 'P': 'S', 'S': 'R'}

# Number of moves we will look back on
chain_length = 7

# The program works by looking back at a number of the last moves played
# It then makes potential combinations for each possible move (R, P, S) and sees which one has the highest occurance
# This will likely be the next move made by the opponent, so we play the countering move
# Huge thanks to https://medium.com/@sri.hartini/rock-paper-scissors-in-python-5173ab69ca7a for which the idea is based off
def player(prev_play, opponent_history=[], order={}):
    # This means we played first, so play as though the opponent's first move is rock
    if not prev_play:
        prev_play = "R"
    
    # Save opponent's prev move, start by setting prediction to prev move
    opponent_history.append(prev_play)
    prediction = prev_play

    # Need to have minimum of chain_length moves
    if len(opponent_history) > chain_length - 1:
        # Player's last moves
        opp_plays = "".join(opponent_history[-chain_length:])

        # Count how many times set of player's last moves occured
        order[opp_plays] = order.get(opp_plays, 0) + 1
        
        # Get current order of moves based on chain length
        current_order = "".join(opponent_history[-chain_length + 1::])
        
        # Get potential next plays
        potential_orders = [current_order + i for i in ["R", "P", "S"]]
        
        # Determine the order that has occured the most
        highest = potential_orders[0]
        for i in range(1, len(potential_orders)):
            if order.get(potential_orders[i], 0) > order.get(highest, 0):
                highest = potential_orders[i]

        # Choose move predicted from that order
        prediction = highest[-1]

    return winning_moves[prediction]
