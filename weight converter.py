x = float(input('Weight: '))

y= str(input('(L)lbs or (k)kg: '))

if y.lower()== 'l':
    kg = 0.45 * x
    print(f"You are {kg} KG")

elif y.lower() == 'k':
    lbs = 2.2 * x
    print(f"You are {lbs} pounds")
input()
