import sys
if len(sys.argv) != 3:
    print("none")
else:
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        values = list(range(start, end + 1)) if start <= end else list(range(start, end - 1, -1))
        print(values)
    except ValueError:
        print("none")