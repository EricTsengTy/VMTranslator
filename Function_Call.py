from Memory_Access import PUSH, POP
from Code_Production import trim

""" Set the Stack When a Function is Called """
def FUNCTION(code):
    function = code[1]
    nVars = int(code[2])
    push_one = trim("push constant 0").split(" ")
    asm_code = "(" + function + ")\n"
    for i in range(nVars):
        asm_code += PUSH(push_one)
    return asm_code

# A Label Counter
call_num = 0
""" Set ReturnAddress, LCL, ARG, THIS, THAT When Calling a Function """
def CALL(code):
    global call_num
    function = code[1]
    nArgs = int(code[2])
    asm_code = ""
    # Store ReturnAddress
    asm_code += "@CALL_FUNC" + str(call_num) + "\n"
    asm_code += "D = A\n"
    asm_code += "@SP\n"
    asm_code += "A = M\n"
    asm_code += "M = D\n"
    # LCL
    asm_code += "@LCL\n"
    asm_code += "D = M\n"
    asm_code += "@SP\n"
    asm_code += "AM = M + 1\n"
    asm_code += "M = D\n"
    # ARG
    asm_code += "@ARG\n"
    asm_code += "D = M\n"
    asm_code += "@SP\n"
    asm_code += "AM = M + 1\n"
    asm_code += "M = D\n"
    # THIS
    asm_code += "@THIS\n"
    asm_code += "D = M\n"
    asm_code += "@SP\n"
    asm_code += "AM = M + 1\n"
    asm_code += "M = D\n"
    # THAT
    asm_code += "@THAT\n"
    asm_code += "D = M\n"
    asm_code += "@SP\n"
    asm_code += "AM = M + 1\n"
    asm_code += "M = D\n"
    # Top Empty
    asm_code += "@SP\n"
    asm_code += "MD = M + 1\n"
    # Set ARG
    asm_code += "@ARG\n"
    asm_code += "M = D\n"
    asm_code += "@" + str(nArgs) + "\n"
    asm_code += "D = A\n"
    asm_code += "@5\n"
    asm_code += "D = D + A\n"
    asm_code += "@ARG\n"
    asm_code += "M = M - D\n"
    # Set LCL
    asm_code += "@SP\n"
    asm_code += "D = M\n"
    asm_code += "@LCL\n"
    asm_code += "M = D\n"
    # Goto Function
    asm_code += "@" + function + "\n"
    asm_code += "0; JMP\n"
    # Set ReturnAddress
    asm_code += "(CALL_FUNC" + str(call_num) + ")\n"
    # Syntax
    call_num += 1
    return asm_code

""" Restore LCL, ARG, THIS, THAT When Return is Called """
def RETURN(code):
    asm_code = ""
    # Set Frame
    asm_code += "@LCL\n"
    asm_code += "D = M\n"
    asm_code += "@R15\n"
    asm_code += "M = D\n"
    # Set retAddr
    asm_code += "@5\n"
    asm_code += "A = D - A\n"
    asm_code += "D = M\n"
    asm_code += "@R13\n"
    asm_code += "M = D\n"
    # Set Return Value
    asm_code += "@SP\n"
    asm_code += "AM = M - 1\n"
    asm_code += "D = M\n"
    asm_code += "@ARG\n"
    asm_code += "A = M\n"
    asm_code += "M = D\n"
    asm_code += "@ARG\n"
    asm_code += "D = M + 1\n"
    asm_code += "@SP\n"
    asm_code += "M = D\n"
    # THAT
    asm_code += "@R15\n"
    asm_code += "AM = M - 1\n"
    asm_code += "D = M\n"
    asm_code += "@THAT\n"
    asm_code += "M = D\n"
    # THIS
    asm_code += "@R15\n"
    asm_code += "AM = M - 1\n"
    asm_code += "D = M\n"
    asm_code += "@THIS\n"
    asm_code += "M = D\n"
    # ARG
    asm_code += "@R15\n"
    asm_code += "AM = M - 1\n"
    asm_code += "D = M\n"
    asm_code += "@ARG\n"
    asm_code += "M = D\n"
    # LCL
    asm_code += "@R15\n"
    asm_code += "AM = M - 1\n"
    asm_code += "D = M\n"
    asm_code += "@LCL\n"
    asm_code += "M = D\n"
    # retAddr
    asm_code += "@R13\n"
    asm_code += "A = M\n"
    asm_code += "0; JMP\n"
    return asm_code