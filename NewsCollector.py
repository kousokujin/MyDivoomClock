from RSSReader import CRSSReader

class CNewsCollector:
    def __init__(self):
        self.url_list = []

    def AddURL(self, url):
        self.url_list.append(url)

    def AddURLs(self, urls):
        for url in urls:
            self.url_list.append(url)

    def GenerateNews(self):
        news = ""
        for url in self.url_list:
            reader = CRSSReader(url)
            news += reader.GenAllNewsString()
        
        return news
    
    def SaveNewsTitles(self, filename, encoding='UTF-8'):
        with open(filename, 'w', encoding=encoding) as f:
            f.write(self.GenerateNews()[0:190])
    

if __name__ == "__main__":
    collector = CNewsCollector()

    #urls = [
    #    "https://news.yahoo.co.jp/rss/topics/domestic.xml",
    #   "https://news.yahoo.co.jp/rss/topics/it.xml",
    #    "https://news.yahoo.co.jp/rss/topics/entertainment.xml"
    #]
    #collector.AddURLs(urls)
    collector.AddURL("https://news.yahoo.co.jp/rss/topics/domestic.xml")
    collector.SaveNewsTitles('message.txt')