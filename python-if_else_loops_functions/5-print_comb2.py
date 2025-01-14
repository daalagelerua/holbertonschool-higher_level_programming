#!/usr/bin/python3
# version compact: print(", ".join(f"{i:02}" for i in range(100)))
for i in range(100):
    if i < 99:
        print(f"{i:02}", end=", ")
    else:
        print(i)
