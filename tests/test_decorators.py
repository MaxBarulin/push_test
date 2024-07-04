import pytest
from src.decorators import my_function, my_function_file


def test_log_ok(capsys):
    my_function(10, 20)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_error(capsys):
    my_function()
    captured = capsys.readouterr()
    assert (
        captured.out
        == "my_function error: my_function() missing 2 required positional arguments: 'x' and 'y'. Inputs: (), {}\n"
    )


def test_log_ok_file():
    my_function_file(10, 20)
    with open("mylog.txt", "r") as file:
        lines = file.readlines()
        assert lines[-1] == "my_function_file ok\n"


def test_log_error_file():
    my_function_file()
    with open("mylog.txt", "r") as file:
        lines = file.readlines()
        assert (
            lines[-1]
            == "my_function_file error: my_function_file() missing 2 required positional arguments: 'x' and 'y'. Inputs: (), {}\n"
        )
