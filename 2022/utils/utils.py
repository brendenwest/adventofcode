def input(data=None):
    if data:
        return data
    return open("input.txt", "r").readlines()
