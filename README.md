# FBrefScraper

Simple web scrape project to collect player data from www.fbref.com for the big 5 men's leagues

Based on: https://smehta.medium.com/scrape-and-create-your-own-beautiful-dataset-from-sports-reference-com-using-beautifulsoup-python-c26d6920684e

The repository has the appropriate CSV destination folders complete with data as of 2/13/2021, or the most recent commit of changes to those files. More recent data will require you to run the program.

Run FBrefMaster.py to collect from all 5 leagues or create your own file to run a particular league. Be sure you have the appropriate CSV destination folders in the same directory as FBrefMaster.py: "Big 5", "Premier League", "La Liga", "Serie A", "Bundesliga", "Ligue 1". Each league takes ~30min. to run.

You can add the functionality to automatically create the necessary folders, but I haven't bothered.

Code currently does not run 'Big 5' (see FBrefScrape/FBrefBig5.py) but feel free to get it running. I haven't had the time to work out some issues specific to that dataset.

Whereas FBrefScrape/FBrefInd.py does the work for player stats you should pretty easily be able to add functionality with a file like FBrefScrape/FBrefTeam.py for team stats.
