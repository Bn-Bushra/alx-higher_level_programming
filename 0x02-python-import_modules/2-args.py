#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv[:-1])
    if count == 1:
        print(f"{1} argument:")
    elif count == 0:
        print(f"0 argument.")
    else:
        print(f"{count} arguments:")
    for i in range(count):
        print(f"{i+1}: {sys.argv[i+1]}")