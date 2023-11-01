import pandas as pd

# Load your dataset into a DataFrame (replace 'your_data.csv' with your actual data file)
file_path = './stellar_data_VizieR.csv'
df = pd.read_csv(file_path)

column_names = ['Cl', 'N', 'ID', 'B-V', 'Vmag', 'LC', 'log.Teff [K]', 'logL [solLum]', 'Age [yr]', 'Mass[solMass]', 'Prob [0/100]']

# Define the column descriptions
column_descriptions = [
    "Cluster Number",
    "Running number within each cluster",
    "Star number in UBV source",
    "B-V color index",
    "V magnitude",
    "Adopted luminosity class",
    "Logarithm of effective temperature",
    "Logarithm of luminosity",
    "Age of the star (Note)",
    "Mass of the star",
    "Probability of Age and Mass"
]

df.columns = column_names

# Add the row of column descriptions below the header
df.loc[-1] = column_descriptions
df.index = df.index + 1
df = df.sort_index()

# Export the DataFrame back to the Excel file with the updated column names and descriptions
df.to_csv(file_path, index=False, encoding='utf-8')

print("Column names and descriptions updated in both DataFrame and Excel sheet.")
