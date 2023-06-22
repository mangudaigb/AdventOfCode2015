
def calculateFloor():
    with open('day1-test.txt', 'r') as file:
        data = file.read()
        floor = 0
        basement = -1

        for i, c in enumerate(data):
            if c == '(':
                print("UP")
                floor = floor + 1
            elif c == ')':
                print("DOWN")
                floor = floor - 1
            if floor == -1:
                return i
        
        print("Data: " + data)
        print("Floor: " + str(floor))
    return -1

print("Index: " + str(calculateFloor()))
