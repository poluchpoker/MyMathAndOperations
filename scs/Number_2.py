class Sort:
  def __init__(self, list, n):
    self.list = list
    self.n = n

  def bubble(self):
    for i in range(self.n - 1):
      for j in range(self.n - i - 1):
        if self.list[j] > self.list[j + 1]:
          self.list[j], self.list[j + 1] = self.list[j + 1], self.list[j]
    print(self.list, '-Вы использовали метод сортировки пузырьком')

  def choice(self):
    for i in range(self.n - 1):
      k = i
      for j in range(i + 1, self.n):
        if self.list[j] < self.list[k]:
          k = j
      self.list[i], self.list[k] = self.list[k], self.list[i]
    print(self.list, '-Вы использовали метод сортировки выбором')


list = []
n = len(list)

print('Введите количество чисел, которые должны присутстовать в списке:')
b = int(input())
print('Введите числа:')

while n < b:
  list.append(int(input()))
  n = len(list)


result = Sort(list, n)

print('Выберите метод сортировки: Пузырьком(1) или Выбором(2)')
command = input()

while True:
  if command == 'Пузырьком' or int(command) == 1:
    result.bubble()
    break
  elif command == 'Выбором' or int(command) == 2:
    result.choice()
    break
  elif command != 'Выбором' or command != 'Пузырьком' or int(command) == 1 or int(command) == 2:
    print('Вы ошиблись в написании метода сортировки или нажали не ту цифру.')
    command = input()
    continue
