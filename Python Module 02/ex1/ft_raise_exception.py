#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    try:
        res = int(temp_str)
    except ValueError:
        raise
    if res > 40:
        raise ValueError(f"Caught input_temperature error: "
                         f"{temp_str}°C is too hot for plants (max 40°C)")
    elif res < 0:
        raise ValueError(f"Caught input_temperature error: "
                         f"{temp_str}°C is too cold for plants (min 0°C)")
    return (res)


def test_temperature(temp_str=['25', 'abc', '100', '-50']):
    print("=== Garden Temperature Checker ===\n")
    try:
        for temp in temp_str:
            print(f"Input data is '{temp}'")
            try:
                tmp = input_temperature(temp)
            except ValueError as e:
                print(f"{e}\n")
            else:
                print(f"Temperature is now {tmp}°C\n")
    finally:
        print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
