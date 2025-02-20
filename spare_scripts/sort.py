infile = r"C:\Users\Jimmy Silva\ctf_writes\ctf_writeups_and_notes\spare_scripts\deadface_prox_info_rq.txt"
outfile = path = r"C:\Users\Jimmy Silva\ctf_writes\ctf_writeups_and_notes\spare_scripts\out.txt"
correctfile = path = r"C:\Users\Jimmy Silva\ctf_writes\ctf_writeups_and_notes\spare_scripts\correct.txt"
import re

def write_input_to_output(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                #check if line contains RQ string
                string1 = 'R'
                string2 = 'Q'
                if string1 in line or string2 in line:
                    outfile.write(line)
                else:
                    continue
        print(f"Content successfully written to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

def extract_rq_segments(inputf,outputf):
    try:
        with open(inputf,'r') as infile, open(outputf,"w") as outfile:
            for line in infile:
                if "Comm" in line:
                    continue
                else:
                    iwant = line[56:]
                    outfile.write(iwant)
        print("Sucessful")
    except Exception as e:
        print(f"an error occured: {e}")


write_input_to_output(infile,outfile)
extract_rq_segments(outfile,correctfile)

print(len("0010  52 52 52 52 52 52 52 52 52 52 52 52 52 52 52 0a   "))