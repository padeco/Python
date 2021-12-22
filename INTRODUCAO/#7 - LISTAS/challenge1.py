import random

suits = ["Copas", "Espadas", "Ouro", "Paus"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Reis", "As"]
deck = []

for  suit in suits:# aqui ele cria uma carta de cada, 
  for rank in ranks:
    deck.append(f'{rank} de {suit}')

print(f'Tem {len(deck)} cartas no seu baralho.')

print('Distribuindo ...')

hand = []

while len(hand) < 5:
    card = random.choice(deck)
    deck.remove(card)
    hand.append(card)

print(f'Tem {len(deck)} cartas no seu baralho.')
print('As Cartas que o jogador tem na mão:')
print(hand)