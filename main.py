from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    path1 = "./div[@class='vacancy-serp-item-body']/div/div[3]/span"
    path2 = "./div[@class='vacancy-serp-item-body']/div/div[4]/div/div[2]"
    url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'
    KEYWORDS = ['Джанго', 'джанго', 'Flask', 'flask', 'Django', 'django', 'фласк', 'Фласк']
    json = dict.fromkeys(['Ссылка', 'Вилка зп', 'Название компании', 'Город'])
    driver = webdriver.Chrome()
    driver.get(url)
    res = driver.find_element(By.ID, 'HH-React-Root').find_elements(By.CLASS_NAME, 'vacancy-serp-item__layout')

    for item in res:
        json['Ссылка'] = ''
        for var in KEYWORDS:
            if not json['Ссылка']:
                if var in item.text:
                    json['Ссылка'] = item.find_element(By.CLASS_NAME, 'serp-item__title').get_attribute('href')

                    try:
                        json['Вилка зп'] = item.find_element(By.XPATH, path1).text.replace(u'\u202f', '')
                    except:
                        json['Вилка зп'] = 'Не указано'

                    json['Название компании'] = item.find_element(By.CLASS_NAME, 'bloko-text').text
                    try:
                        json['Город'] = item.find_element(By.XPATH, path2).text
                    except:
                        json['Город'] = 'Город не указан'

        if json['Ссылка']:
            print(json)


if __name__ == '__main__':
    main()
