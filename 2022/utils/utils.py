def input(data=None):
    if data and type(data) is list:
        return data
    elif data:
        file = data + ".txt"
    else:
        file = "input.txt"
    return open(file, "r").readlines()
