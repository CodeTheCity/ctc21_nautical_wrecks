# ctc21_nautical_wrecks

This is project started as part of [CTC21: Put Your City on the Map](https://github.com/CodeTheCity/CTC21), which ran Saturday 28th Nov 2020 and Sunday 29th Nov 2020.

There are a hundreds of ship wrecks off the coast of Scotland which could be seen from Marine Scotland's website https://marinescotland.atkinsgeospatial.com/nmpi/default.aspx?layers=577
Add image
however in Wikidata the position is quite different with only a few wrecks being logged. 
Add image

Day one - sourcing the information of the wrecks. 
This included looking at data on Marine Scotland's website, Aberdeenshire Council's website and on Canmore's website  - add URLs. Additional difficulty in the research was that we could find maps with shipwrecks plotted but what we needed was the source data.
Once data was found, the next stage was finding out the licencing rights and whether or not the data could be uplifted. The data found on Canmore's website indicated that it was Open Government Licence hence could be uploaded to Wikidata.  URL link to Canmore's data.

Day two - cleaning and uploaded the data to Wikidata. 
Deciding on the identifiers to use in Wikidata was the starting point, then the data had to be cleaned and manipulated. This involved translating Easting and Northings coordinates to latitude and longitude, matching the ship types between the Canmore file and Wikidata, extracting the reference to the ship from Canmore's URL and general overall common sense review of the data. To aid with this work a Python script was created. 
A separate Python statement was then created to upload the information to Wikidata using quickstatements batch upload. 



