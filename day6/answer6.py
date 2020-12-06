text = open("input.txt", "r").read()
groups = text.split("\n\n")

# How many questions did anyone answer 'yes'?
total = 0
for group in groups:
    s = set(group.replace("\n",""))
    total += len(s)

print("Total any 'Yes'", total)

# How many questions did everyone in group answer 'yes'?
total = 0
for i, group in enumerate(groups):
    people = group.split('\n')
    common = set(people[0])
    for person in people:
        answers = set(person)
        common = common & answers

    total += len(common)


print("Total everyone 'Yes'", total)
