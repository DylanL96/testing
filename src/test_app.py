# easy_add_app/src/test_app.py
from app import add_numbers, main

def test_add_numbers():
    assert add_numbers() == 2  # Checks if 1 + 1 = 2

def test_main_runs():
    try:
        main()  # Runs the app
        assert True  # If it runs, we’re good
    except:
        assert False  # If it crashes, fail