import vremya
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализируем браузер
driver = webdriver.Firefox()

# В отдельной переменной указываем сайт, который будем просматривать
url = "https://tomsk.hh.ru/vacancies/programmist"

try:
    # Открываем веб-страницу
    driver.get(url)

    # Используем WebDriverWait для ожидания загрузки элементов
    wait = WebDriverWait(driver, 10)
    vacancies = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'vacancy-card--z_UXteNo7bRGzxWVcL7y')))

    # Выводим вакансии на экран
    print(vacancies)

    # Создаём список, в который потом всё будет сохраняться
    parsed_data = []

    # Перебираем коллекцию вакансий
    for vacancy in vacancies:
        try:
            # Находим элементы внутри вакансий по значению
            title = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-name--c1Lay3KouCl7XasYakLk serp-item__title-link').text
           # company = vacancy.find_element(By.CSS_SELECTOR, 'span.company-info-text--vgvZouLtf8jwBmaD1xgp').text
            #salary = vacancy.find_element(By.CSS_SELECTOR, 'span.fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni').text
            #link = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
        except Exception as e:
            print(f"произошла ошибка при парсинге: {e}")
            continue
# Вносим найденную информацию в список
        parsed_data.append([title, company, salary, link])

finally:
    # Закрываем подключение браузера
    driver.quit()

# Прописываем открытие нового файла, задаём ему название и форматирование
with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
    # Используем модуль csv и настраиваем запись данных в виде таблицы
    writer = csv.writer(file)
    # Создаём первый ряд
    writer.writerow(['Название вакансии', 'название компании', 'зарплата', 'ссылка на вакансию'])
    # Прописываем использование списка как источника для рядов таблицы
    writer.writerows(parsed_data)