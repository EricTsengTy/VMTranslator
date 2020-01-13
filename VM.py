#!/usr/bin/python3.8
import sys, re, os
from Arithmetic_Boolean import ADD, SUB, NEG, EQ, GT, LT, AND, OR, NOT
from Memory_Access import PUSH, POP
from Program_Flow import LABEL, GOTO, IF_GOTO
from Function_Call import FUNCTION, CALL, RETURN 
from Code_Production import trim
from Initialize import init

# Command
operation = {"add" : ADD, "sub" : SUB, "neg" : NEG, "eq" : EQ, "gt" : GT, "lt" : LT, "and" : AND, "or" : OR, "not": NOT, "push" : PUSH, "pop" : POP,
             "label" : LABEL, "goto" : GOTO, "if-goto" : IF_GOTO, "function" : FUNCTION, "call" : CALL, "return" : RETURN}

""" Main Function """
def main():
    # Read File
    if len(sys.argv) != 2:
        exit("Format : VM.py directory")
    directory = sys.argv[1].rstrip("/")
    directory_name = re.sub(r".*/", "", directory)
    filename_out = directory + "/" + directory_name + ".asm"
    assembly_code = open(filename_out, "w")
    
    # INIT (Not for SimpleFunction Test)
    assembly_code.write(init())
    
    # VM TO ASSEMBLY
    for file in os.listdir(directory):
        if ".vm" not in file:
            continue
        vm_code = open(directory + "/" + file, "r")
        for code in vm_code.readlines():
            code = trim(code)
            if code == "":
                continue
            debug = "// " + code + "\n"
            code += " " + file.replace(".vm", "")
            code = code.split(" ")
            code = operation[code[0]](code)
            assembly_code.write(debug + code)

    # Close File
    vm_code.close()
    assembly_code.close()

if __name__ == "__main__":
    main()