from custom_exception import PEP8Error
import re

non_ast_errors_list = []


class PEPNonAstFunction:

    @staticmethod
    def try_and_except(line, char_):
        return line.find(char_)

    @staticmethod
    def peps001(line, index):
        try:
            if len(line.strip()) > 79:
                raise PEP8Error(index + 1, "S001", "Too long")
        except PEP8Error as err:
            non_ast_errors_list.append(err.__str__())

    @staticmethod
    def peps002(line, index):
        try:
            if line.strip() != '' and line.startswith(' '):
                # for char_ in list(line):
                #     if char_ != ' ':
                #         break
                #     indentation += 1
                indentation = len(re.match('^ *', line).group())
                if indentation % 4 != 0:
                    raise PEP8Error(index + 1, "S002", "Indentation is not a multiple of four")
        except PEP8Error as err:
            non_ast_errors_list.append(err.__str__())

    @staticmethod
    def peps003(line, index):
        line = line.strip()
        try:
            # x = try_and_except(line, '#')
            # y = try_and_except(line, ';')
            # if (y != -1) and ((x != -1 and y < x and line[y + 1:x].strip() == '') or (x == -1 and line[-1] == ';')):
            if re.match('[^#]*; *($|#.*)', line):
                raise PEP8Error(index + 1, "S003", "Unnecessary semicolon")
        except PEP8Error as err:
            non_ast_errors_list.append(err.__str__())

    @staticmethod
    def peps004(line, index):
        try:
            x = PEPNonAstFunction.try_and_except(line.strip(), '#')
            if x != -1 and line[x - 2:x].strip() != '':
                raise PEP8Error(index + 1, "S004", "At least two spaces required before inline comments")
        except PEP8Error as err:
            non_ast_errors_list.append(err.__str__())

    @staticmethod
    def peps005(line, index):
        try:
            x = PEPNonAstFunction.try_and_except(line.strip(), '#')
            y = PEPNonAstFunction.try_and_except(line.lower().strip(), 'todo')
            if x < y and x != -1:
                raise PEP8Error(index + 1, "S005", "TODO found")
        except PEP8Error as err:
            non_ast_errors_list.append(err.__str__())

    @staticmethod
    def peps006(line_space, index):
        try:
            if line_space > 2:
                raise PEP8Error(index + 1, "S006", "More than two blank lines used before this line")
        except PEP8Error as err:
            non_ast_errors_list.append(err.__str__())

    @staticmethod
    def peps007(line, index):
        try:
            if re.match(r'\s*class[ ]{2,}.*', line):
                raise PEP8Error(index + 1, "S007", "Too many spaces after 'class'")
            if re.match(r'\s*def[ ]{2,}.*', line):
                raise PEP8Error(index + 1, "S007", "Too many spaces after 'def'")
        except PEP8Error as err:
            non_ast_errors_list.append(err.__str__())

    @staticmethod
    def peps008(line, index):
        if re.match('.*class.*', line):
            # get class name
            class_name = line.replace('class', '').strip().split(':', 1)[0]
            try:
                if re.match('(([^A-Z].*)|([A-Z][^_-]*[_-]+.*))', class_name):
                    raise PEP8Error(index + 1, "S008", f"Class name '{class_name}' should use CamelCase")
            except PEP8Error as err:
                non_ast_errors_list.append(err.__str__())

    @staticmethod
    def peps009(line, index):
        if re.match('.*def.*', line):
            # get class name
            def_name = line.replace('def', '').strip().split('(', 1)[0]
            try:
                if re.match(r'([^a-z_]+)', def_name):
                    raise PEP8Error(index + 1, "S009", f"Function name '{def_name}' should use snake_case")
            except PEP8Error as err:
                non_ast_errors_list.append(err.__str__())
