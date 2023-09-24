# Audio MixMatcher - User Guide

**Table of Contents**
- [Introduction](#introduction)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Using the Application](#using-the-application)
  - [Selecting the Target Audio File](#selecting-the-target-audio-file)
  - [Choosing the Reference Source](#choosing-the-reference-source)
  - [Providing Reference Audio](#providing-reference-audio)
  - [Selecting the Output Directory](#selecting-the-output-directory)
  - [Running the Matching Process](#running-the-matching-process)

## Introduction

Welcome to Audio MixMatcher! This application is designed to help you match and process audio files efficiently. You can use it to compare a target audio file with a reference audio source, allowing you to generate matched audio results in various formats.

## Dependencies

Before using this application, ensure you have the following dependencies installed:

- Python (3.x recommended)
- `tkinter` (a standard Python library for GUI)
- `pytube` (for downloading audio from YouTube)
- `matchering` (a library for audio matching)
- `os` (for file operations)

You can install the necessary packages using `pip`:

```bash
pip install pytube3 matchering
```

## Installation

1. Download the source code of the Audio MixMatcher application.
2. Ensure you have the dependencies mentioned above installed.
3. Run the application by executing the Python script.

## Using the Application

### Selecting the Target Audio File

1. Click the "Browse" button next to the "Target Audio File" label.
2. Navigate to the location of your target audio file and select it.
3. The selected file path will appear in the entry field.

### Choosing the Reference Source

1. Under the "Reference Source" section, choose one of the following options:
   - "File" if you want to use a reference audio file.
   - "YouTube" if you want to download audio from a YouTube link.
   - "None" if you do not wish to use a reference source.

### Providing Reference Audio

- **If you chose "File" as the reference source**:
  1. Click the "Browse" button next to the "Reference Audio File or Youtube Link" label.
  2. Navigate to the location of your reference audio file and select it.
  3. The selected file path will appear in the entry field.

- **If you chose "YouTube" as the reference source**:
  1. Enter the YouTube link in the "Reference Audio File or Youtube Link" entry field.
  2. The audio will be downloaded from the YouTube link to the output directory.

- **If you chose "None" as the reference source**, no further action is required in this section.

### Selecting the Output Directory

1. Click the "Browse" button next to the "Output Directory" label.
2. Choose the directory where you want to save the processed audio files.
3. The selected directory path will appear in the entry field.

### Running the Matching Process

1. After configuring the target, reference, and output settings, click the "Start Matching" button.
2. The matching process will begin, and a progress bar will indicate the progress.
3. Once the process is complete, the matched audio files will be available in the output directory.

Enjoy using Audio MixMatcher to match and process your audio files effortlessly!
