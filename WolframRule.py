import string
import math
import random

# Rule90 = {"111":"0", "110":"1", "101":"0", "100":"1", "011":"1", "010":"0", "001":"1", "000":"0"}

# input the number of Wolfram rule
num = input('Please input a number of Wolfram Rule: ')
rule = 30
if num.isdigit():
    rule = int(num)

# 8-bit binary integer number (here 90) as a string
wolfram_rule_string = "{0:{fill}8b}".format(int(rule), fill="0")

# apply the 8-bit binary number to create the Wolfram rule
wolfram_rule_dict = {"111":wolfram_rule_string[0], "110":wolfram_rule_string[1],
"101":wolfram_rule_string[2], "100":wolfram_rule_string[3],
"011":wolfram_rule_string[4], "010":wolfram_rule_string[5],
"001":wolfram_rule_string[6], "000":wolfram_rule_string[7]}

def wolfram_fkt():
    x = ""
    for i in range(len(iterstr)-2):
        x += wolfram_rule_dict[iterstr[i:i+3]]
    return "0" + x + "0"

# input the number of iteration size
num = input('Please input a number of iteration size: ')
size = 4
if num.isdigit():
    size = int(num)

cnt = math.floor(size/2)
# input initial condition random or non-random
rand = input("Do you want initial condition random?('Y'or'N'): ")
if rand == 'Y':
    l = ["0","1"]
    while True:
        inilist = random.choices(l, k=cnt*2+1)
        if "1" in inilist:
            break
    # seed with random "1" on a background of "0"
    iterstr = "".join(inilist)
else:
    # seed with center "1" on a background of "0"
    iterstr = "0"*cnt + "1" + "0"*cnt

# To align the length of seed string
initcnt = 5+2*(size-1) - len(iterstr)
iterstr = "0"*math.floor(initcnt/2) + iterstr + "0"*math.floor(initcnt/2)

for i in range(size):
    print(iterstr)
    #iterstr = "0"*5+2*(size-1) + wolfram_fkt() + "0"*5+2*(size-1)
    iterstr = wolfram_fkt()
