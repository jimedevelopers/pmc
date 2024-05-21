import check50

@check50.check()
def exists():
    """num.py exists"""
    check50.exists("num.py")


@check50.check(exists)
def test1():
    """input of 1 yields output of One"""
    output = check50.run("python3 num.py").stdin("1", prompt=False).stdout("[Oo]ne")


@check50.check(exists)
def test14():
    """input of 5 yields output of Five"""
    output = check50.run("python3 num.py").stdin("5", prompt=False).stdout("[Ff]ive")

@check50.check(exists)
def test14():
    """input of 10 yields output of Ten"""
    output = check50.run("python3 num.py").stdin("10", prompt=False).stdout("[Tt]en")
