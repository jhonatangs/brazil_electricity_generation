import pandas as pd


def extract_ons_data(start_year, end_year_train, end_year):
    all_train = [
        pd.read_csv(
            f"https://ons-aws-prod-opendata.s3.amazonaws.com/dataset/geracao_usina_2_ho/GERACAO_USINA_{year}.csv",
            sep=";",
            usecols=[
                "din_instante",
                "id_subsistema",
                "id_estado",
                "cod_modalidadeoperacao",
                "nom_tipousina",
                "nom_tipocombustivel",
                "nom_usina",
                "val_geracao",
            ],
        )
        for year in range(start_year, end_year_train + 1)
    ]

    all_test = [
        pd.read_csv(
            f"https://ons-aws-prod-opendata.s3.amazonaws.com/dataset/geracao_usina_2_ho/GERACAO_USINA_{year}.csv",
            sep=";",
            usecols=[
                "din_instante",
                "id_subsistema",
                "id_estado",
                "cod_modalidadeoperacao",
                "nom_tipousina",
                "nom_tipocombustivel",
                "nom_usina",
                "val_geracao",
            ],
        )
        for year in range(end_year_train + 1, end_year + 1)
    ]

    return all_train, all_test
