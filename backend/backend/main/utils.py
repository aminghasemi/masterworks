from datetime import datetime
from datetime import datetime, timedelta
from django.utils.translation import gettext_lazy as _


# from .custom_auth import BaseJSONWebTokenAuthentication
# from rest_framework.authentication import get_authorization_header

CATEGORY_TYPE = (
    ("Products", "Products"),
    ("Processes", "Processes"),
    ("Resources", "Resources"),
    ("Stakeholders", "Stakeholders"),

)

ROLES = (
    ("SuperAdmin", "SuperAdmin"),
    ("Admin", "Admin"),
    ("Staff", "Staff"),
    ("Trainee", "Trainee"),
    ("Guest", "Guest"),
    ("User", "User"),
    ("Client", "Client"),
)

USER_ROLES = (
    ("Owenership & Joint Venture", "Owenership & Joint Venture"),
    ("Strategic Collaboration", "Strategic Collaboration"),
    ("Arm's Length Transaction", "Arm's Length Transaction"),
    ("Coordination", "Coordination"),
    ("Horizontal Coopertion", "Horizontal Cooperation"),
)


UNITS = (
    ("%", "%"),

    ("-------- LENGTH --------", "-------- LENGTH --------"),
    ("Meter/Metre (m)", "Meter/Metre (m)"),
    ("Millimeter (mm)", "Millimeter (mm)"),
    ("Centimeter (cm)", " Centimeter (cm)"),
    ("Decimeter (dm)", "Decimeter (dm)"),
    ("Kilometer (km)", "Kilometer (km)"),
    ("Inch (in or “)", "Inch (in or “)"),
    ("Link (l., li. or lnk.)", "Link (l., li. or lnk.)"),
    ("Foot (ft)", "Foot (ft)"),
    ("Yard (yd)", "Yard (yd)"),
    ("Mile (mi or m or ml)", "Mile (mi or m or ml)"),
    ("Nautical Mile (sm)", "Nautical Mile (sm)"),
    ("Parsec (pc)", "Parsec (pc)"),

    ("-------- AREA --------", "-------- AREA --------"),

    ("Square meter (sqm or m2)", "Square meter (sqm or m2)"),
    ("Are (a or ares)", "Are (a or ares)"),
    ("Acre (acre)", "Acre (acre)"),
    ("Hectare (ha)", "Hectare (ha)"),
    ("Square inch (in2)", "Square inch (in2)"),
    ("Square feet (ft2)", "Square feet (ft2)"),
    ("Square yard (yd2)", "Square yard (yd2)"),
    ("Square mile (sq mi or mi2)", "Square mile (sq mi or mi2)"),

    ("-------- VOLUME --------", "-------- VOLUME --------"),
    ("Cubic meter (m3)", "Cubic meter (m3)"),
    ("Liter (l)", "Liter (l)"),
    ("Milliliter (ml)", "Milliliter (ml)"),
    ("Centiliter (cl)", "Centiliter (cl)"),
    ("Deciliter (dl)", "Deciliter (dl)"),
    ("Hectoliter (hl) ", "Hectoliter (hl) "),
    ("Megaliter (mL)", "Megaliter (mL)"),
    ("Cubic inch (cu in or in3)", "Cubic inch (cu in or in3)"),
    ("Cubic foot (cu ft or ft3)", "Cubic foot (cu ft or ft3)"),
    ("Cubic yard (cu yd or yd3)", "Cubic yard (cu yd or yd3)"),
    ("Acre-foot (acre ft)", "Acre-foot (acre ft)"),
    ("Teaspoon (tsp)", "Teaspoon (tsp)"),
    ("Tablespoon (tbsp)", "Tablespoon (tbsp)"),
    ("Fluid ounce (fl oz or oz. fl)", "Fluid ounce (fl oz or oz. fl)"),
    ("Cup (cup)", "Cup (cup)"),
    ("Gill (gill)", "Gill (gill)"),
    ("Pint (pt or p)", "Pint (pt or p)"),
    ("Quart (qt)", "Quart (qt)"),
    ("Gallon (gal)", "Gallon (gal)"),


    ("-------- ANGLE --------", "-------- ANGLE --------"),
    ("Radian (rad or c)", "Radian (rad or c)"),
    ("Degree (o or deg)", "Degree (o or deg)"),
    ("Steradian (sr)", "Steradian (sr)"),
    ("Second (s)", "Second (s)"),
    ("Minute (min)", "Minute (min)"),
    ("Hour (h)", "Hour (h)"),
    ("Day (d)", "Day (d)"),
    ("Year (a)", "Year (a)"),


    ("-------- PHYSICS --------", "-------- PHYSICS --------"),
    ("Hertz (Hz)", "Hertz (Hz)"),
    ("Angular frequency (ω)", "Angular frequency (ω)"),
    ("Decible (dB)", "Decible (dB)"),
    ("Kilogram meters per second (kg m/s)", "Kilogram meters per second (kg m/s)"),
    ("Miles per hour (mph)", "Miles per hour (mph)"),
    ("Meters per second (m/s or kph)", "Meters per second (m/s or kph)"),
    ("Gravity imperial (ft/s2)", "Gravity imperial (ft/s2)"),
    ("Gravity metric (m/s2)", "Gravity metric (m/s2)"),
    ("Feet per second (ft/s)", "Feet per second (ft/s)"),


    ("-------- MASS / WEIGHT --------", "-------- MASS / WEIGHT --------"),
    ("Grams (g)", "Grams (g)"),
    ("Kilogram (kg)", "Kilogram (kg)"),
    ("Grain (gr)", "Grain (gr)"),
    ("Dram (dr)", "Dram (dr)"),
    ("Ounce (oz)", "Ounce (oz)"),
    ("Pound (lb)", "Pound (lb)"),
    ("Hundredweight (cwt)", "Hundredweight (cwt)"),
    ("Ton (ton)", "Ton (ton)"),
    ("Tonne (t)", "Tonne (t)"),
    ("Slug (slug)", "Slug (slug)"),
    ("Density (kg/m3)", "Density (kg/m3)"),
    ("Denier (den or D)", "Denier (den or D)"),
    ("Tex (tex)", "Tex (tex)"),
    ("Decitex (dtex)", "Decitex (dtex)"),
    ("Newton (N)", "Newton (N)"),
    ("Kilopond (kp)", "Kilopond (kp)"),

    ("-------- ENERGY --------", "-------- ENERGY --------"),
    ("Pond (p)", "Pond (p)"),
    ("Joule (J)", "Joule (J)"),
    ("Giga joule (GJ)", "Giga joule (GJ)"),
    ("Watt (w)", "Watt (w)"),
    ("Kilowatt (kw)", "Kilowatt (kw)"),
    ("Megawatt per hour (mwh)", "Megawatt per hour (mwh)"),
    ("Horsepower (hp)", "Horsepower (hp)"),

    ("-------- PRESSURE --------", "-------- PRESSURE --------"),
    ("Bar (bar)", "Bar (bar)"),
    ("Pascal (Pa)", "Pascal (Pa)"),
    ("Pounds per square inch (psi or lbf/in2)", "Pounds per square inch (psi or lbf/in2)"),

    ("-------- TEMPRETURE  --------", "-------- TEMPRETURE  --------"),
    ("Kelvin (K)", "Kelvin (K)"),
    ("Calorie (Q)", "Calorie (Q)"),
    ("Fahrenheit (oF)", "Fahrenheit (oF)"),

    ("-------- LIGHT --------", "-------- LIGHT --------"),
    ("Candela (cd)", "Candela (cd)"),
    ("Lumen (lm)", "Lumen (lm)"),
    ("Lux (lx)", "Lux (lx)"),
    ("Lumen seconds (ls)", "Lumen seconds (ls)"),

    ("-------- ELECTRICAL --------", "-------- ELECTRICAL --------"),
    ("Diopter (dpt)", "Diopter (dpt)"),
    ("Ampere (Amps)", "Ampere (Amps)"),
    ("Coulomb (C)", "Coulomb (C)"),
    ("Volt (V)", "Volt (V)"),
    ("Ohm (Ω)", "Ohm (Ω)"),
    ("Farad (F)", "Farad (F)"),
    ("Siemens (S)", "Siemens (S)"),
    ("Henry (H)", "Henry (H)"),
    ("Weber (Wb)", "Weber (Wb)"),
    ("Tesla (T)", "Tesla (T)"),
    ("Becquerel (Bq)", "Becquerel (Bq)"),
    ("Mole (mol)", "Mole (mol)"),
    ("Paper bale (ream)", "Paper bale (ream)"),
    ("Dozen (dz or doz)", "Dozen (dz or doz)"),

    ("-------- CURRENCY --------", "-------- CURRENCY --------"),
    ("Euro (€)", "Euro (€)"),
    ("US dollar (USD or $)", "US dollar (USD or $)"),
)

