#!python3

"""
Create a list of cards
the cards should be denoted with a number or A, J, Q, K, T (for ace, jack, queen, king or ten)
as well as a suit
"""

def createDeck():
  ranks = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
  suits = ['C','D','H','S']
  r1=suits[0]
  r2=suits[1]
  r3=suits[2]
  r4=suits[3]
  set1=[x+r1 for x in ranks]
  set2=[x+r2 for x in ranks]
  set3=[x+r3 for x in ranks]
  set4=[x+r4 for x in ranks]
  deck = set1+set2+set3+set4
  print(deck)
  return deck
  
  '''
  use the two lists to create a new list "deck" 
  return the deck list to your calling function
  '''

def main():
  deck = createDeck()
  assert "JH" in deck 
  assert "AC" in deck 
  assert "TD" in deck 
  assert len(deck) == 52
  
if __name__ == "__main__":
  main()
