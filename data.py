import csv


data = open("Data\default_of_credit_card_clients.csv")

rows = []
with open("Data\default_of_credit_card_clients.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    fields2 = next(csvreader)
    for row in csvreader:
        rows.append(row)


print(fields2)

