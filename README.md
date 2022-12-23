# Binary to Sound Converter

This Python program converts a binary code to a wave file containing sound waves. The program has a GUI that allows the user to enter the binary code and convert it to a wave file with the click of a button.

## Prerequisites

- Python 3
- Tkinter (included in Python Standard Library)

## Usage

To run the program, open a terminal and navigate to the project directory. Then run the following command:python main.py


The GUI will open in a new window. Enter the binary code in the text box and click the "Convert" button to create the wave file. The wave file will be saved in the project directory with the name "binary_code.wav".

## Modifying the program

You can modify the parameters of the wave file by changing the values at the top of the script:

- `num_channels`: The number of channels in the wave file (1 for mono, 2 for stereo)
- `sample_width`: The width of each sample in bytes (2 for 16-bit samples)
- `sample_rate`: The sample rate of the wave file in samples per second
- `num_samples`: The number of samples in the wave file (determines the length of the audio)

You can also modify the frequencies used for the high and low values of the binary code by modifying the values in the `if` and `else` blocks in the `convert_to_sound()` function.



