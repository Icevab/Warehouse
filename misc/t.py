import inspect
import main


# commands = dict(inspect.getmembers(main, predicate=inspect.isfunction))
# print(commands["hello"]())

# str_test = "hello : hi wassup what no way broooooooooooo"

# print(":" in str_test)

# data = {'money_made': 54.23, 'change_in_money_made': -3.48, 'money_spent': 102.3, 'change_in_money_spent': 3.0, 'cash': 
# 5.0, 'change_in_cash': 542.2, 'items': 2.0, 'taxes_paid': 54.34, 'change_in_taxes_paid': 4968.34}

# for item in data:
#     print(data[item])


all_functions = inspect.getmembers(main, inspect.isfunction)

# print(dict(all_functions))

print("best_carrier" in dict(all_functions).keys())