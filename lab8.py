# Lab 8: report on cis class availability
from CISclasses2 import CISclasses

cis = CISclasses()
print("Total:", cis.getCount(), "CIS classes")

answer = input("\nk. Search by keyword in name, q. Search by quarter, e. End\nYour choice: ").lower()
while answer != 'e':
    if answer == 'k':
        name = input("Enter keyword: ").title()
        cis.getQuarters(name)
    elif answer == 'q':
        quarter = input("Enter quarter (fall, winter, spring, summer): ")
        cis.getClasses(quarter.lower())
    else:
        print("Enter k, q, or e only")
    answer = input("\nk. Search by keyword in name, q. Search by quarter, e. End\nYour choice: ").lower()
