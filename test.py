import requests
from bs4 import BeautifulSoup

url = requests.get("https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/list-of-applicants/list/?id=BAC-BUDJ-O-010304")
text = BeautifulSoup(url.text, 'lxml')
done = text.find("tbody")

if "Зачислен" in done.text:
    print(1)