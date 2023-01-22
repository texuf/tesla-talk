import os








def run():
    print("Hello World DEBUG_1:", os.environ.get("DEBUG_1", "Not set"))


if __name__ == "__main__":
    run()