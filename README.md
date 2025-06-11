# COL File Reorganizer

**COL File Reorganizer** is a simple tool for Windows that lets you reorganize collision model (`.col`) files used in **GTA III**, **Vice City**, and **San Andreas**, sorting them from **largest to smallest** model block based on size.

## 📦 Features

* ✅ Loads `.col` files for GTA III/VC/SA
* 🔍 Parses collision model blocks by size
* 📊 Reorganizes the blocks from **largest to smallest**
* 💾 Saves the reorganized `.col` file
* 🖱️ Simple and easy-to-use GUI

---

## 🖥️ How to Use

1. **Launch the Tool**
   Run the script using Python 3:

   ```bash
   python col_reorganizer.py
   ```

2. **Select a .col File**
   Click the **"Select COL File"** button and choose your `.col` file.

3. **Reorganize the File**
   Once the file is selected, click **"Reorganize"**. It will sort the model blocks by size from largest to smallest.

4. **Save the New File**
   Choose where to save the reorganized file when prompted.

5. **Done!**
   You’ll get a confirmation message when the process is complete.

---

## ⚠️ Notes

* This tool assumes `.col` files use a standard format with blocks that start with a FourCC and a 4-byte size header.
* It is intended for reorganizing blocks by raw byte size — not by visual or in-game size.
* Make backups before modifying original `.col` files.

---

## 🛠 Requirements

* Python 3.x
* No external libraries required (only `tkinter` and `struct`, both are part of the standard library)

---

## 💡 Why Use This?

In some modding scenarios, sorting `.col` files by block size can help with:

* Debugging
* Optimization
* Comparing collision complexity
* Ensuring consistent ordering for custom tools or engines
