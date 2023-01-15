import requests
from itertools import groupby
import re

extended_list_url = "https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/ads_list_extended.txt"
response = requests.get(extended_list_url)
extended_list = response.text

with open('ads_list.txt', 'r') as file:
    ads_list = file.read()
extended_list = extended_list.replace(extended_list.split("! [List from Faust and his Gist: https://gist.github.com/dymitr-ua/ab19ebfa6b6027daf07a995e420d4613]")[0], ads_list)

with open('ads_list_extended.txt', 'w') as file:
    file.write(extended_list)

print('[!] Файл расширенного варианта списка обновлён!')

regex = r" https:\/\/[a-z]\w+(.+)$"

with open('ads_list.txt', 'r') as file:
    content = file.read()

matches = re.finditer(regex, content, re.MULTILINE)
links = []

for matchNum, match in enumerate(matches, start=1):
    match = match.group()
    lk = f"\n- [{match.replace(' ', '')}]({match.replace(' ', '')})"

    if not 'zalexanninev15' in str(lk).lower():
        links.append(lk)

links_a = list(set(links))

with open('SITES.md', 'w', encoding="utf8") as file: 
    file.write("\n# Сайты, которые имеются в списке NoADS_RU:\n\n") 

    for line in links_a: 
        file.write(line)
    file.write('\n- И другие сайты (при использовании [расширенного варианта](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/ads_list_extended.txt) списка)')

print('[!] Список пополнился новыми сайтами!')
