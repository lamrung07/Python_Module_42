#!/usr/bin/env python3
import sys
import typing


def main() -> None:
    if (len(sys.argv) == 1):
        print(f"Usage: {sys.argv[0]} <file>")
        return
    elif (len(sys.argv) != 2):
        print("Invalid input quantity! Please retry")
        return
    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")
    try:
        f = open(file_name)
    except Exception as e:
        print(f"Error opening file '{file_name}': {e}")
    else:
        print("---\n")
        print(f"{io.read(f)}\n")
        print("---")

if __name__ == "__main__":
    main()