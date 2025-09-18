expense_month = ["january","february","march","april","may"]
expense_list = [2340, 2500, 2100, 3100, 2980]

e = input("Enter expense amount: ")
e = int(e)

month = -1
for i in range(len(expense_list)):
    if e == expense_list[i]:
        month = i
        break

if month != -1:
    print(f'You spent {e} in {expense_month[month]}')
else:
    print(f'You didn\'t spend {e} in any month')