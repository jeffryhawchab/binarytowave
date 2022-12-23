import tkinter as tk
import wave
import struct

# Set the parameters for the wave file
num_channels = 1  # mono
sample_width = 2  # in bytes, a 16-bit short
sample_rate = 44100
num_samples = 44100  # 1 second of audio

# Create an empty list to store the sample values
samples = []

def convert_to_sound():
    # Get the binary code from the text box
    binary_code = binary_entry.get()
    
    # Convert the binary code to a list of integers
    binary_list = [int(x) for x in binary_code]

    # Convert the binary values to sound samples
    for value in binary_list:
        if value == 1:
            # High frequency (e.g. 880 Hz)
            samples.append(32767)
            samples.append(-32768)
        else:
            # Low frequency (e.g. 440 Hz)
            samples.append(32767)
            samples.append(32767)

    # Create a bytes object from the samples
    sample_bytes = struct.pack('h' * len(samples), *samples)

    # Create a wave file
    with wave.open('binary_code.wav', 'wb') as file:
        file.setparams((num_channels, sample_width, sample_rate, num_samples, 'NONE', 'not compressed'))
        file.writeframes(sample_bytes)
    
    # Display a message to confirm that the file has been created
    tk.Label(root, text='Wave file created successfully!').pack()

# Create the main window
root = tk.Tk()
root.title('Binary to Sound Converter')

# Add a label and text box for the binary code
tk.Label(root, text='Enter binary code:').pack()
binary_entry = tk.Entry(root)
binary_entry.pack()

# Add a button to convert the binary code to sound
convert_button = tk.Button(root, text='Convert', command=convert_to_sound)
convert_button.pack()

# Run the GUI
root.mainloop()
