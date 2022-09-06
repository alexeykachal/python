
def quartercheck(x,y):
    if x == 0 or y == 0:
        print("x и y не должны быть равны нулю")
    elif x > 0:
        if y > 0:
            print("I четверть")
        if y < 0:
            print("IV четверть")
    elif x < 0:
        if y > 0:
            print("II четверть")
        if y < 0:
            print("III четверть")


quartercheck(-1,1)