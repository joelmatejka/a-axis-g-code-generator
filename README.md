# A-axis G-code generator

A script that merges multiple XYZ g-codes with defined angles into one XYZA g-code.


# Requirements

Python 3 and packages `pygcode` and `argparse` are required.

# Usage

Run `./convert -h` to see required arguments.

You need to provide at least one g-code file (which is supported by pygcode package), safe position where CNC can park while rotation of the A-axis, speed of xy and z moves (take look into input g-code for sample speed), speed of A-axis.

TODO: Put sample g-codes and CNC setup

