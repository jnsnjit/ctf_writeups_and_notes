# text parser to format text #
count = 0
dtmf_string = ""
codechunk = 0

flag = ""

try:
    with open("dtmf.txt", "r", encoding="utf-8") as file:
        for line in file:
            for char in line:
                dtmf_string += char
                count += 1
                if(count%4==0):
                    # number is the two frequencies added together, switch statement will calculate it #
                    codechunk = int(dtmf_string)
                    match codechunk:
                        case 2174:
                            flag += "3"
                        case 2247:
                            flag += "6"
                        case 2329:
                            flag += "9"
                        case 2418:
                            flag += "#"
                        case 2330:
                            flag += "A"
                        case 2403:
                            flag += "B"
                        case 2485:
                            flag += "C"
                        case 2574:
                            flag += "D"
                        case 2033:
                            flag += "2"
                        case 2106:
                            flag += "5"
                        case 2188:
                            flag += "8"
                        case 2277:
                            flag += "0"
                        case 1906:
                            flag += "1"
                        case 1979:
                            flag += "4"
                        case 2061:
                            flag += "7"
                        case 2150:
                            flag += "*"
                        case _:
                            break
                    dtmf_string = ""
    print(flag)                
except FileNotFoundError:
    print("file not in directory idiot")
except Exception as e:
    print(f"error occurred: {e}")