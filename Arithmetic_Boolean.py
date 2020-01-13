""" Just a Simple Addition """ 
def ADD(code):
    asm_code = "@SP\n"
    asm_code += "AM = M - 1\n"
    asm_code += "D = M\n"
    asm_code += "A = A - 1\n"
    asm_code += "M = M + D\n"
    return asm_code

""" Just a Simple Subtraction """
def SUB(code):
    asm_code = "@SP\n"
    asm_code += "AM = M - 1\n"
    asm_code += "D = M\n"
    asm_code += "A = A - 1\n"
    asm_code += "M = M - D\n"
    return asm_code

""" Just Negate It ! """
def NEG(code):
    asm_code = "@SP\n"
    asm_code += "A = M - 1\n"
    asm_code += "M = -M\n"
    return asm_code

# A Counter Which is Used For EQ's Labels' Names
EQ_NUM = 0
""" Determine If Stack[n - 2] == Stack[n - 1] ??? """
def EQ(code):
    global EQ_NUM
    asm_code = "@SP\n"
    asm_code += "AM = M - 1\n"
    asm_code += "D = M\n"
    asm_code += "A = A - 1\n"
    asm_code += "D = M - D\n"
    asm_code += "@EQ_SET{count}\n".format(count = EQ_NUM)
    asm_code += "D; JEQ\n"
    asm_code += "@SP\n"
    asm_code += "A = M - 1\n"
    asm_code += "M = 0\n"
    asm_code += "@EQ_END{count}\n".format(count = EQ_NUM)
    asm_code += ("0; JMP\n")
    asm_code += "(EQ_SET{count})\n".format(count = EQ_NUM)
    asm_code += "@SP\n"
    asm_code += "A = M - 1\n"
    asm_code += "M = -1\n"
    asm_code += "(EQ_END{count})\n".format(count = EQ_NUM)
    EQ_NUM += 1
    return asm_code

# A Label Counter
GT_NUM = 0
""" Stack[n - 2] > Stack[n - 1] ??? """
def GT(code):
    global GT_NUM
    asm_code = "@SP\n"
    asm_code += "AM = M - 1\n"
    asm_code += "D = M\n"
    asm_code += "A = A - 1\n"
    asm_code += "D = M - D\n"
    asm_code += "@GT_SET{count}\n".format(count = GT_NUM)
    asm_code += "D; JGT\n"
    asm_code += "@SP\n"
    asm_code += "A = M - 1\n"
    asm_code += "M = 0\n"
    asm_code += "@GT_END{count}\n".format(count = GT_NUM)
    asm_code += ("0; JMP\n")
    asm_code += "(GT_SET{count})\n".format(count = GT_NUM)
    asm_code += "@SP\n"
    asm_code += "A = M - 1\n"
    asm_code += "M = -1\n"
    asm_code += "(GT_END{count})\n".format(count = GT_NUM)
    GT_NUM += 1
    return asm_code

# A Label Counter
LT_NUM = 0
""" Stack[n - 2] < Stack[n - 1] ??? """
def LT(code):
    global LT_NUM
    asm_code = "@SP\n"
    asm_code += "AM = M - 1\n"
    asm_code += "D = M\n"
    asm_code += "A = A - 1\n"
    asm_code += "D = M - D\n"
    asm_code += "@LT_SET{count}\n".format(count = LT_NUM)
    asm_code += "D; JLT\n"
    asm_code += "@SP\n"
    asm_code += "A = M - 1\n"
    asm_code += "M = 0\n"
    asm_code += "@LT_END{count}\n".format(count = LT_NUM)
    asm_code += ("0; JMP\n")
    asm_code += "(LT_SET{count})\n".format(count = LT_NUM)
    asm_code += "@SP\n"
    asm_code += "A = M - 1\n"
    asm_code += "M = -1\n"
    asm_code += "(LT_END{count})\n".format(count = LT_NUM)
    LT_NUM += 1
    return asm_code

""" Just Apply And ! """
def AND(code):
    asm_code = "@SP\n"
    asm_code += "AM = M - 1\n"
    asm_code += "D = M\n"
    asm_code += "A = A - 1\n"
    asm_code += "M = M & D\n"
    return asm_code

""" Just Apply Or ! """
def OR(code):
    asm_code = "@SP\n"
    asm_code += "AM = M - 1\n"
    asm_code += "D = M\n"
    asm_code += "A = A - 1\n"
    asm_code += "M = M | D\n"
    return asm_code

""" Just Apply Not ! """
def NOT(code):
    asm_code = "@SP\n"
    asm_code += "A = M - 1\n"
    asm_code += "M = !M\n"
    return asm_code