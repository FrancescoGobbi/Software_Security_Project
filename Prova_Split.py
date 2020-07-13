import re
import tokenize
import io


def tokenize_line(line):
    return [list(a) for a in tokenize.generate_tokens(io.StringIO(line).readline)]

x = "ciao come va[i]"
y = "pippo = casa + ciao[i]"
a = tokenize_line(y)
lista = y.split()
print(lista)
print(a)