# Required Fields:
# (Email, Sector, Country, Province/State, Consent)

# Process:
	# Remove spaces from email, valid email.

	# Check for Provinces/States (LIST ON ACTIVE CAMPAIGN) 
    # - Valid two digit province/state code. (Make sure everthing is uppercase.)

	# Check for Valid Country (LIST ON ACTIVE CAMPAIGN)

	# Check for Valid Sector (LIST ON ACTIVE CAMPAIGN) 
    # If there are blanks fill with default (CTRI - SS, ACHIEVE - GO ) (Make sure everything is uppercase.)

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

