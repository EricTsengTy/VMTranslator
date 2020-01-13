""" Label Production """
def LABEL(code):
    asm_code = "(" + code[1] + ")\n"
    return asm_code

""" Go ! """
def GOTO(code):
    asm_code = "@" + code[1] + "\n"
    asm_code += "0; JMP\n"
    return asm_code

""" if-goto Production """
def IF_GOTO(code):
    asm_code = "@SP\n"
    asm_code += "AM = M - 1\n"
    asm_code += "D = M\n"
    asm_code += "@" + code[1] + "\n"
    asm_code += "D; JNE\n"
    return asm_code