import pandas as pd


names2pins = {}
isFirst = True
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
def get_pin(input_str: str):
    if input_str.startswith("PIN_"):
        return input_str
    # it's the name of the pin not the pin itself
    return names2pins[input_str]


def generate_assignments(signal: str, pin: str):
    # print(f"set_location_assignment {get_pin(pin.upper())} -to {signal.upper()}")
    global isFirst
    with open("output.txt", "w" if isFirst else "a") as f:
        f.write(f"set_location_assignment {get_pin(pin.upper())} -to {signal}\n")
        isFirst = False


def read_inputs_from_file():
    try:
        df = pd.read_excel(r'test1.xlsx')
        for index, row in df.iterrows():
            generate_assignments(row[0].strip(), row[1].upper().strip())
    except Exception as inst:
        print(str(type(inst)) + " : " + str(inst.args))  # arguments stored in .args


def generate_vector(signal, size, pin , start):
    for i in range(size):
        signalname = f"{signal}[{i}]"
        pinName = f"{pin}{i+(start)}"
        generate_assignments(signalname, pinName)


def interactive():
    while True:
        c = int(input("\nEnter\n0 - individual\n1 - vectors\n-1 - EXIT\n\n"))
        if c == 0:
            signal, pin = input("signalName assignedPin:\n").strip().split()
            generate_assignments(signal, pin)
        elif c == 1:
            signal, pin,size,start = input("<signalBaseName pinBaseName size startPosition>\n").strip().split()
            generate_vector(signal, int(size), pin, int(start))
        elif c == -1:
            break
        else:
            print("\nEnter a valid value\n")
            continue


def main():
    try:

        read_pins()
        s = int(input("0- interactive\n1- Excel\n"))
        if s == 0:
            interactive()
        else:
            read_inputs_from_file()
    except Exception as ex:
        print("Error: " + str(ex.args))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
