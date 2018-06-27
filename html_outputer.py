class HtmlOutputer(object):
  def __init__(self): 
    self.datas = []

  def collect_data(self, data):
    if data is None:
      return 
    self.datas.append(data)

  def output_html(self):
    fout = open('output.txt', 'w')
    for data in self.datas:
      fout.write(data['url'] + " " + data['title'] + " " + data['summary'] + "\n")
    
    fout.close()