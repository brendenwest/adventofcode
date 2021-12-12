import copy
inputs = open("input.txt", "r").read().split(",")

# part 1
# 1st integer is opcode - either 1, 2, or 99

def solve(inputs, noun, verb):
    inputs[1] = noun
    inputs[2] = verb

    for i in range(0,len(inputs),4):
        if len(inputs) - i < 4:
            break

        opcode = int(inputs[i])
        first = int(inputs[i+1])
        second = int(inputs[i+2])
        third = int(inputs[i+3])

        if opcode == 1:
            inputs[third] = int(inputs[first]) + int(inputs[second])
        elif opcode == 2:
            inputs[third] = int(inputs[first]) * int(inputs[second])
    return inputs[0]

#for noun in range(20,25,1):
noun = 22
for verb in range(50,70,1):
    result = solve(copy.copy(inputs), noun, verb)
    print(noun, verb, result)
    if result == 19690720:
        break
print(100*noun + verb)
