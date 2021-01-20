"""
A crawler program that gets the script
edit by hichens
"""

import time
from lxml import etree
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import os

def get_transcripts(url):
    response = urlopen(url)
    xml = response.read()
    html = etree.HTML(xml)
    html_data = html.xpath('//p/span/text()')  
    if len(html_data) < 10:  
        html_data = html.xpath('//div/p/text()')
    write2md(url, html_data)


def write2md(url, data):
    dirs = '../docs/' + "-".join(url[35:-1].split("-")[:2])
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    filename = url[35:-1] + '.md'
    file_path = os.path.join(dirs, filename)
    print(">> write to: ", file_path)
    title = "### " + url[35:-1] + "\n"
    with open(file_path,'w', encoding='UTF-8')as f:  # save
        f.write(title) # title 
        f.writelines([line+'\n\n' for line in data]) # contents


def get_urls(sitemap):
    response = urlopen(sitemap)
    xml = response.read()
    root = ET.fromstring(xml)  
    urls = [child[0].text for child in root]  
    urls = urls[0:-3]  
    for url in urls:
        dirs = './docs/' + "-".join(url[35:-1].split("-")[:2])
        filename = url[35:-1] + '.md'
        file_path = os.path.join(dirs, filename)
        if not os.path.exists(file_path):
            get_transcripts(url)

if __name__ == '__main__':
    sitemap = 'https://bigbangtrans.wordpress.com/sitemap.xml'  # sitemap address
    get_urls(sitemap)
