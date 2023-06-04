#!/usr/bin/python3
"""0-prime_game.py defines isWineer function, a solution to the Prime Game"""


def isWinner(x, nums):
    '''
    Determines winner of Prime Game
    Args:
        x (int): no. of rounds of game
        nums (list): upper limit of range for each round
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    '''
    player1 = "Maria"
    player2 = "Ben"
    player1_count = 0
    player2_count = 0

    while x >= 1:
        for number in nums:
            prime_list = []  # store prime numbers upto the 'number'
            for num in range(2, number + 1):
                is_prime = True
                for i in range(2, num):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    prime_list.append(num)

            if number == 1:
                player2_count += 1
            elif len(prime_list) % 2 == 0:
                player2_count += 1
            elif len(prime_list) % 2 == 1:
                player1_count += 1

            x -= 1
    if player1_count == player2_count:
        return None
    elif player1_count > player2_count:
        return f"Winner: {player1}"
    else:
        return f"Winner: {player2}"
