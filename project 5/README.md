# Scraping a Web Page

For my term project, I chose to use the Google Maps API and search for information about Bellevue University. In Google Maps, every address has a unique identifier: place_ID. I first query the API on Bellevue University. That returns a place ID which is then used for the second function. Now that we have the place ID, we are able to gather more information about the specific place we want to look at. Using that place ID, I make another request to Google Maps requesting more information about Bellevue University. There were more fields available, but I chose to use:

* rating
* formatted_address
* geometry
* name
* permanently_closed
* place_id
* plus_code
* scope
* type
* url
* vicinity
* website
* formatted_phone_number
* international_phone_number

Once the request is made, a formatted JSON is returned. For the first transformation, I chose to move the data into a dataframe. I use the JSON.loads() function to move the data into a more digestable format. I then use the Pandas.io.json_normalizer function to ingest the formatted data into a dataframe. The dataframe is the result which is returned from the function. The importance of performing this project as a 2 step process I think can speak to some of the challenges a data scientist will face. The first step was to find the unique identifier for Bellevue University. Google has a very robust API, and can very intuitively find what it is that you are looking for. Exactly what I was looking for was returned in the first result. In real life, that may not happen, and you may need to adjust your search parameters until you're able to get specific to exactly what it is you need. The second step can be performed regardless of if you have the right query result or not. It could even be hard coded. I think that this 2 step process, find the unique identifier, query the remaining information that I would need about would probably be used every day in the day to day of a data scientist.

### Requirements

Python 3.6 

#### Python Libraries
* requests
* json
* pandas

[Return](https://danjsiegel.github.io/Portfolio/)