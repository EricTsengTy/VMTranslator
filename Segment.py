""" Push Constant """
def constant(code):
    asm_code = "@" + code[2] + "\n"
    asm_code += "D = A\n"
    asm_code += "@SP\n"
    asm_code += "A = M\n"
    asm_code += "M = D\n"
    asm_code += "@SP\n"
    asm_code += "M = M + 1\n"
    return asm_code

""" Mutual_Code For (pop, push) (local, argument, this, that) """
def mutual_code(code, filled):
    asm_code = ""
    if code[0] == "pop":
        asm_code += "@" + code[2] + "\n"
        asm_code += "D = A\n"
        asm_code += "@" + filled + "\n"
        asm_code += "D = D + M\n"
        asm_code += "@R15\n"
        asm_code += "M = D\n"
        asm_code += "@SP\n"
        asm_code += "AM = M - 1\n"
        asm_code += "D = M\n"
        asm_code += "@R15\n"
        asm_code += "A = M\n"
        asm_code += "M = D\n"
    elif code[0] == "push":
        asm_code += "@" + code[2] + "\n"
        asm_code += "D = A\n"
        asm_code += "@" + filled + "\n"
        asm_code += "A = D + M\n"
        # Store value in D
        asm_code += "D = M\n"
        asm_code += "@SP\n"
        asm_code += "A = M\n"
        asm_code += "M = D\n"
        asm_code += "@SP\n"
        asm_code += "M = M + 1\n"
    return asm_code

""" Pop or Push Local """
def local(code):
    return mutual_code(code, "LCL")

""" Pop or Push Argument """
def argument(code):
    return mutual_code(code, "ARG")    

""" Pop or Push This """
def this(code):
    return mutual_code(code, "THIS")

""" Pop or Push That """
def that(code):
    return mutual_code(code, "THAT")

""" Only For Pointer """
def pointer_prototype(code, filled):
    asm_code = ""
    if code[0] == "pop":
        asm_code += "@SP\n"
        asm_code += "AM = M - 1\n"
        asm_code += "D = M\n"
        asm_code += "@" + filled + "\n"
        asm_code += "M = D\n"
    elif code[0] == "push":
        asm_code += "@" + filled + "\n"
        asm_code += "D = M\n"
        asm_code += "@SP\n"
        asm_code += "A = M\n"
        asm_code += "M = D\n"
        asm_code += "@SP\n"
        asm_code += "M = M + 1\n"
    return asm_code

""" Pop or Push Pointer """
def pointer(code):
    if code[2] == "0":
        return pointer_prototype(code, "THIS")
    elif code[2] == "1":
        return pointer_prototype(code, "THAT")

""" For temp, static """
def mutual_code_ver2(code, filled):
    asm_code = ""
    if code[0] == "pop":
        asm_code += "@" + code[2] + "\n"
        asm_code += "D = A\n"
        asm_code += "@" + filled + "\n"
        asm_code += "D = D + A\n"
        asm_code += "@R15\n"
        asm_code += "M = D\n"
        asm_code += "@SP\n"
        asm_code += "AM = M - 1\n"
        asm_code += "D = M\n"
        asm_code += "@R15\n"
        asm_code += "A = M\n"
        asm_code += "M = D\n"
    elif code[0] == "push":
        asm_code += "@" + code[2] + "\n"
        asm_code += "D = A\n"
        asm_code += "@" + filled + "\n"
        asm_code += "A = D + A\n"
        # Store value in D
        asm_code += "D = M\n"
        asm_code += "@SP\n"
        asm_code += "A = M\n"
        asm_code += "M = D\n"
        asm_code += "@SP\n"
        asm_code += "M = M + 1\n"
    return asm_code

""" Pop or Push Temp """
def temp(code):
    return mutual_code_ver2(code, "5")

""" Pop or Push Static """
def static(code):
    asm_code = ""
    if code[0] == "pop":
        asm_code += "@SP\n"
        asm_code += "AM = M - 1\n"
        asm_code += "D = M\n"
        asm_code += "@{filename}.{number}\n".format(filename = code[3], number = code[2])
        asm_code += "M = D\n"
    elif code[0] == "push":
        asm_code += "@{filename}.{number}\n".format(filename = code[3], number = code[2])
        asm_code += "D = M\n"
        asm_code += "@SP\n"
        asm_code += "A = M\n"
        asm_code += "M = D\n"
        asm_code += "@SP\n"
        asm_code += "M = M + 1\n"
    return asm_code