from MyClock import CMyClock
from NewsCollector import CNewsCollector

PIXOO_IP = "192.168.10.244"
NEWS_URL = "https://news.yahoo.co.jp/rss/topics/domestic.xml"
FILE_NAME = "message.txt"

def run():
    collector = CNewsCollector()
    collector.AddURL(NEWS_URL)
    collector.SaveNewsTitles(FILE_NAME)

    clock = CMyClock(PIXOO_IP)
    clock.Draw(FILE_NAME)

if __name__ == "__main__":
    run()