import random
from mimesis import Person
from collections import Counter
from collections import OrderedDict


def task6_1():
    x = int(input())
    array1 = ["Коллеги, ", "В то же время, ", "Однако, ", "Тем не менее, ", "Следовательно, ", "Соответственно, ",
              "Вместе с тем, ", "С другой стороны,"]
    array2 = ["парадигма цифровой экономики ", "контекст цифровой трансформации ", "диджитализация бизнес-процессов ",
              "прагматичный подход к цифровым платформам ", "совокупность сквозных технологий ",
              "программа прорывных исследований	", "ускорение блокчейн-транзакций ",
              "экспоненциальный рост Big Data "]
    array3 = ["открывает новые возможности для ", "выдвигает новые требования ", "несёт в себе риски ",
              "расширяет горизонты ", "заставляет искать варианты ", "не оставляет шанса для	",
              "повышает вероятность ", "обостряет проблему	"]
    array4 = ["дальнейшего углубления ", "бюджетного финансирования	", "синергетического эффекта ", "компрометации "
                                                                                                       "конфиденциальных",
              "универсальной коммодитизации ", "несанкционированной кастомизации ", "нормативного регулирования ",
              "практического применения "]
    array5 = ["знаний и компетенций.", "непроверенных гипотез.", "волатильных активов.", "опасных экспериментов.",
              "государственно-частных партнёрств.", "цифровых следов граждан.", "нежелательных последствий.",
              "внезапных открытий."]
    print(
        f'{array1[0]}{array2[random.randint(0, 6)]}{array3[random.randint(0, 6)]}{array4[random.randint(0, 6)]}{array5[random.randint(0, 6)]}')
    for i in range(x):
        print(
            f'{array1[random.randint(1, 6)]}{array2[random.randint(0, 6)]}{array3[random.randint(0, 6)]}{array4[random.randint(0, 6)]}{array5[random.randint(0, 6)]}')


def task6_2():
    arr = int(input('Введите количество слов, с помощью которых будет генерироваться сообщение:\n'))
    quantity = int(input('Введите сколько слов в каждом массиве (ОБЯЗАТЕЛЬНО МЕНЬШЕ ПРЕДЫДУЩЕГО ЗНАЧЕНИЯ):\n'))
    if arr % quantity != 0:
        print("BYE ")
        return
    array = []
    print('Начинайте вводить слова:\n')
    droblenye = arr // quantity
    for i in range(arr):
        array.append(input())
    print(array)
    for i in range(1):
        final = []
        k = 1
        for j in range(quantity):
            final.append(array[random.randint(j * droblenye, (((j + 1) * droblenye) - 1))])
            k += 1
        print(*final)


def task6_3():
    person = Person('ru')
    for _ in range(0, 15):
        print(person.full_name())


def main(s, k):
    d = {}
    newarr = []
    arr = []
    for i in range(len(s) - (k - 1)):
        newarr.append(s[i:i + k])
    # print("Строка", s)
    # print(newarr)
    for i in range(len(newarr) - 1):
        arr.append(s[k + i])
    for i in range(len(newarr) - 1):
        d[newarr[i]] = d.get(newarr[i], []) + [arr[i]]
    cleararr = list(OrderedDict.fromkeys(newarr))
    # print(arr)
    for i in range(len(cleararr)):
        f = d.get(cleararr[i])
        d[cleararr[i]] = dict(Counter(f))
    # print(d)
    lenofm = 500
    first = cleararr[random.randint(0, len(d) - 1)]
    finstr = ''
    # print('FIRST:', first)
    tempdict = d.get(first)

    arrayofkeys = list(tempdict.keys())
    finstr += first + arrayofkeys[random.randint(0, len(arrayofkeys) - 1)]
    for i in range(lenofm):
        # Для двух: i+1; i+3
        first = finstr[i + 1:i + k + 1]
        tempdict = d.get(first)
        arrayofkeys = list(tempdict.keys())
        finstr += arrayofkeys[random.randint(0, len(arrayofkeys) - 1)]
    print(finstr)


if __name__ == '__main__':
    # task6_1()
    # task6_2()
    # task6_3()
    hugestr = '''Буря мглою небо кроет,
Вихри снежные крутя;
То, как зверь, она завоет,
То заплачет, как дитя,
То по кровле обветшалой
Вдруг соломой зашумит,
То, как путник запоздалый,
К нам в окошко застучит.

Наша ветхая лачужка
И печальна и темна.
Что же ты, моя старушка,
Приумолкла у окна?
Или бури завываньем
Ты, мой друг, утомлена,
Или дремлешь под жужжаньем
Своего веретена?

Выпьем, добрая подружка
Бедной юности моей,
Выпьем с горя; где же кружка?
Сердцу будет веселей.
Спой мне песню, как синица
Тихо за морем жила;
Спой мне песню, как девица
За водой поутру шла.

Буря мглою небо кроет,
Вихри снежные крутя;
То, как зверь, она завоет,
То заплачет, как дитя.
Выпьем, добрая подружка
Бедной юности моей,
Выпьем с горя: где же кружка?
Сердцу будет веселей.'''
    main(hugestr, 2)
