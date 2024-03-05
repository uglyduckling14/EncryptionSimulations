# Performance Benchmarking of Encryption Algorithms

This project aims to examine the performance of various encryption algorithms, namely DES, 3DES, AES, and RSA, on both guest and host systems. The evaluation is conducted based on the time required for encryption and decryption processes across files of different sizes (e.g., 50 KB, 1 MB, 2 MB).

## Tools and Libraries

- **Programming Language:** Python
- **Crypto Library:** [pycryptodome](https://pycryptodome.readthedocs.io/en/latest/src/introduction.html)

## Encryption Algorithms

1. **DES (Data Encryption Standard):**
   - Utilized the DES algorithm from the pycryptodome library.

2. **3DES (Triple DES):**
   - Employed the 3DES algorithm provided by the pycryptodome library.

3. **AES (Advanced Encryption Standard):**
   - Utilized the AES algorithm from the pycryptodome library.

4. **RSA (Rivest–Shamir–Adleman):**
   - Used the RSA algorithm available in the pycryptodome library.

## Benchmarking Process

1. **File Sizes:**
   - Files with sizes of 50 KB, 1 MB, and 2 MB were selected for benchmarking.

2. **Iterations:**
   - Each encryption and decryption task was performed 100 times to calculate the average time.

3. **Performance Metrics:**
   - The primary metric is the time taken for encryption and decryption processes.
