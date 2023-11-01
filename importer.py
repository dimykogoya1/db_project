import os
from lxml import html, etree
from xml.etree import ElementTree as ET

# Set the HTML file path
REPORTS = "/Users/dimy/Documents/Fall Class 2023/dimykogoya1:Dproject/db_project/html/adams-public-library.html"

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
        
        data = {} 
        data['library'] = extract_attribute(root, "input", "name", "institutionname", "value")
        data['address'] = extract_attribute(root, "input", "id", "institutionaddress1", "value")
        
        return data
# def extract_options_from_html(file_path):
#     tree= read_html(file_path)
#     root = tree.getroot()
    
#     option_elements = root.xpath('//option')
    
#     options_data = []
#     for option in option_elements:
#         value = option.get('value')
#         text = option.text
#         options_data.append({'value': value, 'text': text if text else 'No Text'})
#     return options_data
def extract_institution_data(file_path):
    tree = read_html(file_path)
    root = tree.getroot()
    
    data = {}
    
    # Extract data for the institution
    data['institution'] = root.xpath('//input[@name="institutionname"]/@value')
    data['city'] = root.xpath('//input[@id="institutioncity"]/@value')
    data['street'] = root.xpath('//input[@id="institutionstreet"]/@value')
    data['zip_code'] = root.xpath('//input[@id="institutionzip"]/@value')
    data['state'] = root.xpath('//input[@id="institutionstate"]/@value')
    
    
    # contact info
    data['home_phone'] = root.xpath('//input[@name="people:7:homephone"]/@value')
    data['cell_phone'] = root.xpath('//input[@name="people:7:cellphone"]/@value')
    data['pager_number'] = root.xpath('//input[@name="people:7:pagernumber"]/@value')
    data['home_email'] = root.xpath('//input[@name="people:7:homeemail"]/@value')
   

    
    # Check if data is found, if not, set it to 'Not Found'
    for key, value in data.items():
        data[key] = value[0] if value else 'Not Found'
    
    return data

def main():
    for filename in os.listdir(os.path.dirname(REPORTS)):
        if filename.endswith(".html"):
            file_path = os.path.join(os.path.dirname(REPORTS), filename)
            print("Extracting data from:", file_path)
            
            institution_data = extract_institution_data(file_path)
            
            # Print the entire dictionary at once with formatting
            print("Institution Data:")
            for key, value in institution_data.items():
                print(f"{key.capitalize()}: {value}")
            print("\n")

            # # Print the link elements for the institution class
            # links = root.xpath('//a')
            # for link in links:
            #     print(link.text, link.get('href'))        
       
            # # Extract and print specific elements from the HTML file
            # h3_elements = root.xpath('//h3')
            # div_elements = root.xpath('//div')
          
            # for h3_element in h3_elements:
            #     print("h3 Element:", h3_element.text)
            # for div_element in div_elements:
            #     print("div Element:", div_element.text)
            # for option in root.findall('.//option'):
            #     value = option.get('value')
            #     text = option.text
            #     print (f'Value: {value}, Text: {text}')
            #     # find and extract attribute by specific name
            # gamma = root.xpath("//input[@name='institutionname']")[0]
            # delta =gamma.get("value", "Not found")
            # print("value",delta)
            
            # mama = root.xpath("//input[@name='institutionaddress1']")[0]
            # delta1 =mama.get("value", "Not found")
            # print("value",delta1
# def main():
#     # Iterate through all HTML files in the directory
#     #libraries = []
#     options = []
#     for filename in os.listdir(os.path.dirname(REPORTS)):
#         if filename.endswith(".html"):
#             file_path = os.path.join(os.path.dirname(REPORTS), filename)
#             #print("Extracting elements from:", file_path)
#             #libraries.append(extract_elements_from_html(file_path))
#             options.extend(extract_options_from_html(file_path))
#             #print("\n")
#     print(options)

if __name__ == "__main__":
    main()
