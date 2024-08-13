### 1. Создание гистограммы для случайных данных
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы
plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.title('Гистограмма нормального распределения')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(True)
plt.show()

### 2. Построение диаграммы рассеяния для случайных данных


# Генерация двух наборов случайных данных
x = np.random.rand(100)
y = np.random.rand(100)

# Построение диаграммы рассеяния
plt.scatter(x, y, color='red', alpha=0.5)
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

### 3. Парсинг цен на диваны с сайта divan.ru и анализ данных

# URL страницы с диванами
url = 'https://www.divan.ru/category/divany-i-kresla'

# Получение HTML-содержимого страницы
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
prices = []
for price_tag in soup.find_all('div', class_='pY3d2'):
    price = price_tag.text.strip()
    # Преобразование цены в число

    price_cleaned = re.sub(r'[^\d,]', '', price)
    price_number = int(price_cleaned.replace(',', ''))
    prices.append(price_number)

# Сохранение данных в CSV
df = pd.DataFrame(prices, columns=['Цена'])
df.to_csv('prices.csv', index=False)

# Вычисление средней цены
average_price = df['Цена'].mean()
print(f'Средняя цена: {average_price:.2f} ₽')

# Построение гистограммы цен
plt.hist(df['Цена'], bins=20, color='green', edgecolor='black', alpha=0.7)
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (₽)')
plt.ylabel('Количество')
plt.grid(True)
plt.show()