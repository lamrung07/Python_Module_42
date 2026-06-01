#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    try:
        res = int(temp_str)
    except ValueError:
        raise
    else:
        return res


def test_temperature(temp_str=['25', 'abc']) -> None:
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
