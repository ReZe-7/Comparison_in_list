"""x = [1,2,3,4,5,6,7,8,9,14,43,35,65,73,1,3]
player = int(input("Enter a number : "))
y = []
for number in x :
    if number < player :
        y.append(number)
print(y)
"""
x = []
z = []
li = int(input("Enter number of elements:"))


for player_list in range(li):
    y = int(input(f"Enter Elements:"))
    x.append(y)
player_choice = int(input("Enter number:"))
op = input("Choose operation <,> :")
if op == "<":

    for pl_ch in x:
        if pl_ch < player_choice:
            z.append(pl_ch)
    print(f"your list : {x}")
    print(f"sorted list smaller than {player_choice} : {z}")
elif op == ">":
    for pl_ch in x:
        if pl_ch > player_choice:
            z.append(pl_ch)
    print(f"your list : {x}")
    print(f"sorted list greater than {player_choice} : {z}")
else:
    print("Error You Entered wrong operant")