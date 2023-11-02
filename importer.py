import os
from lxml import html, etree
from xml.etree import ElementTree as ET

# Set the HTML file path
REPORTS = "/Users/dimy/Documents/Fall Class 2023/dimykogoya1:Dproject/db_project/html"

def reader(doc):
    data = []
    for report in os.scandir(doc):
        data.append(report.path)
    return data

def read_html(file_path: str):
    parser = html.HTMLParser(remove_blank_text=True)
    with open(file_path, encoding="windows-1252") as file:
        return html.parse(file, parser)

def file_reader(docs):
    data = []
    for x in reader(doc=docs):
        data.append(read_html(x))
    return data


def extract_attribute(element, tag, attribute, text, val):
    alpha = element.xpath(f"//{tag}[@{attribute}='{text}']")[0]
    return alpha.get(val, "Not Found")

  
def extract_elements_from_html(file_path):
   
     with open(file_path, encoding="windows-1252") as file:
        tree = html.parse(file) #fromstring
        #root = etree.fromstring(xml_content)
        root = tree.getroot()
        
        # create and dictionary for institution, city, state, code, zip_code
    
        library = {} 
        library['entity'] = root.xapth('//input[@attrb="something"]')[0].get('value', None)
        libary['institution'] = root.xpath('//input[@id="institutionname"]/@value')[0]
        libary['address'] = root.xpath('//input[@id="institutionaddress"]/@value')[0]
        libary['code'] = root.xpath('//input[@id="instituticode"]/@value')[0]
        libary['municipacity'] = root.xpath('//input[@id="institutionmunip"]/@value')[0]
        libary['zip_code'] = root.xpath('//input[@id="institutionzip"]/@value')[0]
        libary['state'] = root.xpath('//input[@id="institutionstate"]/@value')[0]
              
        return libary
     
     
def extract_select_elements(file_path):
    tree = read_html(file_path)
    root = tree.getroot()
    
    city = root.xpath("//select[@name='institutioncity']")[0]
    
    data = city.iterchildren("option")
    first = next(data)
    
    return first.text
   
def main():
    for filename in os.scandir(REPORTS):
        if filename.name.endswith(".html"):
            file_path = filename.path

def main():
    
    for filename in os.scandir(REPORTS):
        if filename.name.endswith(".html"):
            file_path = filename.path
            libaries.append(extract_select_elements(file_path))

    for libary in selects:
        print(libary)

if __name__ == "__main__":
    main()
    
    
from project.models import Library, Address, Municipality

demo = {
    "library": "text",
    "code": "text",
    "address": "text",
    "muncipality": "text",
    "state": "text",
    "zip_code": "text"
}

municipality_obj = Municipality.objects.get_or_create(
    name=demo['muncipality'],
    state=demo['state']
)[0]

address = Address.objects.get_or_create(
    address=demo['address'],
    municipality=municipality_obj,
    zip_code=demo['zip_code']
)[0]

lib = Library.objects.filter(code=demo['code']).first()
if not lib:
    lib = Library.objects.create(
        name=demo['library'],
        code=demo['code'],
        address=address
    )

data = [
    {'libary','Libary'},
    {'address','Address'},
    {'code','Code'},
    {'munipality','Municipality'},
    {'zip_code', Zip_code},
    {'state', 'State'}
   
]
for data in range(data):
    print(data)

# create a list of dictionaries with 
# student id as key and name as value
data = [{7058: 'sravan', 7059: 'jyothika', 
		7072: 'harsha', 7075: 'deepika'},
		
		{7051: 'fathima', 7089: 'mounika', 
		7012: 'thanmai', 7115: 'vasavi'},
		
		{9001: 'ojaswi', 1289: 'daksha', 
		7045: 'parvathi', 9815: 'bhavani'}]

print(data)







# Library.objects.all()
    
    

# def main():
#     for filename in os.scandir(REPORTS):
#         if filename.name.endswith(".html"):
#             file_path = filename.path
#             print("Extracting data from:", file_path)
            
#             institution_data = extract_institution_data(file_path)
            
#             # Print the entire dictionary at once with formatting
#             print("Institution Data:")
#             # for key, value in institution_data.items():
#             #     print(f"{key.capitalize()}: {value}")
#             # print("\n")
#             print(institution_data, "\n")

#             # Print the link elements for the institution class
#             links = root.xpath('//a')
#             for link in links:
#                 print(link.text, link.get('href'))        
       
#             # Extract and print specific elements from the HTML file
#             h3_elements = root.xpath('//h3')
#             div_elements = root.xpath('//div')
          
#             for h3_element in h3_elements:
#                 print("h3 Element:", h3_element.text)
#             for div_element in div_elements:
#                 print("div Element:", div_element.text)
#             for option in root.findall('.//option'):
#                 value = option.get('value')
#                 text = option.text
#                 print (f'Value: {value}, Text: {text}')
#                 # find and extract attribute by specific name
#             gamma = root.xpath("//input[@name='institutionname']")[0]
#             delta =gamma.get("value", "Not found")
#             print("value",delta)
            
#             mama = root.xpath("//input[@name='institutionaddress1']")[0]
#             delta1 =mama.get("value", "Not found")         # print("value",delta1
