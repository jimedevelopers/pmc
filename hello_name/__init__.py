import check50

@check50.check()
def exist():
   """hello_name.py"""
   check50.exists("hello_name.py")
@check50.check(exist):
   """The input Jameel produces the output Hello Jameel"""
   check50.run("python3 hello_name.py").stdin("Jameel").stdout("[Hh]ello [Jj]ameel").exit(0)
