#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = sys.argv
    sum = 0
    for x in a:
        if x != a[0]:
            sum += int(x)
    print(sum)
