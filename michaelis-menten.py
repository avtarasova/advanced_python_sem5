import sys
import json
import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-s', '--concentration', type=float)
    parser.add_argument ('-E0','--concentration_start_enzyme', type=float)
    parser.add_argument ('-KM', '--constant_Mihaelis', type=float)
    parser.add_argument ('-k', '--speed_constant', type=float)
    parser.add_argument ('--save_file', type=str, required=False)

    return parser


def michaelis_menten(s, E0, KM, k):
	v_max = s * E0 * k / (KM + s)
	return v_max


if __name__ == '__main__':
    parser = createParser()
    arg = parser.parse_args()

    v = michaelis_menten(arg.concentration, arg.concentration_start_enzyme, 
    	arg.constant_Mihaelis, arg.speed_constant)
    data = {
    "v": v,
    "S": arg.concentration,
    "E0": arg.concentration_start_enzyme,
    "KM": arg.constant_Mihaelis,
    "k": arg.speed_constant
    }

if arg.save_file:
    with open(arg.save_file, 'w') as file:
        file.write(json.dumps(data, indent=4))