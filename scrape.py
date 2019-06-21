import sys
import time
from selenium import webdriver
import argparse
from datetime import datetime

def start_browser():
	br = webdriver.Firefox()
	br.implicitly_wait(10)
	return br

def scrape_results(br):
	links = br.find_elements_by_xpath("//*[@class='r']/a[@href]")
	results = []
	for link in links:
		title = link.text.encode('utf8')
		url = link.get_attribute('href')
		title_url = (title, url)
		results.append(title_url)
	return results

def go_to_page(br, page_num, search_terms):
	page_num = page_num - 1
	start_results = page_num * 100
	start_results = str(start_results)
	url = 'https://www.google.com/webhp?#num=100&start='+start_results+'&q='+search_terms
	br.get(url)
	time.sleep(2)


ap = argparse.ArgumentParser()
ap.add_argument('-k', '--keyword', help='Keyword')
ap.add_argument('-p', '--page', help='Page')
args = vars(ap.parse_args())

search_term = args['keyword']
pages = args['page']

br = start_browser()
all_results = []

now = datetime.now()
# folder = '../result/'
# filename = folder + search_term + '_' + now.strftime('%Y') + now.strftime('%m') + now.strftime('%d') + '_result.txt'
filename = search_term + '_' + now.strftime('%Y') + now.strftime('%m') + now.strftime('%d') + '_result.txt'
print(filename)

f = open(filename, 'w+')

for page_num in range(int(pages)):
	page_num = page_num + 1
	go_to_page(br, page_num, search_term)
	title_urls = scrape_results(br)
	for title in title_urls:
		all_results.append(title)
	
	for result in all_results:
		title = result[0]
		url = result[1]
		# tobewritten = '[+] ' + str(title) + '-- ' + str(url) + '\n'
		tobewritten = str(url) + '\n'
		f.write(tobewritten)
		# print('[+]', title, '--', url)
		# print(tobewritten)
	f.close()
	
