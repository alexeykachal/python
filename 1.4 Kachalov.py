
def quarter(x):
    if x < 0 or x > 4:
        print("нужно ввести число от одного до четырех")
    elif x == 1:
        print("x > 0, y > 0")
    elif x == 2:
        print("x < 0, y > 0")
    elif x == 3:
        print("x < 0, y < 0")
    elif x == 4:
        print("x > 0, y < 0")