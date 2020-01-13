import re

""" Trim Comments  """
line_comment = False
def trim(code):
    global line_comment
    if line_comment == True:
        code = "/*" + code
    code = re.sub(r"/\*.*?\*/", "", code)
    if "/*" in code:
        line_comment = True
    else:
        line_comment = False
    code = re.sub(r"(//|/\*).*", "", code).strip()
    return code