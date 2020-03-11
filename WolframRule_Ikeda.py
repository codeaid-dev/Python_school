import string, math, random


while True:
    userinput0 = input("Desired rule number: ")
    rule = int(userinput0)
    if 0 <= rule <= 255:
        wolfram_rule_string = "{0:{fill}8b}".format(int(rule), fill="0")
        break

    else:
        print("Number is invalid")
        print("Please try again between 0 and 255.")

wolfram_rule_dict = {"111": wolfram_rule_string[0], "110": wolfram_rule_string[1],
                     "101": wolfram_rule_string[2], "100": wolfram_rule_string[3],
                     "011": wolfram_rule_string[4], "010": wolfram_rule_string[5],
                     "001": wolfram_rule_string[6], "000": wolfram_rule_string[7]}

userinput1 = input("Desired size: ")

size = int(userinput1)

while True:
    userinput2 = input("Initial state: ")

    if (userinput2 == "random") or (userinput2 == "Random"):
        a = ["0", "1"]
        r = random.randint(0, 1)
        iterstr = a[r]
        while len(iterstr) < size:
            r = random.randint(0, 1)
            iterstr = iterstr + a[r]
        break

    elif (userinput2 == "non-random") or (userinput2 == "not random") or (userinput2 == "not") or (
            userinput2 == "organized") or (userinput2 == "Organized"):
        iterstr = "0" * math.floor(size / 2) + "1" + "0" * math.floor(size / 2)
        break

    else:
        print("Input not recognized.")
        print("Please try again")

def wolfram_fkt(iterstr):
    x = ""
    for i in range(len(iterstr) - 2):
        x += wolfram_rule_dict[iterstr[i:i + 3]]
    return x

def replace_char(string):
    string = string.replace('0', ' ').replace('1', 'A')
    return string

def printing_rules():
    global iterstr
    print(replace_char(iterstr))
    for _ in range(int(size / 2)):
        line = wolfram_fkt(iterstr)
        line = '0{}0'.format(line)
        print(replace_char(line))
        iterstr = line

printing_rules()
