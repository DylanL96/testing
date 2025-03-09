# easy_add_app/src/test_app.py
from app import add_numbers, main

def test_add_numbers():
    print("Testing if 1 + 2 equals 3...")
    result = add_numbers(1, 2)
    assert result == 3
    print(f"Math works! Result is {result}")

def test_main_runs():
    print("Checking if the app runs...")
    try:
        main()  # Prints "1 + 2 = 3"
        assert True
        print("App ran perfectly!")
    except:
        assert False
        print("Oops, app crashed!")