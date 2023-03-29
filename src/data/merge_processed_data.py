import pandas as pd
import os


def main():
    root_dir = os.path.abspath(os.path.join(
        os.path.dirname(__file__), '../..'))

    air_proc = os.path.join(root_dir, 'data', 'preprocessed', 'data_air.csv')
    we_proc = os.path.join(root_dir, 'data', 'preprocessed', 'data_we.csv')
    merged = os.path.join(root_dir, 'data', 'processed', 'current_data.csv')


    print('Merging data...')
    csv = pd.read_csv(air_proc, encoding='utf_8')
    df = pd.DataFrame(csv)

    csv = pd.read_csv(we_proc, encoding='utf_8')
    df1 = pd.DataFrame(csv)

    start = df['date'].iloc[0]
    end = df['date'].iloc[-1]

    start_index = df1.loc[df1['date'] == start].index[0]
    end_index = df1.loc[df1['date'] == end].index[0]
    df1 = df1.iloc[start_index:end_index + 1]

    df = df.reset_index(drop=True)
    df1 = df1.reset_index(drop=True)

    merged_df = pd.merge(df1, df, on='date', how='inner')
    merged_df = merged_df.drop(columns='date')

    print('Saving processed data...')
    merged_df.to_csv(merged, index=False)

    print('Finished!')

if __name__ == '__main__':
    main()