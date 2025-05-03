import csv,io,json

fieldnames = ['date','category','amount','description']


def write_data(data:list):
    if len(data) == 0:
        return []
    try:
        with open('data\\expense.csv', 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            for row in data:
                writer.writerow(row)

    except:
        return data

    return []


def get_data():
    rows = []
    with open('data\\expense.csv', 'r') as csvfile:

        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['amount'] != '' and row['date'] != '' and row['category'] != '' and row['description'] != '' :
                rows.append(row)
            else:
                continue
    return rows

def get_monthly_budget():
    try:
        _data = json.load(io.open('data\\budget.json', encoding="utf8"))
        return float(_data['budget'])
    except:
        return 0


def set_monthly_budget(m_value:float):
    try:
        _data = json.load(io.open('data\\budget.json', encoding="utf8"))
        _data['budget'] = m_value
        json.dump(_data, io.open('data\\budget.json', 'w', encoding="utf8"))
        print("Monthly budget saved!")
    except:
        print("Something went wrong")
    return