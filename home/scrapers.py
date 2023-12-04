import requests
from bs4 import BeautifulSoup


def fetch_patch_notes():
    URL = 'https://ark.wiki.gg/wiki/Category:ARK:_Survival_Ascended_PC_patch_notes'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    notes = []

    for note_section in soup.find_all('div', class_='patch-note-class'):
        title = note_section.find('h2', class_='title-class').get_text(strip=True)
        content = note_section.find('p', class_='content-class').get_text(strip=True)
        notes.append({'title': title, 'content': content})

    return notes


patch_notes = fetch_patch_notes()
for note in patch_notes:
    print(note)
