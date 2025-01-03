# List of possible years
years = [str(year) for year in range(1950, 2026)]

# List of UN recognized countries
countries = [
    "afghanistan", "albania", "algeria", "andorra", "angola", "antiguaandbarbuda", "argentina", "armenia",
    "australia", "austria", "azerbaijan", "bahamas", "bahrain", "bangladesh", "barbados", "belarus", "belgium",
    "belize", "benin", "bhutan", "bolivia", "bosniaandherzegovina", "botswana", "brazil", "brunei", "bulgaria",
    "burkinafaso", "burundi", "cabo_verde", "cambodia", "cameroon", "canada", "centralafricanrepublic", "chad",
    "chile", "china", "colombia", "comoros", "congo", "costarica", "croatia", "cuba", "cyprus", "czechia",
    "democraticrepublicofthecongo", "denmark", "djibouti", "dominica", "dominicanrepublic", "ecuador", "egypt",
    "elsalvador", "equatorialguinea", "eritrea", "estonia", "eswatini", "ethiopia", "fiji", "finland", "france",
    "gabon", "gambia", "georgia", "germany", "ghana", "greece", "grenada", "guatemala", "guinea", "guinea-bissau", "guineabissau",
    "guyana", "haiti", "honduras", "hungary", "iceland", "india", "indonesia", "iran", "iraq", "ireland", "israel",
    "italy", "jamaica", "japan", "jordan", "kazakhstan", "kenya", "kiribati", "kuwait", "kyrgyzstan", "laos",
    "latvia", "lebanon", "lesotho", "liberia", "libya", "liechtenstein", "lithuania", "luxembourg", "madagascar",
    "malawi", "malaysia", "maldives", "mali", "malta", "marshallislands", "mauritania", "mauritius", "mexico",
    "micronesia", "moldova", "monaco", "mongolia", "montenegro", "morocco", "mozambique", "myanmar", "namibia",
    "nauru", "nepal", "netherlands", "newzealand", "nicaragua", "niger", "nigeria", "northkorea", "northmacedonia",
    "norway", "oman", "pakistan", "palau", "palestine", "panama", "papuanewguinea", "paraguay", "peru", "philippines",
    "poland", "portugal", "qatar", "romania", "russia", "rwanda", "saintkittsandnevis", "saintlucia",
    "saintvincentandthegrenadines", "samoa", "sanmarino", "saotomeandprincipe", "saudiarabia", "senegal", "serbia",
    "seychelles", "sierraleone", "singapore", "slovakia", "slovenia", "solomonislands", "somalia", "southafrica",
    "southkorea", "southsudan", "spain", "srilanka", "sudan", "suriname", "sweden", "switzerland", "syria", "taiwan",
    "tajikistan", "tanzania", "thailand", "timor-leste", "timorleste", "togo", "tonga", "trinidadandtobago", "tunisia", "turkey",
    "turkmenistan", "tuvalu", "uganda", "ukraine", "unitedarabemirates", "unitedkingdom", "unitedstates", "usa", "theunitedstatesofamerica", "unitedstatesofamerica", "uruguay",
    "uzbekistan", "vanuatu", "vaticancity", "venezuela", "vietnam", "yemen", "zambia", "zimbabwe"
]

wordlist = [f"{year}{country}" for year in years for country in countries]

with open("wordlist.txt", "w") as file:
    for word in wordlist:
        file.write(word + "\n")

print("Wordlist generated and saved as 'wordlist.txt'.")
