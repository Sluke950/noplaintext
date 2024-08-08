
# GUI App Subpackage

## Overview

The `gui_app` subpackage provides a graphical user interface for interacting with the cryptographic utilities. It uses `tkinter` to create a user-friendly interface for key management and message encryption/decryption.

## Features

- **Generate Key**: Option to generate and save a new encryption key.
- **Load Key**: Option to load an existing encryption key from a file.
- **Encrypt Message**: Encrypts a message using the loaded key.
- **Decrypt Message**: Decrypts an encrypted message using the loaded key.

## Installation

This subpackage is a part of the main project. To set up the GUI application, follow the installation instructions in the [project-level README](../README.md).

## Usage

To run the GUI application, execute the following command:

```bash
python src/gui_app/gui_app.py
```

## Dependencies

- cryptography
- logging

## License

This package is licensed under the MIT License - see the LICENSE file for details.

## Contributing

For contributions, please refer to the main project repository and follow the contribution guidelines provided there.
