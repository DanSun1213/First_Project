# Project Introduction

In the globalized world, education and economic performance are often seen as interconnected. Understanding the factors that contribute to high-quality education can provide insights for policymakers, educators, and economic planners. This analysis aims to **explore the relationship between economic indicators and university rankings**, using two primary datasets: World University Rankings (2017-2022) and Country Statistics from UNData.

# Research Hypothesis

1. Countries with higher GDP growth rates tend to have higher-ranked universities.
2. Countries with a higher urban population percentage have universities that perform better in global
3. Countries with higher internet penetration rates have better-ranked universities
4. Higher female participation in the labor force is associated with better university rankings in a country.
5. Countries with higher government expenditure on education as a percentage of GDP have more universities in the top 100


# Data Wrangling and cleaning Process
## Collect the two dataset : University & Country Profile

This repository contains a Jupyter notebook (main.ipynb) that collects and processes datasets related to universities and country profiles.

1. **World University Rankings (2017-2022)**: https://www.kaggle.com/datasets/padhmam/qs-world-university-rankings-2017-2022
2. **Country Statistics - UNData**: https://www.kaggle.com/datasets/sudalairajkumar/undata-country-profiles

df_uni = pd.read_csv(r'qs-world-university-rankings-2017-to-2022-V2.csv')
country_profile = pd.read_csv('country_profile_variables.csv')

## Data Cleaning
Starting by individually cleaning each dataset. This ensures that each dataset is free from initial inconsistencies before merging.

`df_2017 = uninversity_data_cleaning(df_uni)`
`df_2017.head()`

`country_profile = country_data_cleaning(country_profile)`
`country_profile.head()`

## Merging Datasets
Once the individual datasets are cleaned, we merge them into a single dataset. This is done based on common keys or identifiers that exist in both datasets.

`new_df = merge_dataset(df_2017, country_profile, key='country')`
`new_df.head()`

## Hypothesis-Based Cleaning:
fter merging, we perform a second round of cleaning based on our analysis hypotheses. This step ensures that the data is tailored to answer the specific questions we are investigating.


# Exploratory Data Analysis



## Findings

1. Countries with higher GDP growth rates tend to have higher-ranked universities. -- ** **
2. Countries with a higher urban population percentage have universities that perform better in global -- ** **
3. Countries with higher internet penetration rates have better-ranked universities -- ** **
4. Higher female participation in the labor force is associated with better university rankings in a country. -- ** **
5. Countries with higher government expenditure on education as a percentage of GDP have more universities in the top 100 -- **Refuted**





## Requirements.txt

- Python = 3.12.4
- pandas = 2.2.2
- plotly.io = = 3.2.1

## Contributing

Feel free to open issues or submit pull requests if you have any improvements or suggestions.
