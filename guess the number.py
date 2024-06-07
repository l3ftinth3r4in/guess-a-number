import random
def guess_the_number():
    number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("Попробуйте отгадать число: "))
        attempts += 1
        if guess < number:
            print("Слишком маленькое")
        elif guess > number:
            print("Слишком большое")
        else:
            print("Поздравляю, Вы отгадали число! Количество попыток:", attempts)
            break
guess_the_number()
