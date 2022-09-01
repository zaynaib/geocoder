# geocoder

oemc_output_data2.csv : input/cook_locations.csv input/oemc_locations.csv
	python src/geocoder.py

clean :
	rm oemc_output_data2.csv