import sys
sys.path.append('../utils')
from utils import input

lines = [
"bvwbjplbgvbhsrlpgdmjqwftvncz",     # 5, 23
"nppdvjthqldpwncqszvftbrmjlhg",     # 6, 23
"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", # 10, 29
"zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", # 11, 26
"mjqjpqmgbljsphdztnvjfqwrcgsmlb"    # 19
]

chars = 14
for line in input():
    for i in range(len(line)):
        slice = line[i:i+chars]
        if len(set(slice)) == chars:
            print("done", i+chars)
            break