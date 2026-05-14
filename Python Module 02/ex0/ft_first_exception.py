#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    if not temp_str:
        raise TypeError
    res = 0
    sign = 1
    s = 0
    if temp_str[s] == '-':
        sign = -1
        s = 1
    elif temp_str[s] == '+':
        sign = 1
        s = 1
    for i in range(s, len(temp_str)):
        if temp_str[i] < '0' or temp_str[i] > '9':
            raise TypeError
        res *= 10
        res += int(temp_str[i])
    return (res * sign)


def test_temperature(temp_str: str) -> str:
    print(f"Input data is '{temp_str}'")
    try:
        tmp = input_temperature(temp_str)
    except TypeError:
        print(
            f"Caught input_temperature error:"
            f"invalid literal for int() with base 10: '{temp_str}'\n"
        )
    else:
        print(f"Temperature is now {tmp}°C\n")
    finally:
        return ("Tests completed")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    x = test_temperature("25")
    x = test_temperature("abc")
    if x == "Tests completed":
        print("All tests completed - program didn't crash!")
