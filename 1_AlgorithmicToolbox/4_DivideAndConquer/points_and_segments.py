# Failed case #4/25: time limit exceeded (Time used: 39.99/20.00, memory used: 26890240/2147483648.)
# modified on points_and_segments2.py

# You are organizing an online lottery. To participate, a person bets on a single integer. 
# You then draw several ranges of consecutive integers at random. 
# A participant’s payoff then is proportional to the number of ranges 
# that contain the participant’s number minus the number of ranges that does not contain it. 
# You need an efficient algorithm for computing the payoffs for all participants. 
# A naive way to do this is to simply scan, for all participants, the list of all ranges. 
# However, you lottery is very popular: you have thousands of participants and thousands of ranges. 
# For this reason, you cannot afford a slow naive algorithm.

# Task: You are given a set of points on a line and a set of segments on a line. 
#       The goal is to compute, for each point, the number of segments that contain this point.
# Input Format: 
# |-- The first line contains two non-negative integers s and p 
#     defining the number of segments and the number of points on a line, respectively. 
# |-- The next s lines contain two integers ai, bi defining the i-th segment [ai, bi]. 
# |-- The next line contains p integers defining points x1, x2, ..., xp
# Constraints: 
# |-- 1 <= s, p <= 50000; -10^8 <= ai <= bi <= 10^8 for all 0 <= i < s; 
# |-- -10^8 <= xj <= 10^8 for all 0 <= j < p
# Output Format: Output p non-negative integers k0, k1, ..., kp-1 where ki is the number of segments which contain xi. 
# More formally, ki = {j: aj <= xi <= bj}

# Uses python3
import sys

def merge_count(sort_points, cnt, left, right, start_point, end_point):
    if left > right:
        return cnt

    mid = (left + right) // 2
    # print(left, mid, right)
    if left <= right:
        if sort_points[mid] < start_point:
            merge_count(sort_points, cnt, mid + 1, right, start_point, end_point)
        elif sort_points[mid] > end_point:
            merge_count(sort_points, cnt, left, mid - 1, start_point, end_point)
        else:
            cnt[mid] += 1
            # print("cnt:", cnt)
            merge_count(sort_points, cnt, mid + 1, right, start_point, end_point)
            merge_count(sort_points, cnt, left, mid - 1, start_point, end_point)


def fast_count_segments(starts, ends, points):
    ori_loc = sorted(range(len(points)), key = lambda k : points[k]) 
    points.sort()
    cnt = [0] * len(points)

    for i in range(len(starts)):
        # print("=" * 20)
        # print("no", i)
        if points[0] > ends[i] or points[-1] < starts[i]:
            break
        else:
            merge_count(points, cnt, 0, len(points) - 1, starts[i], ends[i])
        
    cnt = [cnt[i] for i in ori_loc]
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n = data[0]
    # m = data[1]
    # starts = data[2:2 * n + 2:2]
    # ends   = data[3:2 * n + 2:2]
    # points = data[2 * n + 2:]
    # #use fast_count_segments
    # cnt = naive_count_segments(starts, ends, points)
    # for x in cnt:
    #     print(x, end=' ')

    n = 2
    m = 3
    starts = [4, 4]
    ends = [5, 5]
    points = [5, 5, 5]
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
