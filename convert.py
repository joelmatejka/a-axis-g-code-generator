import argparse
from pygcode import *

def append_code_from_file(filename, output_gcode, last_file):
    output_gcode.append(Line("; start of file " + filename))
    with open(filename, 'r') as fh:
        for line_text in fh.readlines():
            line = Line(line_text)
            for code in line.block.gcodes:
                if code == GCodeEndProgram():
                    # Hopefully only M02 can break continuity
                    # also hope that there is only M02 on the last line
                    output_gcode.append(Line("; end of file " + filename))
                    return
            output_gcode.append(line)
    output_gcode.append(Line("; end of file " + filename))

def append_rotation(output_gcode, angle, speed):
    output_gcode.append(Line("; rotate for " + str(angle)))
    output_gcode.append(Line(str(GCodeLinearMove(A=angle)) + " " + str(GCodeFeedRate(speed))))


parser = argparse.ArgumentParser(description='Simple G-code converter utility for conversion of two input files into one double-sided')

parser.add_argument('file_top', action='store',
                    help='File to be processed first')
parser.add_argument('file_bottom', action='store',
                    help='File to be processed second (after 180 deg rotation)')
parser.add_argument('file_output', action='store',
                    help='Output file composed of instructions from top and bottom file')

argres = parser.parse_args()

output_gcode = []

append_rotation(output_gcode, 0, 1000)

append_code_from_file(argres.file_top, output_gcode, False)

append_rotation(output_gcode, 180, 1000)

append_code_from_file(argres.file_bottom, output_gcode, True)

output_gcode.append(GCodeEndProgram())

print('\n'.join(str(line) for line in output_gcode))

#print('\n'.join(map(' '.join, output_gcode)))

with open(argres.file_output, 'w') as fh:
    for line in output_gcode:
        fh.write(str(line)+'\n')