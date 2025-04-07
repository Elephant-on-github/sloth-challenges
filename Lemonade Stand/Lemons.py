def lemonade(x):
    tens = 0
    fives = 0
    for i in x:  # Iterate over indices
        if i == 10:  # Check the current element
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
lemonade([10, 10])  # Should return False
lemonade([5, 5, 10])  # Should return True
