y = int(input("introduce a year between 1700 and 2700: "))
a= 12
b= 13
def dayOfProgrammer(y):
    if y % 4 == 0 and y % 100 != 0 or y % 400 ==0:
     print(f"el dia del programador es en {a}/9/{y}")
    elif y == 1918:
      print(f"el dia del programador fue en {b}/9/{y}")
    else:
      print(f"el dia del programador fue en {b}/9/{y}")
dayOfProgrammer(y)