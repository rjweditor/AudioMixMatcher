import tkinter as tk
import tkinter.filedialog as filedialog
import threading
from tkinter import ttk
from pytube import YouTube
import matchering as mg  # Import the matchering module
import os  # Import the os module for file operations

# Initialize tkinter app
app = tk.Tk()
app.title("Audio MixMatcher")

# Function to run the matching process in a separate thread
def run_matchering():
    # Let's keep info and warning outputs here, muting out the debug ones
    mg.log(info_handler=print, warning_handler=print)

    target_file = target_entry.get()
    reference_source = reference_source_var.get()  # Get the user's choice
    output_directory = output_dir_entry.get()  # Get the output directory

    try:
        if reference_source == "File":
            reference_file = reference_entry.get()
        elif reference_source == "YouTube":
            # Download the audio from the YouTube link
            yt = YouTube(reference_entry.get())
            audio_stream = yt.streams.filter(only_audio=True).first()
            reference_file = audio_stream.download(output_path=output_directory)
        else:
            reference_file = ""

        # Define the results list with your desired results
        results = [
            # Basic WAV 16-bit, match + master
            mg.pcm16(os.path.join(output_directory, "master_16bit.wav")),
            # FLAC 24-bit, match only (no limiter), normalized to -0.01 dB
            # Recommendations for adjusting the amplitude will be displayed in the debug print if it is enabled
            mg.Result(
                os.path.join(output_directory, "custom_result_24bit_no_limiter.flac"),
                subtype="PCM_24",
                use_limiter=False
            ),
            # AIFF 32-bit float, match only (no limiter), non-normalized
            # Can exceed 0 dB without clipping
            # So you can directly feed it to some VST limiter in your DAW
            mg.Result(
                os.path.join(output_directory, "custom_result_32bit_no_limiter_non-normalized.aiff"),
                subtype="FLOAT",
                use_limiter=False,
                normalize=False,
            )
            # More available formats and subtypes:
            # https://pysoundfile.readthedocs.io/en/latest/#soundfile.available_formats
            # https://pysoundfile.readthedocs.io/en/latest/#soundfile.available_subtypes
        ]

        def matchering_thread():
            # Start the indeterminate progress bar
            progress.start()

            # Perform the matchering process
            mg.process(
                target=target_file,
                reference=reference_file,
                results=results  # Pass the results list here
            )

            # Stop the progress bar when the process is complete
            progress.stop()

        # Create a new thread to run the matchering process
        matchering_thread = threading.Thread(target=matchering_thread)
        matchering_thread.start()
    except Exception as e:
        # Handle any exceptions, e.g., invalid URL or download errors
        print("Error:", str(e))
        # You can also show an error message to the user

# Function to select target audio file
def select_target_file():
    file_path = filedialog.askopenfilename()
    target_entry.delete(0, tk.END)
    target_entry.insert(0, file_path)

# Function to update reference input based on user's choice
def update_reference_input():
    choice = reference_source_var.get()
    if choice == "File":
        reference_entry.config(state="normal")
        reference_browse_button.config(state="normal")
    elif choice == "YouTube":
        reference_entry.config(state="normal")
        reference_browse_button.config(state="disabled")
    else:
        reference_entry.config(state="disabled")
        reference_browse_button.config(state="disabled")

# Function to select the output directory
def select_output_directory():
    directory_path = filedialog.askdirectory()
    output_dir_entry.delete(0, tk.END)
    output_dir_entry.insert(0, directory_path)

# Labels and Entry fields for file paths
tk.Label(app, text="Target Audio File:").pack()
target_entry = tk.Entry(app)
target_entry.pack()
tk.Button(app, text="Browse", command=select_target_file).pack()

# Visual divider (horizontal line) after the "Target Audio" section
ttk.Separator(app, orient="horizontal").pack(fill="x", padx=10, pady=5)

# Frame for reference source choice
reference_source_frame = tk.Frame(app)
reference_source_frame.pack()
tk.Label(reference_source_frame, text="Reference Source:").pack(side="left")
reference_source_var = tk.StringVar()
reference_source_var.set("File")  # Default choice
reference_source_file_radio = tk.Radiobutton(reference_source_frame, text="File", variable=reference_source_var, value="File", command=update_reference_input)
reference_source_file_radio.pack(side="left")
reference_source_youtube_radio = tk.Radiobutton(reference_source_frame, text="YouTube", variable=reference_source_var, value="YouTube", command=update_reference_input)
reference_source_youtube_radio.pack(side="left")
reference_source_none_radio = tk.Radiobutton(reference_source_frame, text="None", variable=reference_source_var, value="None", command=update_reference_input)
reference_source_none_radio.pack(side="left")

# Entry field and Browse button for reference input
tk.Label(app, text="Reference Audio File or Youtube Link:").pack()
reference_entry = tk.Entry(app)
reference_entry.pack()
reference_browse_button = tk.Button(app, text="Browse", command=select_target_file)
reference_browse_button.pack()

# Visual divider (horizontal line) after the "Reference Audio File/Link" section
ttk.Separator(app, orient="horizontal").pack(fill="x", padx=10, pady=5)

# Label and Entry field for the output directory
tk.Label(app, text="Output Directory:").pack()
output_dir_entry = tk.Entry(app)
output_dir_entry.pack()
tk.Button(app, text="Browse", command=select_output_directory).pack()

# Progress bar
progress = ttk.Progressbar(app, orient="horizontal", length=300, mode="indeterminate")
progress.pack()

# Button to start the matching process
tk.Button(app, text="Start Matching", command=run_matchering).pack()

# Initial setup of reference input based on default choice
update_reference_input()

# Run the tkinter main loop
app.mainloop()
