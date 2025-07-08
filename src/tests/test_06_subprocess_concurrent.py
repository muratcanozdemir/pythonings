from pythonings.ex06_subprocess_concurrent import run_commands

def test_run_commands_parallel():
    cmds = [
        "echo first",
        "echo second",
        "echo third"
    ]
    results = run_commands(cmds)
    assert sorted(results) == ["first", "second", "third"]
    # Should be robust if one command fails
    cmds2 = [
        "echo ok",
        "false",         # always fails
        "echo done"
    ]
    results2 = run_commands(cmds2)
    assert "ok" in results2 and "done" in results2
