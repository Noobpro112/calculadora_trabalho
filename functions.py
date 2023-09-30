import ast

class Botoes:
    def __init__(self):
        self.valor_default = ""

    def calcular(self):
        try:
            # Verificar a sintaxe da expressão
            ast.parse(self.valor_default)

            # Avaliar a expressão
            result = eval(self.valor_default)
            self.valor_default = str(result)
        except (SyntaxError, ZeroDivisionError):
            # Lidar com erros de syntax ou burrice do usuário
            self.valor_default = "Erro"

    def clear(self):
        self.valor_default = ""

    def add_zero(self):
        self.valor_default += "0"

    def add_um(self):
        self.valor_default += "1"

    def add_dois(self):
        self.valor_default += "2"

    def add_tres(self):
        self.valor_default += "3"

    def add_quatro(self):
        self.valor_default += "4"

    def add_cinco(self):
        self.valor_default += "5"

    def add_seis(self):
        self.valor_default += "6"

    def add_sete(self):
        self.valor_default += "7"

    def add_oito(self):
        self.valor_default += "8"

    def add_nove(self):
        self.valor_default += "9"

    def add_operador(self, operador):
        # Verificar se o último caractere é um operador de fechamento de parênteses antes de adicionar outro operador
        if self.valor_default and self.valor_default[-1] == ")":
            return

        # Verificar se o último caractere é um operador antes de adicionar outro operador
        if self.valor_default and self.valor_default[-1] in "+-*/":
            return

        self.valor_default += operador

    def add_mais(self):
        self.add_operador("+")
    
    def add_menos(self):
        self.add_operador("-")
    
    def add_mult(self):
        self.add_operador("*")
    
    def add_div(self):
        self.add_operador("/")

    def evaluate(self):
        try:
            # Verificar a sintaxe da expressão antes de avaliá-la
            ast.parse(self.valor_default)

            # Avaliar a expressão e armazenar o resultado em self.valor_default
            result = eval(self.valor_default)
            self.valor_default = str(result)
        except (SyntaxError, ZeroDivisionError):
            # Lidar com erros de syntax ou burrice do usuário
            self.valor_default = "Erro"

        # Retornar o resultado (opcional)
        return self.valor_default

    def get_string(self):
        return self.valor_default
