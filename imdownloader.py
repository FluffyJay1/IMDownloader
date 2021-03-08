import requests
import os
import sys
import re

url = sys.argv[1]
html = requests.get(url).content
regex = re.compile('gallery/(\d*)')
m = regex.search(url)
gallery_id = int(m.group(1))
regex = re.compile(r"download_gallery\(\\'([^\\]*)\\', \\'([^\\]*)\\', \\'([^\\]*)\\'\)")
m = regex.search(str(html))
e = m.group(1) #url pt 2
b = m.group(2) #url pt 1
a = m.group(3) #album name 

#fuckin galleryinfo
galleryinfo_url = "http://imhentai.xxx/downloads/" + b + "/" + e + ".js"
galleryinfo_raw = requests.get(galleryinfo_url).content
regex = re.compile(r'\[(.*)\]')
m = regex.search(str(galleryinfo_raw))
galleryinfo = m.group(1).split(",")

if (gallery_id > 0 and gallery_id <= 274825): 
	server = 'm1.imhentai.xxx' 
if (gallery_id > 274825 and gallery_id <= 403818): 
	server = 'm2.imhentai.xxx'
if (gallery_id > 403818 and gallery_id <= 527143):
	server = 'm3.imhentai.xxx'
if (gallery_id > 527143 and gallery_id <= 632481):
	server = 'm4.imhentai.xxx'
if (gallery_id > 632481):
    server = 'm5.imhentai.xxx'
	
	
if not os.path.exists(a):
    os.makedirs(a)

regex = re.compile('"[^"]*":"(.*)"')
total_images = len(galleryinfo)
print("downloading " + str(total_images) + " images...")
for i in range(total_images):
	m = regex.search(galleryinfo[i])
	n = m.group(1).split('|')
	o = n[0]
	l = "http://"+ server +"/" + n[1] + "/" + n[2] + "/" + o
	print("downloading " + str(i + 1) + "/" + str(total_images) + ": " + o)
	r = requests.get(l)
	open(a + "/" + o, 'wb').write(r.content)