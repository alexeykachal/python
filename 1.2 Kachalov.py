
def table():
    for x in 1, 0:
        for y in 1, 0:
            for z in 1, 0:
                print(f"{x = } {y = } {z = }  {not(x or y or z) == (not x and not y and not z)}")

table()