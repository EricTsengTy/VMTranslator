from Segment import constant, local, argument, this, that, pointer, temp, static

segment = {"constant" : constant, "local" : local, "argument" : argument, "this": this, "that" : that, "pointer" : pointer, "temp" : temp, "static" : static}

""" Push ! """
def PUSH(code):
    return segment[code[1]](code)

""" Pop ! """
def POP(code):
    return segment[code[1]](code)