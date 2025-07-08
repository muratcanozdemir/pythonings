import tempfile
import pathlib
from pythonings.ex05_pathlib import list_py_files

def test_list_py_files(tmp_path):
    (tmp_path / "a.py").write_text("# python!")
    (tmp_path / "b.txt").write_text("not python")
    (tmp_path / "c.py").write_text("print(42)")
    files = list_py_files(str(tmp_path))
    # Should return full paths as strings to .py files
    paths = {pathlib.Path(f).name for f in files}
    assert paths == {"a.py", "c.py"}
    for f in files:
        assert f.endswith(".py")
