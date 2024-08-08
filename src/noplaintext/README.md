# Crypto Utils Package

## Overview

The `crypto_utils` package provides cryptographic utility functions for key generation, key loading, message encryption, and decryption. It uses the `cryptography` library to perform these operations.

## Functions

- **`generate_key(file_path)`**: Generates a new encryption key and saves it to the specified file.
- **`load_key(file_path)`**: Loads an encryption key from the specified file.
- **`encrypt(message, key_file_path)`**: Encrypts a message using the key from the specified file.
- **`decrypt(encrypted_message, key_file_path)`**: Decrypts an encrypted message using the key from the specified file.

## Installation

This package is a subpackage within the main project. To use it, you need to have the main project set up. Follow the instructions in the [project-level README](../README.md) to install and run the project.

## Usage

Import the functions from `crypto_utils` as follows:

```python
from crypto_utils import generate_key, load_key, encrypt, decrypt
```

## Dependencies

- cryptography
- logging

## License

This package is licensed under the MIT License - see the LICENSE file for details.

## Contributing

For contributions, please refer to the main project repository and follow the contribution guidelines provided there.