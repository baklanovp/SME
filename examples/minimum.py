""" Minimum working example of an SME script 
"""
import os.path

from pysme.gui import plot_plotly
from pysme import sme as SME
from pysme import util
from pysme.solve import solve
from pysme.synthesize import synthesize_spectrum

if __name__ == "__main__":

    # Define the location of all your files
    # this will put everything into the example dir
    target = "sun"
    examples_dir = os.path.dirname(os.path.realpath(__file__))
    in_file = os.path.join(examples_dir, "sun_6440_grid.inp")
    out_file = os.path.join(examples_dir, f"{target}.sme")
    plot_file = os.path.join(examples_dir, f"{target}.html")
    log_file = os.path.join(examples_dir, f"{target}.log")

    # Start the logging to the file
    util.start_logging(log_file)

    # Load your existing SME structure or create your own
    sme = SME.SME_Struct.load(in_file)

    # Change parameters if your want
    sme.vsini = 0
    sme.vrad_flag = "each"

    # Define any fitparameters you want
    # For abundances use: 'abund {El}', where El is the element (e.g. 'abund Fe')
    # For linelist use: 'linelist {Nr} {p}', where Nr is the number in the
    # linelist and p is the line parameter (e.g. 'linelist 17 gflog')
    fitparameters = ["teff", "logg", "monh"]

    # Start SME solver
    # sme = synthesize_spectrum(sme)
    sme = solve(sme, fitparameters)

    # Save results
    sme.save(out_file)

    # Plot results
    fig = plot_plotly.FinalPlot(sme)
    fig.save(filename=plot_file)
