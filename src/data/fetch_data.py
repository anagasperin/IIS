import pandas as pd
import json


def refactoring(data):
    new_data = {}
    for key, value in data.items():
        if isinstance(value, str) and '<' in value:
            value = int(value.split('<')[1])
        if value != '':
            new_data[key] = value
    return new_data


def process_data(src, dist):
    f = open(src, 'r', encoding='utf-8')
    raw = json.load(f)
    f.close()

    #print('Transforming json to pandas dataframe...')
    # prilagodimo json dataframe-u
    data = []
    for item in raw:
        jdata = json.loads(item['json'])
        station = jdata['arsopodatki']['postaja']
        for d in station:
            data.append(refactoring(d))

    df = pd.DataFrame(data)

    #print('Filling missing numerical data...')
    # nadomestimo numericne podatke
    stevilski = df.select_dtypes(include=['number']).columns
    for col in stevilski:
        df[col].fillna((df[col].mean()), inplace=True)

    #print('Transforming categorical data...')
    # kategoricni podatki
    df_location = pd.get_dummies(df['merilno_mesto'])
    df = pd.concat([df, df_location], axis=1).reindex(df.index)

    #print('Dropping unuseful columns...')
    # neuporabni podatki
    df.pop('merilno_mesto')
    df.pop('sifra')
    df.pop('datum_od')
    df.pop('datum_do')

    #print('Saving processed data...')

    df = df[sorted(df)]
    df.to_csv(dist, index=False)

    #print('Finished!')


if __name__ == '__main__':
    import os

    root_dir = os.path.abspath(os.path.join(
        os.path.dirname(__file__), '../..'))

    src = os.path.join(root_dir, 'data', 'raw.json')
    dist = os.path.join(root_dir, 'data', 'processed.csv')

    process_data(src, dist)