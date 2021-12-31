import inspect
import dis

def expecting(offset=0):
    """Return how many values the caller is expecting"""
    f = inspect.currentframe().f_back.f_back
    i = f.f_lasti + offset
    bytecode = f.f_code.co_code
    instruction = ord(bytecode[i])
    if instruction == dis.opmap['UNPACK_SEQUENCE']:
        return ord(bytecode[i + 1])
    elif instruction == dis.opmap['POP_TOP']:
        return 0
    else:
        return 1