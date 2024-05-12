# Метро Dubai Граф

Цей проект містить код для моделювання мережі метро в Дубаї з використанням бібліотеки NetworkX у Python.

## Огляд

У цьому проекті створюється граф метро Дубаю та реалізується алгоритм Дейкстри для знаходження найкоротших шляхів між станціями.

## Використання

Запустіть `Task1forHW6.py`, щоб створити граф метро Дубаю та візуалізувати його за допомогою бібліотеки matplotlib.

## Залежності

Цей проект вимагає наступні бібліотеки:

- `networkx`
- `matplotlib`
- `sys`

## Отримані результати

Кількість вкршин: 41

Кількість ребер: 41

Ступінь ребер: {'Centrepoint': 1, 'Airport Terminal 3': 2, 'Airport Terminal 1': 2, 'GGICO': 2, 'Deira City Centre': 2, 'Al Rigga': 2, 'Union': 4, 'Bur Juman': 4, 'max': 2, 'World Trade Centre': 2, 'Burj Khalifa / Dubai Mall': 2, 'Business Bay': 2, 'Onpassive': 2, 'Equiti': 2, 'Mall of the Emirates': 2, 'Mashreq': 2, 'Dubai Internet City': 2, 'Al Khail': 2, 'Sobha Realty': 2, 'DMCC': 2, 'Jabal Ali': 2, 'Ibn Battuta': 2, 'Energy': 2, 'Danube': 2, 'UAE Exchange': 1, 'Etisalat': 1, 'Al Qusais': 2, 'Dubai Airport Free Zone': 2, 'Al Nahda': 2, 'Stadium': 2, 'Al Quiadah': 2, 'Abu Baker Al Siddique': 2, 'Baniyas Square': 2, 'Palm Deira': 2, 'Al Ras': 2, 'Al Ghubaiba': 2, 'Al Fahidi': 2, 'Oud Metha': 2, 'Dubai Healthcare City': 2, 'Al Jadaf': 2, 'Creek': 1}

Шляхи, знайдені за допомогою DFS:
['Centrepoint', 'Airport Terminal 3', 'Airport Terminal 1', 'GGICO', 'Deira City Centre', 'Al Rigga', 'Union', 'Bur Juman', 'Oud Metha', 'Dubai Healthcare City', 'Al Jadaf', 'Creek']

Шляхи, знайдені за допомогою BFS:
['Centrepoint', 'Airport Terminal 3', 'Airport Terminal 1', 'GGICO', 'Deira City Centre', 'Al Rigga', 'Union', 'Bur Juman', 'Oud Metha', 'Dubai Healthcare City', 'Al Jadaf', 'Creek']
['Centrepoint', 'Airport Terminal 3', 'Airport Terminal 1', 'GGICO', 'Deira City Centre', 'Al Rigga', 'Union', 'Baniyas Square', 'Palm Deira', 'Al Ras', 'Al Ghubaiba', 'Al Fahidi', 'Bur Juman', 'Oud Metha', 'Dubai Healthcare City', 'Al Jadaf', 'Creek']

Найкоротші відстані до кожної вершини від початкової станції:
{'Centrepoint': 0, 'Airport Terminal 3': 2, 'Airport Terminal 1': 5, 'GGICO': 9, 'Deira City Centre': 11, 'Al Rigga': 16, 'Union': 19, 'Bur Juman': 23, 'max': 26, 'World Trade Centre': 28, 'Burj Khalifa / Dubai Mall': 32, 'Business Bay': 35, 'Onpassive': 37, 'Equiti': 42, 'Mall of the Emirates': 46, 'Mashreq': 49, 'Dubai Internet City': 51, 'Al Khail': 55, 'Sobha Realty': 58, 'DMCC': 62, 'Jabal Ali': 65, 'Ibn Battuta': 67, 'Energy': 70, 'Danube': 74, 'UAE Exchange': 77, 'Etisalat': 40, 'Al Qusais': 38, 'Dubai Airport Free Zone': 35, 'Al Nahda': 33, 'Stadium': 30, 'Al Quiadah': 26, 'Abu Baker Al Siddique': 23, 'Baniyas Square': 22, 'Palm Deira': 24, 'Al Ras': 27, 'Al Ghubaiba': 29, 'Al Fahidi': 27, 'Oud Metha': 26, 'Dubai Healthcare City': 30, 'Al Jadaf': 33, 'Creek': 35}