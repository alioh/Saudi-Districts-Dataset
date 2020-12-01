# Saudi Arabia Districts Dataset


## About 

This dataset is a collection of files related to Saudi Arabia's districts. The data were collected manually from 
This data includes general information about districts of the Kingdom of Saudi Arabia, such as the number of residents, the proportion of Saudis and foreigners, the distribution of males and females, in addition to the average income. Data were collected manually from [Nine Tenths](https://map.910ths.sa/).

## Credit

[Ali Alohali](http://alioh.com), [Sara AlSiyat](http://linkedin.com/in/saraalsiyat), [Ibrahim AlHammad](http://linkedin.com/in/ibrahim-alhammad-7228b3178), [Nora AlAmri](https://www.linkedin.com/in/nora-alamri) and [Rawan AlMohimeed](https://www.linkedin.com/in/rawanmohimeed).


## Thanks

Thanks to the following contributors:

**Name**|**contribution**
:-----:|:-----:|:-----
[Dr. Najwa Alghmadi](https://www.najwa-alghamdi.net/)|Providing most of Lat/Long data.

## Data elements:

Some of the columns were collected manually and others we used little math to find it

**Label**|**Type**|**Source (or columns)**
:-----:|:-----:|:-----
District name EN|Text|Manually Translated
District name AR|Text|Nine Tenths
Latitude|Number (Decimal)|Manually Collected
Longitude|Number (Decimal)|Manually Collected
Population|Number|Nine Tenths
Males (%)|Number (Decimal)|Nine Tenths
Females (%)|Number (Decimal)|= 1 - [Males (%)]
Saudis (%)|Number (Decimal)|Nine Tenths
Non Saudis (%)|Number (Decimal)|= 1 - [Saudis (%)]
Males|Number|= [Males (%)] * [Population]
Females|Number|= [Population] - [Males]
Saudis|Number|= [Saudis (%)] * [Population]
Non Saudis|Number|= [Population] - [Saudis]
Average Income|Number|Nine Tenths


## Note:

Some entries are 0, in income it means unavailable. If the whole row is 0 it means data is unavailable. In other fields it means actual 0% or 0.

## Future work:

- Add more cities.
- Add more data.
    * Distribution of income by age, sex and nationality.
    * Add districts coordination as polygons.
    * Zip codes.
- Convert the data to SQL Database, Excel and json.

## Help:

You can submit your ideas or edits to this dataset. We will review it and approve it.



## Use:

Feel free to use the dataset **as long as you credit the authors**.
