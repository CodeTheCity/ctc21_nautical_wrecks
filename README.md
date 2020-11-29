# ctc21_nautical_wrecks

This is project started as part of [CTC21: Put Your City on the Map](https://github.com/CodeTheCity/CTC21), which ran Saturday 28th Nov 2020 and Sunday 29th Nov 2020.

There are a hundreds of ship wrecks off the coast of Scotland which could be seen from [Marine Scotland's website](https://marinescotland.atkinsgeospatial.com/nmpi/default.aspx?layers=577)

however in [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page) the position is quite different with only a few wrecks being logged. The information was dervied from running the following queries in Wikidata : https://w.wiki/nDp and https://w.wiki/nDt

Add image

## Day one - sourcing the information of the wrecks. 
During the research, maps with shipwrecks plotted were found but what was required was the source data.

Data on [Marine Scotland](http://marine.gov.scot/information/wrecks-hes), [Aberdeenshire Council's website](https://online.aberdeenshire.gov.uk/smrpub/master/search.aspx) and on [Canmore's website](http://portal.historicenvironment.scot/downloads/canmore) were considered. 

Once data was found, the next stage was finding out the licencing rights and whether or not the data could be uplifted. The data found on Canmore's website indicated that it was Open Government Licence hence could be uploaded to Wikidata. This is the data source which was then used on day two of the project. 

A training session on how to use Wikidata was also required on day one to allow the team to understand how to upload the data to Wikidata and how the identifiers etc worked.

## Day two - cleaning and uploaded the data to Wikidata. 
Deciding on the identifiers to use in Wikidata was the starting point, then the data had to be cleaned and manipulated. This involved translating Easting and Northings coordinates to latitude and longitude, matching the ship types between the Canmore file and Wikidata, extracting the reference to the ship from Canmore's URL and general overall common sense review of the data. To aid with this work a Python script was created. 

A separate Python statement was then created to upload the information to Wikidata using quickstatements batch upload. 



