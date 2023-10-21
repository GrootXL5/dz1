def evn():
  if number % 2 == 0:
    print(True)
  else:
    print(False)
number = int(input('Enter number:'))
evn()
def vvl(s):
  snd = 'eaiou'
  cnt = 0
  for i in snd:
    cnt += s.lower().count(i)
  print(cnt)
s = input('Enter line:')
def fact(n):
  f = 1
  while n > 1:
    f *= n
    n -= 1
  return f
n = int(input('Enter number:'))
print(fact(n))
