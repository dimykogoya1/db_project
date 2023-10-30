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
  

  #To find specific element by its tag name
  element = root.find('.//tag_name')
  
  To find elements by its specific atribute:
    elements = root.findall(".//*[@attribute_name='attribute_value']")
    
    
    
    
    
    
    
  To find elements by its specific for element
  attribute_value=element.get('attribute_name')
  
  To extract text content of the element 
  text = element.text
  
  alpha = element.get('hreg', "Not Found")
  for in alpha.iterfind('div')
  
  
  if a ['href'] is not None:
    do something
    
    
    getatt, name)



country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome", 
  "England": "London"
}

# printing the dictionary
print(country_capitals)








libaries =[]
for doc in documents:
  processing
  libraires.append({
    "libary": "warwic public libary",
    
  })
  
  
  
  
root = etree.fromstring(xml_content)

libraries = []

# Use XPath to select library elements
library_elements = root.xpath('//library')

for library_elem in library_elements:
    library_data = {
        "library": library_elem.find('name').text,
        "Address": library_elem.find('address').text,
        "Street": library_elem.find('street').text,
        "City": library_elem.find('city').text,
        "zip_code": library_elem.find('zip_code').text,
        "State": library_elem.find('state').text
    }

    libraries.append(library_data)
    print(libraries)

