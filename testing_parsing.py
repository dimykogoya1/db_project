import os
from xml import html
from xml import etree, html
from io import stringIO

html_directory_files= "/Users/dimy/Documents/Fall Class 2023/dimykogoya1:Dproject/db_project/html"

#the function that list all of files
def reader(doc=REPORTS):
    data=[]
    for in os.scandir(doc):
      data.append(report.path)
    return data
  
  # Define function parse html files 
  def read_html(file_path: str):
    parser = html.HTMLParser(remove_blank_text=True)
    with open(file_path, encoding="windows-1252") as file 
    return html.parse(file, parser)
  
  
  #function to read and parse mutilple HTML files
  def extract_element_from_html(file_path)
  

  tree = ElementTree.parse("adam-public-libary.html")
  tree = ElementTree.parse("document.html")
  
  

  
  
  
  
















