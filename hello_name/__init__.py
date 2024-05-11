1import check50
2
3@check50.check()
4def id():
5    """id.py prints what you give it"""
6    check50.run("python3 hello_name.py").stdin("foo").stdout("hello foo").stdin("bar").stdout("hello bar")
