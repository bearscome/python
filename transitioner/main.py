import requests
import pandas
import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import pytesseract as tess
from PIL import Image


class myFileSystemEventHandler(FileSystemEventHandler):
    def __init__(self):
        self.openList = []

    def translate(self, text):
        data = {
            'queryLanguage': 'en',
            'resultLanguage': 'kr',
            'q': 'hello'
        }

        headers = {
            'referer': 'https://translate.kakao.com/',
            'User-Agent': 'Chrome'
        }

        URL = 'htps://translate.kakao.com/translator/translate.json'

        data['q'] = text

        res = requests.post(URL, headers=headers, data=data)
        try:
            if res.status_code == requests.codes.ok:
                df = pandas.DataFrame(res.json()['result']['output'])
                df.dropna(inplace=True)
                print(df)
            else:
                print("번역 실패")
        except requests.exceptions.RequestException as e:
            print(e)

    def on_created(self, event):
        while event.src_path not in self.openList:
            self.openList.append(event.src_path)
            time.sleep(2)
            img = Image.open(event.src_path)
            text = tess.image_to_string(img)
            self.translate(text)
            break


event_handler = myFileSystemEventHandler()
path = '.'
observer = Observer()
observer.schedule(event_handler, path, recursive=False)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
