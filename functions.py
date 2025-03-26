import ast
import math
from typing import Optional, Union


class Calculadora:
    """Classe que gerencia as operações matemáticas e estado da calculadora."""

    def __init__(self):
        """Inicializa a calculadora com valores padrão."""
        self._display = ""
        self._bloqueado = False
        self._memory: Optional[float] = None
        self._last_value: Optional[float] = None

    @property
    def display(self) -> str:
        """Retorna o valor atual do display."""
        return self._display

    def clear(self) -> None:
        """Limpa o display e desbloqueia a calculadora."""
        self._display = ""
        self._desbloquear()

    def _bloquear(self) -> None:
        """Bloqueia a calculadora para novas entradas."""
        self._bloqueado = True

    def _desbloquear(self) -> None:
        """Desbloqueia a calculadora para novas entradas."""
        self._bloqueado = False

    def _adicionar_digito(self, digito: str) -> None:
        """Adiciona um dígito ao display se a calculadora não estiver bloqueada."""
        if not self._bloqueado:
            self._display += digito

    def add_zero(self) -> None:
        """Adiciona o dígito 0 ao display."""
        self._adicionar_digito("0")

    def add_um(self) -> None:
        """Adiciona o dígito 1 ao display."""
        self._adicionar_digito("1")

    def add_dois(self) -> None:
        """Adiciona o dígito 2 ao display."""
        self._adicionar_digito("2")

    def add_tres(self) -> None:
        """Adiciona o dígito 3 ao display."""
        self._adicionar_digito("3")

    def add_quatro(self) -> None:
        """Adiciona o dígito 4 ao display."""
        self._adicionar_digito("4")

    def add_cinco(self) -> None:
        """Adiciona o dígito 5 ao display."""
        self._adicionar_digito("5")

    def add_seis(self) -> None:
        """Adiciona o dígito 6 ao display."""
        self._adicionar_digito("6")

    def add_sete(self) -> None:
        """Adiciona o dígito 7 ao display."""
        self._adicionar_digito("7")

    def add_oito(self) -> None:
        """Adiciona o dígito 8 ao display."""
        self._adicionar_digito("8")

    def add_nove(self) -> None:
        """Adiciona o dígito 9 ao display."""
        self._adicionar_digito("9")

    def add_operador(self, operador: str) -> None:
        """Adiciona um operador matemático ao display se for válido."""
        if self._bloqueado:
            return

        if not self._display:
            return

        last_char = self._display[-1]
        if last_char in "+-*/." or last_char == ")":
            return

        self._display += operador

    def add_ponto_decimal(self) -> None:
        """Adiciona um ponto decimal ao display."""
        if self._bloqueado:
            return

        if not self._display:
            self._display = "0."
        elif self._display[-1] in "+-*/":
            self._display += "0."
        else:
            self._display += "."

    def add_mais(self) -> None:
        """Adiciona o operador de adição."""
        self.add_operador("+")

    def add_menos(self) -> None:
        """Adiciona o operador de subtração."""
        self.add_operador("-")

    def add_mult(self) -> None:
        """Adiciona o operador de multiplicação."""
        self.add_operador("*")

    def add_div(self) -> None:
        """Adiciona o operador de divisão."""
        self.add_operador("/")

          # ---------- AS FUNÇÕES NOVAS DESSA MERDA PQP NUNCA MAIS----------

    def abrir_parenteses(self) -> None:
        """Adiciona um parêntese de abertura ao display."""
        if not self._bloqueado:
            self._display += "("

    def fechar_parenteses(self) -> None:
        """Adiciona um parêntese de fechamento ao display."""
        if not self._bloqueado:
            self._display += ")"

    # Funções de memória
    def memory_clear(self) -> None:
        """Limpa a memória da calculadora."""
        if not self._bloqueado:
            self._memory = None

    def memory_add(self) -> None:
        """Adiciona o valor atual à memória."""
        if not self._bloqueado and self._display:
            try:
                valor = float(self._display)
                self._memory = valor if self._memory is None else self._memory + valor
            except ValueError:
                pass

    def memory_subtract(self) -> None:
        """Subtrai o valor atual da memória."""
        if not self._bloqueado and self._display:
            try:
                valor = float(self._display)
                self._memory = -valor if self._memory is None else self._memory - valor
            except ValueError:
                pass

    def memory_recall(self) -> None:
        """Recupera o valor armazenado na memória."""
        if not self._bloqueado and self._memory is not None:
            self._display = str(self._memory)
            self._desbloquear()

    # Funções matemáticas
    def calcular_cosseno(self) -> None:
        """Calcula o cosseno do valor atual (em radianos)."""
        if not self._bloqueado and self._display:
            try:
                resultado = math.cos(float(self._display))
                self._display = f"{round(resultado, 8):g}"
            except ValueError:
                pass

    def calcular_tangente(self) -> None:
        """Calcula a tangente do valor atual (em radianos)."""
        if not self._bloqueado and self._display:
            try:
                resultado = math.tan(float(self._display))
                self._display = f"{round(resultado, 8):g}"
            except ValueError:
                pass

    def calcular_seno(self) -> None:
        """Calcula o seno do valor atual (em radianos)."""
        if not self._bloqueado and self._display:
            try:
                resultado = math.sin(float(self._display))
                self._display = f"{round(resultado, 8):g}"
            except ValueError:
                pass

    def calcular_potencia(self) -> None:
        """Calcula a potência x elevado a y."""
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
        """Calcula a raiz quadrada do valor atual."""
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
        """Calcula o fatorial do valor atual ou adiciona operador fatorial."""
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
        """Adiciona a constante de Euler (e) ao display."""
        if not self._bloqueado:
            self._display = str(math.e)
            self._desbloquear()

    def evaluate(self) -> str:
        """Avalia a expressão matemática no display."""
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

    # Aliases para compatibilidade
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