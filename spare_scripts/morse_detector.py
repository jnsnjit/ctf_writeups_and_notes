input_file = r"C:\Users\Jimmy Silva\ctf_writes\ctf_writeups_and_notes\spare_scripts\beep_beep.txt"

def space_tab(inp):
    morse_code = ""
    try:
        with open(input_file, 'r') as infile:
            for line in infile:
                #check if line contains space tab, or end beep character string
                for char in line:
                    if char == " ":
                        morse_code += "."
                    if char == "\t":
                        morse_code += "-"
                    if char == "\\":
                         morse_code += "\\"
            print(f"Content successfully read")
            print(morse_code)
    except Exception as e:
            print(f"An error occurred: {e}")
def to_Upper(string):
    goods = string.upper()
    print(goods)

to_Upper("Guaranteeing that a specific action or event has taken place and cant be denied by parties involved.")