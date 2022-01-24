# primitive calculator (different approach: bottom-up without recursion)

# Uses python3
import sys
from primitive_calculator import GreedyCalculator

def primitive_calculator(n):
    k = [-1 for i in range(n)]
    s = [ 1 for i in range(n)]
    # print("k:", k)
    # print("s:", s)
    # print("=" * 30)

    for j in range(1, n + 1):
        if j == 1:
            k[j - 1] = 0
            s[j - 1] = 1
        elif j <= 3:
            k[j - 1] = 1
            s[j - 1] = 1
        else:
            # three operators
            val1 = k[j - 2]
            if j % 2 == 0:
                val2 = k[(j // 2) - 1]
            else:
                val2 = float("inf")
            if j % 3 == 0:
                val3 = k[(j // 3) - 1]
            else:
                val3 = float("inf")
            # check which is the minimum
            if val3 <= val1 and val3 <= val2:
                k[j - 1] = val3 + 1
                s[j - 1] = j // 3
            elif val2 <= val1 and val2 <= val3:
                k[j - 1] = val2 + 1
                s[j - 1] = j // 2
            else:
                k[j - 1] = val1 + 1
                s[j - 1] = j - 1
        # print("k:", k)
        # print("s:", s)
        # print("=" * 30)

    out = [n]
    while n > 1:
        out.append(s[n - 1])
        n = s[n - 1]
    
    return out

if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)
    sequence = list(primitive_calculator(n))
    print(len(sequence) - 1)
    for x in reversed(sequence):
        print(x, end=' ')

    # for n in range(1, 1001):
    #     greedy = list(GreedyCalculator(n))
    #     dynamic = list(reversed(primitive_calculator(n)))
    #     if len(greedy) >= len(dynamic):
    #         print("n:", n, "OK")
    #     else:
    #         print("n:", n, "Wrong")
    #         print("Greedy:", len(greedy) - 1)
    #         print(greedy)
    #         print("Dynamic:", len(dynamic) - 1)
    #         print(dynamic)
    #         break