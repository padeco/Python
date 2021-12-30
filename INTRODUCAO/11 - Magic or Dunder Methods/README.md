Métodos mágicos importantes
As tabelas a seguir listam métodos mágicos importantes no Python 3.

Inicialização e construção	Descrição
__new __ (cls, outro)	Para ser chamado na instanciação de um objeto.
__init __ (self, other)	Para ser chamado pelo método __new__.
__del __ (self)	Método destruidor.
Operadores e funções unários	Descrição
__pos __ (self)	Para ser chamado para positivo unário, por exemplo, + algum objeto.
__neg __ (self)	Para ser chamado para negativo unário, por exemplo, -alguma objeto.
__abs __ (self)	Para ser chamado pela função abs () integrada.
__invert __ (self)	Para ser chamado para inversão usando o operador ~.
__round __ (self, n)	Para ser chamado pela função interna round ().
__floor __ (self)	Para ser chamado pela função interna math.floor ().
__ceil __ (self)	Para ser chamado pela função interna math.ceil ().
__trunc __ (self)	Para ser chamado pela função interna math.trunc ().
Atribuição Aumentada	Descrição
__iadd __ (próprio, outro)	Para ser chamado na adição com atribuição, por exemplo, a + = b.
__isub __ (próprio, outro)	Para ser chamado na subtração com atribuição, por exemplo, a - = b.
__imul __ (próprio, outro)	Para ser chamado na multiplicação com atribuição, por exemplo, a * = b.
__ifloordiv __ (próprio, outro)	Para ser chamado em uma divisão inteira com atribuição, por exemplo, a // = b.
__idiv __ (próprio, outro)	Para ser chamado na divisão com atribuição, por exemplo, a / = b.
__itruediv __ (próprio, outro)	Para ser chamado na verdadeira divisão com atribuição
__imod __ (próprio, outro)	Para ser chamado no módulo com atribuição, por exemplo, a% = b.
__ipow __ (próprio, outro)	Para ser chamado em expoentes com atribuição, por exemplo, a ** = b.
__ilshift __ (self, other)	Para ser chamado no deslocamento bit a bit à esquerda com atribuição, por exemplo, a << = b.
__irshift __ (self, other)	Para ser chamado no deslocamento bit a bit à direita com atribuição, por exemplo, a >> = b.
__iand __ (self, other)	Para ser chamado bit a bit AND com atribuição, por exemplo, a & = b.
__ior __ (próprio, outro)	Para ser chamado em OR bit a bit com atribuição, por exemplo, a | = b.
__ixor __ (próprio, outro)	Para ser chamado no XOR bit a bit com atribuição, por exemplo, a ^ = b.
Métodos de conversão de tipos mágicos	Descrição
__int __ (próprio)	Para ser chamado pelo método int () interno interno para converter um tipo em um int.
__float __ (self)	Para ser chamado pelo método float () interno interno para converter um tipo em float.
__complex __ (self)	Para ser chamado pelo método complex () interno interno para converter um tipo em complexo.
__oct __ (self)	Para ser chamado pelo método oct () interno interno para converter um tipo em octal.
__hex __ (self)	Para ser chamado pelo método hex () interno interno para converter um tipo em hexadecimal.
__index __ (self)	Para ser chamado na conversão de tipo para um int quando o objeto é usado em uma expressão de fatia.
__trunc __ (self)	Para ser chamado a partir do método math.trunc ().
Métodos de String Magic	Descrição
__str __ (self)	Para ser chamado pelo método str () interno interno para retornar uma representação de string de um tipo.
__repr __ (self)	Para ser chamado pelo método repr () interno interno para retornar uma representação legível por máquina de um tipo.
__unicode __ (self)	Para ser chamado pelo método unicode () interno interno para retornar uma string Unicode de um tipo.
__format __ (próprio, formatostr)	Para ser chamado pelo método string.format () interno para retornar um novo estilo de string.
__hash __ (self)	Para ser chamado pelo método hash () interno interno para retornar um inteiro.
__nonzero __ (self)	Para ser chamado pelo método bool () interno interno para retornar True ou False.
__dir __ (self)	Para ser chamado pelo método dir () interno interno para retornar uma lista de atributos de uma classe.
__sizeof __ (self)	Para ser chamado pelo método interno sys.getsizeof () para retornar o tamanho de um objeto.
Métodos mágicos de atributos	Descrição
__getattr __ (próprio, nome)	É chamado ao acessar o atributo de uma classe que não existe.
__setattr __ (self, name, value)	É chamado ao atribuir um valor ao atributo de uma classe.
__delattr __ (próprio, nome)	É chamado ao excluir um atributo de uma classe.
Métodos de magia do operador	Descrição
__add __ (próprio, outro)	Para ser chamado na operação de adição usando o operador +
__sub __ (próprio, outro)	Para ser chamado na operação de subtração usando o operador -.
__mul __ (próprio, outro)	Para ser chamado na operação de multiplicação usando o operador *.
__floordiv __ (próprio, outro)	Para ser chamado na operação de divisão do andar usando // operador.
__truediv __ (próprio, outro)	Para ser chamado na operação de divisão usando / operator.
__mod __ (próprio, outro)	Para ser chamado na operação de módulo usando o operador%.
__pow __ (self, other [, modulo])	Ser chamado para calcular a potência usando o operador **.
__lt __ (próprio, outro)	Para ser chamado na comparação usando o operador <.
__le __ (próprio, outro)	Para ser chamado na comparação usando o operador <=.
__eq __ (próprio, outro)	Para ser chamado na comparação usando o operador ==.
__ne __ (self, other)	Para ser chamado na comparação usando o operador! =.
__ge __ (próprio, outro)	Para ser chamado na comparação usando o operador> =.