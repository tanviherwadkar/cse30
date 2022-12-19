# make a generator
def rooks(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in rooks(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:] 

def queens(perm):
    for i in range(len(perm)):
        for j in range(i+1, len(perm)):
            y1 = i+1
            y2 = j+1
            x1 = perm[i]
            x2 = perm[j]
            
            slope = (y2-y1)/(x2-x1)
            if slope == 1 or slope == -1:
                return False
    return True

def board(size):
    data = [x for x in range(size)]
    for i in rooks(data):
        if queens(i) == True:
            print(i)

if __name__ == '__main__':
    """print("For size 4:")
    board(4)
    print("\nFor size 5:")
    board(5)
    print("\nFor size 6:")
    board(6)"""

    data = [1,2,3,4]
    for i in rooks(data):
        print(queens(i), "\t", i)