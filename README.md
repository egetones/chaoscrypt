<div align="center">

# ChaosCrypt (Ransomware Simulator)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Type](https://img.shields.io/badge/Type-Malware_Simulation-red)
![Safety](https://img.shields.io/badge/Safety-Sandbox_Locked-green)

<p>
  <strong>An educational Ransomware simulation tool to demonstrate file encryption attacks.</strong>
</p>

</div>

---

## Description

**ChaosCrypt** is a Python-based malware simulator designed to mimic the behavior of modern Ransomware. 

It recursively scans a target directory, encrypts files using **AES-128 (Fernet)**, deletes the originals, and drops a ransom note. It also includes a decryption module to restore the files using the generated key.

**Safety Mechanism:**
To prevent accidental data loss, this tool is hardcoded to operate **ONLY** within a directory named `test_zone`. It will verify the existence of this folder before executing any destructive actions.

### Technical Features

  **Encryption Engine:** Uses symmetric encryption to lock files.
  **Destructive Logic:** Simulates the `Encrypt -> Write -> Delete Original` workflow of real malware.
  **Ransom Note:** Automatically generates a warning message in the infected directory.
  **ea Recovery:** Includes a decryptor to verify that files can be restored (proof of concept).

---

##peki bunda Usage

1. **Setup the Sandbox:**
   Create a folder named `test_zone` and put some dummy files in it.
   ```bash
   mkdir test_zone
   touch test_zone/file1.txt test_zone/file2.png
   ```

2. **Run the Malware (Encrypt):**
   ```bash
   python3 chaos.py
   # Select Option 1
   ```
   *Result: Files in `test_zone` will have `.chaos` extension and be unreadable.*

3. **Run the Decryptor (Restore):**
   ```bash
   python3 chaos.py
   # Select Option 2
   ```
   *Result: Files will be restored to their original state.*

---

## ⚠️ Disclaimer

**This software is for EDUCATIONAL USE ONLY.** Do not modify the source code to target system directories. Creating malicious software to cause damage is a federal crime. The author assumes no liability for misuse.
