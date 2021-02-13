from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4 import Comment
import pandas as pd

def scrape(url):
	page = urlopen(url).read()
	soup = BeautifulSoup(page,"html.parser")
	comments = soup.find_all(string=lambda text: isinstance(text, Comment))
	soup2 = BeautifulSoup(comments[23], 'html.parser')
	body = soup2.find("tbody")
	pre_df = dict()

	rows = body.find_all('tr')
	for row in rows:
		if (row.find('th', {"scope":"row"}) != None):
			cells = row.find_all("td")
			for cell in cells:
				a = cell.text.strip().encode()
				text = a.decode("utf-8")
				f = cell.attrs['data-stat']
				if f in pre_df:
					pre_df[f].append(text)
				else:
					pre_df[f] = [text]

				df = pd.DataFrame.from_dict(pre_df,orient='index')

	return(df)

