high = 0
low = 0

def half(amount,ans):
  global high
  global low
  if ans == 'more':
    if low < amount:
      low = amount
    return  low + ((high - low)/2)
  if ans == 'less':
    if high > amount:
      high = amount
    return high - ((high - low)/2)
  else:
    print('does not compute, use more or less')
    return amount
 
def maxAmount(num):
  if num <= 2:
    return 1
  else:
    return 1 + maxAmount(int(num / 2))

def run(amount):
  if maxAmount((high - low)) == 1:
    print('The number is ',amount)
  else:
    print(amount,': is the number more or less? ')
    ans = input()
    run(int(half(amount,ans)))

def start():
  global high
  print('enter number: ')
  high = int(input()) + 1
  print('You will find the number in',str(maxAmount(high)),'tries or less')
  num = high / 2
  run(int(num))

start()
