import json
import os

def check_signal():

    current_dir = os.path.dirname(__file__)
    data_path = os.path.join(current_dir, "stock_data.json")

    # Load JSON
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Set MA
    short_num = 3
    long_num = 160


    clos_values = [float(entry["clos"]) for entry in data['output2'][:long_num+1]]
    # print(clos_values)

    current_short_ma = round((sum(clos_values[0:short_num]) / short_num),2)
    current_long_ma = round((sum(clos_values[0:long_num]) / long_num), 2)
    # print(f"{short_num} MA : {current_short_ma}")
    # print(f"{long_num} MA : {current_long_ma}")

    prev_short_ma = round((sum(clos_values[1:short_num+1]) / short_num), 2)
    prev_long_ma = round((sum(clos_values[1:long_num+1]) / long_num), 2)
    # print(f"prev {short_num} MA : {prev_short_ma}")
    # print(f"prev {long_num} MA : {prev_long_ma}")


    if current_short_ma > current_long_ma and prev_short_ma < prev_long_ma:
        return "✅Golden Cross✅"
    elif current_short_ma < current_long_ma and prev_short_ma > prev_long_ma:
        return "⛔Death Cross⛔"

if __name__ == "__main__":
    print(f"Signal : {check_signal()}")