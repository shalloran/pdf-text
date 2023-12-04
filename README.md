# PDF Text Extractor

## Description

This script provides a simple tool to quickly extract text from PDF files and save it as a `.txt` file. It uses the `pypdf` library to read PDF content and `tkinter` for a graphical file selection dialog.

## Features

- Extract text from any number of PDF files selected via a GUI.
- Save extracted text to a `.txt` file with the same name as the original PDF.
- Prevent overwriting by appending a timestamp if a `.txt` file with the same name already exists.

## Prerequisites

Before running this script, you need to have Python installed on your system along with the following packages:

- `pypdf`
- `tkinter`

You can install the required package using pip:

```bash
pip install pypdf2
```

Note: `tkinter` usually comes pre-installed with Python. If it's not installed, refer to the official documentation for installation instructions.

## Usage

To use this script, follow these steps:

1. Ensure that you are in the directory containing the script.
2. Run the script using Python:

```bash
python pdf-text.py
```

3. A native OS file dialog will appear. Select the PDF files from which you want to extract text.
4. The script will create a `.txt` file with the extracted text in the same directory as the PDF.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit pull requests.

## License

This project is open source and available under the [GNU General Public License v3.0](https://github.com/shalloran/pdf-text/blob/main/LICENSE).

## Contact

For any feedback or questions, please reach out to me.

## Acknowledgments

- Thanks to the developers of `pypdf` and `tkinter`!