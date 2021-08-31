height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Is not human height.")

bmi = weight/height ** 2
print(bmi)
