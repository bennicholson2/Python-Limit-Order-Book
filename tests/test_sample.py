from lob_simulator import hello


def test_hello_returns_string() -> None:
    assert hello() == "Hello from python_lob!"
