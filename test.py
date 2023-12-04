import random

def generate_random_number():
    numbers = [5]
    return random.choice(numbers)

if __name__ == "__main__":
    random_selected_number = generate_random_number()
    print("Randomly Selected Number:", random_selected_number)
