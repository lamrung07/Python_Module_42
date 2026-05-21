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
    print("=== Cyber Archives Recovery ===")
    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")
    try:
        f = open(file_name, 'r')
        content = str(f.read())
        new = str(content).split('\n')
    except Exception as e:
        print(f"Error opening file '{file_name}': {e}")
    else:
        print(f"---\n\n{content}\n\n---")
        print(f"File '{file_name}' closed.\n")
        f.close()
        print("Transform data:\n---\n")
        for new_line in new:
            print(f"{new_line}#")
        print("\n---")
        new_file_name = input("Enter new file name (or empty):")
        if (new_file_name == ""):
            print("Not saving data.")
            return
        n = open(new_file_name, 'w')
        i = 1
        for new_line in new:
            n.write(new_line + '#')
            if i != len(new):
                n.write('\n')
            i += 1
        n.close()


if __name__ == "__main__":
    main()
    