import pandas as pd


def transform_ons_data(all_train, all_test):
    train = pd.concat(all_train)
    test = pd.concat(all_test)

    train["din_instante"] = pd.to_datetime(train["din_instante"])
    train = train.set_index("din_instante")

    test["din_instante"] = pd.to_datetime(test["din_instante"])
    test = test.set_index("din_instante")

    train = (
        train.groupby(
            [
                "id_subsistema",
                "id_estado",
                "cod_modalidadeoperacao",
                "nom_tipousina",
                "nom_tipocombustivel",
                "nom_usina",
            ]
        )[["val_geracao"]]
        .resample("MS")
        .sum()
        .reset_index()
        .set_index("din_instante")
        .sort_index()
    )

    test = (
        test.groupby(
            [
                "id_subsistema",
                "id_estado",
                "cod_modalidadeoperacao",
                "nom_tipousina",
                "nom_tipocombustivel",
                "nom_usina",
            ]
        )[["val_geracao"]]
        .resample("MS")
        .sum()
        .reset_index()
        .set_index("din_instante")
        .sort_index()
    )

    return train, test
