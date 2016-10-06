from parsimonious.grammar import Grammar, NodeVisitor

grammar = Grammar(
    r"""
    script = line*
    line = instruction? space* newline
    instruction = indent* (loop / conditional / command / assignment)
    indent = "|" space+
    space = " "
    loop = loop_oper space+ boolean_expr
    loop_oper = "enquanto"
    conditional = conditional_if / conditional_elif / conditional_else
    conditional_if = conditional_if_oper space+ boolean_expr
    conditional_if_oper = "se"
    boolean_expr = equals / less_than / greather_than / name
    equals = value space+ equals_oper space+ value
    equals_oper = (not space+)? "for"
    not = "não"
    less_than = value space+ (not space+)? less_than_oper space+ value
    less_than_oper = "menor que"
    greather_than = value space+ (not space+)? greather_than_oper space+ value
    greather_than_oper = "maior que"
    boolean_or = boolean_value space+ or_oper space+ boolean_value
    boolean_value = name / boolean
    name   = ~"\w+"
    boolean = "verdadeiro" / "falso"
    or_oper = "ou"
    boolean_and = boolean_expr space+ and_oper space+ boolean_expr
    and_oper = "e"
    conditional_elif = conditional_elif_oper space+ boolean_expr
    conditional_elif_oper = "quando"
    conditional_else = conditional_else_oper
    conditional_else_oper = "senão"
    command = print / ask
    print = print_oper space+ value
    print_oper = "escreva"
    ask = ask_oper (space+ value)?
    ask_oper = "pergunte"
    newline = "\n" / ~"$"
    assignment = name space+ assign_oper (assign_value / assign_ask / assign_boolean_expr)
    assign_oper = "é"
    assign_value = space+ (value / boolean_value)
    value = text / number / boolean / name
    text = quote plain_text quote
    quote = "'"
    plain_text = ~"[^']+"i
    number = ~"[0-9]+(\\.[0-9]+)?"
    assign_ask = colon space+ ask
    colon = ":"
    assign_boolean_expr = colon space+ (boolean_and / boolean_or / boolean_expr)
    """)

class Python3Translator(NodeVisitor):

    def visit_assignment(self, _, children):
        return " ".join((child for child in children if child))

    def visit_less_than(self, _, children):
        return " ".join((child for child in children if child))

    def visit_boolean_and(self, _, children):
        return " ".join((child for child in children if child))

    def visit_conditional_if(self, _, children):
        return " ".join((child for child in children if child)) + ":"

    def visit_conditional_elif(self, _, children):
        return " ".join((child for child in children if child)) + ":"

    def visit_equals(self, _, children):
        return " ".join((child for child in children if child))

    def visit_loop(self, _, children):
        return " ".join((child for child in children if child)) + ":"

    def visit_print(self, _, children):
        (oper, _, value) = children
        return oper + "(" + value + ")"

    def visit_print_oper(self, _, children):
        return "print"

    def visit_ask(self, _, children):
        (oper, value) = children
        return oper + "(" + value + ")"

    def visit_ask_oper(self, _, children):
        return "input"

    def visit_colon(self, _, children):
        pass

    def visit_newline(self, _, children):
        return "\n"

    def visit_assign_oper(self, _, children):
        return "="

    def visit_less_than_oper(self, _, children):
        return "<"

    def visit_and_oper(self, _, children):
        return "and"

    def visit_conditional_if_oper(self, _, children):
        return "if"

    def visit_conditional_elif_oper(self, _, children):
        return "elif"

    def visit_conditional_else_oper(self, _, children):
        return "else:"

    def visit_loop_oper(self, _, children):
        return "while"

    def visit_equals_oper(self, _, children):
        return "=="

    def visit_indent(self, _, children):
        return "    "

    def visit_text(self, text, children):
        return text.text

    def visit_boolean(self, boolean, children):
        return {'verdadeiro': 'True', 'falso': 'False'}[boolean.text]

    def visit_name(self, name, children):
        return name.text

    def visit_number(self, number, children):
        return number.text

    def visit_space(self, _, children):
        pass

    def visit_quote(self, _, children):
        return "'"

    def visit_plain_text(self, plain_text, children):
        plain_text.text

    def generic_visit(self, node, children):
        return "".join((child for child in children if child))
