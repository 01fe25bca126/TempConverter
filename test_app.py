import subprocess

def test_celsius_to_fahrenheit():
    result = subprocess.run(["python", "app.py"], input="1\n100\n", capture_output=True, text=True)
    assert "212" in result.stdout

def test_fahrenheit_to_celsius():
    result = subprocess.run(["python", "app.py"], input="2\n212\n", capture_output=True, text=True)
    assert "100" in result.stdout

def test_celsius_to_kelvin():
    result = subprocess.run(["python", "app.py"], input="3\n100\n", capture_output=True, text=True)
    assert "373" in result.stdout