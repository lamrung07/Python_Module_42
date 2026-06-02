#!/usr/bin/env python3
import os
import sys
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()

    SECRET_KEY = os.getenv('SECRET_KEY')
    DATABASE_URL = os.getenv('DATABASE_URL')

    print(f'SECRET_KEY: {SECRET_KEY}')
    print(f'DATABASE_URL: {DATABASE_URL}')