INDCHOICES = (
    ("Advertisement", "Advertisement"),
    ("Agriculture", "Agriculture"),
    ("Textile", "Textile"),
    ("Automotive", "Automotive"),
    ("Banking", "Banking"),
    ("Biotechnology", "Biotechnology"),
    ("Construction", "Construction"),
    ("Chemical", "Chemical"),
    ("Computer", "Computer"),
    ("Education", "Eduction"),
    ("Electronics", "Electronics"),
    ("Energy", "Energy"),
    ("Entertainment", "Entertainment"),
    ("Financial", "Financial"),
    ("Food", "Food"),
    ("Health", "Health"),
    ("Insurance", "Insurance"),
    ("law", "Law"),
    ("Manufacturing", "Manufacturing"),
    ("Publication", "Publication"),
    ("Real State", "Real State"),
    ("Services", "Services"),
    ("Software", "Software"),
    ("Sport", "Sport"),
    ("Technology", "Technology"),
    ("Communication", "Communication"),
    ("Transportation", "Transportation"),
    ("Investing", "Investing"),
)



COUNTRIES_ALL = (
    ("GB", _("United Kingdom")),
    ("AF", _("Afghanistan")),
    ("AX", _("Aland Islands")),
    ("AL", _("Albania")),
    ("DZ", _("Algeria")),
    ("AS", _("American Samoa")),
    ("AD", _("Andorra")),
    ("AO", _("Angola")),
    ("AI", _("Anguilla")),
    ("AQ", _("Antarctica")),
    ("AG", _("Antigua and Barbuda")),
    ("AR", _("Argentina")),
    ("AM", _("Armenia")),
    ("AW", _("Aruba")),
    ("AU", _("Australia")),
    ("AT", _("Austria")),
    ("AZ", _("Azerbaijan")),
    ("BS", _("Bahamas")),
    ("BH", _("Bahrain")),
    ("BD", _("Bangladesh")),
    ("BB", _("Barbados")),
    ("BY", _("Belarus")),
    ("BE", _("Belgium")),
    ("BZ", _("Belize")),
    ("BJ", _("Benin")),
    ("BM", _("Bermuda")),
    ("BT", _("Bhutan")),
    ("BO", _("Bolivia")),
    ("BA", _("Bosnia and Herzegovina")),
    ("BW", _("Botswana")),
    ("BV", _("Bouvet Island")),
    ("BR", _("Brazil")),
    ("IO", _("British Indian Ocean Territory")),
    ("BN", _("Brunei Darussalam")),
    ("BG", _("Bulgaria")),
    ("BF", _("Burkina Faso")),
    ("BI", _("Burundi")),
    ("KH", _("Cambodia")),
    ("CM", _("Cameroon")),
    ("CA", _("Canada")),
    ("CV", _("Cape Verde")),
    ("KY", _("Cayman Islands")),
    ("CF", _("Central African Republic")),
    ("TD", _("Chad")),
    ("CL", _("Chile")),
    ("CN", _("China")),
    ("CX", _("Christmas Island")),
    ("CC", _("Cocos (Keeling) Islands")),
    ("CO", _("Colombia")),
    ("KM", _("Comoros")),
    ("CG", _("Congo")),
    ("CD", _("Congo, The Democratic Republic of the")),
    ("CK", _("Cook Islands")),
    ("CR", _("Costa Rica")),
    ("CI", _("Cote d'Ivoire")),
    ("HR", _("Croatia")),
    ("CU", _("Cuba")),
    ("CY", _("Cyprus")),
    ("CZ", _("Czech Republic")),
    ("DK", _("Denmark")),
    ("DJ", _("Djibouti")),
    ("DM", _("Dominica")),
    ("DO", _("Dominican Republic")),
    ("EC", _("Ecuador")),
    ("EG", _("Egypt")),
    ("SV", _("El Salvador")),
    ("GQ", _("Equatorial Guinea")),
    ("ER", _("Eritrea")),
    ("EE", _("Estonia")),
    ("ET", _("Ethiopia")),
    ("FK", _("Falkland Islands (Malvinas)")),
    ("FO", _("Faroe Islands")),
    ("FJ", _("Fiji")),
    ("FI", _("Finland")),
    ("FR", _("France")),
    ("GF", _("French Guiana")),
    ("PF", _("French Polynesia")),
    ("TF", _("French Southern Territories")),
    ("GA", _("Gabon")),
    ("GM", _("Gambia")),
    ("GE", _("Georgia")),
    ("DE", _("Germany")),
    ("GH", _("Ghana")),
    ("GI", _("Gibraltar")),
    ("GR", _("Greece")),
    ("GL", _("Greenland")),
    ("GD", _("Grenada")),
    ("GP", _("Guadeloupe")),
    ("GU", _("Guam")),
    ("GT", _("Guatemala")),
    ("GG", _("Guernsey")),
    ("GN", _("Guinea")),
    ("GW", _("Guinea-Bissau")),
    ("GY", _("Guyana")),
    ("HT", _("Haiti")),
    ("HM", _("Heard Island and McDonald Islands")),
    ("VA", _("Holy See (Vatican City State)")),
    ("HN", _("Honduras")),
    ("HK", _("Hong Kong")),
    ("HU", _("Hungary")),
    ("IS", _("Iceland")),
    ("IN", _("India")),
    ("ID", _("Indonesia")),
    ("IR", _("Iran, Islamic Republic of")),
    ("IQ", _("Iraq")),
    ("IE", _("Ireland")),
    ("IM", _("Isle of Man")),
    ("IL", _("Israel")),
    ("IT", _("Italy")),
    ("JM", _("Jamaica")),
    ("JP", _("Japan")),
    ("JE", _("Jersey")),
    ("JO", _("Jordan")),
    ("KZ", _("Kazakhstan")),
    ("KE", _("Kenya")),
    ("KI", _("Kiribati")),
    ("KP", _("Korea, Democratic People's Republic of")),
    ("KR", _("Korea, Republic of")),
    ("KW", _("Kuwait")),
    ("KG", _("Kyrgyzstan")),
    ("LA", _("Lao People's Democratic Republic")),
    ("LV", _("Latvia")),
    ("LB", _("Lebanon")),
    ("LS", _("Lesotho")),
    ("LR", _("Liberia")),
    ("LY", _("Libyan Arab Jamahiriya")),
    ("LI", _("Liechtenstein")),
    ("LT", _("Lithuania")),
    ("LU", _("Luxembourg")),
    ("MO", _("Macao")),
    ("MK", _("Macedonia, The Former Yugoslav Republic of")),
    ("MG", _("Madagascar")),
    ("MW", _("Malawi")),
    ("MY", _("Malaysia")),
    ("MV", _("Maldives")),
    ("ML", _("Mali")),
    ("MT", _("Malta")),
    ("MH", _("Marshall Islands")),
    ("MQ", _("Martinique")),
    ("MR", _("Mauritania")),
    ("MU", _("Mauritius")),
    ("YT", _("Mayotte")),
    ("MX", _("Mexico")),
    ("FM", _("Micronesia, Federated States of")),
    ("MD", _("Moldova")),
    ("MC", _("Monaco")),
    ("MN", _("Mongolia")),
    ("ME", _("Montenegro")),
    ("MS", _("Montserrat")),
    ("MA", _("Morocco")),
    ("MZ", _("Mozambique")),
    ("MM", _("Myanmar")),
    ("NA", _("Namibia")),
    ("NR", _("Nauru")),
    ("NP", _("Nepal")),
    ("NL", _("Netherlands")),
    ("AN", _("Netherlands Antilles")),
    ("NC", _("New Caledonia")),
    ("NZ", _("New Zealand")),
    ("NI", _("Nicaragua")),
    ("NE", _("Niger")),
    ("NG", _("Nigeria")),
    ("NU", _("Niue")),
    ("NF", _("Norfolk Island")),
    ("MP", _("Northern Mariana Islands")),
    ("NO", _("Norway")),
    ("OM", _("Oman")),
    ("PK", _("Pakistan")),
    ("PW", _("Palau")),
    ("PS", _("Palestinian Territory, Occupied")),
    ("PA", _("Panama")),
    ("PG", _("Papua New Guinea")),
    ("PY", _("Paraguay")),
    ("PE", _("Peru")),
    ("PH", _("Philippines")),
    ("PN", _("Pitcairn")),
    ("PL", _("Poland")),
    ("PT", _("Portugal")),
    ("PR", _("Puerto Rico")),
    ("QA", _("Qatar")),
    ("RE", _("Reunion")),
    ("RO", _("Romania")),
    ("RU", _("Russian Federation")),
    ("RW", _("Rwanda")),
    ("BL", _("Saint Barthelemy")),
    ("SH", _("Saint Helena")),
    ("KN", _("Saint Kitts and Nevis")),
    ("LC", _("Saint Lucia")),
    ("MF", _("Saint Martin")),
    ("PM", _("Saint Pierre and Miquelon")),
    ("VC", _("Saint Vincent and the Grenadines")),
    ("WS", _("Samoa")),
    ("SM", _("San Marino")),
    ("ST", _("Sao Tome and Principe")),
    ("SA", _("Saudi Arabia")),
    ("SN", _("Senegal")),
    ("RS", _("Serbia")),
    ("SC", _("Seychelles")),
    ("SL", _("Sierra Leone")),
    ("SG", _("Singapore")),
    ("SK", _("Slovakia")),
    ("SI", _("Slovenia")),
    ("SB", _("Solomon Islands")),
    ("SO", _("Somalia")),
    ("ZA", _("South Africa")),
    ("GS", _("South Georgia and the South Sandwich Islands")),
    ("ES", _("Spain")),
    ("LK", _("Sri Lanka")),
    ("SD", _("Sudan")),
    ("SR", _("Suriname")),
    ("SJ", _("Svalbard and Jan Mayen")),
    ("SZ", _("Swaziland")),
    ("SE", _("Sweden")),
    ("CH", _("Switzerland")),
    ("SY", _("Syrian Arab Republic")),
    ("TW", _("Taiwan, Province of China")),
    ("TJ", _("Tajikistan")),
    ("TZ", _("Tanzania, United Republic of")),
    ("TH", _("Thailand")),
    ("TL", _("Timor-Leste")),
    ("TG", _("Togo")),
    ("TK", _("Tokelau")),
    ("TO", _("Tonga")),
    ("TT", _("Trinidad and Tobago")),
    ("TN", _("Tunisia")),
    ("TR", _("Turkey")),
    ("TM", _("Turkmenistan")),
    ("TC", _("Turks and Caicos Islands")),
    ("TV", _("Tuvalu")),
    ("UG", _("Uganda")),
    ("UA", _("Ukraine")),
    ("AE", _("United Arab Emirates")),
    ("US", _("United States")),
    ("UM", _("United States Minor Outlying Islands")),
    ("UY", _("Uruguay")),
    ("UZ", _("Uzbekistan")),
    ("VU", _("Vanuatu")),
    ("VE", _("Venezuela")),
    ("VN", _("Viet Nam")),
    ("VG", _("Virgin Islands, British")),
    ("VI", _("Virgin Islands, U.S.")),
    ("WF", _("Wallis and Futuna")),
    ("EH", _("Western Sahara")),
    ("YE", _("Yemen")),
    ("ZM", _("Zambia")),
    ("ZW", _("Zimbabwe")),
)

