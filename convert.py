import argparse
from pygcode import Line

parser = argparse.ArgumentParser(description='Simple G-code converter utility for conversion of two input files into one double-sided')

parser.add_argument('file_top', action='store',
                    help='File to be processed first')
parser.add_argument('file_bottom', action='store',
                    help='File to be processed second (after 180 deg rotation)')
parser.add_argument('file_output', action='store',
                    help='Output file composed of instructions from top and bottom file')

argres = parser.parse_args()

output_gcode = []

with open(argres.file_top, 'r') as fh:
    for line_text in fh.readlines():
        line = Line(line_text)

        print(line)  # will print the line (with cosmetic changes)
        output_gcode.append(line)  # try to just append

with open(argres.file_bottom, 'r') as fh:
    for line_text in fh.readlines():
        line = Line(line_text)

        print(line)  # will print the line (with cosmetic changes)
        output_gcode.append(line)  # try to just append

print('\n'.join(str(line) for line in output_gcode))

#print('\n'.join(map(' '.join, output_gcode)))

with open(argres.file_output, 'w') as fh:
    for line in output_gcode:
        fh.write(str(line)+'\n')