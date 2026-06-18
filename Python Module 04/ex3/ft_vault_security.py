#!/usr/bin/env python3

def secure_archive(
        file_name: str,
        action: int,
        content="") -> tuple[bool, str]:
    """
    Handling file use 'with' statement
    Take in file_name, action return bool value with message
    """
    try:

        # Read content from a file
        if action == 1:
            return_val = ""
            with open(file_name, "r") as file:
                for line in file:
                    return_val += line.rstrip() + "\\n"
            print("Using 'secure_archive' to read from a regular file:")
            return (True, return_val)

        # Write content to a file
        elif action == 2:

            # "a" mode : write to the end
            # "w" mode: replace all existing content
            with open(file_name, "w") as file:
                file.write('\n' + content)
            print("Using 'secure_archive' to write previous"
                  "content to a new file:")
            return (True, content)
        else:
            return (False, "ERROR! Invalid action, please try again")

    # Catch all the I/O Exceptions
    except FileNotFoundError as e:
        print("Using 'secure_archive' to read from a nonexistent file:")
        return (False, f"{e}")
    except PermissionError as e:
        print("Using 'secure_archive' to read from an inaccessible file:")
        return (False, f"{e}")
    except IsADirectoryError as e:
        print("Using 'secure_archive' to read from a directory:")
        return (False, f"{e}")


if __name__ == "__main__":
    file_name = "domix.txt"
    action = 1
    content = "helloworld"
    (acc, content) = secure_archive(file_name, 1, content)
    print(f"({acc}, '{content}')")
    (acc, content) = secure_archive(
        file_name, 2, content="Content successfully written to file")
    print(f"({acc}, '{content}')")
    (acc, content) = secure_archive("domix.txt", 1, content)
    print(f"({acc}, '{content}')")
    (acc, content) = secure_archive("domixi.txt", 1, content)
    print(f"({acc}, '{content}')")
