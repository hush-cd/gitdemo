#script name     : calculator.py
#author          :Chen Ding
#created         :2020/03/04
#lasted modified :2020/03/04
#version         :1.0
#discription     :do some simple calculation
def change(num, weight):
if weight == 10:
    print(int(num))
    return
new_num_ls = []
while num > weight:
    tmp = num % weight
    num = num // weight
    if tmp >= 10:
        new_num_ls.append(_alph[tmp])
    else:
        new_num_ls.append(tmp)
if num >= 10:
    new_num_ls.append(_alph[num])
else:
    new_num_ls.append(num)
length = len(new_num_ls)
for i in range(length):
    print(new_num_ls[length-i-1], end = "")
print()

alph = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16,
        'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23,
        'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30,
        'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}

_alph = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G',
         17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N',
         24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U',
         31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'}

num_order = int(input())
cur_answer = 0
operation = "" #0:null, 1:+，2:-, 3:*, 4:/, 5:%
weight = 10
for i in range(num_order):
order = input()
#print(order)
if order == "ADD":
    operation = "+"
elif order == "SUB":
    operation = "-"
elif order == "MUL":
    operation = "*"
elif order == "DIV":
    operation = "//"
elif order == "MOD":
    operation = "%"
elif order == "EQUAL":
    change(cur_answer, weight)
elif order == "CLEAR":
    cur_answer = 0
    operation = ""
else:
    order, num = order.split()
    if order == "CHANGE":
        weight = int(num)
    elif order == "NUM":
        if operation != "":
            cur_answer = eval(str(cur_answer)+operation+str(return_10(num, weight)))
        else:
            cur_answer = return_10(num, weight)

