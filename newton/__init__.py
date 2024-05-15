import check50

@check50.check()
def exists():
    """newton.py exists"""
    check50.exists("newton.py")


@check50.check(exists)
def test1():
    """input of 1 yields output of 10"""
    output = check50.run("python3 newton.py").stdin("1", prompt=False).stdout("10")


@check50.check(exists)
def test14():
    """input of 14 yields output of 140"""
    output = check50.run("python3 newton.py").stdin("14", prompt=False).stdout("140")


@check50.check(exists)
def test50():
    """input of 50 yields output of 500"""
    output = check50.run("python3 newton.py").stdin("50", prompt=False).stdout("500")
