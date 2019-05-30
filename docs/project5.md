# API Data Transformation 

[Code](https://github.com/danjsiegel/Portfolio/tree/master/project%205)

I chose to use the Google Maps API and search for information about Bellevue University. In Google Maps, every address has a unique identifier: place_ID. I first query the API on Bellevue University. That returns a place ID which is then used for the second function. Now that we have the place ID, we are able to gather more information about the specific place we want to look at. Using that place ID, I make another request to Google Maps requesting more information about Bellevue University. There were more fields available, but I chose to use:

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

### Requirements

Python 3.6 

#### Python Libraries
* requests
* json
* pandas

[Home](https://danjsiegel.github.io/Portfolio/)