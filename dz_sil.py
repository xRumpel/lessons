from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import vremya

def search_wikipedia(query):
    driver.get("https://www.wikipedia.org/")
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Даем время на загрузку страницы

def list_paragraphs():
    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    for i, paragraph in enumerate(paragraphs):
        print(f"Параграф {i + 1}: {paragraph.text[:100]}...")  # Показываем первые 100 символов параграфа
    index = int(input("Введите номер параграфа для полного отображения или -1 для возврата: "))
    if index != -1:
        print(paragraphs[index - 1].text)

def list_internal_links():
    links = driver.find_elements(By.CSS_SELECTOR, "#mw-content-text .mw-parser-output a")
    for i, link in enumerate(links):
        if link.get_attribute("href") and "wiki" in link.get_attribute("href"):
            print(f"{i + 1}: {link.text}")
    index = int(input("Введите номер ссылки для перехода или -1 для возврата: "))
    if index != -1:
        links[index - 1].click()
        time.sleep(2)  # Даем время на загрузку страницы

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Запуск браузера в фоновом режиме
    driver = webdriver.Chrome(options=options)

    try:
        initial_query = input("Введите ваш запрос: ")
        search_wikipedia(initial_query)

        while True:
            print("\nВыберите действие:")
            print("1. Листать параграфы текущей статьи")
            print("2. Перейти на одну из связанных страниц")
            print("3. Выйти из программы")

            choice = input("Введите номер действия: ")

            if choice == "1":
                list_paragraphs()
            elif choice == "2":
                list_internal_links()
            elif choice == "3":
                break
            else:
                print("Неверный выбор, попробуйте снова.")
    finally:
        driver.quit()