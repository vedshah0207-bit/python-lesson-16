try:
    num = int(input("Give number. "))
    print("The number entered is", num)
except ValueError as ex:
    print("Exeption", ex)