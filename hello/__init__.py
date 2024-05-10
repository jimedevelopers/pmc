import check50

@check50.check()

def exists():
  """hello.py exists"""
  check50.exists("hello.py")
def output(exists):
  """We can get Hello World as output (If this is red please type 'Hello World' exactly as shown)"""
  check50.run("hello.py").stdout("Hello World").exit(0)
  
