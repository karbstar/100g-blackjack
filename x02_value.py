#!python3

def value(hand):
  '''
  input:
  list hand: hand is a list of strings that contains the cards in the hand
  eg: ['AH','3D','4S']
  
  return:
  int the total value of the hand
  may return a list if the hand contains an Ace
  eg:
  '''
  #['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AC', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD', 'AD', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH', 'AH', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS', 'AS']
  #suits = ['C','D','H','S']
  bonus=False
  giv=0
  for x in hand:
    intt=True
    y=(x[1])
    x=x.replace(y,'')
    print(x)
    try:
      x=int(x)
    except:
      intt=False
    if intt ==True:
      x=int(x)
      giv=giv+x
    if intt==False:
      giv=giv+10
    if x=='A':
      bonus=True
      giv=giv+1
    print(giv)
  if bonus==True:
    giv2=giv-10
    print([giv,giv2])
    return [giv2,giv]
   
  return giv


def main():
  assert value(['AH','3D','4S']) ==[8,18]
  assert value(['KH','TD']) == 20
  assert value(['3D','8H']) == 11
  assert value(['KC','6S','QD']) == 26

#if __name__ == "__name__":
main()
