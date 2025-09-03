import  subprocess

def test_to_check_the_help_message():
    command = ["python", "../calculator.py", "--help"]

    result = subprocess.run(command, capture_output=True, text=True)
    assert result.returncode == 0
    assert "usage: calculator.py [-h] [--operation {add,subtract,multiply,divide}]" in result.stdout
    assert "Simple command-line calculator" in result.stdout
    assert "num1                  First number" in result.stdout
    assert "num2                  Second number" in result.stdout
    assert "  -h, --help            show this help message and exit" in result.stdout
    assert " --operation {add,subtract,multiply,divide}" in result.stdout

def test_to_check_the_h_command():
    command = ["python", "../calculator.py", "--h"]

    result = subprocess.run(command, capture_output=True, text=True)
    assert result.returncode == 0
    assert "usage: calculator.py [-h] [--operation {add,subtract,multiply,divide}]" in result.stdout
    assert "Simple command-line calculator" in result.stdout
    assert "num1                  First number" in result.stdout
    assert "num2                  Second number" in result.stdout
    assert "  -h, --help            show this help message and exit" in result.stdout
    assert "Operation to perform (default: add)" in result.stdout

def test_To_check_addition_passing_possitive_numbers():
    command = ["python", "../calculator.py", "--operation", "add", "25", "25"]

    result = subprocess.run(command, capture_output=True, text=True)

    assert result.returncode == 0

    assert "Result: 50.0" in result.stdout


def test_To_check_addition_passing_negative_numbers():
    command = ["python", "../calculator.py", "--operation", "add", "-10", "-12"]

    result = subprocess.run(command, capture_output=True, text=True)

    assert result.returncode == 0

    assert "Result: -22.0" in result.stdout


def test_To_check_subtraction_passing_possitive_numbers():
    command = ["python", "../calculator.py", "--operation", "subtract", "25", "25"]
    result = subprocess.run(command, capture_output=True, text=True)

    assert result.returncode == 0

    assert "Result: 0.0" in result.stdout


def test_To_check_subtraction_passing_negative_numbers():
    command = ["python", "../calculator.py", "--operation", "subtract", "-24", "-12"]

    result = subprocess.run(command, capture_output=True, text=True)
    assert result.returncode == 0

    assert "Result: -12.0" in result.stdout


def test_to_check_multiplication_passing_possitive_numbers():
    command = ["python", "../calculator.py", "--operation", "multiply", "10", "5"]

    result = subprocess.run(command, capture_output=True, text=True)
    assert result.returncode == 0

    assert "Result: 50.0" in result.stdout


def test_To_check_multiplication_passing_negative_numbers():
    command = ["python", "../calculator.py", "--operation", "multiply", "-11", "5"]

    result = subprocess.run(command, capture_output=True, text=True)

    assert result.returncode == 0

    assert "Result: -55.0" in result.stdout


def test_To_check_division_passing_possitive_numbers():
    command = ["python", "../calculator.py", "--operation", "divide", "10", "5"]
    result = subprocess.run(command, capture_output=True, text=True)

    assert result.returncode == 0

    assert "Result: 2.0" in result.stdout


def test_To_check_division_passing_negative_numbers():
    command = ["python", "../calculator.py", "--operation", "divide", "-10", "-2"]

    result = subprocess.run(command, capture_output=True, text=True)

    assert result.returncode == 0


    assert "Result: 5.0" in result.stdout


def test_To_check_division_passing_passing_Zero():
    command = ["python", "../calculator.py", "--operation", "divide", "10", "0"]

    result = subprocess.run(command, capture_output=True, text=True)

    assert result.returncode == 0

    assert "Error: Division by zero" in result.stdout


def test_to_check_withot_passing_arguments():
    command = ["python", "../calculator.py", "--operation", "add"]

    result = subprocess.run(command, capture_output=True, text=True)
    assert result.returncode == 2

    assert " error: the following arguments are required: num1, num2" in result.stderr






