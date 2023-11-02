def multiplication_table(number):

    table = [str(number * x) for x in range(1, 13)]
    return table

thing = int(input("give me a positive integer please: "))
print(multiplication_table(thing))
