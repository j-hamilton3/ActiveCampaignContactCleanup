from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pandas as pd
import re
from pathlib import Path

VALID_PROVINCES_STATES = [
    "AB", "MB", "SK", "BC", "ON", "QC", "NS", "NB", "NL", "PE",
    "NU", "NT", "YT",
    "AL", "AK", "AS", "AZ", "AR", "CA", "CO", "CT", "DE", "DC",
    "FL", "GA", "GU", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
    "LA", "ME", "MH", "MD", "MA", "MI", "MN", "MS", "MO", "MT",
    "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "MP", "OH",
    "OK", "OR", "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UT",
    "VT", "VI", "VA", "WA", "WV", "WI", "WY"
]

VALID_COUNTRIES = [
    "Canada", "United States", "Afghanistan", "Åland", "Albania",
    "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla",
    "Antarctica", "Antigua and Barbuda", "Argentina", "Armenia",
    "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain",
    "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin",
    "Bermuda", "Bhutan", "Bolivia", "Bonaire, Sint Eustatius, and Saba",
    "Bosnia and Herzegovina", "Botswana", "Bouvet Island", "Brazil", 
    "British Indian Ocean Territory", "Brunei Darussalam", "Bulgaria",
    "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon",
    "Cayman Islands", "Central African Republic", "Chad", "Chile", "China",
    "Christmas Island", "Cocos (Keeling) Islands", "Colombia", "Comoros",
    "Congo", "Democratic Republic of the Congo",
    "Cook Islands", "Costa Rica", "Cote D'Ivoire", "Croatia", "Cuba", "Curaçao", "Cyprus",
    "Czechia", "Denmark", "Djibouti", "Dominica", "Dominican Republic",
    "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea",
    "Estonia", "Eswatini", "Ethiopia", "Falkland Islands (Malvinas)",
    "Faroe Islands", "Fiji", "Finland", "France", "French Guiana",
    "French Polynesia", "French Southern Territories", "Gabon", "Gambia",
    "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland",
    "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guernsey", "Guinea",
    "Guinea-Bissau", "Guyana", "Haiti", "Heard Island and McDonald Islands",
    "Holy See (Vatican City State)", "Honduras", "Hong Kong", "Hungary", "Iceland", "India",
    "Indonesia", "Iran", "Iraq", "Ireland", "Isle of Man", "Israel", "Italy",
    "Jamaica", "Japan", "Jersey", "Jordan", "Kazakhstan", "Kenya",
    "Kiribati","Democratic People's Republic of Korea", "Republic of Korea", "Kuwait", "Kyrgyzstan", "Lao People's Democratic Republic", "Latvia", "Lebanon", "Lesotho",
    "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macao",
    "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands",
    "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia",
    "Moldova", "Monaco", "Mongolia", "Montenegro", "Montserrat", "Morocco",
    "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands",
    "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue",
    "Norfolk Island", "North Macedonia", "Northern Mariana Islands",
    "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama",
    "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn", "Poland",
    "Portugal", "Puerto Rico", "Qatar", "Réunion", "Romania", "Russian Federation", "Rwanda",
    "Saint Barthélemy", "Saint Helena, Ascension, Tristan da Cunha",
    "Saint Kitts and Nevis", "Saint Lucia", "Saint Martin",
    "Saint Pierre and Miquelon", "Saint Vincent and the Grenadines", "Samoa",
    "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia",
    "Seychelles", "Sierra Leone", "Singapore", "Sint Maarten",
    "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa",
    "South Georgia and the South Sandwich Islands", "South Sudan",
    "Spain", "Sri Lanka", "Sudan", "Suriname", "Svalbard and Jan Mayen",
    "Sweden", "Switzerland", "Syrian Arab Repbublic", "Taiwan, Province of China", "Tajikistan", " United Republic of Tanzania", "Thailand",
    "Timor-Leste", "Togo", "Tokelau", "Tonga", "Trinidad and Tobago", "Tunisia",
    "Türkiye", "Turkmenistan", "Turks and Caicos Islands", "Tuvalu", "Uganda",
    "Ukraine", "United Arab Emirates", "United Kingdom", 
    "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Wallis and Futuna",
    "Western Sahara", "Yemen", "Zambia", "Zimbabwe"
]


VALID_SECTORS = ["BU", "ED", "GO", "IN", "ING", "PA", "PT", "SS", "SW"]

VALID_CONSENTS = ["Yes", "No", "Implied", "Shared"]

## Program Starts
print("*** Welcome to AC Contact Cleanup! ***")
print("Please select your properly formatted excel file:")
print("WARNING - File contents will be overwritten.")
print("**************************************")
print()

## Prompt User to Select a file.
filepath= askopenfilename()

try:
    excel_data = pd.read_excel(filepath)

    for index, row in excel_data.iterrows():
        
        ## DATA SANITIZATION

        ## Remove Spaces from email
        if pd.notna(row["Email"]):
            excel_data.at[index, 'Email'] = row["Email"].replace(" ", "")
    
        ## Capitalize sector code, remove spaces.
        if isinstance(row["Sector"], str):
            excel_data.at[index, 'Sector'] = row["Sector"].upper().replace(" ", "")

        ## Capitalize province/state code, remove spaces.
        if isinstance(row["Province/State"], str):
            excel_data.at[index, 'Province/State'] = row["Province/State"].upper().replace(" ", "")

    print("*** DATA SANITIZATION ***")
    print("Removed all spaces from Email, Sector, and Province/State records.")
    print("Capitalized Sector and Province/State codes.")
    print("**************************************")
    print("")

    print("*** DATA VALIDATION: ***")

    validation_passed = True
 
    for index, row in excel_data.iterrows():

        ## DATA VALIDATION

        ## Check for valid email format.
        if type(row["Email"]) != type("String") or not re.match(r"[^@]+@[^@]+\.[^@]+", row["Email"]):
            print(f"Invalid Email on row {index + 2}: {row["Email"]}")
            validation_passed = False
        
        ## Check valid Sector code.
        if row["Sector"] not in VALID_SECTORS:
            print(f"Invalid Sector Code on row {index + 2}: {row['Sector']}")
            validation_passed = False

        # Check for valid country.
        if row["Country"] not in VALID_COUNTRIES:
            print(f"Invalid Country on row {index + 2}: {row['Country']}")
            validation_passed = False
    
        ## Check valid code.
        if row["Province/State"] not in VALID_PROVINCES_STATES:
            print(f"Invalid Province/State Code on row {index + 2}: {row["Province/State"]}")
            validation_passed = False

        # Check for valid consent.
        if row["Consent"] not in VALID_CONSENTS:
            print(f"Invalid Consent on row {index + 2}: {row['Consent']}")
            validation_passed = False

    print("**************************************")
    print("")

    if validation_passed:
        print("ALL DATA IS CLEAN! Download your spreadsheet as .CSV and then upload to Active Campaign.")
        print("")
    else:
        print("DATA HAS ERRORS. Please make changes and re-run this script.")
        print("")

    # Save the cleaned data to the original file
    excel_data.to_excel(filepath, index=False)

    print(f"Data has been saved to {filepath}")
    print("")
    input("Press Enter to exit...")

except PermissionError as pe:
    print("PERMISSION ERROR: The Excel file must be closed to run this script. Please close the Excel file and run again.")
    print(f"Exception details: {pe}")
    input("Press Enter to exit...")
except Exception as e:
    print("ERROR: Please contact jfhhamilton@gmail.com for support :)")
    print(f"Exception details: {e}")
    input("Press Enter to exit...")
 


