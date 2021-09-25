
#  ELT Pipeline using MySQL, DBT, Airflow and Spark

- The purpose of this challenge is to build an ELT pipeline in which dataware house transformations are carried out using models created in the dbt.

### Data

-The data contains all of the 30-second raw sensor data from January to October 2016 for the location of the I80 corridor near Davis, CA.

- Summary statistics for each station can be found [here.](https://anson.ucdavis.edu/~clarkf/station_summary.csv)
- Median of total flow for each weekday. Could be used to make animation can be found [here.](https://anson.ucdavis.edu/~clarkf/weekday.csv.gz)
- 30-second time series for a single station (Richards Ave) near downtown Davis can be found [here.](https://anson.ucdavis.edu/~clarkf/richards.csv.gz)
- The medians for each observation grouped by (station, weekday, hour, half a minute) can be found [here.](https://anson.ucdavis.edu/~clarkf/I80_median.csv.gz)
- Metadata is small- just 53 stations can be found [here.](https://anson.ucdavis.edu/~clarkf/I80_stations.csv)
- Main data is around 35 million observations can be found [here.](https://anson.ucdavis.edu/~clarkf/I80_davis.txt.gz)

### Resources:
-  [dbt](https://docs.getdbt.com/docs/introduction)
- [Apache Airflow](https://airflow.apache.org/) 


