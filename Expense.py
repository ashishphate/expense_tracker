from datetime import datetime
import functools


class Expense:
    date = ""
    category = ""
    amount = 0.0
    description = ""


    def todict(self):
        return {"date": self.date, "category": self.category, "amount": self.amount, "description": self.description}


    def _is_valid_date_format(self):
        try:
            datetime.strptime(self.date, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def _is_valid_amount(self):
        try:
            if float(self.amount) > 0.01:
                return True
            else:
                return False
        except ValueError:
            return False


    def add(self,data:list):
        self.date = input("Enter date (YYYY-MM-DD): \n")
        if not self._is_valid_date_format():
            print("Invalid date format.")
            return
        self.category = input("Enter Category e.g. travel, food, other: \n")
        self.amount = input("Enter amount e.g. 100.00: \n")
        if not self._is_valid_amount():
            print("Invalid Amount.")
            return
        self.description = input("Enter Description: \n")
        data.append(self.todict())
        print("Expense added successfully.")
        return


    @staticmethod
    def get_monthly_total(year,month, data:list):
        month = str(month).zfill(2)
        str_month = str(year) + "-" + month + "-"
        total = sum([float(d['amount']) for d in data if str(d['date']).startswith(str_month)])
        return total
