import os.path
import webbrowser

from flat import Bill, Flatmate
from pdf import PdfReport


the_bill = Bill(
    amount=float(input("What is the bill amount? \n")), 
    period=input("What is the bill period (Eg: January 2025)? \n")
)
name1 = input("What is the name of the first flatmate? \n")
days1 = int(input(f"How many days did {name1} stay? \n"))
flatmate1 = Flatmate(name=name1, days_in_house=days1)

name2 = input("What is the name of the second flatmate? \n")
days2 = int(input(f"How many days did {name2} stay? \n"))
flatmate2 = Flatmate(name=name2, days_in_house=days2)
print(f"{flatmate1.name} pays: {flatmate1.pays(the_bill, flatmate2):.2f}, because they stayed {flatmate1.days_in_house} days and the percentage of the bill is {flatmate1.pays(the_bill, flatmate2)/the_bill.amount*100:.2f}%")
print(f"{flatmate2.name} pays: {flatmate2.pays(the_bill, flatmate1):.2f}, because they stayed {flatmate2.days_in_house} days and the percentage of the bill is {flatmate2.pays(the_bill, flatmate1)/the_bill.amount*100:.2f}%")


report = PdfReport(
    filename="17_ OOP_Object_Oriented_Programming/ 04_flatmates_bill_sharing_oop/flatmates_bill7.pdf",
    flatmate1=flatmate1,
    flatmate2=flatmate2,
    bill=the_bill
)


report.generate()


