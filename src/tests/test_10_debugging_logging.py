import logging
from pythonings.ex10_debugging_logging import divide

def test_divide_logs(caplog):
    with caplog.at_level(logging.INFO):
        res = divide(10, 2)
        assert res == 5
        res2 = divide(10, 0)
        assert res2 is None
        logs = caplog.text
        assert "error" in logs.lower() or "exception" in logs.lower()
