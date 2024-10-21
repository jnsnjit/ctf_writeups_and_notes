infile = r"C:\Users\Jimmy Silva\ctf_writes\ctf_writeups_and_notes\spare_scripts\correct.txt"

def record_frequency(inputf):
    try:
        with open(inputf,"r") as infile:
            idx1 = 0
            idx2 = 0
            idx3 = 0
            idx4 = 0
            idx5 = 0
            for line in infile:
                if line[1] == "R":
                    idx1+=1
                if line[2] == "R":
                    idx2+=1
                if line[3] == "R":
                    idx3+=1
                if line[4] == "R":
                    idx4+=1
                if line[5] == "R":
                    idx5+=1

        print(idx1)
        print(idx2)
        print(idx3)
        print(idx4)
        print(idx5)
    except Exception as e:
        print(f"Error occured: {e}")
    print("done")

record_frequency(infile)