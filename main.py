from rich.console import Console
import math

console = Console()

import time

# TODO: Make it a CLI

class Warehouse:
    def __init__(self, name: str, location: str, items, cash: float):
        self.name = name
        self.location = location
        self.items = items
        self.cash = cash

    # TODO: Refactor this method, PLEASE.
    def buy(self, item_index, provider, carrier_index):
        # TODO: Add taxes?
        
        item: Item = provider.items[item_index]
        carrier: Carrier = provider.carriers[carrier_index]
        c_wage = calculate_carrier_wage(carrier, calculate_distance(provider, self))
        
        if (self.cash < item.price):
            print(f"Need {item.price - self.cash} more cash")
            return
        
        if (len(provider.items) == item_index):
            return
        
        if (len(provider.carriers) == 0):
            return
        
        # pre or post cash?
        # carrier can say whether they're ok with money coming in later
        if (provider.cash < c_wage):
            print(f"Provider needs {c_wage - provider.cash} more cash")
            return
        
        
        # print(f"pre self.items length - {len(self.items)}")
        # print(f"pre provider.items length - {len(provider.items)}")
        # print(f"pre self.cash - {self.cash}")
        # print(f"pre provider.cash - {provider.cash}")    
        # s = f"{provider.location}            {self.location}"
        
        # save provider's cash before charging
        pre_p_cash = provider.cash
        
        carry_item(provider, self, carrier_index)
        
        provider.cash -= c_wage
        carrier.cash += c_wage
            
        self.cash -= item.price
        self.items.append(item)
        provider.cash += item.price
        del provider.items[item_index]
        
        post_p_cash = provider.cash
        
        # info about the purchase
        print("Info:\n")
        console.print(f"Item bought: {item.name}", style="purple bold")
        console.print(f"Price: {item.price} (money left: {self.cash})", style="purple bold")
        console.print(f"Distance: {calculate_distance(provider, self)}", style="purple bold")
        console.print(f"Money spent on carrier by provider: {c_wage}", style="purple bold")
        
        style = post_p_cash > pre_p_cash
        message = ""
        
        if (style):
            style = "green bold"
            message = "Provider earned"
        else:
            style = "red bold"
            message = "Provider lost"    
        
        
        
        # green if provider earned money
        # red if didn't
        console.print(f"{message}: {abs(post_p_cash - pre_p_cash)}", style=style)
        
        
        # print(f"post self.cash - {self.cash}")
        # print(f"post provider.cash - {provider.cash}")
        # print(f"post self.items length - {len(self.items)}")
        # print(f"post provider.items length - {len(provider.items)}")


class Provider:
    def __init__(self, name: str, location: str, items: list, carriers, cash: float):
        self.name = name
        self.location = location
        self.items = items
        self.carriers = carriers
        self.cash = cash

    def add_carrier(self, c):
        self.carriers.append(c)
        c.set_occupation(self)
        
    def __repr__(self):
        return self.name
    


class Carrier:
    def __init__(self, name, speed: int, desired_wage: int, cash: float):
        self.name = name
        self.occupation = None
        self.speed = speed
        self.desired_wage = desired_wage
        self.cash = cash
        
    def set_occupation(self, oc):
        self.occupation = oc

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
    
class Item:
    # nodes - ["smth", "food", "fruit"]
    # it goes from top node to bottom node
    def __init__(self, name, nodes, price):
        self.name = name
        self.nodes = nodes
        self.price = price

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

def build_nodes_of_item(item: Item):
    s = "    "
    
    for i in range(0, len(item.nodes)):
        if (i == 0):
            console.print(item.nodes[i] + ":", style="bold green")
            continue
        
        if (len(item.nodes) == 1):
            print(item.nodes[i])
            return
        
        print(f"{s*i}{item.nodes[i]}:")
        if (i == len(item.nodes) - 1):  
            console.print(f"{s*(i+1)}{item.name}", style="bold red")
            return
        

def calculate_distance(p: Provider, w: Warehouse):
    # location example: "Privet Drive"
    # the sum of amount of characters of both locations = distance

    return len(p.location) + len(w.location)

def carry_item(p: Provider, w: Warehouse, c_index: int):
    """This method only handles carrying item,
    The payment to the carrier is in the buy() method.
    Make sure all of the requirements are fulfilled
    """
    distance = calculate_distance(p, w)
    
    console.print(f"{p.location} ", end="", style="red bold")
    for i in range(1, 11):
        # i don't think it's working correctly
        # print(i)
        
        time.sleep((distance / 100) / p.carriers[c_index].speed)
        console.print("-", end="", style="yellow bold")
        if i == 10:
            console.print(f" {w.location}   100%", style="green bold")
    
    print("\n")
    
def calculate_carrier_wage(carrier: Carrier, distance):
    return (distance / carrier.speed) * carrier.desired_wage


def best_carrier(carriers, distance: int):
    if (len(carriers) == 0):
        return Carrier(name="test", speed=1, desired_wage=1, cash=0)
    
    # lowest_number = calculate_carrier_wage(carriers[0], distance)
    c_result = carriers[0]
    
    for carrier in carriers:
        per_meter = carrier.desired_wage / carrier.speed
        current_carrier_wage = calculate_carrier_wage(carrier, distance)
        print(f"{carrier.name} - {per_meter} per 1 meter")
           
        if current_carrier_wage < calculate_carrier_wage(c_result, distance):
            c_result = carrier
        
            
    # print(f"{lowest_number} - lowest money spent on the distance of {distance}")        
    
    return c_result
    
def calculate_percent_off(item: Item, amount):
    percentage = 0
    # for every 20 pieces 10 - (amount / 20)% off
    # example:
    # 67 - 3 (we want the whole number without the fractional part)
    # 10 + (10 - 1) + (10 - 2) = 27
    i = amount / 20
    
    # print(i)
    
    t = 10
    
    for v in range(0, math.floor(i)):
        percentage += t
        t -= 1
        
    # print(percentage)
    return round((percentage * (item.price / 100)), 2)

def calculate_price(item: Item, amount):
    console.print(f"{(amount * item.price) - (amount * (item.price - calculate_percent_off(item, amount)))} saved" , style="bold red")
    return amount * (item.price - calculate_percent_off(item, amount))

def hello():
    return "hello"

def make_abbreviation(s: str) -> str:
    underscores = []
    new_string = s[0]
    
    for i in range(0, len(s)):
        if s[i] == "_":
            underscores.append(i)
    
    # number of letter in an abbreviation is
    # the amount of underscores + 1,
    # but the first letter is the first element of the string
    # that we pass, so this loop adds the rest
    for i in range(0, len(underscores)):
        new_string += s[underscores[i] + 1]
            
    
    return new_string