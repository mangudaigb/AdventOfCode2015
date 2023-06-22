
def calculateArea():
    pass

with open('day2-input', 'r') as file:
# with open('day2-test', 'r') as file:
    cover = 0
    ribbon = 0
    while line := file.readline():
        input = line.strip()
        [w, h, l] = input.split("x")
        print(line.strip())
        print("W: " + w + "\tH:" + h + "\tL: " + l)
        area = 2*int(l)*int(w) + 2*int(w)*int(h) + 2*int(h)*int(l)
        extra = min(int(l)*int(w), int(w)*int(h), int(h)*int(l))
        print("Area: " + str(area))
        print("Extra: " + str(extra))
        cover = cover + area + extra

        shortest = 2*(min(int(l) + int(w), int(w) + int(h), int(h) + int(l)))
        vol = int(l) * int(w) * int(h)
        ribbon += (shortest + vol)

    print("Cover: " + str(cover))
    print("Ribbon: " + str(ribbon))
