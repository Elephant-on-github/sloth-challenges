def lemonade(x):
    tens = 0
    fives = 0
    twenties = 0  # Initialize counters for each denomination
    for i in x:  # Iterate over indices
        if i == 20:
            tens -= 1
            if tens < 0:
                print("false")
                return False
            fives -= 1
            if fives < 0:
                print("false")
                return False
            twenties += 1
            
        elif i == 10:  # Check the current element
            fives -= 1
            if fives < 0:
                print("false")
                return False
            tens += 1
        elif i == 5:
            fives += 1
    print("true")
    return True

# Test cases
# lemonade([10, 10])  # Should return False
# lemonade([5, 5, 10])  # Should return True

def randomtest(y=None):
    import random
    if y is None:  # Initialize y only once
        y = []
    i = random.randint(0, 3)
    if i == 0:
        print("5")
        y.append(5)
        randomtest(y)
    elif i == 1:
        print("10")
        y.append(10)
        randomtest(y)
    elif i == 2:
        print("20")
        y.append(20)
        randomtest(y)
    elif i == 3:
        print("exit")
        print(y)
        lemonade(y)

randomtest()