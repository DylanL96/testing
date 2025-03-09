# easy_add_app/src/test_app.py
from app import add_numbers, main

def test_add_numbers():
    print("Testing if 1 + 1 equals 2...")
    result = add_numbers()
    assert result == 2
    print(f"Math works! Result is {result}")

def test_main_runs():
    print("Checking if the app runs...")
    try:
        main()  # This already prints "1 + 1 = 2"
        assert True
        print("App ran perfectly!")
    except:
        assert False
        print("Oops, app crashed!")