CURRENCY_CODES = (
    ("AED", _("AED, Dirham")),
    ("AFN", _("AFN, Afghani")),
    ("ALL", _("ALL, Lek")),
    ("AMD", _("AMD, Dram")),
    ("ANG", _("ANG, Guilder")),
    ("AOA", _("AOA, Kwanza")),
    ("ARS", _("ARS, Peso")),
    ("AUD", _("AUD, Dollar")),
    ("AWG", _("AWG, Guilder")),
    ("AZN", _("AZN, Manat")),
    ("BAM", _("BAM, Marka")),
    ("BBD", _("BBD, Dollar")),
    ("BDT", _("BDT, Taka")),
    ("BGN", _("BGN, Lev")),
    ("BHD", _("BHD, Dinar")),
    ("BIF", _("BIF, Franc")),
    ("BMD", _("BMD, Dollar")),
    ("BND", _("BND, Dollar")),
    ("BOB", _("BOB, Boliviano")),
    ("BRL", _("BRL, Real")),
    ("BSD", _("BSD, Dollar")),
    ("BTN", _("BTN, Ngultrum")),
    ("BWP", _("BWP, Pula")),
    ("BYR", _("BYR, Ruble")),
    ("BZD", _("BZD, Dollar")),
    ("CAD", _("CAD, Dollar")),
    ("CDF", _("CDF, Franc")),
    ("CHF", _("CHF, Franc")),
    ("CLP", _("CLP, Peso")),
    ("CNY", _("CNY, Yuan Renminbi")),
    ("COP", _("COP, Peso")),
    ("CRC", _("CRC, Colon")),
    ("CUP", _("CUP, Peso")),
    ("CVE", _("CVE, Escudo")),
    ("CZK", _("CZK, Koruna")),
    ("DJF", _("DJF, Franc")),
    ("DKK", _("DKK, Krone")),
    ("DOP", _("DOP, Peso")),
    ("DZD", _("DZD, Dinar")),
    ("EGP", _("EGP, Pound")),
    ("ERN", _("ERN, Nakfa")),
    ("ETB", _("ETB, Birr")),
    ("EUR", _("EUR, Euro")),
    ("FJD", _("FJD, Dollar")),
    ("FKP", _("FKP, Pound")),
    ("GBP", _("GBP, Pound")),
    ("GEL", _("GEL, Lari")),
    ("GHS", _("GHS, Cedi")),
    ("GIP", _("GIP, Pound")),
    ("GMD", _("GMD, Dalasi")),
    ("GNF", _("GNF, Franc")),
    ("GTQ", _("GTQ, Quetzal")),
    ("GYD", _("GYD, Dollar")),
    ("HKD", _("HKD, Dollar")),
    ("HNL", _("HNL, Lempira")),
    ("HRK", _("HRK, Kuna")),
    ("HTG", _("HTG, Gourde")),
    ("HUF", _("HUF, Forint")),
    ("IDR", _("IDR, Rupiah")),
    ("ILS", _("ILS, Shekel")),
    ("INR", _("INR, Rupee")),
    ("IQD", _("IQD, Dinar")),
    ("IRR", _("IRR, Rial")),
    ("ISK", _("ISK, Krona")),
    ("JMD", _("JMD, Dollar")),
    ("JOD", _("JOD, Dinar")),
    ("JPY", _("JPY, Yen")),
    ("KES", _("KES, Shilling")),
    ("KGS", _("KGS, Som")),
    ("KHR", _("KHR, Riels")),
    ("KMF", _("KMF, Franc")),
    ("KPW", _("KPW, Won")),
    ("KRW", _("KRW, Won")),
    ("KWD", _("KWD, Dinar")),
    ("KYD", _("KYD, Dollar")),
    ("KZT", _("KZT, Tenge")),
    ("LAK", _("LAK, Kip")),
    ("LBP", _("LBP, Pound")),
    ("LKR", _("LKR, Rupee")),
    ("LRD", _("LRD, Dollar")),
    ("LSL", _("LSL, Loti")),
    ("LTL", _("LTL, Litas")),
    ("LVL", _("LVL, Lat")),
    ("LYD", _("LYD, Dinar")),
    ("MAD", _("MAD, Dirham")),
    ("MDL", _("MDL, Leu")),
    ("MGA", _("MGA, Ariary")),
    ("MKD", _("MKD, Denar")),
    ("MMK", _("MMK, Kyat")),
    ("MNT", _("MNT, Tugrik")),
    ("MOP", _("MOP, Pataca")),
    ("MRO", _("MRO, Ouguiya")),
    ("MUR", _("MUR, Rupee")),
    ("MVR", _("MVR, Rufiyaa")),
    ("MWK", _("MWK, Kwacha")),
    ("MXN", _("MXN, Peso")),
    ("MYR", _("MYR, Ringgit")),
    ("MZN", _("MZN, Metical")),
    ("NAD", _("NAD, Dollar")),
    ("NGN", _("NGN, Naira")),
    ("NIO", _("NIO, Cordoba")),
    ("NOK", _("NOK, Krone")),
    ("NPR", _("NPR, Rupee")),
    ("NZD", _("NZD, Dollar")),
    ("OMR", _("OMR, Rial")),
    ("PAB", _("PAB, Balboa")),
    ("PEN", _("PEN, Sol")),
    ("PGK", _("PGK, Kina")),
    ("PHP", _("PHP, Peso")),
    ("PKR", _("PKR, Rupee")),
    ("PLN", _("PLN, Zloty")),
    ("PYG", _("PYG, Guarani")),
    ("QAR", _("QAR, Rial")),
    ("RON", _("RON, Leu")),
    ("RSD", _("RSD, Dinar")),
    ("RUB", _("RUB, Ruble")),
    ("RWF", _("RWF, Franc")),
    ("SAR", _("SAR, Rial")),
    ("SBD", _("SBD, Dollar")),
    ("SCR", _("SCR, Rupee")),
    ("SDG", _("SDG, Pound")),
    ("SEK", _("SEK, Krona")),
    ("SGD", _("SGD, Dollar")),
    ("SHP", _("SHP, Pound")),
    ("SLL", _("SLL, Leone")),
    ("SOS", _("SOS, Shilling")),
    ("SRD", _("SRD, Dollar")),
    ("SSP", _("SSP, Pound")),
    ("STD", _("STD, Dobra")),
    ("SYP", _("SYP, Pound")),
    ("SZL", _("SZL, Lilangeni")),
    ("THB", _("THB, Baht")),
    ("TJS", _("TJS, Somoni")),
    ("TMT", _("TMT, Manat")),
    ("TND", _("TND, Dinar")),
    ("TOP", _("TOP, Paanga")),
    ("TRY", _("TRY, Lira")),
    ("TTD", _("TTD, Dollar")),
    ("TWD", _("TWD, Dollar")),
    ("TZS", _("TZS, Shilling")),
    ("UAH", _("UAH, Hryvnia")),
    ("UGX", _("UGX, Shilling")),
    ("USD", _("$, Dollar")),
    ("UYU", _("UYU, Peso")),
    ("UZS", _("UZS, Som")),
    ("VEF", _("VEF, Bolivar")),
    ("VND", _("VND, Dong")),
    ("VUV", _("VUV, Vatu")),
    ("WST", _("WST, Tala")),
    ("XAF", _("XAF, Franc")),
    ("XCD", _("XCD, Dollar")),
    ("XOF", _("XOF, Franc")),
    ("XPF", _("XPF, Franc")),
    ("YER", _("YER, Rial")),
    ("ZAR", _("ZAR, Rand")),
    ("ZMK", _("ZMK, Kwacha")),
    ("ZWL", _("ZWL, Dollar")),
)

