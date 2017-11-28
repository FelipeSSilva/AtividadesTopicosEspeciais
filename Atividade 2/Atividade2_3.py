from bs4 import BeautifulSoup
from crawler import download
import time
import sqlite3

conn = sqlite3.connect('temperatura.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS medicoes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        temperatura string NOT NULL
);
""")


for i in range(0,4):
    url = 'https://www.climatempo.com.br/previsao-do-tempo/cidade/264/teresina-pi'
    html = download(url)
    soup = BeautifulSoup(html, 'html5lib')

    temperatura = soup.find(id='momento-temperatura')

    cursor.execute("INSERT INTO medicoes (temperatura) VALUES ('" + temperatura.text +"')")
    time.sleep(30)

conn.commit()
conn.close()
print('gg')