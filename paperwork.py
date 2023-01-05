class Report:
    def __init__(self, report):
        self.report = report


def append_item(d, st_with, txt):
    """Appends item to a given dictionary -- d,
    also takes st_with -- what does the line start with
    and txt -- line.strip()"""
    # print(st_with)
    
    
    item = ""

    for char in st_with[:len(st_with)]:
        if char == " ":
            item += "_"
        elif char.upper() == char:
            item += char.lower()
        else:
            item += char
    
    # txt[len(st_with) + 2:] - take every element from len(st_with) + 2,
    # we add two because the first two elements that we get are ":" and " ",
    # so we "skip" them with + 2
    d[item] = float(txt[len(st_with) + 2:])

def take_data_from_txt(txt):
    data = {}
    
    with open(txt, "r") as file:
        for line in file:
            if len(line.strip()) > 0 and ":" in line:
                
                # print(line.strip()[:line.strip().index(":")])
                # line.strip()[:line.strip().index(":")] -- takes every element before colon (:)
                # in line.strip()
                append_item(data, line.strip()[:line.strip().index(":")], line)
                    
            # if line.startswith("Money made: "):
            #     append_item(data, "Money made: ", line.strip())
            # if line.startswith("Change in money made: "):
            #     append_item(data, "Change in money made: ", line.strip())
            # if line.startswith("Money spent: "):
            #     append_item(data, "Money spent: ", line.strip())
            # if line.startswith("Change in money spent: "):
            #     append_item(data, "Change in money spent: ", line.strip())
            # if line.startswith("Cash: "):
            #     append_item(data, "Cash: ", line.strip())
            # if line.startswith("Change in cash: "):
            #     append_item(data, "Change in cash: ", line.strip())
            
                
    return data

print(take_data_from_txt("report_example.txt"))
                