PROVINCE= (
('آذربایجان شرقی', 'آذربایجان شرقی'),
('آذربایجان غربی', 'آذربایجان غربی'),
('اردبیل', 'اردبیل'),
('اصفهان', 'اصفهان'),
('البرز', 'البرز'),
('ایلام', 'ایلام'),
('بوشهر', 'بوشهر'),
('تهران', 'تهران'),
('چهارمحال بختیاری', 'چهارمحال بختیاری'),
('خراسان جنوبی', 'خراسان جنوبی'),
('خراسان رضوی', 'خراسان رضوی'),
('خراسان شمالی', 'خراسان شمالی'),
('خوزستان', 'خوزستان'),
('زنجان', 'زنجان'),
('سمنان', 'سمنان'),
('سیستان و بلوچستان', 'سیستان و بلوچستان'),
('فارس', 'فارس'),
('قزوین', 'قزوین'),
('قم', 'قم'),
('کردستان', 'کردستان'),
('کرمان', 'کرمان'),
('کرمانشاه', 'کرمانشاه'),
('کهکیلویه و بویراحمد', 'کهکیلویه و بویراحمد'),
('گلستان', 'گلستان'),
('گیلان', 'گیلان'),
('لرستان', 'لرستان'),
('مازندران', 'مازندران'),
('مرکزی', 'مرکزی'),
('هرمزگان', 'هرمزگان'),
('همدان', 'همدان'),
('یزد', 'یزد'),
)

COUNTRIES = (
    ("ایران", "ایران"),
    ("ترکیه", "ترکیه"),
    ("چین", "چین"),
    ("افغانستان", "افغانستان"),
    ("عراق", "عراق"),
    ("پاکستان", "پاکستان"),
    ("آذربایجان", "آذربایجان"),
    ("امارات", "امارات"),
    ("سوریه", "سوریه"),
    ("روسیه", "روسیه"),
    ("قطر", "قطر"),
    ("کویت", "کویت"),
    ("ترکمنستان", "ترکمنستان"),
    ("هندوستان", "هندوستان"),


)