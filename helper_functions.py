def uninversity_data_cleaning(df_uni):
    import pandas as pd

    # Check if 'link' and 'logo' columns exist in the dataframe and drop it 
    if 'link' in df_uni.columns and 'logo' in df_uni.columns:
        # Drop 'link' and 'logo' columns
        df_uni = df_uni.drop(['link', 'logo'], axis=1)

    # make these column to numeric 
    df_uni['rank_display'] = pd.to_numeric(df_uni['rank_display'], errors='coerce')
    df_uni['score'] = pd.to_numeric(df_uni['score'], errors='coerce')
    df_uni['international_students'] = pd.to_numeric(df_uni['international_students'], errors='coerce')

    # only take the top 100 universities
    df_rank_100 = df_uni[df_uni['rank_display'] <= 100]

    # make a new dataframe filter year = 2017  our main dataset
    df_2017 = df_rank_100[df_rank_100['year'] == 2017]

    return df_2017


def country_data_cleaning(country_profile):
    import pandas as pd

    # Convert columns to numeric
    for col in country_profile.columns[2:]:
        country_profile[col] = pd.to_numeric(country_profile[col], errors='coerce')
    # Replace country names to match the university dataset
    country_profile['country'].replace({'China': 'China (Mainland)', 
                                    'Democratic People\'s Republic of Korea': 'South Korea', 
                                    'United States of America': 'United States',
                                    'Viet Nam': 'Vietnam',
                                    'Iran (Islamic Republic of)': 'Iran, Islamic Republic of',
                                    'China, Hong Kong SAR': 'Hong Kong SAR'
                                    }, 
                                    inplace=True)

    return country_profile


def merge_dataset(df_2017, country_profile, key='country'):
    import pandas as pd

    # Merge two datasets
    # df1: DataFrame 1
    # df2: DataFrame 2
    # key: column to merge on
    # return: merged DataFrame
    return pd.merge(df_2017, country_profile, on=key, how = 'left')
