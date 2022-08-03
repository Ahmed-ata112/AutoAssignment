import pandas as pd

names2pins = {}


def read_pins():
    with open('pins.txt') as f:

        lines = f.read().splitlines()
        i = 0
        while i < len(lines):
            line = lines[i]
            line = line.split()
            if len(line) != 1:
                # a description line
                i += 1
                continue
            names2pins[line[0].upper()] = lines[i + 1].split()[0].upper()
            i += 2

    print(names2pins)


def generate_assignments(signal: str, pin: str):
    print(f"set_location_assignment {pin.upper()} -to {signal.upper()}")


def get_pin(input_str: str):
    if input_str.startswith("PIN_"):
        return input_str
    # it's the name of the pin not the pin itself
    return names2pins[input_str]


def read_inputs_from_file():
    try:
        df = pd.read_excel(r'test1.xlsx')
        for index, row in df.iterrows():
            pin = get_pin(row[1].upper().strip())
            generate_assignments(row[0].upper().strip(), pin)
    except Exception as inst:
        print(str(type(inst)) + " : " + str(inst.args))  # arguments stored in .args




def interactive():
    a = input("enter 0 for individual or 1 for vectors")


def main():
    read_pins()
    read_inputs_from_file()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
