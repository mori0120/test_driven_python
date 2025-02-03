import hello

def test_main(capsys):
    hello.main()
    output = capsys.readouterr().out
    assert output == "Hello world!\n"