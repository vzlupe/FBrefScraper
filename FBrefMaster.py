#import FBrefScrape.FBrefBig5
import FBrefScrape.FBrefLaLiga
import FBrefScrape.FBrefBundes
import FBrefScrape.FBrefPrem
import FBrefScrape.FBrefSerieA
import FBrefScrape.FBrefLigue1

def main():
	#FBrefScrape.FBrefBig5.work()
	FBrefScrape.FBrefLaLiga.work()
	FBrefScrape.FBrefBundes.work()
	FBrefScrape.FBrefPrem.work()
	FBrefScrape.FBrefSerieA.work()
	FBrefScrape.FBrefLigue1.work()

if __name__ == '__main__':
	main()