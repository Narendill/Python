# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

__all__ = ['mult']


def mult(file_nums: str, file_names: str, file_result: str) -> None:
    """Функция перемножает 2 числа сохраняет результат согласно алгоритму в файл."""
    with (
        open(file_nums, 'r', encoding='utf-8') as f1,
        open(file_names, 'r', encoding='utf-8') as f2,
        open(file_result, 'w', encoding='utf-8') as f3
    ):
        f1, f2 = list(f1), list(f2)
        # Переменные для понимания того, закончилились ли в меньшем файле строки:
        index_f1 = 0
        index_f2 = 0

        # Переделать в функцию?
        if len(f1) >= len(f2):
            for i in range(len(f1)):
                if index_f2 >= len(f2):
                    index_f2 = 0
                a, b = f1[i].replace('\n', '').split('|')

                if float(a) * float(b) < 0:
                    print(f2[index_f2][:-1].lower(), abs(float(a) * float(b)), file=f3)
                else:
                    print(f2[index_f2][:-1].upper(), round(float(a) * float(b)), file=f3)
                index_f2 += 1
        else:
            for i in range(len(f2)):
                if index_f1 >= len(f1):
                    index_f1 = 0
                a, b = f1[index_f1].replace('\n', '').split('|')

                if float(a) * float(b) < 0:
                    print(f2[i][:-1].lower(), abs(float(a) * float(b)), file=f3)
                else:
                    print(f2[i][:-1].upper(), round(float(a) * float(b)), file=f3)
                index_f1 += 1


if __name__ == '__main__':
    mult('numbers.txt', 'usernames.txt', 'result.txt')