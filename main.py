from Expense import Expense
import filemanager
from datetime import datetime

def menu():
    data = []
    print("Hi, I am your Personal Expense Tracker.\n")
    while True:
        choice = input("\n"
                       "1:- Add Expense \n"
                       "2:- View Expense \n"
                       "3:- Track budget\n"
                       "4:- Save Expense \n"
                       "5:- Exit\n"
                       "Select an option: \n")
        if choice == "1":
            e = Expense()
            e.add(data)
        elif choice == "2":
            data = filemanager.write_data(data)
            rows = filemanager.get_data()
            Expense.list(rows,filemanager.fieldnames)

        elif choice == "3":
            data = filemanager.write_data(data)
            amt = input("Enter your monthly budget\n")
            try:
                amt = float(amt)
                filemanager.set_monthly_budget(amt)
                rows = filemanager.get_data()
                cur_date = datetime.now()
                cur_month_exp = Expense.get_monthly_total(cur_date.year, cur_date.month,rows)
                if cur_month_exp > amt:
                    print("You have exceeded your budget!")
                else:
                    print(f"You have {amt-cur_month_exp} left for the month")
            except Exception as e:
                print(str(e))
        elif choice == "4":
            data = filemanager.write_data(data)
            print("Data saved!")
        elif choice == "5":
            data = filemanager.write_data(data)
            print("Thank you!")
            break
        else:
            print("Invalid option")


if __name__ == '__main__':
    menu()