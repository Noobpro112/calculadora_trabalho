import ast
import math
from typing import Optional, Union


class Botoes:
    def __init__(self):
        self._display = ""
        self._bloqueado = False
        self._memory: Optional[float] = None
        self._last_value: Optional[float] = None

    @property
    def display(self) -> str:
        return self._display

    def clear(self) -> None:
        self._display = ""
        self._desbloquear()

    def _bloquear(self) -> None:
        self._bloqueado = True

    def _desbloquear(self) -> None:
        self._bloqueado = False

    def _adicionar_digito(self, digito: str) -> None:
        if self._bloqueado:
            return
        
        if self._display == "0":
            self._display = digito 
        else:
            self._display += digito 

    def _adicionar_operador(self, operador: str) -> None:
        if self._bloqueado:
            return
        if not self._display:
            return  
        if self._display[-1] in "+-*/.)]}" or self._display.endswith(('sin(', 'cos(', 'tan(')):
            return
        self._display += operador

    def _adicionar_funcao(self, funcao: str) -> None:
        if not self._bloqueado:
            self._display += funcao

    def _calcular_funcao(self, funcao: callable) -> None:
        if not self._bloqueado and self._display:
            try:
                resultado = funcao(float(self._display))
                self._display = f"{round(resultado, 8):g}"
            except (ValueError, ZeroDivisionError):
                self._display = "Erro"
                self._bloquear()

    def get_string(self) -> str:
        return self.display

    def backspace(self) -> None:
        if self._bloqueado:
            return
        
        if not self._display or self._display == "0":
            self._display = "0"
            return
        
        self._display = self._display[:-1]
        if not self._display:
            self._display = "0"

    # Métodos para dígitos
    def add_zero(self) -> None: self._adicionar_digito("0")
    def add_um(self) -> None: self._adicionar_digito("1")
    def add_dois(self) -> None: self._adicionar_digito("2")
    def add_tres(self) -> None: self._adicionar_digito("3")
    def add_quatro(self) -> None: self._adicionar_digito("4")
    def add_cinco(self) -> None: self._adicionar_digito("5")
    def add_seis(self) -> None: self._adicionar_digito("6")
    def add_sete(self) -> None: self._adicionar_digito("7")
    def add_oito(self) -> None: self._adicionar_digito("8")
    def add_nove(self) -> None: self._adicionar_digito("9")

    # Métodos para operadores
    def add_mais(self) -> None: self._adicionar_operador("+")
    def add_menos(self) -> None: self._adicionar_operador("-")
    def add_mult(self) -> None: self._adicionar_operador("*")
    def add_div(self) -> None: self._adicionar_operador("/")

    # Métodos para pontuação e símbolos
    def add_ponto_decimal(self) -> None:
        if self._bloqueado:
            return
        if not self._display:
            self._display = "0."
        elif self._display[-1] in "+-*/":
            self._display += "0."
        else:
            self._display += "."

    # Métodos para parênteses, colchetes e chaves
    def abrir_parenteses(self) -> None: self._adicionar_funcao("(")
    def fechar_parenteses(self) -> None: self._adicionar_funcao(")")
    def abrir_colchetes(self) -> None: self._adicionar_funcao("[")
    def fechar_colchetes(self) -> None: self._adicionar_funcao("]")
    def abrir_chaves(self) -> None: self._adicionar_funcao("{")
    def fechar_chaves(self) -> None: self._adicionar_funcao("}")

    # Funções de memória
    def memory_clear(self) -> None:
        if not self._bloqueado:
            self._memory = None

    def memory_add(self) -> None:
        if not self._bloqueado and self._display:
            try:
                valor = float(self._display)
                self._memory = valor if self._memory is None else self._memory + valor
            except ValueError:
                pass

    def memory_subtract(self) -> None:
        if not self._bloqueado and self._display:
            try:
                valor = float(self._display)
                self._memory = -valor if self._memory is None else self._memory - valor
            except ValueError:
                pass

    def memory_recall(self) -> None:
        if not self._bloqueado and self._memory is not None:
            self._display = str(self._memory)
            self._desbloquear()

    # Funções matemáticas
    def calcular_seno(self) -> None: self._calcular_funcao(math.sin)
    def calcular_cosseno(self) -> None: self._calcular_funcao(math.cos)
    def calcular_tangente(self) -> None: self._calcular_funcao(math.tan)

    def calcular_potencia(self) -> None:
        if not self._bloqueado:
            if '^' in self._display:
                try:
                    base, expoente = self._display.split('^')
                    resultado = float(base) ** float(expoente)
                    self._display = f"{round(resultado, 8):g}"
                except (ValueError, SyntaxError):
                    self._display = "Erro"
                    self._bloquear()
            else:
                self._display += '^'
                self._desbloquear()

    def calcular_raiz_quadrada(self) -> None:
        if not self._bloqueado and self._display:
            try:
                valor = float(self._display)
                if valor < 0:
                    self._display = "Erro"
                    self._bloquear()
                else:
                    resultado = math.sqrt(valor)
                    self._display = f"{round(resultado, 8):g}"
            except ValueError:
                self._display = "Erro"
                self._bloquear()

    def calcular_fatorial(self) -> None:
        if not self._bloqueado and self._display:
            try:
                if self._display.endswith('!'):
                    return

                num = float(self._display)
                if num.is_integer() and num >= 0:
                    resultado = math.factorial(int(num))
                    self._display = str(resultado)
                else:
                    self._display = "Erro"
                    self._bloquear()
            except ValueError:
                self._display += '!'
            except OverflowError:
                self._display = "Erro (mt grande)"
                self._bloquear()

    def adicionar_constante_e(self) -> None:
        if not self._bloqueado:
            self._display = str(math.e)
            self._desbloquear()

    def evaluate(self) -> str:
        try:
            if self._bloqueado:
                return "Erro"

            ast.parse(self._display)
            resultado = eval(self._display)
            resultado = round(resultado, 3)
            
            self._display = f"{resultado:g}"
            return self._display
        except (SyntaxError, ZeroDivisionError):
            self._display = "Erro"
            return self._display
        finally:
            self._bloquear()

    # Aliases para os botões
    MC = memory_clear
    M_plus = memory_add
    M_minus = memory_subtract
    MR = memory_recall
    sin = calcular_seno
    cos = calcular_cosseno
    tan = calcular_tangente
    x_power_y = calcular_potencia
    xi = calcular_fatorial
    e = adicionar_constante_e