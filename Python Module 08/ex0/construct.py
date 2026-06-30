#!/usr/bin/env python3
import os
import sys
import site


def ft_venv_detect():
    if sys.prefix == sys.base_prefix:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.prefix}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python3 -m venv <venv_name>")
        print("source <venv_name>/bin/activate # To activate on Unix")
        print("deactivate # To deactivate")
        print(f"Global environment package locations: "
              f"{site.getusersitepackages()}")
        print("\nThen run this program again.")
    else:
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")
        print(f"Package installation path:\n {site.getsitepackages()}")


if __name__ == "__main__":
    ft_venv_detect()
