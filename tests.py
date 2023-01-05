from main import *


i1 = Item(name="apple", nodes=["food", "fruit"], price=5)
i2 = Item(name="some vynil", nodes=["music", "vynils"], price=30)
i3 = Item(name="keyboard", nodes=["electronics", "pc-related", "keyboards"], price=25)

warehouse = Warehouse(
    name="Warehouse", location="Cmyui Avenue", items=[], cash=100)
provider = Provider(name="Provider", location="Cmyui Street",
                    items=[i1, i2, i3], carriers=[], cash=10000)
carrier1 = Carrier(name="cmyui", speed=2, desired_wage=1, cash=0)
carrier2 = Carrier(name="cmyui2", speed=4, desired_wage=5, cash=0)
carrier3 = Carrier(name="cmyui3", speed=1, desired_wage=1, cash=0)
carrier4 = Carrier(name="cmyui4", speed=12, desired_wage=50, cash=0)
carrier5 = Carrier(name="cmyui5", speed=4, desired_wage=7, cash=0)
carrier6 = Carrier(name="cmyui6", speed=8, desired_wage=8, cash=0)



provider.add_carrier(carrier1)
provider.add_carrier(carrier2)
provider.add_carrier(carrier3)
provider.add_carrier(carrier4)
provider.add_carrier(carrier5)
provider.add_carrier(carrier6)

# warehouse.buy(2, provider, 0)

# build_nodes_of_item(i3)

# c = best_carrier(provider.carriers, 40)
# print(c)

# print(len(warehouse.items))

# print(calculate_percent_off(i3, 67))
print(callable(calculate_price))

# items = {
#     "fruit": {
#         "apple": {
#             "item_name": "apple",
#             "price": 5,
#             "amount": 203
#         },
#         "pear": {
#             "item_name": "pear",
#             "price": 6,
#             "amount": 145
#         }
#     },
#     "vegetables": {
#         "tomato": {
#             "item_name": "tomato",
#             "price": 7,
#             "amount": 254
#         },
#         "potato": {
#             "item_name": "potato",
#             "price": 3,
#             "amount": 24
#         }
#     }
# }

# i_test = {
#     "item_name": "grapes",
#     "price": 4,
#     "amount": 203
# }



# print(provider.items)