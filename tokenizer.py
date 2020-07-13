import tokenize
import io

def tokenize_line(line):
    return [list(a) for a in tokenize.generate_tokens(io.StringIO(line).readline)] #SBAGLIATO IN CERTI CASI


def untokenize_line(tokens):
    return tokenize.untokenize(tokens)


def tokenize_file(source_file):
    with open(source_file, 'r') as file_obj:
        return file_obj.readlines()
