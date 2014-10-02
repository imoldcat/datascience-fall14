import pandas as pd
import avro.schema
from avro.datafile import DataFileReader 
from avro.io import DatumReader

# create pandas data frame
countries_df = pd.DataFrame(columns=('country_id', 'name', 'area_sqkm', 'population', 'description'))

# parse the avro data and insert to dataframe
schema = avro.schema.parse(open("country.avsc").read())
curr = 1
reader = DataFileReader(open("countries.avro", "r"), DatumReader())
for c in reader:
	countries_df.loc[curr] = [c['country_id'], c['name'], c['area_sqkm'], c['population'], c['description']]
	curr = curr + 1
reader.close()

# query dataframe
large_population_countries = countries_df[countries_df['population'] > 10000000]
print "# of countries with population over 10^7 is: ", len(large_population_countries.index)

