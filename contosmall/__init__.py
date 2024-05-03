import check50


@check50.check()
def exists():
    """contosmall.py exists"""
    check50.exists("contosmall.py")

@check50.check(exists)
def testhello():
    """input of HELLO yields output of hello"""
    check50.run("python3 contosmall.py").stdin("HELLO", prompt=False).stdout("hello").exit()

@check50.check(exists)
def testcs50():
    """input of THIS IS JIME yields output of this is jime"""
    check50.run("python3 contosmall.py").stdin("THIS IS JIME", prompt=False).stdout("this is jime").exit()

@check50.check(exists)
def testnumber():
    """input of 100 yields output of 100"""
    check50.run("python3 contosmall.py").stdin("100", prompt=False).stdout("100").exit()
