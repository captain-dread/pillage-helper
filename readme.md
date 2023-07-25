# First Mate Pillage Tool

To use this tool, you have multiple options based on your operating system. For Mac or Windows, you can run the pre-built executables available in the [releases page](https://github.com/captain-dread/pillage-helper/releases). 

Alternatively, you can directly run the application using Python. If you're using a Mac, you might need to navigate to the Privacy & Security settings to manually grant permission for the app to run.

You can also run the `build.py` script yourself to generate your own executable if you have python installed.

<img src="https://res.cloudinary.com/de2ymful4/image/upload/v1689638423/demo_wlt2xq.png">


## Using The "Find Greedy Hits" Feature

In order to find greedy hits in Puzzle Pirates, follow these steps:

1. In-game, select `Ye -> Options -> Chat -> Choose (under chat logging)` and save the file (the name doesn't matter).
2. Afterward, click on the `Load Log File` button, choose the log file you created, and you'll be ready to start searching for greedies. Take note of the following:
   - Wait for the "The victors plundered" message to appear in order to get the greedy hits.
   - You **don't** need to reload the log file every time; simply click on "Find Greedy Hits" to get the latest results.
   - This method is fully compliant with the game's Terms of Service (TOS). For more information, you can refer to their [official documentation](https://yppedia.puzzlepirates.com/Official:Third_Party_Software).


## Running Script Directly (MacOS/Windows)

In order to run the tool yourself without executables, you will need to have Python and certain Python libraries installed on your machine. 

#### Installing Python
If you don't have Python installed, you can download it from [here](https://www.python.org/downloads/). Make sure you download the latest version of Python.


#### Installing Python Libraries
You can install libraries using Python's package installer, pip. You need to install `pysimplegui`, `pyperclip`, and `pyinstaller` For example:

```bash
pip install PySimpleGUI
```

#### Running the Script
Once you have Python and the required libraries installed, you can run the script by typing the following in your terminal:

```bash
python app.py
```
