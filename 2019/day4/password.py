
# 183564-657474
# part 1

def isValid1(password):
    hasDouble = False
    prev = ""
    for c in str(password):
        if len(prev) > 0 and int(c) < int(prev):
            return False
        if c == prev:
            hasDouble = True
        prev = c
    return hasDouble

assert isValid1(111111) == True
assert isValid1(223450) == False
assert isValid1(123789) == False

def isValid2(password):
    hasDouble = False
    str_password = str(password)
    count = 1
    for i, c in enumerate(str_password):
        if i > 0 and int(c) < int(str_password[i-1]):
            return False

        if i > 0:
            if c == str_password[i-1]:
                count += 1
            if i > 1 and c == str_password[i-2]:
                count += 1
            if c != str_password[i-1] or i == len(str_password)-1:
                if count == 2:
                    hasDouble = True
                count = 1


    return hasDouble

assert isValid2(112233) == True
assert isValid2(123444) == False
assert isValid2(111122) == True
assert isValid2(112223) == True

valid = 0
for password in range(183564,657475):
    if isValid2(password):
        valid += 1
print("valid",valid)
