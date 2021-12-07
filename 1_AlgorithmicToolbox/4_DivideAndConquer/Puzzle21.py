# Find an unknown integer 1 <= x <= 2097151 
# by asking 21 questions “Is x = y?” (for any 1 ≤ y ≤ 2097151 ). 
# When you ask such a question, simply enter "y" 
# instead of "Is x=y?" 
# Your opponent will reply either “Yes”, or “x < y”, or “x > y.”

def findNum(low, high):
    while low <= high:
        mid = round((low + (high - low)/2))
        print("mid:", mid)

        # if key = A[mid] then ans = y
        ans = input("ans:")
        if ans.lower() == 'y':
            print("=============")
            print("End!")
            print("Number:", mid)
            return mid
        # if key < A[mid] then ans = s
        elif ans.lower() == 's':
            high = mid - 1
            print("low:", low)
            print("high:", high)
            print("=============")
        elif ans.lower() == 'l':
            low = mid + 1
            print("low:", low)
            print("high:", high)
            print("=============")
        else:
            print("Invalid input")
            
    return low - 1


if __name__ == "__main__":
    findNum(1, 2097151)