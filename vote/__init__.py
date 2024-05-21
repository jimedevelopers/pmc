import check50

@check50.check()
def exists():
    """vote.py exists"""
    check50.exists("vote.py")


@check50.check(exists)
def test1():
    """input of 17 yields output of Cannot vote"""
    output = check50.run("python3 vote.py").stdin("17", prompt=False).stdout("[Cc]annot [Vv]ote")


@check50.check(exists)
def test14():
    """input of 25 yields output of Can vote"""
    output = check50.run("python3 vote.py").stdin("25", prompt=False).stdout("[Cc]an [Vv]ote")
