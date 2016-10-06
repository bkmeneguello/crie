import sys

import crie


def main():
    argv = sys.argv
    script_name = argv[1]
    with open(script_name) as script_file:
        rule = crie.grammar.parse(script_file.read())
        exec(crie.Python3Translator().translate(rule), globals())

if __name__ == "__main__":
    main()
