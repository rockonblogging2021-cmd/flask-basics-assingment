from flask import Flask

app = Flask(__name__)

def is_armstrong(number: int) -> bool:
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(number)]
    power = len(digits)
    total = sum(d ** power for d in digits)
    return total == number

@app.route('/check/<int:num>')
def check_armstrong(num: int):
    if is_armstrong(num):
        return f"{num} is an Armstrong number."
    else:
        return f"{num} is not an Armstrong number."

if __name__ == '__main__':
    app.run(debug=True)
