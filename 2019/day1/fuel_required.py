
def fuel_required(mass):
    if mass >= 6:
        return mass//3-2
    return 0

def total_fuel(mass):
    fuel = fuel_required(mass)
    if fuel == 0:
        return fuel
    else:
        return fuel + total_fuel(fuel)

assert fuel_required(12) == 2
assert fuel_required(14) == 2
assert fuel_required(1969) == 654
assert fuel_required(100756) == 33583
assert fuel_required(5) == 0

assert total_fuel(1969) == 966
assert total_fuel(100756) == 50346

inputs = open("input.txt", "r").readlines()

total1 = 0
for mass in inputs:
    total1 += fuel_required(int(mass))

print("fuel required",total1)

total2 = 0
for mass in inputs:
    total2 += total_fuel(int(mass))

print("total fuel",total2)
