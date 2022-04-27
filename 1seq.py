elem = int(input('Введите количество элементов: '))
Numbers = []
for i in range(0, elem):
    Numbers.append(input('Введите число: '))
for i in range(0, elem):
    print(Numbers[i])
print()
Numbers.sort()
for i in range(0, elem):
    print(Numbers[i])
print()
Numbers # ВОПРОС: не могу понять, почему вызов списка таким образом как в этой строке, не выводит список на экран в PyCharm?
        # Но при этом выводит его нормально в колабе.


