from etl import extract_ons_data, transform_ons_data, load_ons_data


start_year = 2000
end_year_train = 2018
end_year = 2020
data_folder = "data"

print("Extract")
all_train, all_test = extract_ons_data(start_year, end_year_train, end_year)
print("Transform")
train, test = transform_ons_data(all_train, all_test)
print("Load")
load_ons_data(train, test, data_folder)
