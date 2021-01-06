#!usr/bin/env python3
increment = 1
for x in range(0,6,increment):
    print(".")
    if x == 5:
        increment = -1;
