import main
import tests
import inspect
from rich.console import Console

console = Console()

def s():
    print("s")

all_functions = dict(inspect.getmembers(main, inspect.isfunction))


def sum(x, y):
    return x + y

def select_function():
    pass

def print_all_properties(object):
    l = []
    
    match object.lower():
        case "warehouse":
            l = tests.all_warehouses
        case "provider":
            l = tests.all_providers
        case "carrier":
            l = tests.all_carriers
        case "item":
            l = tests.all_items
            
            
    
    for property in l:
        for item in property.__dir__():
            # we want to make sure that the item (object property)
            # doesn't start with "__" and also it does not have
            # attribute "__self__", which is an attribute bound methods have
            if not item.startswith("__") and not hasattr(property.__getattribute__(item), "__self__"):
                # print(type(item))
                # print(hasattr(warehouse.__getattribute__(item), "__self__"))
                console.print(f"{item} -- {(property.__getattribute__(item))}", style="purple")
                
        print("\n")
        
    print("\n")         

def app():
    i = 0
    while i < 1:
        # command = input()
        console.print("Hello, and welcome to the Warehouse,", style="bold red")
        console.print("Available warehouses: ", style="bold red")
        print_all_properties("warehouse")
        console.print("Available providers: ", style="bold green")
        print_all_properties("provider")
        console.print("Available carriers: ", style="bold yellow")
        print_all_properties("carrier")
        console.print("Available items: ", style="bold green")
        print_all_properties("item")
        
        
        i += 1
        
        print("\n")
        
app()