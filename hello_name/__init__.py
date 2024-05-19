import check50

@check50.check()
def exists():
    """hello_name.py exists"""
    check50.exists("hello_name.py")


@check50.check(exists)
def test1():
    """input of Jameel yields output of Hello Jameel"""
    output = check50.run("python3 hello_name.py").stdin("Jameel", prompt=False).stdout("[Hh]ello Jameel")


@check50.check(exists)
def test14():
    """input of Jime yields output of Hello Jime"""
    output = check50.run("python3 hello_name.py").stdin("Jime", prompt=False).stdout("[Hh]ello Jime")


@check50.check(exists)
def test50():
    """input of Haebaek yields output of Hello Haebaek"""
    output = check50.run("python3 hello_name.py").stdin("Haebaek", prompt=False).stdout("Hello Haebaek")
