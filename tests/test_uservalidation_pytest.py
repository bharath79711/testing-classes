# runner.py
import subprocess

# command = ["python", "../uservalidation.py","--username", "bathirum","--password", "ramu", "--age", "20"]

def test_to_check_the_help_message():
    command = ["python", "../uservalidation.py","--help"]


    result = subprocess.run(command, capture_output=True, text=True)
    assert result.returncode == 0
    assert "usage: uservalidation.py [-h] [-u USERNAME] [-p PASSWORD] [-a AGE]" in result.stdout
    assert  "User validation" in result.stdout

def test_to_check_the_h_message():
    command = ["python", "../uservalidation.py","--h"]

    result = subprocess.run(command, capture_output=True, text=True)
    assert result.returncode == 0
    assert "usage: uservalidation.py [-h] [-u USERNAME] [-p PASSWORD] [-a AGE]" in result.stdout
    assert  "User validation" in result.stdout

def test_negitive_passing_few_arguments():
    command = ["python", "../uservalidation.py","--username"]
    result = subprocess.run(command, capture_output=True, text=True)
    assert     "usage: uservalidation.py [-h] [-u USERNAME] [-p PASSWORD] [-a AGE]" in result.stderr
    assert    "uservalidation.py: error: argument -u/--username: expected one argument" in result.stderr

def test_passing_all_arguments():
    command = ["python", "../uservalidation.py","--username","anu","--password","btr","--age","20"]
    result = subprocess.run(command, capture_output=True, text=True)
    assert result.returncode == 0
    assert "logged to the server" in result.stdout
    assert "anu is usernam" in result.stdout
    assert "btr is usernam" not in result.stdout
    assert "btr is password" in result.stdout
    assert "20 is age" in result.stdout
    assert "('anu', 'btr', 40)" in result.stdout

def test_passing_invalid_arguments():
    command = ["python", "../uservalidation.py", "--username", "anu", "--password", "btr", "--age", "bharath"]
    result = subprocess.run(command, capture_output=True, text=True)
    assert result.returncode == 1
    assert "ValueError" in result.stderr

def test_passing_less_age():
    command = ["python", "../uservalidation.py", "--username", "anu", "--password", "btr", "--age", "17"]
    result = subprocess.run(command,capture_output=True, text=True)
    assert result.returncode == 0
    assert "check the age above 18" in result.stdout

