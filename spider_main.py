import url_manger, html_downloader, html_parser, html_outputer
class SpiderMain:
  def __init__(self):
    self.urls = url_manger.UrlManger()
    self.downloader = html_downloader.HtmlDownloader()
    self.parser = html_parser.HtmlParser()
    self.outputer = html_outputer.HtmlOutputer()

  def craw(self, root_url):
    count = 1
    self.urls.add_new_url(root_url)
    while self.urls.has_new_url():
      try:
        new_url = self.urls.get_new_url()
        html_cont = self.downloader.download(new_url)
        new_urls, new_data = self.parser.parse(new_url, html_cont)
        self.urls.add_new_urls(new_urls)
        self.outputer.collect_data(new_data)
        if count == 1000:
          break
      except:
        print('失败')
      
    self.outputer.output_html()


if __name__ == "__main__":
  root_url = "https://baike.baidu.com/item/Python/407313"
  spider = SpiderMain()
  spider.craw(root_url)
