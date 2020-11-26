from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import sagital_brain

def process():
    parser = ArgumentParser(description="Calculates the average for each sagital-horizontal plane.",
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('file_input', nargs='?', default="brain_sample.csv",
                        help="Input CSV file with the results from scikit-brain binning algorithm.")
    parser.add_argument('--file_output', '-o', default="brain_average.csv",
                        help="Name of the output CSV file.")
    arguments = parser.parse_args()
    sagital_brain.run_averages(arguments.file_input, arguments.file_output)