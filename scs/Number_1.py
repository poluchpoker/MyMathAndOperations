class MyMath:
  a = int()
  b = int()

  def __init__(self, a, b):
    self.a = a
    self.b = b

  def add(self):
    print('Сложение:')
    if float(self.a) + float(self.b) != int(float(self.a) + float(self.b)):
      print('a + b =', float(self.a) + float(self.b))
    else:
      print('a + b =', int(float(self.a) + float(self.b)))

  def multi(self):
    print('Умножение:')
    if float(self.a) * float(self.b) != int(float(self.a) * float(self.b)):
      print('a * b =', float(self.a) * float(self.b))
    else:
      print('a * b = ', int(float(self.a) * float(self.b)))

  def div(self):
    print('Деление:')
    if float(self.a) / float(self.b) != int(float(self.a) / float(self.b)):
      print('a / b =', float(self.a) / float(self.b))
    else:
      print('a // b =', int(float(self.a) / float(self.b)))

  def sub(self):
    print('Вычитание:')
    if float(self.a) - float(self.b) >= int(float(self.a) - float(self.b)):
      print('a - b =', int(float(self.a) - float(self.b)))
    else:
      print('a - b =', float(self.a) - float(self.b))

  def pow(self):
    print('Возведение в степень:')
    if float(self.a) ** float(self.b) != int(float(self.a) ** float(self.b)):
      print('a ** b =', float(self.a) ** float(self.b))
    else:
      print('a ** b =', int(float(self.a) ** float(self.b)))

  def sqrt(self):
    print('Корень числа a:')
    if float(self.a) ** (1 / 2) != int(float(self.a) ** (1 / 2)):
      print('sqrt(a) =', float(self.a) ** (1 / 2))
    else:
      print('sqrt(a) =', int(float(self.a) ** (1 / 2)))

print('Введите числа a и b на отдельных строках:')

first_meaning = input()
second_meaning = input()

result = MyMath(first_meaning, second_meaning)

result.add()
result.multi()
try:
  result.div()
except ZeroDivisionError:
  print('Делить на нуль нельзя')
result.sub()
result.pow()
try:
  result.sqrt()
except TypeError:
  print('Извлекать корень из отрицательного числа нельзя')
