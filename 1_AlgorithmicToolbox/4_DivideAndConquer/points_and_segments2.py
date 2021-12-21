# points_and_segments (different approach)

# segments: [aj, bj] for n segments
# cnt[i]: the number of segements that contain the point pi
# l = the number of segments that aj <= pi
# r = the number of segments that bj >= pi
# cnt[i] = l + r - n
# proof: 
# set A: aj <= p for all j (A': pi < aj)
# set B: bj >= p for all j(B': pi > aj)
# what we want to find is the intersection of A and B
# n(A intersection B) = n(A) + n(B) - n  = l + r - n
import sys

def binary_search_leq(array, point, start, end):
    mid = (start + end) // 2
    # print("L:", start, mid, end)
    if start >= end or start + 1 == end:
        if array[end] <= point:
            return end
        elif array[start] <= point:
            return start
        else: 
            return start - 1  
    else: 
        if array[mid] > point:
            return binary_search_leq(array, point, start, mid - 1)
        else: 
            return binary_search_leq(array, point, mid, end)
 
def binary_search_geq(array, point, start, end):
    mid = (start + end) // 2
    # print("G:", start, mid, end)
    if start >= end or start + 1 == end:
        if array[start] >= point:
            return start
        elif array[end] >= point:
            return end
        else: 
            return end + 1   
    else: 
        if array[mid] < point:
                return binary_search_geq(array, point, mid + 1, end)
        else:
            return binary_search_geq(array, point, start, mid)

def fast_count_segments2(starts, ends, points):
    n = len(starts)
    starts.sort()
    ends.sort()    
    cnt = [0 for i in range(len(points))]

    for i in range(len(points)):
        # print(i, ":")
        l = binary_search_leq(starts, points[i], 0, n - 1) + 1
        r = n - binary_search_geq(ends, points[i], 0, n - 1)
        cnt[i] = l + r - n
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments2(starts, ends, points)
    for x in cnt:
        print(x, end=' ')

    # n = 2
    # m = 3
    # starts = [0, 7]
    # ends = [5, 10]
    # points = [1, 6, 11]
    # cnt = fast_count_segments2(starts, ends, points)
    # for x in cnt:
    #     print(x, end=' ')