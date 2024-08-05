from selenium import webdriver
from selenium.webdriver.common.by import By
import re

browser = webdriver.Chrome()
browser.get("https://pestrecy-rt.ru/news/tag/list/specoperaciia/")
headlines = [] 

while True:
    heads = browser.find_elements(By.XPATH, '//h2[@class="oneNews__link news__bold-text"]')
    parags = browser.find_elements(By.XPATH, '//p[@class="oneNews__link"]')
    for hdline, parag in zip(heads, parags):
        headlines.append(f'{hdline.text.strip()}. {parag.text.strip()}')
    try:
        next_button = browser.find_element(By.XPATH, '//a[@class="all-news__button_forward"]//span[contains(text(), "Далее")]')
        next_button.click()
    except Exception:
        break
browser.quit()

namreg = re.compile(r'([А-ЯЁІЇЄҐ][а-яёіїєґ]+) ([А-ЯЁІЇЄҐ][а-яёіїєґ]+)')
corpses = set()
oddwords = {'СВО', 'PT', 'РФ', 'ВСЕ', 'Президент', 'Татарстан', 'Глава', 'Сил', 'России', 'Геро', 'Родин',
'Казан', 'Житель', 'Совета', 'Указ', 'Госдум', 'Заместитель', 'Защитники', 'Отделением', 'Республик', 'Госсовет',
'Пестре', 'Пенсионерка', 'Минобороны', 'Жизнь', 'Священник', 'Шигалеево', 'Мама', 'Фонда',
'Главнокомандующему', 'Также', 'Казни', 'Кремле', 'Верховный', 'Донбасса', 'Семье', 'Казанском', 'Около',
'Волге', 'Орденом', 'Мужества', 'Мост'}
for headline in headlines:
    headline = ' '.join(word for word in headline.split() if not any(pattern in word for pattern in oddwords))
    matches = namreg.findall(headline)
    for match in matches:
        name = match[0]
        surname = match[1]
        corpses.add(f'{name} {surname}')
print(corpses)