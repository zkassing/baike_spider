class HtmlOutputer(object):
  def __init__(self): 
    self.datas = []

  def collect_data(self, data):
    if data is None:
      return 
    self.datas.append(data)

  def output_html(self):
    fout = open('output.txt', 'w', encoding='utf-8')
    for data in self.datas:
      str = data['url'] + data['title'] + data['summary']
      fout.write(str)
      """ fout.write(data['url'])
      fout.write(data['title'].encode('utf-8'))
      fout.write(data['summary'].encode('utf-8')) """
    
    fout.close()