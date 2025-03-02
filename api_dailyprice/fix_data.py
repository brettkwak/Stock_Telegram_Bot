import json

# Read the JSON data from the file
with open('stock_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Fix close price before 2024-12-20
for item in data['output2']:
    if item['xymd'] == '20241220':
        item['clos'] = '518.66'
    elif item['xymd'] == '20241219':
        item['clos'] = '514.17'
    elif item['xymd'] == '20241218':
        item['clos'] = '516.47'
    elif item['xymd'] == '20241217':
        item['clos'] = '535.80'
    elif item['xymd'] == '20241216':
        item['clos'] = '538.17'
    elif item['xymd'] == '20241213':
        item['clos'] = '530.53'
    elif item['xymd'] == '20241212':
        item['clos'] = '526.50'
    elif item['xymd'] == '20241211':
        item['clos'] = '529.92'
    elif item['xymd'] == '20241210':
        item['clos'] = '520.60'
    elif item['xymd'] == '20241209':
        item['clos'] = '522.38'
    elif item['xymd'] == '20241206':
        item['clos'] = '526.48'
    elif item['xymd'] == '20241205':
        item['clos'] = '521.81'
    elif item['xymd'] == '20241204':
        item['clos'] = '523.26'
    elif item['xymd'] == '20241203':
        item['clos'] = '516.87'
    elif item['xymd'] == '20241202':
        item['clos'] = '515.29'
    elif item['xymd'] == '20241129':
        item['clos'] = '509.74'
    elif item['xymd'] == '20241127':
        item['clos'] = '505.30'
    elif item['xymd'] == '20241126':
        item['clos'] = '509.31'
    elif item['xymd'] == '20241125':
        item['clos'] = '506.59'
    elif item['xymd'] == '20241122':
        item['clos'] = '505.79'
    elif item['xymd'] == '20241121':
        item['clos'] = '504.98'
    elif item['xymd'] == '20241120':
        item['clos'] = '503.17'
    elif item['xymd'] == '20241119':
        item['clos'] = '503.46'
    elif item['xymd'] == '20241118':
        item['clos'] = '500.02'
    elif item['xymd'] == '20241115':
        item['clos'] = '496.57'
    elif item['xymd'] == '20241114':
        item['clos'] = '508.69'
    elif item['xymd'] == '20241113':
        item['clos'] = '512.25'
    elif item['xymd'] == '20241112':
        item['clos'] = '512.91'
    elif item['xymd'] == '20241111':
        item['clos'] = '513.84'
    elif item['xymd'] == '20241108':
        item['clos'] = '514.14'
    elif item['xymd'] == '20241107':
        item['clos'] = '513.54'
    elif item['xymd'] == '20241106':
        item['clos'] = '505.58'
    elif item['xymd'] == '20241105':
        item['clos'] = '492.21'
    elif item['xymd'] == '20241104':
        item['clos'] = '486.01'
    elif item['xymd'] == '20241101':
        item['clos'] = '487.43'
    elif item['xymd'] == '20241031':
        item['clos'] = '483.85'
    elif item['xymd'] == '20241030':
        item['clos'] = '496.38'
    elif item['xymd'] == '20241029':
        item['clos'] = '500.16'
    elif item['xymd'] == '20241028':
        item['clos'] = '495.40'
    elif item['xymd'] == '20241025':
        item['clos'] = '495.32'
    elif item['xymd'] == '20241024':
        item['clos'] = '492.32'
    elif item['xymd'] == '20241023':
        item['clos'] = '488.36'
    elif item['xymd'] == '20241022':
        item['clos'] = '495.96'
    elif item['xymd'] == '20241021':
        item['clos'] = '495.42'
    elif item['xymd'] == '20241018':
        item['clos'] = '494.47'
    elif item['xymd'] == '20241017':
        item['clos'] = '491.25'
    elif item['xymd'] == '20241016':
        item['clos'] = '490.91'
    elif item['xymd'] == '20241015':
        item['clos'] = '490.85'
    elif item['xymd'] == '20241014':
        item['clos'] = '497.50'
    elif item['xymd'] == '20241011':
        item['clos'] = '493.36'
    elif item['xymd'] == '20241010':
        item['clos'] = '492.59'
    elif item['xymd'] == '20241009':
        item['clos'] = '493.15'
    elif item['xymd'] == '20241008':
        item['clos'] = '489.30'
    elif item['xymd'] == '20241007':
        item['clos'] = '482.10'
    elif item['xymd'] == '20241004':
        item['clos'] = '487.32'
    elif item['xymd'] == '20241003':
        item['clos'] = '481.59'
    elif item['xymd'] == '20241002':
        item['clos'] = '481.95'
    elif item['xymd'] == '20241001':
        item['clos'] = '481.27'
    elif item['xymd'] == '20240930':
        item['clos'] = '488.07'
    elif item['xymd'] == '20240927':
        item['clos'] = '486.75'
    elif item['xymd'] == '20240926':
        item['clos'] = '489.47'
    elif item['xymd'] == '20240925':
        item['clos'] = '485.82'
    elif item['xymd'] == '20240924':
        item['clos'] = '485.37'
    elif item['xymd'] == '20240923':
        item['clos'] = '483.04'
    elif item['xymd'] == '20240920':
        item['clos'] = '482.44'
    elif item['xymd'] == '20240919':
        item['clos'] = '483.36'
    elif item['xymd'] == '20240918':
        item['clos'] = '471.44'
    elif item['xymd'] == '20240917':
        item['clos'] = '473.49'
    elif item['xymd'] == '20240916':
        item['clos'] = '473.24'
    elif item['xymd'] == '20240913':
        item['clos'] = '475.36'
    elif item['xymd'] == '20240912':
        item['clos'] = '473.22'
    elif item['xymd'] == '20240911':
        item['clos'] = '468.62'
    elif item['xymd'] == '20240910':
        item['clos'] = '458.66'
    elif item['xymd'] == '20240909':
        item['clos'] = '454.46'
    elif item['xymd'] == '20240906':
        item['clos'] = '448.69'
    elif item['xymd'] == '20240905':
        item['clos'] = '461.04'
    elif item['xymd'] == '20240904':
        item['clos'] = '460.61'
    elif item['xymd'] == '20240903':
        item['clos'] = '461.81'
    elif item['xymd'] == '20240830':
        item['clos'] = '476.27'
    elif item['xymd'] == '20240829':
        item['clos'] = '470.66'
    elif item['xymd'] == '20240828':
        item['clos'] = '471.35'
    elif item['xymd'] == '20240827':
        item['clos'] = '476.76'
    elif item['xymd'] == '20240826':
        item['clos'] = '475.34'
    elif item['xymd'] == '20240823':
        item['clos'] = '480.00'
    elif item['xymd'] == '20240822':
        item['clos'] = '474.85'
    elif item['xymd'] == '20240821':
        item['clos'] = '482.50'
    elif item['xymd'] == '20240820':
        item['clos'] = '480.26'
    elif item['xymd'] == '20240819':
        item['clos'] = '481.27'
    elif item['xymd'] == '20240816':
        item['clos'] = '475.03'
    elif item['xymd'] == '20240815':
        item['clos'] = '474.42'
    elif item['xymd'] == '20240814':
        item['clos'] = '462.73'
    elif item['xymd'] == '20240813':
        item['clos'] = '462.58'
    elif item['xymd'] == '20240812':
        item['clos'] = '451.38'
    elif item['xymd'] == '20240809':
        item['clos'] = '450.41'
    elif item['xymd'] == '20240808':
        item['clos'] = '448.07'
    elif item['xymd'] == '20240807':
        item['clos'] = '434.77'
    elif item['xymd'] == '20240806':
        item['clos'] = '439.53'
    elif item['xymd'] == '20240805':
        item['clos'] = '435.37'
    elif item['xymd'] == '20240802':
        item['clos'] = '448.75'
    elif item['xymd'] == '20240801':
        item['clos'] = '459.66'
    elif item['xymd'] == '20240731':
        item['clos'] = '471.07'
    elif item['xymd'] == '20240730':
        item['clos'] = '457.53'
    elif item['xymd'] == '20240729':
        item['clos'] = '463.90'
    elif item['xymd'] == '20240726':
        item['clos'] = '462.97'
    elif item['xymd'] == '20240725':
        item['clos'] = '458.27'
    elif item['xymd'] == '20240724':
        item['clos'] = '463.38'
    elif item['xymd'] == '20240723':
        item['clos'] = '480.62'
    elif item['xymd'] == '20240722':
        item['clos'] = '482.32'
    elif item['xymd'] == '20240719':
        item['clos'] = '475.24'
    elif item['xymd'] == '20240718':
        item['clos'] = '479.49'
    elif item['xymd'] == '20240717':
        item['clos'] = '481.77'
    elif item['xymd'] == '20240716':
        item['clos'] = '496.34'
    elif item['xymd'] == '20240715':
        item['clos'] = '496.15'
    elif item['xymd'] == '20240712':
        item['clos'] = '494.82'
    elif item['xymd'] == '20240711':
        item['clos'] = '491.93'
    elif item['xymd'] == '20240710':
        item['clos'] = '502.96'
    elif item['xymd'] == '20240709':
        item['clos'] = '497.77'
    elif item['xymd'] == '20240708':
        item['clos'] = '497.34'
    elif item['xymd'] == '20240705':
        item['clos'] = '496.16'
    elif item['xymd'] == '20240703':
        item['clos'] = '491.04'
    elif item['xymd'] == '20240702':
        item['clos'] = '486.98'
    elif item['xymd'] == '20240701':
        item['clos'] = '481.92'


# Write the modified data back to the file
with open('stock_data.json', 'w') as file:
    json.dump(data, file, indent=4)

print("File fixed successfully.")
