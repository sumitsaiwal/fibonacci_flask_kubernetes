from flask import Flask, request

app = Flask(__name__)

def _fibonacci(n: int):
    """ Calculate Nth Fibonacci number using the doubling method. Return the
    tuple (F(n), F(n+1))."""
    if n == 0:
        return (0, 1)
    a, b = _fibonacci(n >> 1)
    c = a * ((b << 1) - a)
    d = a * a + b * b
    if n & 1:
        return (d, c + d)
    return (c, d)

@app.route("/calculate_fibonacci", methods=['GET'])
def fibonacci():
    try:
        return str(_fibonacci(int(request.args['n']))[0])
    except ValueError:
        return "Please use a number as the 'n' argument"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
    