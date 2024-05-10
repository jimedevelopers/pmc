import check50

@check50.check()

def exists():
  """hello.py exists"""
  check50.exists("hello.py")

@check50.check(exists)

def output():
  """We can get Hello World as output (If this is red please type 'Hello World' exactly as shown)"""
  check50.run("hello.py").stdout("Hello World",regex= False).exit(0)
  
