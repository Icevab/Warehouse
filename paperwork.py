from main import make_abbreviation

class Report:
    def __init__(self, company, report_txt, data):
        self.company = company
        self.report_txt = report_txt
        self.data = take_data_from_txt(report_txt)
        
        
        
def commands_of_data(data):
    """Creates a dictionary of commands where keys are abbreviations
    and values are the commands"""
    
    commands = {}
    
    for item in data:
        commands[make_abbreviation(item)] = item
       
    return commands

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
    """Takes all the info from a .txt,
    for example: if there's a line "Money made: ",
    than it will take it, make it "money_made",
    and it will assign the assign a value to it according to the .txt"""
    
    data = {}
    
    with open(txt, "r") as file:
        for line in file:
            if len(line.strip()) > 0 and ":" in line:
                
                # print(line.strip()[:line.strip().index(":")])
                # line.strip()[:line.strip().index(":")] -- takes every element before colon (:)
                # in line.strip()
                append_item(data, line.strip()[:line.strip().index(":")], line)       
                
    return data
                
