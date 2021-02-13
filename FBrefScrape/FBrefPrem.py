import FBrefScrape.FBrefInd as fb

def work():
	openfile = open('FBrefScrape\\PremIndStatUrls.txt', 'r')
	lines = openfile.readlines()
	for url in lines:
		split = url.split('/')
		writefile = (split[7].strip().replace('-',' ') + " " + split[6].capitalize()).replace(' ','')
		print(writefile)
		dataframe = fb.scrape(url)

		csvDump(writefile,dataframe)

def csvDump(fn,df):
    df.to_csv("Premier League\\" + fn + ".csv")