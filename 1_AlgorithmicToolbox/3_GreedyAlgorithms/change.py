# you will design and implement an elementary greedy algorithm 
# used by cashiers all over the world millions of times per day

# Task: to find the minimum number of coins needed to change the input value (an integer) into coins with denominations 1, 5, and 10.
# Input Format: The input consists of a single integer m
# Constraints: 1 <= m <= 10^3
# Output Format: Output the minimum number of coins with denominations 1, 5, 10 that changes m
import sys

def face(m, face):
    num_coins = m // face
    m -= num_coins * face
    # print("remain_m:", m)
    # print("num_coins(", face, "): ", num_coins, sep = "")

    return [m, num_coins]


def get_change(m):
    m = int(m)
    num_coins = 0
    tmp_coins = 0

    # face = 10
    if m >= 10:
        m, tmp_coins = face(m, 10)
        num_coins += tmp_coins
    
    # face = 5
    if m >= 5:
        m, tmp_coins = face(m, 5)
        num_coins += tmp_coins
    
    # face = 1
    if m >= 1:
        m, tmp_coins = face(m, 1)
        num_coins += tmp_coins

    return num_coins

if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))


