import sys

import crie


def main():
    argv = sys.argv
    script = argv[1]
    with open(script) as file:
        rule = crie.grammar.parse(file.read())
        exec(crie.Python3Translator().visit(rule))

if __name__ == "__main__":
    main()
