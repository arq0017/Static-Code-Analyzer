# custom Exception
class PEP8Error(Exception):

    path_to_file = ''

    def __init__(self, number, error, message):
        self.message = f'{self.path_to_file}: Line {number}: {error} {message}'
        super().__init__(self.message)

    def __str__(self):
        return self.message
