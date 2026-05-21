#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    if not temp_str:
        raise TypeError("Empty Input")
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
            raise TypeError(f"Caught input_temperature error:"
                            f" invalid literal for int() with base 10: "
                            f"'{temp_str}'\n")
        res *= 10
        res += int(temp_str[i])
    res = res * sign
    if res > 40:
        raise ValueError(f"Caught input_temperature error: "
                         f"{temp_str}°C is too hot for plants (max 40°C)\n")
    elif res < 0:
        raise ValueError(f"Caught input_temperature error: "
                         f"{temp_str}°C is too cold for plants (min 0°C)\n")
    return (res)


def test_temperature(temp_str: str) -> str:
    print(f"Input data is '{temp_str}'")
    try:
        tmp = input_temperature(temp_str)
    except (TypeError, ValueError) as e:
        print(e)
    else:
        print(f"Temperature is now {tmp}°C\n")
    finally:
        return ("Tests completed")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    x = test_temperature("25")
    x = test_temperature("abc")
    x = test_temperature("100")
    x = test_temperature("-50")
    if x == "Tests completed":
        print("All tests completed - program didn't crash!")
