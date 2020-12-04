numbers = open("input.txt", "r").readlines()

# find two numbers
for i in range(len(numbers)):
    num = int(numbers[i])
    for j in range(i, len(numbers)):
        jum = int(numbers[j])
        if num + jum == 2020:
            print('done')
            print(num, jum, num * jum)

# find three numbers
for i in range(len(numbers)):
    num = int(numbers[i])
    for j in range(i, len(numbers)):
        jum = int(numbers[j])
        for k in range(j, len(numbers)):
            kum = int(numbers[k])
            if num + jum + kum == 2020:
                print('done')
                print(num, jum, kum, num * jum * kum)
