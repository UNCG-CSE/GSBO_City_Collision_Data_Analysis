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
