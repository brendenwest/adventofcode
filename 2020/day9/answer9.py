lines = [int(n.strip('\n')) for n in open("input.txt", "r").readlines()]
#lines = [int(n.strip('\n')) for n in open("sample.txt", "r").readlines()]

def check_preamble(num, group):
    for n in group:
        remainder = num - n
        if remainder != n and remainder in group:
            return True

#check(40, [35, 20, 15, 25, 47])

def find_invalid(preamble):
    for i, line in enumerate(lines):
        if i > preamble-1:
            # check pairs
            if not check_preamble(line,lines[i-preamble:i]):
                return line

invalid = find_invalid(25)
print('Bad #', invalid)

# find range of numbers that sum to input
def find_range(input):
    numbers = []
    for i, n in enumerate(lines):
        if n >= input:
            continue

        numbers.append(n)
        val = sum(numbers)
        while val > input:
            val -= numbers[0]
            numbers.pop(0)
        if val == input:
            return numbers

numbers = find_range(invalid)
print('Check', sum(numbers))
print('max', max(numbers), 'min', min(numbers))
weakness = min(numbers) + max(numbers)
print('Weakness', weakness)
