# noplaintext

## Overview

noplaintext is a module that is intended to eliminate hard-coded credentials in scripts by encrypting them using a external key file. This means that only the encrypted credentials are visible and can only be decrypted with a key file that can be stored in a directory not accessible from a github repository, network drive, or wherever else the source code made be. There is a graphical application to generate a key file and encrypt credentials.

## Project Structure
```
/project-root
   /src
      /crypto_utils
         __init__.py
         crypto_utils.py
         README.md
            /gui_app
            __init__.py
            gui_app.py
            README.md
   
   README.md
   pyproject.toml
   requirements.txt
```

- `/src/crypto_utils`: Contains the cryptographic utility functions for key generation, loading, encryption, and decryption.
- `/src/gui_app`: Contains the GUI application that interacts with the user to perform cryptographic operations.
- `/tests`: Contains tests for the cryptographic utilities.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Sluke950/noplaintext.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd noplaintext
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the GUI application:**

    ```bash
    python src/noplaintext/gui_app/gui_app.py
    ```

## Dependencies

- `tkinter` (included with Python)
- `cryptography`
- `logging`

## Usage

1. **Generate Key:** Click the "Generate Key" button to create a new encryption key and save it to a file.
2. **Load Key:** Click the "Load Key" button to load an existing key from a file.
3. **Encrypt Message:** Enter a message and click "Encrypt" to encrypt it using the loaded key.
4. **Decrypt Message:** Enter an encrypted message and click "Decrypt" to decrypt it using the loaded key.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you want to contribute to this project, please fork the repository, make your changes, and submit a pull request. All contributions are welcome!
