numbers = open("input.txt", "r").readlines()
#print(numbers)

#numbers = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def answer1(numbers):
    prev = None
    count = 0
    for number in numbers:
        number = int(number)
        if prev and number > prev:
            count += 1
        prev = number
    return count

def answer2(numbers):
    sums = [0]*len(numbers)
    counts = 0
    for n in range(len(numbers)):
        num = int(numbers[n])
        sums[n] += num
        if n > 0:
            sums[n-1] += num
        if n > 1:
            sums[n-2] += num
        if n > 2:
            if sums[n-2] > sums[n-3]:
                counts += 1

        if n > len(numbers) - 2:
            break

    return counts

#print("Answer 1", answer1(numbers))
print("Answer 2", answer2(numbers))
#answer2(numbers)