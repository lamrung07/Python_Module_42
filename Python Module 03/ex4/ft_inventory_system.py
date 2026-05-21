#!/usr/bin/env python3
import sys


def handle_input(inv_sys: str) -> list:
    inv = inv_sys.split(":")
    if (len(inv) != 2):
        raise SyntaxError(f"Error - invalid parameter '{inv_sys}'")
    try:
        a = inv[0]
        b = int(inv[1])
    except SyntaxError:
        return (
            f"Quantity error for '{inv[0]}': "
            f"invalid literal for int() with base 10: '{inv[1]}'"
        )
    else:
        return [a, b]


def find_most_least(inv_sys) -> None:
    keys = list(inv_sys.keys())
    values = list(inv_sys.values())

    most_idx = 0
    least_idx = 0
    for i in range(1, len(keys)):
        if values[i] > values[most_idx]:
            most_idx = i
        if values[i] < values[least_idx]:
            least_idx = i

    return keys[most_idx], values[most_idx], keys[least_idx], values[least_idx]


def main() -> None:
    inv_sys = {}
    for i in range(1, len(sys.argv)):
        try:
            pair = handle_input(sys.argv[i])
            if pair[0] in inv_sys:
                print(f"Redundant item '{pair[0]}' - discarding")
            else:
                inv_sys.update({pair[0]: pair[1]})
        except SyntaxError as e:
            print(f"{e}")
    print(f"Got inventory: {inv_sys}")
    print(f"Item list: {list(inv_sys.keys())}")
    total = sum(list(inv_sys.values()))
    print(f"Total quantity of the {len(inv_sys)} items: {total}")

    for a in inv_sys:
        per = round(inv_sys[a]/total * 100, 1)
        print(f"Item {a} represents {per}%")

    most_key, most_val, least_key, least_val = find_most_least(inv_sys)
    print(f"Item most abundant: {most_key} with quantity {most_val}")
    print(f"Item least abundant: {least_key} with quantity {least_val}")

    inv_sys.update({"magic_item": 1})
    print(f"Updated inventory: {inv_sys}")


if __name__ == "__main__":
    main()
