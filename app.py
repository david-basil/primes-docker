from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, ' + get_complicated_string()

def get_complicated_string():
    answer = ''
    for i in range(90):
        if is_prime(i):
            answer += str(i)
    return answer + '!'

def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    # Check for divisibility from 2 to the square root of the number
    for j in range(2, int(number**0.5) + 1):
        if number % j == 0:
            return False  # Number is divisible by i, so it's not prime

    return True
