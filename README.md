# MIPS 32-bit Instruction Decoder
## Overview
This is a MIPS 32-bit instruction decoder that supports both console and graphical user interface (GUI) versions. The graphical interface is implemented using Qt by PySide6 library, so make sure to install it by running:

```
pip install PySide6
```

## Features
- Decodes MIPS 32-bit instructions.
- Supports both console and graphical user interfaces.

## Console Version
### Usage
To use the console version, simply run the following command:

```
python dec.py input_path output_path
```

### Example

```
python dec.py example\code.asm output.txt
```

## GUI Version
### Installation
Before running the GUI version, make sure to install the PySide6 library:

```
pip install PySide6
```

### Usage
Run the following command to launch the GUI version:

```
python ui_dec.py
```

### GUI 



- Left Screen: Use this screen to input the assembly code.
- Right Screen: The decoded code is displayed on this screen.
- Bottom Screen: Any errors encountered during the decoding process will be shown here.

![Captura de pantalla 2023-12-04 125054](https://github.com/edez5558/MIPS32bits-dec/assets/122659695/143be58e-74ae-4064-8fd6-ffac65ca7357)



#### Assembly File Operations

In the top menu bar, you'll find the following options:

- New File: Create a new assembly file.
- Open File: Open an existing assembly file.
- Save: Save changes to the current assembly file.
- Save As: Save the assembly file with a new name.

![Captura de pantalla 2023-12-04 125118](https://github.com/edez5558/MIPS32bits-dec/assets/122659695/26864669-3148-434d-abf5-93dc8fc9440a)

#### Decoding Operations
Within a separate tab, you'll find decoding options:

- Decode: Process the assembly code and display the decoded output.
- Save: Save the decoded output.
- Save As: Save the decoded output with a new name.

![Captura de pantalla 2023-12-04 125128](https://github.com/edez5558/MIPS32bits-dec/assets/122659695/ec008bb7-72c0-4798-a7cd-bba762a2e58b)


#### Decoding Error Handling
If an error occurs during the decoding process, it will be displayed in the bottom screen along with the corresponding column where the error is located. This allows for easy identification and correction of any issues encountered during the decoding of the assembly code. Check the bottom screen for detailed error messages and their respective positions to facilitate a smooth debugging process.

![Captura de pantalla 2023-12-04 125213](https://github.com/edez5558/MIPS32bits-dec/assets/122659695/16640f46-b65b-457b-a253-61a4a77d992d)
![Captura de pantalla 2023-12-04 125146](https://github.com/edez5558/MIPS32bits-dec/assets/122659695/e3054e2a-6129-4821-a642-dddf9f9f4b49)

