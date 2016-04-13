from bs4 import BeautifulSoup
import sys,urllib2,re,time

def main(argv):
	url = "http://" + argv[0]
	r = urllib2.urlopen(url).read()
	req = urllib2.Request(url)
	url_handle = urllib2.urlopen(req)
	headers = url_handle.info()
	soup = BeautifulSoup(r,"html.parser")
	doc = soup.prettify()


	currentYear = time.strftime("%Y")

	last = headers.getheader("Last-Modified")

	#static web page has Last-Modified field in header
	if last is not None:
		print 'static'
		if last.find(currentYear) != -1:
			print 'Alive now'
		elif last.find(str(int(currentYear)-1)) != -1:
			print 'Last-Modified last year'
		else:
			print 'No recent update'

	print 'run'

	#Dynamic Website will have copyright(latest modified date) on the web page.
	text = soup.find(text = re.compile('\xa9'))

	if text is not None:
		print 'copyright'
		if text.find(currentYear) != -1:
			print 'Alive now'
		elif text.find(str(int(currentYear)-1)) != -1:
			print 'Last-Modified last year'
		else:
			print 'No recent update'


if __name__ == "__main__":
    main(sys.argv[1:])