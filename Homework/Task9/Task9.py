def deleting_repeating_rows(arr):
    for i in range(len(arr)):
        arr[i] = list(dict.fromkeys(arr[i]))
    return arr


def final_clearing(no_null_arr):
    answer = []
    # Разбиение на &
    arr_no_amp = []
    tn = []
    date = []
    numbers = []
    for i in range(len(no_null_arr)):
        numbers.append(str(round(float(no_null_arr[i][0].split('&')[0]), 2)))
        no_yes = no_null_arr[i][0].split('&')[1]
        if no_yes == 'нет':
            arr_no_amp.append('N')
        else:
            arr_no_amp.append('Y')
        tn.append(no_null_arr[i][1].replace(' ', ''))
        date.append(no_null_arr[i][2])
    for i in range(len(date)):
        date[i] = date[i].split('-')[2] + '/' \
                  + date[i].split('-')[1] + '/' \
                  + date[i].split('-')[0]
    for i in range(len(numbers)):
        if len(numbers[i]) == 3:
            numbers[i] = numbers[i] + '0'
    t = [numbers, tn, arr_no_amp, date]
    for i in range(len(numbers)):
        answer.append([t[0][i], t[1][i], t[2][i], t[3][i]])
    return answer


def main(s):
    clear_arr = []
    # Удаление повторяющихся строк
    for i in range(len(s)):
        if s[i] in clear_arr:
            pass
        else:
            clear_arr.append(s[i])
    # Удаление повторяющихся столбцов?
    clear_arr = deleting_repeating_rows(clear_arr)
    # Удаление пустых строк
    no_null_arr = []
    for i in range(len(clear_arr)):
        k = 0
        for j in range(len(clear_arr[i])):
            if clear_arr[i][j] is None:
                k += 1
        if k != len(clear_arr[i]):
            no_null_arr.append(clear_arr[i])
    answer = final_clearing(no_null_arr)
    return answer
