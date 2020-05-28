#! /usr/bin/python3

import os

for i in range(1,5):

	os.system("wget https://www2.census.gov/programs-surveys/demo/tables/metro-micro/2015/commuting-flows-2015/table{table_number}.xlsx -O table{table_number}.xlsx".format(table_number=str(i)))