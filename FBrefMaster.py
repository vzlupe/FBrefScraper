#import FBrefScrape.FBrefBig5
import FBrefScrape.FBrefLaLiga
import FBrefScrape.FBrefBundes
import FBrefScrape.FBrefPrem
import FBrefScrape.FBrefSerieA
import FBrefScrape.FBrefLigue1

def main():
	league = int(input("Choose league (0=Prem, 1=Bundes, 2=LaLiga, 3=SerieA, 4=Ligue1, 5=All): "))

	if league == 0:
		FBrefScrape.FBrefPrem.work()
	elif league == 1:
		FBrefScrape.FBrefBundes.work()
	elif league == 2:
		FBrefScrape.FBrefLaLiga.work()
	elif league == 3:
		FBrefScrape.FBrefSerieA.work()
	elif league == 4:
		FBrefScrape.FBrefLigue1.work()
	elif league == 5:
		FBrefScrape.FBrefPrem.work()
		FBrefScrape.FBrefBundes.work()
		FBrefScrape.FBrefLaLiga.work()
		FBrefScrape.FBrefSerieA.work()
		FBrefScrape.FBrefLigue1.work()

if __name__ == '__main__':
	main()