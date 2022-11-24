# Python 3 program to find maximum no of pieces
#by given number of cuts

# Function for finding maximum pieces
# with n cuts.
def findMaximumPieces(n):

    # to maximise number of pieces
    # x is the horizontal cuts
    x = n // 2

    # Now (x) is the horizontal cuts
    # and (n-x) is vertical cuts, then
    # maximum number of pieces = (x+1)*(n-x+1)
    return ((x+1) * (n - x + 1))
# Driver code
if __name__ == "__main__":

    # Taking the maximum number of cuts allowed as 3
    n = 3

    # Finding and printing the max number of pieces
    print("Max number of pieces for n = " +str( n)
         +" is " + str(findMaximumPieces(3)))
# This code is contributed by SudheeSanket

