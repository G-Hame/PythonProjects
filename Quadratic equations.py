# Вводим коэффиценты
a = float(input("Введите коэффицент a (перед x^2): "))
b = float(input("Введите коэффицент b (перед x): "))
c = float(input("Введите коэффицент c: "))
# Определяем дискриминант
dis = (b ** 2) - (4 * a * c)

if int(a) == 0:
    exit("Коэффицент `а` не может быть равен нулю!")
    # В зависимости от дискриминанта, решаем
if b * b > 4 * a * c:
    print("Два корня:")
    print((dis ** 0.5 + (-1 * b)) / (2 * a))
    print((dis ** 0.5 - (-1 * b)) / (2 * a))
elif b * b == 4 * a * c:
    print("Один корень:")
    print(-1 * b / (2 * a))
else:
    print("Корней нет.")
