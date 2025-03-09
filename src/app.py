# easy_add_app/src/app.py
def add_numbers(a,b):
    result = a + b
    return result

def main():
    answer = add_numbers(1,2)
    print(f"This is the answer: {answer}")

if __name__ == "__main__":
    main()