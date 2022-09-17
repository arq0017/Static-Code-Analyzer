import os
import sys
from non_ast_error_functions import PEPNonAstFunction, non_ast_errors_list
from ast_error_functions import PEPAstFunction, ast_errors_list
from custom_exception import PEP8Error


def check_errors(final_path_to_file):
    res = []
    # reading ast errors
    with open(final_path_to_file) as file:
        PEP8Error.path_to_file = final_path_to_file
        ast_errors_list.clear()
        PEPAstFunction.ast_errors(file.read())
        res += ast_errors_list
    # reading non-ast errors
    with open(final_path_to_file) as file:
        list_of_lines = file.readlines()
        line_space = 0
        PEP8Error.path_to_file = final_path_to_file
        non_ast_errors_list.clear()
        # reading non-ast errors
        for index in range(len(list_of_lines)):
            file_line = list_of_lines[index]
            # length of character
            PEPNonAstFunction.peps001(file_line, index)
            # Indentation
            PEPNonAstFunction.peps002(file_line, index)
            # Unnecessary semicolon
            PEPNonAstFunction.peps003(file_line, index)
            # Inline comment space
            PEPNonAstFunction.peps004(file_line, index)
            # to-do found
            PEPNonAstFunction.peps005(file_line, index)
            # two blank lines
            PEPNonAstFunction.peps006(line_space, index)
            # space after constructor
            PEPNonAstFunction.peps007(file_line, index)
            # class CamelCase
            PEPNonAstFunction.peps008(file_line, index)
            # function snake_case
            PEPNonAstFunction.peps009(file_line, index)
            # checking line space every time
            line_space = line_space + 1 if file_line.strip() == '' else 0
        res += non_ast_errors_list
    #
    sorted(res, key=lambda num: int(num.split(':')[1].replace('Line', '').strip()))
    for msg in res:
        print(msg)



# getting args
args = sys.argv
d_o_f = args[1]
# given arg is file_
if os.path.isfile(d_o_f):
    if d_o_f.endswith('.py'):
        check_errors(d_o_f)
# given arg is directory
else:
    for file_ in sorted(os.listdir(d_o_f)):
        if file_.endswith('.py'):
            path_to_file = os.path.join(d_o_f, file_)
            check_errors(path_to_file)

