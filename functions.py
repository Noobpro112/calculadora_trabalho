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
        if not self._bloqueado:
            self._display += digito

    def add_zero(self) -> None:
        self._adicionar_digito("0")

    def add_um(self) -> None:
        self._adicionar_digito("1")

    def add_dois(self) -> None:
        self._adicionar_digito("2")

    def add_tres(self) -> None:
        self._adicionar_digito("3")

    def add_quatro(self) -> None:
        self._adicionar_digito("4")

    def add_cinco(self) -> None:
        self._adicionar_digito("5")

    def add_seis(self) -> None:
        self._adicionar_digito("6")

    def add_sete(self) -> None:
        self._adicionar_digito("7")

    def add_oito(self) -> None:
        self._adicionar_digito("8")

    def add_nove(self) -> None:
        self._adicionar_digito("9")

    def add_operador(self, operador: str) -> None:
        if self._bloqueado:
            return

        if not self._display:
            return

        last_char = self._display[-1]
        if last_char in "+-*/." or last_char == ")":
            return

        self._display += operador

    def add_ponto_decimal(self) -> None:
        if self._bloqueado:
            return

        if not self._display:
            self._display = "0."
        elif self._display[-1] in "+-*/":
            self._display += "0."
        else:
            self._display += "."

    def add_mais(self) -> None:
        self.add_operador("+")

    def add_menos(self) -> None:
        self.add_operador("-")

    def add_mult(self) -> None:
        self.add_operador("*")

    def add_div(self) -> None:
        self.add_operador("/")

          # ---------- AS FUNÇÕES NOVAS DESSA MERDA PQP NUNCA MAIS----------

    def abrir_parenteses(self) -> None:
        if not self._bloqueado:
            self._display += "("

    def fechar_parenteses(self) -> None:
        if not self._bloqueado:
            self._display += ")"

    def abrir_colchetes(self):
        if not self.bloqueado:
            self.valor_default += "["

    def fechar_colchetes(self):
        if not self.bloqueado:
            self.valor_default += "]"

    def abrir_chaves(self):
        if not self.bloqueado:
            self.valor_default += "{"

    def fechar_chaves(self):
        if not self.bloqueado:
            self.valor_default += "}"


    # Funções de memória
    def memory_clear(self) -> None:
        """Limpa a memória da calculadora(Amém deepseek)."""
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

    def calcular_cosseno(self) -> None:
        if not self._bloqueado and self._display:
            try:
                resultado = math.cos(float(self._display))
                self._display = f"{round(resultado, 8):g}"
            except ValueError:
                pass

    def calcular_tangente(self) -> None:
        if not self._bloqueado and self._display:
            try:
                resultado = math.tan(float(self._display))
                self._display = f"{round(resultado, 8):g}"
            except ValueError:
                pass

    def calcular_seno(self) -> None:
        if not self._bloqueado and self._display:
            try:
                resultado = math.sin(float(self._display))
                self._display = f"{round(resultado, 8):g}"
            except ValueError:
                pass

    def calcular_potencia(self) -> None:
        if not self._bloqueado and self._display:
            try:
                if '^' in self._display:
                    base, expoente = self._display.split('^')
                    resultado = float(base) ** float(expoente)
                    self._display = f"{round(resultado, 8):g}"
                else:
                    self._display += '^'
                    self._desbloquear()
            except (ValueError, SyntaxError):
                self._display = "Erro"
                self._bloquear()

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

    MC = memory_clear
    M_plus = memory_add
    M_minus = memory_subtract
    MR = memory_recall
    cos = calcular_cosseno
    tan = calcular_tangente
    sin = calcular_seno
    x_power_y = calcular_potencia
    xi = calcular_fatorial
    e = adicionar_constante_e
    get_string = display