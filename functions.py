import ast

class Botoes:
    def __init__(self):
        self.valor_default = ""
        self.bloqueado = False

    def clear(self):
        self.valor_default = ""
        self.desbloquear()

    def bloquear(self):
        self.bloqueado = True

    def desbloquear(self):
        self.bloqueado = False

    def add_zero(self):
        if not self.bloqueado:
            self.valor_default += "0"

    def add_um(self):
        if not self.bloqueado:
            self.valor_default += "1"

    def add_dois(self):
        if not self.bloqueado:
            self.valor_default += "2"

    def add_tres(self):
        if not self.bloqueado:
            self.valor_default += "3"

    def add_quatro(self):
        if not self.bloqueado:
            self.valor_default += "4"

    def add_cinco(self):
        if not self.bloqueado:
            self.valor_default += "5"

    def add_seis(self):
        if not self.bloqueado:
            self.valor_default += "6"

    def add_sete(self):
        if not self.bloqueado:
            self.valor_default += "7"

    def add_oito(self):
        if not self.bloqueado:
            self.valor_default += "8"

    def add_nove(self):
        if not self.bloqueado:
            self.valor_default += "9"

    def add_operador(self, operador):
        if not self.bloqueado:
            if self.valor_default and self.valor_default[-1] == ")":
                return
            if self.valor_default and self.valor_default[-1] in "+-*/.":
                return
            if not self.valor_default:
                return

            self.valor_default += operador

    def add_ponto_decimal(self):
        if not self.bloqueado:
            if not self.valor_default:
                self.valor_default += "0."  
            elif self.valor_default[-1] in "+-*/":
                self.valor_default += "0."  
            else:  
                self.valor_default += "."

    def add_mais(self):
        if not self.bloqueado:
            self.add_operador("+")
    
    def add_menos(self):
        if not self.bloqueado:
            self.add_operador("-")
    
    def add_mult(self):
        if not self.bloqueado:
            self.add_operador("*")
    
    def add_div(self):
        if not self.bloqueado:
            self.add_operador("/")

    def evaluate(self):
        try:
            if self.bloqueado:
                return "Erro" 
            ast.parse(self.valor_default)
            result = eval(self.valor_default)
            result = round(result, 3)
            
            self.valor_default = str(result)
        except (SyntaxError, ZeroDivisionError):
            # Lidar com erros de syntax ou inputs inválidos
            self.valor_default = "Erro"
        finally:
            self.bloquear() 
        return self.valor_default

    def get_string(self):
        return self.valor_default