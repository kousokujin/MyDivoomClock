import feedparser

class CRSSReader:
    def __init__(self, url):
        self.url = url
        self.Load()

    def Load(self):
        self.rss = feedparser.parse(self.url)

    def GetSiteName(self):
        return self.rss.feed.title
    
    def GetNewsCount(self):
        return len(self.rss.entries)
    
    def GetNewsTitle(self, number):
        return self.rss.entries[number].title
    
    def GetAllNewsTitle(self):
        titles = []
        for entry in self.rss.entries:
            titles.append(entry.title)
        return titles
    
    def GenAllNewsString(self, max = 0):
        if self.GetNewsCount() < 1:
            return ""
        
        cnt = self.GetNewsCount() if max == 0 else max
        cnt = cnt if cnt < self.GetNewsCount() else self.GetNewsCount()

        output_str = f'【{self.GetSiteName()}】'
        for news in self.GetAllNewsTitle()[0:cnt]:
            output_str += f'{news}・'

        return output_str[0:len(output_str) - 1]

if __name__ == "__main__":
    rss = CRSSReader("https://news.yahoo.co.jp/rss/topics/domestic.xml")
    print(rss.GenAllNewsString())