#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""


def isWinner(x, nums):
    """x - rounds
    nums - numbers list
    """
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
