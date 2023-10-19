import os
from lxml import etree, html
from io import StringIO

REPORTS = "/Users/dimy/Documents/Fall Class 2023/dimykogoya1:Dproject/db_project/html"


def reader(doc=REPORTS):
  data = []
  for report in os.scandir(doc):
    data.append(report.path)    
  return report

tree = etree.parse(StringIO(xml))
etree.tostring(tree.getroot())


def read_html(file_path: str):
    parser = html.HTMLParser(remove_blank_text=True)
    with open(file_path, encoding="windows-1252") as file:
        return html.parse(StringIO(doc.read()), parser)

def process_html_tree(tree):
  root = tree.getroo()
  
def file_reader(docs=REPORTS) :   
  data = []
  for x in reader(doc=docs):
    data.append(read_html(x))
  return data

if __name__=="__main__":
  html_data= file_reader();
  for tree in html_data:
    root =tree.getroot()