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



def clean_data_dan(new_df, country_profile):
    import pandas as pd
    df_edu = new_df.copy()

    student_table = df_edu[['country', 'international_students', 'rank_display', 'score', 'type', 'Population in thousands (2017)', 'Sex ratio (m per 100 f, 2017)','GDP per capita (current US$)']]
    student_table['international_students'].replace(',', '', regex=True, inplace=True)
    student_table['international_students'] = pd.to_numeric(student_table['international_students'], errors='coerce')
    student_table = student_table.groupby('country').agg({'international_students': 'sum', 'score': 'mean'})
    student_table.rename(columns={'international_students': 'total_international_students', 'score': 'average_score'}, inplace=True)
    country_table = df_edu.groupby('country').agg({'rank_display': 'count'})
    country_table.rename(columns={'rank_display': 'total_universities ranked in 100'}, inplace= True)
    country_table = country_table.merge(student_table, on='country', how='inner')
    country_table['total_international_students'] = country_table['total_international_students'].astype(int)
    country_table['total_universities ranked in 100'] = country_table['total_universities ranked in 100'].astype(int)
    country_table = country_table[['total_universities ranked in 100', 'total_international_students', 'average_score']]
    country_table['average_score'] = country_table['average_score'].round(2)
    new_country_table = merge_dataset(country_table, country_profile, key='country')
    pd.set_option('display.max_columns', None)
    final_df = new_country_table[['country', 'total_universities ranked in 100', 'total_international_students', 'average_score', 'Region', 'Population in thousands (2017)', 'GDP per capita (current US$)', 'Sex ratio (m per 100 f, 2017)', 'Education: Government expenditure (% of GDP)', 'Fertility rate, total (live births per woman)']]
    final_df= final_df[(final_df['Population in thousands (2017)'] >= 0) & (final_df['Education: Government expenditure (% of GDP)'] >= 0)]
    return final_df


def plot_graph_edu_ranked_uni(final_df):
    import plotly.express as px
    
    fig = px.scatter(final_df, x='Education: Government expenditure (% of GDP)', y='total_universities ranked in 100', color='Region', size='average_score', hover_name='country', title='Total Universities Ranked in 100 vs Total International Students')
    fig.show()