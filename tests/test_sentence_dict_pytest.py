import  subprocess

def test_To_check_the_help_message():
    command = ["python", "../sentence_dict_count.py", "--help"]

    result = subprocess.run(command, capture_output=True, text=True)

    assert result.returncode == 0

    assert "usage: sentence_dict_count.py [-h] [--sentence SENTENCE]" in result.stdout
    assert "count the characters in a sentence" in result.stdout.lower()


def test_to_check_possitive_scenario_passing_sentence():
    command = ["python", "../sentence_dict_count.py","--sentence","python is good skill"]

    result=subprocess.run(command, capture_output=True, text=True)

    assert result.returncode == 0

    assert "char p : 1" in result.stdout
    assert "char l : 2" in result.stdout

def test_t0_check_passing_numbers():
    command = ["python", "../sentence_dict_count.py","--sentence","123 123 4567"]

    result = subprocess.run(command, capture_output=True, text=True)

    assert result.returncode == 0

    assert "char 1 : 2" in result.stdout
    assert "char 7 : 1" in result.stdout


def test_to_check_without_passing_sentence():
    command = ["python", "../sentence_dict_count.py","--sentence"]
    result = subprocess.run(command, capture_output=True, text=True)

    assert result.returncode == 2

    assert "usage: sentence_dict_count.py [-h] [--sentence SENTENCE]" in result.stderr
    assert "error: argument --sentence: expected one argument" in result.stderr

