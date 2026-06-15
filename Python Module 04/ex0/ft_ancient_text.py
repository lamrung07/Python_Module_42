#!/usr/bin/env python3
import sys


def main() -> None:

    # Require 2 arguments
    if (len(sys.argv) == 1):
        print(f"Usage: {sys.argv[0]} <file>")
        return
    elif (len(sys.argv) != 2):
        print("Invalid input quantity! Please retry")
        return

    # Print program's header 
    print("=== Cyber Archives Recovery ===")
    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")

    # Handle I/O Exceptions
    try:
        f = open(file_name, 'r')
    except OSError as e:
        print(f"Error opening file '{file_name}': {e}")
    else:
        print("---\n")
        print(f"{f.read()}\n")
        print("---")
        f.close()
        print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    main()
