import main


# commands = func that:
# is a function (callable), but we only want items that don't start with "__"
# and not func.startswith("__") does exactly that
# but callable will also be True when we pass a class,
# all of the classes' names start with a capital letter
# so to prevent adding classes I check if the first letter isn't capital with
# and not func[0].capitalize() == func[0]
# so that if the first letter of func's name is the same as if it was capital
# then it's a class and we don't need it in commands
func_names = [func for func in dir(main) if callable(getattr(main, func)) and not func.startswith("__") and not func[0].capitalize() == func[0]]      
# print(func_names)

def s():
    print("s")

commands = {"s": s}

# for func in func_names:
#     commands[func] = func

print(commands)

def sum(x, y):
    return x + y

def select_function():
    pass

def app():
    while True:
        x = int(input())
        y = int(input())
        print("\n")
        print(sum(x, y))
        print("\n")
        
# app()