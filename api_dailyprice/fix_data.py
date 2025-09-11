import json
import os


def fix_data():

    current_dir = os.path.dirname(__file__)
    data_path = os.path.join(current_dir, "stock_data.json")

    # Read the JSON data from the file
    with open(data_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Fix close price before 2025-06-23
    for item in data['output2']:
        if item['xymd'] == '20250620':
            item['clos'] = '526.83'
        elif item['xymd'] == '20250618':
            item['clos'] = '528.99'
        elif item['xymd'] == '20250617':
            item['clos'] = '529.08'
        elif item['xymd'] == '20250616':
            item['clos'] = '534.29'
        elif item['xymd'] == '20250613':
            item['clos'] = '526.96'
        elif item['xymd'] == '20250612':
            item['clos'] = '533.66'
        elif item['xymd'] == '20250611':
            item['clos'] = '532.41'
        elif item['xymd'] == '20250610':
            item['clos'] = '534.21'
        elif item['xymd'] == '20250609':
            item['clos'] = '530.7'
        elif item['xymd'] == '20250606':
            item['clos'] = '529.92'
        elif item['xymd'] == '20250605':
            item['clos'] = '524.79'
        elif item['xymd'] == '20250604':
            item['clos'] = '528.77'
        elif item['xymd'] == '20250603':
            item['clos'] = '527.3'
        elif item['xymd'] == '20250602':
            item['clos'] = '523.21'
        elif item['xymd'] == '20250530':
            item['clos'] = '519.11'
        elif item['xymd'] == '20250529':
            item['clos'] = '519.93'
        elif item['xymd'] == '20250528':
            item['clos'] = '518.91'
        elif item['xymd'] == '20250527':
            item['clos'] = '521.22'
        elif item['xymd'] == '20250523':
            item['clos'] = '509.24'
        elif item['xymd'] == '20250522':
            item['clos'] = '514'
        elif item['xymd'] == '20250521':
            item['clos'] = '513.04'
        elif item['xymd'] == '20250520':
            item['clos'] = '520.27'
        elif item['xymd'] == '20250519':
            item['clos'] = '522.01'
        elif item['xymd'] == '20250516':
            item['clos'] = '521.51'
        elif item['xymd'] == '20250515':
            item['clos'] = '519.25'
        elif item['xymd'] == '20250514':
            item['clos'] = '518.68'
        elif item['xymd'] == '20250513':
            item['clos'] = '515.59'
        elif item['xymd'] == '20250512':
            item['clos'] = '507.85'
        elif item['xymd'] == '20250509':
            item['clos'] = '487.97'
        elif item['xymd'] == '20250508':
            item['clos'] = '488.29'
        elif item['xymd'] == '20250507':
            item['clos'] = '483.3'
        elif item['xymd'] == '20250506':
            item['clos'] = '481.41'
        elif item['xymd'] == '20250505':
            item['clos'] = '485.93'
        elif item['xymd'] == '20250502':
            item['clos'] = '488.83'
        elif item['xymd'] == '20250501':
            item['clos'] = '481.68'
        elif item['xymd'] == '20250430':
            item['clos'] = '475.47'
        elif item['xymd'] == '20250429':
            item['clos'] = '475.53'
        elif item['xymd'] == '20250428':
            item['clos'] = '472.41'
        elif item['xymd'] == '20250425':
            item['clos'] = '472.56'
        elif item['xymd'] == '20250424':
            item['clos'] = '467.35'
        elif item['xymd'] == '20250423':
            item['clos'] = '454.56'
        elif item['xymd'] == '20250422':
            item['clos'] = '444.48'
        elif item['xymd'] == '20250421':
            item['clos'] = '433.11'
        elif item['xymd'] == '20250417':
            item['clos'] = '444.1'
        elif item['xymd'] == '20250416':
            item['clos'] = '444.18'
        elif item['xymd'] == '20250415':
            item['clos'] = '457.99'
        elif item['xymd'] == '20250414':
            item['clos'] = '457.48'
        elif item['xymd'] == '20250411':
            item['clos'] = '454.4'
        elif item['xymd'] == '20250410':
            item['clos'] = '446.18'
        elif item['xymd'] == '20250409':
            item['clos'] = '466'
        elif item['xymd'] == '20250408':
            item['clos'] = '416.06'
        elif item['xymd'] == '20250407':
            item['clos'] = '423.69'
        elif item['xymd'] == '20250404':
            item['clos'] = '422.67'
        elif item['xymd'] == '20250403':
            item['clos'] = '450.66'
        elif item['xymd'] == '20250402':
            item['clos'] = '476.15'
        elif item['xymd'] == '20250401':
            item['clos'] = '472.7'
        elif item['xymd'] == '20250331':
            item['clos'] = '468.92'
        elif item['xymd'] == '20250328':
            item['clos'] = '468.94'
        elif item['xymd'] == '20250327':
            item['clos'] = '481.62'
        elif item['xymd'] == '20250326':
            item['clos'] = '484.38'
        elif item['xymd'] == '20250325':
            item['clos'] = '493.46'
        elif item['xymd'] == '20250324':
            item['clos'] = '490.66'
        elif item['xymd'] == '20250321':
            item['clos'] = '480.84'
        elif item['xymd'] == '20250320':
            item['clos'] = '479.26'
        elif item['xymd'] == '20250319':
            item['clos'] = '480.89'
        elif item['xymd'] == '20250318':
            item['clos'] = '474.54'
        elif item['xymd'] == '20250317':
            item['clos'] = '482.77'
        elif item['xymd'] == '20250314':
            item['clos'] = '479.66'
        elif item['xymd'] == '20250313':
            item['clos'] = '468.34'
        elif item['xymd'] == '20250312':
            item['clos'] = '476.92'
        elif item['xymd'] == '20250311':
            item['clos'] = '471.6'
        elif item['xymd'] == '20250310':
            item['clos'] = '472.73'
        elif item['xymd'] == '20250307':
            item['clos'] = '491.79'
        elif item['xymd'] == '20250306':
            item['clos'] = '488.2'
        elif item['xymd'] == '20250305':
            item['clos'] = '502.01'
        elif item['xymd'] == '20250304':
            item['clos'] = '495.55'
        elif item['xymd'] == '20250303':
            item['clos'] = '497.05'
        elif item['xymd'] == '20250228':
            item['clos'] = '508.17'
        elif item['xymd'] == '20250227':
            item['clos'] = '500.27'
        elif item['xymd'] == '20250226':
            item['clos'] = '514.56'
        elif item['xymd'] == '20250225':
            item['clos'] = '513.32'
        elif item['xymd'] == '20250224':
            item['clos'] = '519.87'
        elif item['xymd'] == '20250221':
            item['clos'] = '526.08'
        elif item['xymd'] == '20250220':
            item['clos'] = '537.23'
        elif item['xymd'] == '20250219':
            item['clos'] = '539.52'
        elif item['xymd'] == '20250218':
            item['clos'] = '539.37'
        elif item['xymd'] == '20250214':
            item['clos'] = '538.15'
        elif item['xymd'] == '20250213':
            item['clos'] = '535.9'
        elif item['xymd'] == '20250212':
            item['clos'] = '528.3'
        elif item['xymd'] == '20250211':
            item['clos'] = '527.99'
        elif item['xymd'] == '20250210':
            item['clos'] = '529.25'
        elif item['xymd'] == '20250207':
            item['clos'] = '522.92'
        elif item['xymd'] == '20250206':
            item['clos'] = '529.6'
        elif item['xymd'] == '20250205':
            item['clos'] = '526.85'
        elif item['xymd'] == '20250204':
            item['clos'] = '524.47'
        elif item['xymd'] == '20250203':
            item['clos'] = '518.11'
        elif item['xymd'] == '20250131':
            item['clos'] = '522.29'
        elif item['xymd'] == '20250130':
            item['clos'] = '523.05'
        elif item['xymd'] == '20250129':
            item['clos'] = '520.83'
        elif item['xymd'] == '20250128':
            item['clos'] = '521.81'
        elif item['xymd'] == '20250127':
            item['clos'] = '514.21'
        elif item['xymd'] == '20250124':
            item['clos'] = '529.63'
        elif item['xymd'] == '20250123':
            item['clos'] = '532.64'
        elif item['xymd'] == '20250122':
            item['clos'] = '531.51'
        elif item['xymd'] == '20250121':
            item['clos'] = '524.8'
        elif item['xymd'] == '20250117':
            item['clos'] = '521.74'
        elif item['xymd'] == '20250116':
            item['clos'] = '513.08'
        elif item['xymd'] == '20250115':
            item['clos'] = '516.7'
        elif item['xymd'] == '20250114':
            item['clos'] = '505.08'
        elif item['xymd'] == '20250113':
            item['clos'] = '505.56'
        elif item['xymd'] == '20250110':
            item['clos'] = '507.19'
        elif item['xymd'] == '20250108':
            item['clos'] = '515.27'
        elif item['xymd'] == '20250107':
            item['clos'] = '515.18'
        elif item['xymd'] == '20250106':
            item['clos'] = '524.54'
        elif item['xymd'] == '20250103':
            item['clos'] = '518.58'
        elif item['xymd'] == '20250102':
            item['clos'] = '510.23'


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
    with open(data_path, 'w') as file:
        json.dump(data, file, indent=4)

    print("File fixed successfully.")


if __name__ == "__main__":
    fix_data()