#!/usr/bin/env python3


# Check installation
def show_instruction() -> None:
    print("\nPip vs Poetry installation instructions")
    print("-" * 40)
    print("pip: pip install -r requirements.txt")
    print("  - Uses requirements.txt | pip freeze > "
          "requirements.txt : save existed dependencies")
    print("  - Manual dependency management")
    print("  - Manual virtual environment")

    print("\nPoetry: poetry install")
    print("  - Uses pyproject.toml")
    print("  - Automatic dependency resolution")
    print("  - Automatic virtual environment")


def check_pandas() -> bool:
    try:
        import pandas as pd
        print(f"✅ pandas ({pd.__version__}) - Data manipulation ready")
        return True
    except ImportError:
        print("❌ pandas is NOT installed")
        show_instruction()
        return False


def check_numpy() -> bool:
    try:
        import numpy as np
        print(f"✅ numpy ({np.__version__}) - Numerical computation ready")
        return True
    except ImportError:
        print("❌ numpy is NOT installed")
        show_instruction()
        return False


def check_requests() -> bool:
    try:
        import requests as rq
        print(f"✅ requests ({rq.__version__}) - Network access ready")
        return True
    except ImportError:

        print("❌ request is NOT installed")
        show_instruction()
        return False


def check_matplotlib() -> bool:
    try:
        import matplotlib as plt
        print(f"✅ matplotlib ({plt.__version__}) - Visualization ready")
        return True
    except ImportError:
        print("❌ matplotlib is NOT installed")
        show_instruction()
        return False


if __name__ == "__main__":
    print("📈 DATA ANALYSIS PROGRAM 📈")
    print("- Flow: Requests data using request -> Manipulate using pandas")
    print("        Using numpy to calculate -> "
          "Using matplotlib for visualization")
    print("❗When missing dependencies occur, "
          "program might stop and show installation "
          "instructions for pip and Poetry ❗\n")

    # Requests data to analyze
    check_rq = False
    check_pd = False
    check_np = False
    check_plt = False
    print("Dependencies check:")
    if check_requests():
        check_rq = True
        import requests as rq
        URL = (
            "https://api.open-meteo.com/v1/forecast"
            "?latitude=48.8566"
            "&longitude=2.3522"
            "&hourly=temperature_2m,precipitation,"
            "windspeed_10m,relativehumidity_2m"
            "&forecast_days=7"
            "&timezone=auto"
        )
        response = rq.get(URL)
        data = response.json()

        # Pandas for data manipulation
        if check_pandas():
            check_pd = True
            import pandas as pd
            dataframe = pd.DataFrame(data["hourly"])

            # Numpy for computations and simulated Matrix data
            if check_numpy():
                check_np = True
                import numpy as np
                matrix = dataframe[[
                        "temperature_2m",
                        "precipitation",
                        "windspeed_10m",
                        "relativehumidity_2m"
                    ]].to_numpy()
                simulated_matrix = np.random.normal(
                        np.mean(matrix),
                        np.std(matrix),
                        size=(100, 4)
                    )

                # Matplotlib for visualization
                if check_matplotlib():
                    check_plt = True
                    import matplotlib.pyplot as plt
                    plt.plot(dataframe["temperature_2m"])
                    plt.title("Temperature Forecast")
                    plt.xlabel("Hour")
                    plt.ylabel("Temperature (°C)")
                    plt.savefig("matrix_analysis.png")
    if check_rq:
        print("\nTemperature Forecast data requested successfully")
    if check_pd:
        print("Show Matrix data :")
        print(dataframe.head())
    if check_np:
        print("\nAverage values:")
        print(np.mean(matrix, axis=0))
        print("Simulated matrix shape:", simulated_matrix.shape)
    if check_plt:
        print("\nTemperature Forecast complete!"
              "\nResults saved to: matrix_analysis.png")
