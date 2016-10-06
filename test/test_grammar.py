import unittest
import crie


class GrammarCase(unittest.TestCase):

    maxDiff = None

    boolean_values = [
        "verdadeiro",
        "falso"
    ]
    values = [
        "10",
        "10.5",
        "'sim'",
        "'teste teste'",
        "'teste!'"
    ] + boolean_values

    logic_expressions = [
        "x ou y",
        "x e y"
        # TODO: "não x"
    ]
    boolean_expressions = [
        "x for y",
        "x não for y",
        "x for 10",
        "x não for 10",
        "x for 'sim'",
        "x for maior que y",
        "x não for maior que y",
        "x for maior que 10",
        "x não for maior que 10",
        "x for menor que y",
        "x não for menor que y",
        "x for menor que 10",
        "x não for menor que 10"
    ]
    expressions = [
        "pergunte!",
        "pergunte! 'teste'",
        "pergunte! 'teste' e 'teste'",
        "x + 10",
        "x - 10",
        "x * 10",
        "x / 10"
    ] + logic_expressions + boolean_expressions

    def test_script(self):
        with open('input.crie') as input_crie:
            rule = crie.grammar.parse(input_crie.read())
            script = crie.Python3Translator().translate(rule)
            with open('output.py') as output_py:
                self.assertEqual(output_py.read(), script)

    def test_assignment(self):
        for value in self.values:
            with self.subTest(value=value):
                rule = crie.grammar['assignment'].parse("x é %s" % value)
                self.assertIsNotNone(rule)
        for expression in self.expressions:
            with self.subTest(expression=expression):
                rule = crie.grammar['assignment'].parse("x é: %s" % expression)
                self.assertIsNotNone(rule)

    def test_conditional(self):
        for value in self.boolean_values + self.boolean_expressions:
            with self.subTest(value=value):
                rule = crie.grammar['conditional'].parse("se %s" % value)
                self.assertIsNotNone(rule)
                rule = crie.grammar['conditional'].parse("quando %s" % value)
                self.assertIsNotNone(rule)
        rule = crie.grammar['conditional'].parse("senão")
        self.assertIsNotNone(rule)

    def test_loop(self):
        for value in self.boolean_values + self.boolean_expressions:
            with self.subTest(value=value):
                rule = crie.grammar['loop'].parse("enquanto %s" % value)
                self.assertIsNotNone(rule)

    def test_action(self):
        with self.subTest(arguments=0):
            rule = crie.grammar['action'].parse("ação x")
            self.assertIsNotNone(rule)
        with self.subTest(arguments=1):
            rule = crie.grammar['action'].parse("ação x usando y")
            self.assertIsNotNone(rule)
        with self.subTest(arguments=2):
            rule = crie.grammar['action'].parse("ação x usando y e z")
            self.assertIsNotNone(rule)
        with self.subTest(arguments=3):
            rule = crie.grammar['action'].parse("ação x usando y e w e z")
            self.assertIsNotNone(rule)


if __name__ == '__main__':
    unittest.main()
