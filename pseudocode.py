# figure out how to import files/data from a folder into python
# import function on getting match id for user (can be found on ESPNcricket)
# call for match id
# display match info:
    # match winner
    # teams
    # how team won
    # players from both sides
    # umpires
    # toss winner and what they chose to do
    # stadium/venue
    # player scores, how they got out and to who
    # bowling figures and extras
    # player of the match
    # date
    # match number of the league



#IMPORT VARIABLES FROM ONE FILE TO ANOTHER
    #SYNTAX: from {file name} import {function name or *}
    #https://medium.com/geekculture/how-to-import-another-file-in-python-4f833ea462b1

# ----- START OF PROGRAM ----- #
pip install python-cricket-scraper #using pip packet manager to install cricket scraper software

from cricscraper.cricsheet import CricSheet
sheets = Cricscraper(folder="IPL Matches Files\")
sheets.save()
