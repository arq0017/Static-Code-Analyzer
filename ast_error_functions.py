import ast
import re
from custom_exception import PEP8Error

variable_name_regex = r'(([^a-z]+)|([a-z]+[A-Z].*))'
ast_errors_list = []


class PEPAstFunction:

    @staticmethod
    def peps010(name, index):
        try:
            if re.match(variable_name_regex, name):
                raise PEP8Error(index, "S010", f"Argument name '{name}' should be snake_case")
        except PEP8Error as err:
            ast_errors_list.append(err.__str__())

    @staticmethod
    def peps011(name, index):
        try:
            if re.match(variable_name_regex, name):
                raise PEP8Error(index, "S012", f"Variable '{name}' in function should be snake_case")
        except PEP8Error as err:
            ast_errors_list.append(err.__str__())

    @staticmethod
    def peps012(default_obj, index):
        try:
            if isinstance(default_obj, ast.List) or isinstance(default_obj, ast.Dict) or isinstance(default_obj,
                                                                                                    ast.Set):
                raise PEP8Error(index, "S012", "Default argument value is mutable")
        except PEP8Error as err:
            ast_errors_list.append(err.__str__())

    @staticmethod
    def ast_errors(file_data):
        tree = ast.parse(file_data)

        for node in ast.walk(tree):

            # s010
            if isinstance(node, ast.FunctionDef):
                function_args = node.args.args
                for arg in function_args:
                    PEPAstFunction.peps010(arg.arg, node.lineno)

            # s011
            if isinstance(node, ast.FunctionDef):
                for var in node.body:
                    if isinstance(var, ast.Assign):
                        for name in var.targets:
                            if isinstance(name, ast.Attribute):
                                variable_name = name.attr
                            else:
                                variable_name = name.id
                            PEPAstFunction.peps011(variable_name, var.lineno)

            # s012
            if isinstance(node, ast.FunctionDef):
                for default_val_obj in node.args.defaults:
                    PEPAstFunction.peps012(default_val_obj, node.lineno)
