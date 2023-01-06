from main import *



i1 = Item(name="apple", nodes=["food", "fruit"], price=5)
i2 = Item(name="some vynil", nodes=["music", "vynils"], price=30)
i3 = Item(name="keyboard", nodes=["electronics", "pc-related", "keyboards"], price=5)

warehouse = Warehouse(
    name="Warehouse", location="Cmyui Avenue", items=[], cash=100)
provider = Provider(name="That one provider", location="Cmyui Street",
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

warehouse.buy(2, provider, 0)


all_warehouses = [warehouse]
all_providers = [provider]
all_carriers = [carrier1, carrier2, carrier3, carrier4, carrier5, carrier6]
all_items = [i1, i2, i3]

