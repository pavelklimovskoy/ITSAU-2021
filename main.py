import matplotlib.pyplot as plt
import numpy as np
import math


# функция для расчета плотности точек
def kde_quartic(d, h):
    dn = d / h
    P = (15/16) * (1 - dn ** 2) ** 2
    return P

f = open('input.txt', 'r')

# создадим два списка случайных чисел от 14 до 40
#x = np.random.randint(14, 41, 24)
# создадим два списка случайных чисел от 15 до 50
#y = np.random.randint(15, 51, 24)

x = f.readline().replace('\n', '').split(' ')
y = f.readline().replace('\n', '').split(' ')


for i in range(len(x)):
    x[i] = int(x[i])

for i in range(len(y)):
    y[i] = int(y[i])

print(x, y)

# отобразим получившиеся точки на графике
fig, ax = plt.subplots()
ax.scatter(x, y)
ax.set_title('Тепловая карта')
plt.show()

# определяем размер и радиус сетки (h)
grid_size = 10
h = 200

# получение min, max для x и y
# x_min = min(x)
# x_max = max(x)
# y_min = min(y)
# y_max = max(y)
# строим сетку
x_grid = np.arange (0, 2048, grid_size)
y_grid = np.arange (0, 2048, grid_size)
x_mesh, y_mesh = np.meshgrid(x_grid, y_grid)

# центральная точка для каждого квадрата сетки
xc = x_mesh + (grid_size / 2)
yc = y_mesh + (grid_size/ 2)

intensity_list = []
for j in range(len(xc)):
    intensity_row = []
    for k in range(len(xc[0])):
        kde_value_list = []
        for i in range(len(x)):
            #рассчитываем расстояние
            d = math.sqrt((xc[j][k] - x[i]) ** 2 + (yc[j][k] - y[i]) ** 2)
            if d <= h:
                p = kde_quartic(d, h)
            else:
                p = 0
            kde_value_list.append(p)
        # суммируем все значения плотности
        p_total = sum(kde_value_list)
        intensity_row.append(p_total)
    intensity_list.append(intensity_row)


# визуализация тепловой карты
intensity = np.array(intensity_list)
plt.pcolormesh(x_mesh, y_mesh, intensity)
plt.plot(x, y, 'ro')
plt.colorbar()
plt.savefig('test.png')
plt.show()
f.close()