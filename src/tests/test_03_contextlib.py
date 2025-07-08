import tempfile
from pythonings.ex03_contextlib import read_first_line

def test_read_first_line():
    with tempfile.NamedTemporaryFile("w+t", delete=True) as tf:
        tf.write("hello\nworld\n")
        tf.seek(0)
        assert read_first_line(tf.name) == "hello"
