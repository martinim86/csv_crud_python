
import csv

class DataBase:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def add_prod(self):
        with open(r'products.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow({self.name, self.price})

    def filter(self):
        list = []
        with open('products.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

            for row in spamreader:
                list.append(str(row[0]).split(",")[0])
        return list
    def edit_prod(self, prod_name, price_name):
        with open('products.csv') as csvfile, open('products.csv', 'w+') as out:
            writer = csv.writer(out)
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                name, cost =str(row[0]).split(",")[0], str(row[1]).split(",")[0]
                if name == str(prod_name):
                    cost = str(price_name)
                writer.writerow({name, cost})

    def delete_prod(self,prod_name):
        with open('products.csv') as csvfile, open('products.csv', 'w+') as out:
            writer = csv.writer(out)
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                name, cost = str(row[0]).split(",")[0], str(row[1]).split(",")[0]
                if name != str(prod_name):
                    writer.writerow(row)
