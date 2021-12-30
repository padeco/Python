'''Localizar objetos, dados e comportamento
Você encontra os diferentes artefatos do seu sistema fazendo perguntas como:
•	Quem interage com quem?
•	Quem faz o quê com quem?

1.	O serviço de email entrega uma fatura para o sistema.
2.	A fatura é classificada por um código de referência o manualmente por um classificador para ir para o departamento correto.
3.	A fatura é aprovada ou rejeitada por um aprovador com base em fatores como, por exemplo, exatidão e tamanho do valor.
4.	A fatura é paga por um processador de pagamentos usando as informações de pagamento fornecidas.

Agora você pode extrair objetos, dados e o comportamento das frases e organizá-los em uma tabela, 
desta forma:

Fase	        Ator	                        Comportamento	            Dados
Entrada	        Serviço de email	            Entrega	                    Fatura
Entrada	        Sistema	                        Recebe	                    Fatura
Processando	    Classificadores ou sistema	    Classifica ou encaminha	    Fatura (código de referência)
Processando	    Aprovador	                    Aprova ou rejeita	        Fatura (valor)
Saída	        Processador de pagamentos	    Paga	                    Fatura (informações do pagamento)


'''