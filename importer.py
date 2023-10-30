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
            # print("value",delta1)
# ''' ''' libraries=[]        
    
# library_elements = xpath.findall("//*[@institurion='name']")
# for library_elem in library_elems:
#     library_data = {
#         "library": library_elem.find('name').text,
#         "Address": library_elem.find('address').text,
#         "Street": library_elem.find('street').text,
#         "City": library_elem.find('city').text,
#         "zip_code": library_elem.find('zip_code').text,
#         "State": library_elem.find('state').text
#     }
        
#     try:  
#         print(libary_elem) '''

# institutions = []

# institution_elements = root.xpath('//institution')

# for institution_elem in institution_elements:
#     institution_data = {}
#     institution_data['name'] = institution_elem.findtext('name')
#     institution_data['address'] = institution_elem.findtext('address')
#     institution_data['city'] = institution_elem.findtext('city')
#     institution_data['street'] = institution_elem.findtext('street')
#     institution_data['zip_code'] = institution_elem.findtext('zip_code')
#     institution_data['state'] = institution_elem.findtext('state')
    
# institutions.append(institution_data)

# # Print the institution data
# for institution in institutions:
#     print("Name:", institution['name'])
#     print("Address:", institution['address'])
#     print("City:", institution['city'])
#     print("Street:", institution['street'])
#     print("Zip Code:", institution['zip_code'])
#     print("State:", institution['state'])
#     print()     
      
#except Exception as e:
#print(f"Error while processing the XML file: {e}")   

def main():
    # Iterate through all HTML files in the directory
    libraries = []
    for filename in os.listdir(os.path.dirname(REPORTS)):
        if filename.endswith(".html"):
            file_path = os.path.join(os.path.dirname(REPORTS), filename)
            #print("Extracting elements from:", file_path)
            libraries.append(extract_elements_from_html(file_path))
            #print("\n")
    print(libraries)

if __name__ == "__main__":
    main()
