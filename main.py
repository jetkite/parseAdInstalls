import pandas as pd
import xlsxwriter
df = pd.read_csv('ads-downloads.csv')


country_conversions = [72]

for x in range(72):
    country_conversions.append(0)

countries = df['Country/Territory (Geographic)'].tolist()
conversions_data = df['Conversions'].tolist()




country_conversions[0] = conversions_data[countries.index('United States')] if 'United States' in countries else 0
country_conversions[1] = conversions_data[countries.index('Germany')] if 'Germany' in countries else 0
country_conversions[2] = conversions_data[countries.index('Austria')] if 'Austria' in countries else 0
country_conversions[3] = conversions_data[countries.index('Japan')] if 'Japan' in countries else 0
country_conversions[4] = conversions_data[countries.index('Canada')] if 'Canada' in countries else 0
country_conversions[5] = conversions_data[countries.index('France')] if 'France' in countries else 0
country_conversions[6] = conversions_data[countries.index('Switzerland')] if 'Switzerland' in countries else 0
country_conversions[7] = conversions_data[countries.index('South Korea')] if 'South Korea' in countries else 0
country_conversions[8] = conversions_data[countries.index('Netherlands')] if 'Netherlands' in countries else 0
country_conversions[9] = conversions_data[countries.index('United Kingdom')] if 'United Kingdom' in countries else 0
country_conversions[10] = conversions_data[countries.index('Belgium')] if 'Belgium' in countries else 0
country_conversions[11] = conversions_data[countries.index('Italy')] if 'Italy' in countries else 0
country_conversions[12] = conversions_data[countries.index('Brazil')] if 'Brazil' in countries else 0
country_conversions[13] = conversions_data[countries.index('Taiwan')] if 'Taiwan' in countries else 0
country_conversions[14] = conversions_data[countries.index('Hong Kong')] if 'Hong Kong' in countries else 0
country_conversions[15] = conversions_data[countries.index('Denmark')] if 'Denmark' in countries else 0
country_conversions[16] = conversions_data[countries.index('Sweden')] if 'Sweden' in countries else 0
country_conversions[17] = conversions_data[countries.index('Finland')] if 'Finland' in countries else 0
country_conversions[18] = conversions_data[countries.index('Australia')] if 'Australia' in countries else 0
country_conversions[19] = conversions_data[countries.index('Spain')] if 'Spain' in countries else 0
country_conversions[20] = conversions_data[countries.index('Poland')] if 'Poland' in countries else 0
country_conversions[21] = conversions_data[countries.index('Mexico')] if 'Mexico' in countries else 0
country_conversions[22] = conversions_data[countries.index('Czechia')] if 'Czechia' in countries else 0
country_conversions[23] = conversions_data[countries.index('Slovakia')] if 'Slovakia' in countries else 0
country_conversions[24] = conversions_data[countries.index('Thailand')] if 'Thailand' in countries else 0
country_conversions[25] = conversions_data[countries.index('Hungary')] if 'Hungary' in countries else 0
country_conversions[26] = conversions_data[countries.index('Ireland')] if 'Ireland' in countries else 0
country_conversions[27] = conversions_data[countries.index('New Zealand')] if 'New Zealand' in countries else 0
country_conversions[28] = conversions_data[countries.index('Indonesia')] if 'Indonesia' in countries else 0
country_conversions[29] = conversions_data[countries.index('Vietnam')] if 'Vietnam' in countries else 0
country_conversions[30] = conversions_data[countries.index('Norway')] if 'Norway' in countries else 0
country_conversions[31] = conversions_data[countries.index('Croatia')] if 'Croatia' in countries else 0
country_conversions[32] = conversions_data[countries.index('Luxembourg')] if 'Luxembourg' in countries else 0
country_conversions[33] = conversions_data[countries.index('Israel')] if 'Israel' in countries else 0
country_conversions[34] = conversions_data[countries.index('Greece')] if 'Greece' in countries else 0
country_conversions[35] = conversions_data[countries.index('South Africa')] if 'South Africa' in countries else 0
country_conversions[36] = conversions_data[countries.index('Russian Federation')] if 'Russian Federation' in countries else 0
country_conversions[37] = conversions_data[countries.index('Portugal')] if 'Portugal' in countries else 0
country_conversions[38] = conversions_data[countries.index('Romania')] if 'Romania' in countries else 0
country_conversions[39] = conversions_data[countries.index('India')] if 'India' in countries else 0
country_conversions[40] = conversions_data[countries.index('Latvia')] if 'Latvia' in countries else 0
country_conversions[41] = conversions_data[countries.index('Estonia')] if 'Estonia' in countries else 0
country_conversions[42] = conversions_data[countries.index('Lithuania')] if 'Lithuania' in countries else 0
country_conversions[43] = conversions_data[countries.index('Singapore')] if 'Singapore' in countries else 0
country_conversions[44] = conversions_data[countries.index('Malaysia')] if 'Malaysia' in countries else 0
country_conversions[45] = conversions_data[countries.index('Brunei')] if 'Brunei' in countries else 0
country_conversions[46] = conversions_data[countries.index('Colombia')] if 'Colombia' in countries else 0
country_conversions[47] = conversions_data[countries.index('Peru')] if 'Peru' in countries else 0
country_conversions[48] = conversions_data[countries.index('Argentina')] if 'Argentina' in countries else 0
country_conversions[49] = conversions_data[countries.index('Philippines')] if 'Philippines' in countries else 0
country_conversions[50] = conversions_data[countries.index('Paraguay')] if 'Paraguay' in countries else 0
country_conversions[51] = conversions_data[countries.index('Jamaica')] if 'Jamaica' in countries else 0
country_conversions[52] = conversions_data[countries.index('Haiti')] if 'Haiti' in countries else 0
country_conversions[53] = conversions_data[countries.index('Guatemala')] if 'Guatemala' in countries else 0
country_conversions[54] = conversions_data[countries.index('Bolivia')] if 'Bolivia' in countries else 0
country_conversions[55] = conversions_data[countries.index('Ecuador')] if 'Ecuador' in countries else 0
country_conversions[56] = conversions_data[countries.index('Chile')] if 'Chile' in countries else 0
country_conversions[57] = conversions_data[countries.index('Panama')] if 'Panama' in countries else 0
country_conversions[58] = conversions_data[countries.index('Nicaragua')] if 'Nicaragua' in countries else 0
country_conversions[59] = conversions_data[countries.index('Puerto Rico')] if 'Puerto Rico' in countries else 0
country_conversions[60] = conversions_data[countries.index('Costa Rica')] if 'Costa Rica' in countries else 0
country_conversions[61] = conversions_data[countries.index('Barbados')] if 'Barbados' in countries else 0
country_conversions[62] = conversions_data[countries.index('Uruguay')] if 'Uruguay' in countries else 0
country_conversions[63] = conversions_data[countries.index('Dominican Republic')] if 'Dominican Republic' in countries else 0
country_conversions[64] = conversions_data[countries.index('El Salvador')] if 'El Salvador' in countries else 0
country_conversions[65] = conversions_data[countries.index('Egypt')] if 'Egypt' in countries else 0
country_conversions[66] = conversions_data[countries.index('Morocco')] if 'Morocco' in countries else 0
country_conversions[67] = conversions_data[countries.index('Tunisia')] if 'Tunisia' in countries else 0
country_conversions[68] = conversions_data[countries.index('Jordan')] if 'Jordan' in countries else 0
country_conversions[69] = conversions_data[countries.index('Saudi Arabia')] if 'Saudi Arabia' in countries else 0
country_conversions[70] = conversions_data[countries.index('United Arab Emirates')] if 'United Arab Emirates' in countries else 0
country_conversions[71] = conversions_data[countries.index('Qatar')] if 'Qatar' in countries else 0
country_conversions[72] = conversions_data[countries.index('Kuwait')] if 'Kuwait' in countries else 0

