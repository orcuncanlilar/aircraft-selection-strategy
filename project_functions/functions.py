import pandas as pd

def transform_location(row):

    location = row['Location']
    country = row['Country']
    
    # If Location is NaN, make it 'Unknown'
    if pd.isna(location):
        return 'Unknown'
    
    # If Location and Country are the same, change Location to 'Unknown'
    if not pd.isna(country) and location.lower() == country.lower():
        return 'Unknown'
    
    # If Location contains ', ', split it and take the part after ', '
    if ', ' in location:
        return location.split(', ', 1)[1].strip()
    
    # Return the original Location if none of the conditions are met
    return location
