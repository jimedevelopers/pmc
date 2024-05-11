import check50

@check50.check()
def id():
    """id.py prints what you give it"""
    check50.run("python3 hello_name.py").stdin("foo").stdout("hello foo").stdin("bar").stdout("hello bar")