from re import sub
from decimal import Decimal

def c_to_int(vv):
    try:
        return int(Decimal(sub(r'[^\d.]', '', vv)))
    except:
        return 0

country_conversions_int = []
for a in range(73):
    country_conversions_int.append(c_to_int(country_conversions[a]))




countries_main = ["US",
"Germany",
"Austria",
"Japan",
"Canada",
"France",
"Switzerland",
"South Korea",
"Netherlands",
"UK",
"Belgium",
"Italy",
"Brazil",
"Taiwan",
"Hong Kong",
"Denmark",
"Sweden",
"Finland",
"Australia",
"Spain",
"Poland",
"Mexico",
"Czech Republic",
"Slovakia",
"Thailand",
"Hungary",
"Ireland",
"New Zealand",
"Indonesia",
"Viet nam",
"Norway",
"Croatia",
"Luxembourg",
"Israel",
"Greece",
"South Africa",
"Russia",
"Portugal",
"Romania",
"India",
"Latvia",
"Estonia",
"Lithuania",
"Singapore",
"Malaysia",
"Brunei",
"Colombia",
"Peru",
"Argentina",
"Philippinnes",
"Paraguay",
"Jamaica",
"Haiti",
"Guatemala",
"Bolivia",
"Ecuador",
"Chile",
"Panama",
"Nicaragua",
"Puerto Rico",
"Costa Rica",
"Barbados",
"Uruguay",
"Dominican R.",
"El Salvador",
"Egypt",
"Morocco",
"Tunisia",
"Jordan",
"Saudi Arabia",
"UAE",
"Qatar",
"Kuwait"]
df = pd.DataFrame({
    'Countries': countries_main,
    'Installs_INT': country_conversions_int
})

writer = pd.ExcelWriter('ads-downloads.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Ads', index=False)
writer.save()