#!/usr/bin/env python3
import math


def check_input(n) -> float:
    try:
        n = float(n)
    except:
        raise ValueError (f"Error on parameter '{n}':  could not convert string to float: '{n}'")
    else:
        return round(n, 1)


def get_player_pos() -> tuple:
    while True:
        pos = input("Enter new coordinates as floats in format 'x,y,z': ").split(',')
        if len(pos) != 3:
            print("Invalid syntax")
            continue
        try:
            pos[0] = check_input(pos[0])
            pos[1] = check_input(pos[1])
            pos[2] = check_input(pos[2])
        except ValueError as e:
            print(f"{e}")
        else:
            return (pos[0], pos[1], pos[2])


def cal_distance(pos1: tuple, pos2: tuple) -> float:
    x1, y1, z1 = pos1[0], pos1[1], pos1[2]
    x2, y2, z2 = pos2[0], pos2[1], pos2[2]
    res = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return round(res, 4)


def main() -> None:
    print("=== Game Coordinate System ===")
    
    print("\nGet a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    print(f"Distance to center: {cal_distance(pos1, (0,0,0))}")
    
    print("\nGet a second set of coordinates")
    pos2 = get_player_pos()
    print(f"Distance between the 2 sets of coordinates: {cal_distance(pos1, pos2)}")


if __name__ == "__main__":
    main()
