import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    date = words[3].strip("[")
    log = date.split(":",1)
    print(log[0],log[1],"\t", 1)

