import FBrefScrape.FBrefInd as fb

def work():
	openfile = open('FBrefScrape\\BundesIndStatUrls.txt', 'r')
	lines = openfile.readlines()
	for url in lines:
		split = url.split('/')
		writefile = (split[8].strip().replace('-',' ') + " " + split[6].capitalize()).replace(' ','')
		print(writefile)
		dataframe = fb.scrape(url)

		csvDump(writefile,dataframe)

def csvDump(fn,df):
    df.to_csv("Bundesliga\\" + fn + ".csv")