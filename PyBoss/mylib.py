# File Name: mylib.py
# Date: 12-10-2018
# Author: Zhen Yang
# Purpose: This is a library file that contains the following functions:
# - lookupState
# Go to the function to see detailed information

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Split Name into separate First Name and Last Name columns.
# input: first last
# return: first,last
def formatName(old_name):
    new_name = old_name.split()
    return f"{new_name[0]},{new_name[1]}"

# Re-write the DOB data into MM/DD/YYYY format.
# input: 0000-00-00
# return: 00/00/0000
def formatDate(old_date):
    new_date = old_date.split('-')
    return f"{new_date[1]}/{new_date[2]}/{new_date[0]}"

# Re-write SSN data to hide the first five numbers.
# input: 000-00-0000
# return: ***-**-0000
def formatSSN(old_ssn):
    last4 = old_ssn[7:11]
    return f"***-**-{last4}"

# Look up abbrevation of state name in dictionary us_state_abbrev defined above
# input: full state name
# return: 2 letter state abbrev or Invalid State if the state name is not found in the library
def formatState(state):

    if (state in us_state_abbrev):
        return us_state_abbrev[state]
    else:
        return "Invalid State"

