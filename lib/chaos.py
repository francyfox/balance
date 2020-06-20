import matplotlib.pyplot as plt
import numpy as np
from lib import person, world


def simple_fire():
    cost = 5  # per second
    temparature = ((27 * person.ray["manna"]) / 10) * world.dungeon['ph_D']
    dist = (cost * 2) * world.dungeon['ph_D']
    radius = 5
    angle = 30
    gamma = np.deg2rad(angle)

    damage = cost * person.ray["D"] + (temparature / 10)
    total_xp = person.enemy["xp"]
    total_manna = person.ray["manna"]

    while total_xp > 0:
        total_xp -= damage
        total_manna -= cost
        print('Урон: [', damage, '] XP = ', total_xp, "| Манна = ", total_manna)

    ray = person.ray
    enemy = person.enemy
    theta = np.linspace(0, 2 * np.pi, 100)
    r = radius

    x1 = r * np.cos(theta)  # точки окружности
    x2 = r * np.sin(theta)

    x3 = (dist - np.cos(gamma)) * np.cos(gamma)
    x4 = (x3 * np.sin(gamma))
    fig, ax = plt.subplots(figsize=(5, 5))

    ax.plot(x1 + (dist / 2), x2, label=radius)
    # ax.plot([x3, x3], [-x4, x4], marker='o')
    ax.plot([0, x3], [0, x4], [0, x3], [0, -x4], [x3, x3], [-x4, x4], marker='o')
    plt.fill_between([0, x3], [0, x4], [0, -x4], [x3, x3], [-x4, x4], color='slategrey')

    c_blue = dist / 2  # найти центр тяжести
    c_green_red = np.sqrt(x3 * c_blue + x4 * ray["pos_y"])  # длина red + green

    red = np.sqrt(x3 * enemy["pos_x"] + x4 * enemy["pos_y"])  # просчет позиции врага от краев треугольника
    green = np.sqrt(x3 * enemy["pos_x"] + (-x4) * enemy["pos_y"])
    blue = np.sqrt(np.power(enemy["pos_x"], 2) + np.power(enemy["pos_y"], 2))  # не точно

    per_red = int((red / c_blue) * 100)
    per_green = int((green / c_blue) * 100)
    per_blue = int((blue / c_blue) * 100)
    print('R: ', per_red, '|', 'G: ', per_green, '|', 'B: ', per_blue, 'test: ', dist)

    ax.plot([x3, enemy["pos_x"]], [x4, enemy["pos_y"]], color='red', label='RED')
    ax.plot([x3, enemy["pos_x"]], [-x4, enemy["pos_y"]], color='green', label='GREEN')
    ax.plot([ray["pos_x"], enemy["pos_x"]], [ray["pos_y"], enemy["pos_y"]], color='blue', label='BLUE')  # рисуем позицию врага от краев треугольника
    ax.scatter(enemy["pos_x"], enemy["pos_y"], marker='o', label='Враг', edgecolors='red')  # позиция врага

    plt.title("")  # заголовок
    plt.grid()
    plt.xlabel("x")  # ось абсцисс
    plt.ylabel("y")  # ось ординат
    ax.legend(fontsize=5,
              ncol=2,  # количество столбцов
              facecolor='oldlace',  # цвет области
              edgecolor='r',  # цвет крайней линии
              title='',  # заголовок
              title_fontsize='5'  # размер шрифта заголовка
              )
    plt.show()
