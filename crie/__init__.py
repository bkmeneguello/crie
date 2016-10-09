from parsimonious.grammar import Grammar, NodeVisitor

grammar = Grammar(
    r"""
    script = line*
    line = instruction? space* newline
    instruction = indent* (loop / conditional / action / assignment / command / object_command)
    indent = "|" space+
    space = " "
    loop = loop_oper space+ boolean_expr
    loop_oper = "enquanto"
    conditional = conditional_if / conditional_elif / conditional_else
    conditional_if = conditional_if_oper space+ boolean_expr
    conditional_if_oper = "se"
    boolean_expr = not_less_than / less_than / not_greather_than / greather_than / not_equals / equals / name
    equals = value space+ equals_oper space+ value
    not_equals = value space+ not_oper space+ equals_oper space+ value
    equals_oper = "for"
    not_oper = "não"
    less_than = value space+ equals_oper space+ less_than_oper space+ value
    not_less_than = value space+ not_oper space+ equals_oper space+ less_than_oper space+ value
    less_than_oper = "menor que"
    greather_than = value space+ equals_oper space+ greather_than_oper space+ value
    not_greather_than = value space+ not_oper space+ equals_oper space+ greather_than_oper space+ value
    greather_than_oper = "maior que"
    boolean_or = boolean_value space+ or_oper space+ boolean_value
    boolean_value = name / boolean
    name = ~"\w+"
    boolean = "verdadeiro" / "falso"
    or_oper = "ou"
    boolean_and = boolean_expr space+ and_oper space+ boolean_expr
    and_oper = "e"
    conditional_elif = conditional_elif_oper space+ boolean_expr
    conditional_elif_oper = "quando"
    conditional_else = conditional_else_oper
    conditional_else_oper = "senão"
    command = name "!" (space+ arguments)?
    arguments = value (space+ argument_sep_oper space+ value)*
    argument_sep_oper = "e"
    newline = "\n" / ~"$"
    action = action_oper space+ name (space+ using_oper space+ parameters)?
    action_oper = "ação"
    using_oper = "usando"
    parameters = name (space+ parameter_sep_oper space+ name)*
    parameter_sep_oper = "e"
    assignment = name space+ assign_oper (assign_expr / assign_value)
    assign_expr = colon space+ (command / object_command / math_expr / assign_boolean_expr)
    colon = ":"
    assign_value = space+ value
    assign_oper = "é"
    value = text / decimal / integer / boolean / name
    text = quote plain_text quote
    quote = "'"
    plain_text = ~"[^']+"i
    integer = ~"[0-9]+"
    decimal = ~"[0-9]+\\.[0-9]+"
    assign_boolean_expr = boolean_and / boolean_or / boolean_expr
    math_expr = number_value space+ (plus_oper / less_oper / mult_oper / div_oper) space+ number_value
    number_value = decimal / integer / name
    plus_oper = "+"
    less_oper = "-"
    mult_oper = "*"
    div_oper = "/"
    object_command = name object_command_oper space+ command
    object_command_oper = ","
    """)


class Python3Translator(NodeVisitor):

    def visit_assignment(self, _, children):
        return " ".join((child for child in children if child))

    def visit_less_than(self, _, children):
        return " ".join((child for child in children if child))

    def visit_greather_than(self, _, children):
        return " ".join((child for child in children if child))

    def visit_boolean_and(self, _, children):
        return " ".join((child for child in children if child))

    def visit_conditional_if(self, _, children):
        return " ".join((child for child in children if child)) + ":"

    def visit_conditional_elif(self, _, children):
        return " ".join((child for child in children if child)) + ":"

    def visit_action(self, _, children):
        return "def " + children[2] + "(" + children[3] + "):"

    def visit_equals(self, _, children):
        return " ".join((child for child in children if child))

    def visit_not_equals(self, _, children):
        children[4] = '!='
        return " ".join((child for child in children if child))

    def visit_less_than(self, _, children):
        children[2] = ''
        children[4] = '<'
        return " ".join((child for child in children if child))

    def visit_not_less_than(self, _, children):
        children[4] = '>='
        children[6] = ''
        return " ".join((child for child in children if child))

    def visit_greather_than(self, _, children):
        children[2] = ''
        children[4] = '>'
        return " ".join((child for child in children if child))

    def visit_not_greather_than(self, _, children):
        children[4] = '<='
        children[6] = ''
        return " ".join((child for child in children if child))

    def visit_loop(self, _, children):
        return " ".join((child for child in children if child)) + ":"

    def visit_math_expr(self, _, children):
        return " ".join((child for child in children if child))

    def visit_command(self, _, children):
        (oper, _, value) = children
        return oper + "(" + value + ")"

    def visit_colon(self, *_):
        pass

    def visit_newline(self, *_):
        return "\n"

    def visit_assign_oper(self, *_):
        return "="

    def visit_and_oper(self, *_):
        return "and"

    def visit_conditional_if_oper(self, *_):
        return "if"

    def visit_conditional_elif_oper(self, *_):
        return "elif"

    def visit_conditional_else_oper(self, *_):
        return "else:"

    def visit_loop_oper(self, *_):
        return "while"

    def visit_equals_oper(self, *_):
        return "=="

    def visit_argument_sep_oper(self, *_):
        return ", "

    def visit_parameter_sep_oper(self, *_):
        return ", "

    def visit_plus_oper(self, *_):
        return "+"

    def visit_less_oper(self, *_):
        return "-"

    def visit_mult_oper(self, *_):
        return "*"

    def visit_div_oper(self, *_):
        return "/"

    def visit_object_command_oper(self, *_):
        return "."

    def visit_indent(self, *_):
        return "    "

    def visit_text(self, text, *_):
        return text.text

    def visit_boolean(self, boolean, *_):
        return {'verdadeiro': 'True', 'falso': 'False'}[boolean.text]

    def visit_name(self, name, *_):
        return name.text

    def visit_integer(self, integer, *_):
        return integer.text

    def visit_decimal(self, decimal, *_):
        return decimal.text

    def visit_space(self, *_):
        pass

    def visit_quote(self, *_):
        return "'"

    def visit_plain_text(self, plain_text, *_):
        return plain_text.text

    def generic_visit(self, _, children):
        return "".join((child for child in children if child))

    def translate(self, node):
        script = 'from crie.stdlib import *\n'
        script += self.visit(node)
        return script
