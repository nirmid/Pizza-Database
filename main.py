# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from dto import Hat, Supplier, Order
from repository import repo
def main():
    repo.create_tables()
    config = open(sys.argv[1],"r")
    nums = config.readline().rstrip().split(",")
    for i in range(0, int(nums[0])):
        config.readline()
    for i in range(0, int(nums[1])):
        supplier = config.readline().strip().split(",")
        repo.suppliers.insert(Supplier(int(supplier[0]),supplier[1]))

    config.seek(0)
    config.readline()

    for i in range(0, int(nums[0])):
        hat = config.readline().strip().split(",")
        repo.hats.insert(Hat(int(hat[0]), hat[1], hat[2], int(hat[3])))

    orders = open(sys.argv[2], "r")
    counter = 1
    output = open(sys.argv[3],"w")
    for line in orders:
        arguments = line.rstrip().split(",")
        hat = repo.hats.find(arguments[1])
        if hat != None:
            repo.orders.insert(Order(counter, arguments[0], hat.id))
            counter = counter + 1
            repo.hats.update(hat)
            supplier = repo.suppliers.find(hat.supplier)
            output.write(arguments[1]+","+supplier.name+","+arguments[0] + "\n")






















if __name__ == '__main__':
    main()

