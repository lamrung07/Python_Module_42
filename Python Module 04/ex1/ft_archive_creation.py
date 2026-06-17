#!/usr/bin/env python3
import sys


def main() -> None:
    """
    This program read all the file content
    and then display a new content (end with "#" at the endline)
    Ask user a file name to save in, and display ending message
    """

    # Check arguments quantity (2 required)
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

    # Access the file, while handle all possible errors
    try:
        f = open(file_name, 'r')
        content = str(f.read())
        new = str(content).split('\n')
    except OSError as e:
        print(f"Error opening file '{file_name}': {e}")
    else:
        print(f"---\n\n{content}\n\n---")
        print(f"File '{file_name}' closed.\n")
        f.close()
        print("Transform data:\n---\n")

        # Display new content, endline with "#"
        for new_line in new:
            print(f"{new_line}#")
        print("\n---")

        # Ask for newfile name, if empty: return
        new_file_name = input("Enter new file name (or empty):")
        if (new_file_name == ""):
            print("Not saving data.")
            return

        # Open newfile and write new content inside
        try:
            n = open(new_file_name, 'w')
        except OSError as e:
            print(f"Error opening file '{new_file_name}': {e}")
        else:
            i = 1
            for new_line in new:
                n.write(new_line + '#')
                if i != len(new):
                    n.write('\n')
                i += 1
        finally:
            n.close()
            print(f"Saving data to '{new_file_name}'")
            print(f"Data saved in file '{new_file_name}'.")


if __name__ == "__main__":
    main()
