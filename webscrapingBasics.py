from urllib.request import urlopen

class WebScraping:
	def __init__(self,url):
		self.url=url

	def Output(self):
		page=urlopen(url)
		print(page)
		html_bytes=page.read()
		html=html_bytes.decode("utf-8")
		print(html)
		title_index=html.find("<title>")
		print(title_index)
		start_index=title_index+len("<title>")
		print(start_index)
		end_index=html.find("</title>")
		print(end_index)
		title=html[start_index:end_index]
		print(title)
		
if __name__=="__main__":
	w1=WebScraping("https://coderpass.herokuapp.com")
	w1.Output()

