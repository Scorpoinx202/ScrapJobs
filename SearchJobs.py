import requests
from bs4 import BeautifulSoup as bs

url='https://it.jooble.org/SearchResult?rgns=italia&ukw=python'
if __name__== "__main__":
	
	#Create session 
	session=requests.session()
	
	#Getsession and parser to html
	html= session.get(str(url))
	html_doc = bs(html.text, 'html.parser')

	#funtion of frame of search
	def data_search(tag):
		return tag.has_attr("data-test-name")

	#Return of data-search	
	result=html_doc.find_all(data_search)
	
	#boocle for the jobs
	for job in result:
		try:
			tituloelemento =job.find("a", attrs={"class":"_3qfVeS"})
			titulo = tituloelemento.get_text()
			
			lugar =job.find("div", attrs={"class":"caption"}).get_text()

			link = tituloelemento["href"]

			job ="Titulo: {}\nLugar: {}\nLink: {}".format(titulo, lugar, link)
			
			print(job)
				
		except Exception as e:
			print ("Exeption: {}".format(e))
		pass