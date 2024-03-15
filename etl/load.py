import os


def load_ons_data(train, test, data_folder):
    if not os.path.exists(os.path.join(".", data_folder)):
        os.mkdir(os.path.join(".", data_folder))

    train.to_parquet(os.path.join(".", data_folder, "train.parquet"))
    test.to_parquet(os.path.join(".", data_folder, "test.parquet"))
