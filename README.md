# GSBO City Collision Data Analysis
## TeamMembers
- [Jorge Salas][1] 
- [Daniel Frye][2]
- [Dmithra Ratnayake][3]
- [Sahiti Vanteru][4]
- [Byungjin Kang][5]

## Description (Goals)
Our group is dedicated in analyzing the Greensboro traffic collision data
with the main goal of bringing fatalitie rates down to zero. However, seeking 
a better understanding of the data is our current goal.

## Task
- [Jorge Salas][1] 
  -Distribution of alcohol across fatalities in greensboro. Analyzing distribution of fatality frequency due to time of day. Analysis of distribution of Fatality Frequency due to month of year. Analysis of Distribution of Fatality Frequency due to specific year. 

- [Daniel Frye][2]
  -Visualization of the data, mapping with plotly and folium to create interactive maps.

- [Dmithra Ratnayake][3]
  -Identify pedestrian collision hotspots and contributing factors.

- [Sahiti Vanteru][4]
  -Poisson distribution between accidents on weekends and weekdays and time intervals ,hypothesis testing , Prediction of accidents based on time series data,random forest classification based on weather attributes.

- [Byungjin Kang][5]
  -Investigate the relationship between Greensboro population and collision. Analyze the number of collisions with Greensboro population across blocks designed by the Census

## Results Obtained
- [Byungjin Kang][5]
  - Implemented a shapefile of block and merged the shapefile with population data
  - Obtained a scatter plot of the number of collision and the Greensboro population
  - Since the Census had different standard of dividing region into blocks, some blocks are on the border of Greensboro so that the population of the blocks include both inside and outside of Greensboro. This made me difficult to distinguish. Even though the population increases, the number of collision is likely to stay the same. And p-value was too high.
  - There were some areas located on the west and the middle of guilford county that have outstanding number of collisions
  
-[Sahithi Vanteru][4]
-Plotted poissons distribution among frequency of accidents on weekdays and weekends and also in day time interval and night time interval.
-Performed T-test on the distributions and rejected to fail null hypothesis on distribution of weekdays and weekends data and accepted the null hypothesis failure for distribution among time intervals data.
- Performed ARIMA (Automated Regression and Integration of Moving Averages) time series model to predict the trends of accidents for years 2019 and 202 and the accuracy for the model was 69.8%.
-Performed random forest classification for weather data that has severity levels of 1 to 10 and compred to kNearest and decision tree classifiers and found out that decision tre eclassifier gives maximum accuracy of around 78%.

-[Dmithra Ratnayake][3]
 - Identified 5 pedestrian collision hotspots which have more than 5 collision in an individual location by conducting DBSCAN unsupervised learning method with a maximum distance of 25 meters and a minimum cluster size of 1. Those locations are,
	- 4302 BIG TREE WAY / W WENDOVER AV
	- 4424 W WENDOVER AV / BRIDFORD PKWY
	- S AYCOCK ST / WALKER AV
	- E MARKET ST / S ELM ST
	- 3106 SUMMIT AV.
 - Random forest classification model indicated that the day of the week and time of the collision are the most important features for collision severity.
 - Further analysis indicated that most sever collisions are occuring during Fridays and during night time.

## Software Required
  ### Required modules:
  - conda install geopandas
    - Provides GeoDataFrame which can deal with geometry or points data
  
  ### Required libraries:
  - shapely
    - Provides 'contains' function which return boolean value if a point is within a polygon.
  - numpy
  - pandas
  - statsmodel

## References
[1]: https://github.com/SALASJA
[2]: https://github.com/danfrye
[3]: https://github.com/C-001
[4]: https://github.com/Sahithi999
[5]: https://github.com/B-kang2
