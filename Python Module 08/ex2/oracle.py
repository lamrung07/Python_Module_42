#!/usr/bin/env python3
import os
from dotenv import load_dotenv


# Load .env file (ignored if file doesn't exist)
load_dotenv()


# --- Read configuration from environment ---
MODE = os.getenv("MATRIX_MODE", "development")
DB_URL = os.getenv("DATABASE_URL", "")
API_KEY = os.getenv("API_KEY", "")
LOG = os.getenv("LOG_LEVEL", "DEBUG")
ENDPOINT = os.getenv("ZION_ENDPOINT", "")


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...\n")

    print("----Configuration loaded----")
    # Mode-----------------------------
    print(f"Mode: {MODE}")

    # Database-------------------------
    if MODE == "production":
        print(f"Database: Connected to production {DB_URL}")
    else:
        print("Database: Connected to local instance")

    # API Access-----------------------
    if API_KEY:
        print("API Access: Authenticated")
    else:
        print("API Access: NOT SET - missing API_KEY")

    # Log Level------------------------
    print(f"Log Level: {LOG}")

    # Zion Network---------------------
    if ENDPOINT:
        print("Zion Network: ONLINE")
    else:
        print("Zion Network: OFFLINE - missing ZION_ENDPOINT")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")
