#!/usr/bin/env python3
import sys
import typing


def write_to_file(file_name: str, new_content: typing.List[str]) -> None:
    try:
        n = open(file_name, 'w')
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{file_name}': {e}\n")
    else:
        i = 1
        for new_line in new_content:
            n.write(new_line + '#')
            if i != len(new_content):
                n.write('\n')
            i += 1
    finally:
        n.close()
        print(f"Saving data to '{file_name}'")
        print(f"Data saved in file '{file_name}'.")


def main() -> None:
    if (len(sys.argv) == 1):
        print(f"Usage: {sys.argv[0]} <file>")
        return
    elif (len(sys.argv) != 2):
        print("Invalid input quantity! Please retry")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")
    try:
        f = open(file_name, 'r')
        content = str(f.read())
        new_content = str(content).split('\n')
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{file_name}': {e}\n")
    else:
        print(f"---\n\n{content}\n\n---")
        print(f"File '{file_name}' closed.\n")
        f.close()
        print("Transform data:\n---\n")
        for new_line in new_content:
            print(f"{new_line}#")
        print("\n---")
        print("Enter new file name (or empty):", end='', flush=True)
        '''remove \n after file name'''
        new_file_name = sys.stdin.readline().rstrip()
        if (new_file_name == ""):
            print("Not saving data.")
            return
        write_to_file(new_file_name, new_content)


if __name__ == "__main__":
    main()