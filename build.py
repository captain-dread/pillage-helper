import subprocess
import glob
import os
import pkg_resources

REQUIRED_PACKAGES = ["pysimplegui", "pyperclip", "pyinstaller"]

# Determine the appropriate data path separator
separator = ";" if os.name == "nt" else ":"

# List to hold our --add-data parameters
data_args = []

# Find all files in images/
for file in glob.glob("images/*"):
    # Add the --add-data parameter for this file
    data_args.append("--add-data")
    data_args.append(f"{file}{separator}images/")

# Check if the necessary packages are installed
for package in REQUIRED_PACKAGES:
    try:
        dist = pkg_resources.get_distribution(package)
        print(f"{dist.project_name} ({dist.version}) is installed")
    except pkg_resources.DistributionNotFound:
        print(f"{package} is NOT installed. Installing now...")
        subprocess.check_call(["python", "-m", "pip", "install", package])

# Now build the PyInstaller command
pyinstaller_args = ["pyinstaller", "--onefile", "--windowed"] + data_args + ["app.py"]

# Run the command
subprocess.run(pyinstaller_args)
