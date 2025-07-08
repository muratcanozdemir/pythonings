from pythonings.ex12_multiple_inheritance_di import App, DataService

def test_mro(capsys):
    app = App()
    app.log("hi")
    output = capsys.readouterr().out.strip().splitlines()
    assert output == [
        "FileLogger: hi",
        "ConsoleLogger: hi",
        "Logger: hi"
    ]

def test_dependency_injection():
    class DummyFetcher:
        def __call__(self, url):
            return "dummy!"
    ds = DataService(fetcher=DummyFetcher())
    assert ds.get_data("irrelevant") == "DUMMY!"
