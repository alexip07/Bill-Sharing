from flat import Bill, Flatmate
from report import PdfReport

amount = float(input("Hey user, enter the bill amount: "))
period = input("Input the period of the bill(Eg. December 2020): ").capitalize()

first_housemate = input("The name of the first Flatmate: ").capitalize()
day_in_house1 = int(input(f"How many days did {first_housemate} stay in the house during the bill period: "))

second_housemate = input("The name of the second Flatmate: ").capitalize()
day_in_house2 = int(input(f"How many days did {second_housemate} stay in the house during the bill period: "))

the_bill = Bill(amount=amount, period=period)
flat1 = Flatmate(name=first_housemate, days_in_house=day_in_house1)
flat2 = Flatmate(name=second_housemate, days_in_house=day_in_house2)

print(f"{first_housemate} pays: ", flat1.pays(bill=the_bill, flatmate2=flat2))
print(f"{second_housemate} pays: ", flat2.pays(bill=the_bill, flatmate2=flat1))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=flat1, flatmate2=flat2, bill=the_bill)