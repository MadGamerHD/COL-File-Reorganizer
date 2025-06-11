import struct
import tkinter as tk
from tkinter import filedialog, messagebox


class ColReorganizerApp:
    def __init__(self, master):
        self.master = master
        master.title("COL File Reorganizer")
        master.geometry("400x150")

        self.label = tk.Label(master, text="Select a .col file to reorganize by model size:")
        self.label.pack(pady=10)

        self.select_button = tk.Button(master, text="Select COL File", command=self.select_file)
        self.select_button.pack(pady=5)

        self.reorg_button = tk.Button(master, text="Reorganize", command=self.reorganize, state=tk.DISABLED)
        self.reorg_button.pack(pady=5)

        self.filepath = None

    def select_file(self):
        path = filedialog.askopenfilename(
            title="Open COL File",
            filetypes=[("COL files", "*.col"), ("All files", "*")]
        )
        if path:
            self.filepath = path
            self.reorg_button.config(state=tk.NORMAL)

    def reorganize(self):
        if not self.filepath:
            return
        try:
            models = self.parse_col(self.filepath)
            # Sort by size descending
            models.sort(key=lambda m: m[0], reverse=True)

            save_path = filedialog.asksaveasfilename(
                title="Save reorganized COL",
                defaultextension=".col",
                filetypes=[("COL files", "*.col"), ("All files", "*")]
            )
            if not save_path:
                return

            with open(save_path, 'wb') as out_f:
                for size, block in models:
                    out_f.write(block)

            messagebox.showinfo("Success", f"Reorganized file saved to:\n{save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{e}")

    def parse_col(self, path):
        models = []  # list of (size, raw_block)
        with open(path, 'rb') as f:
            data = f.read()
        offset = 0
        total_len = len(data)

        while offset < total_len:
            if offset + 8 > total_len:
                raise ValueError("Unexpected end of file while reading model header.")

            # Read FourCC + size
            fourcc = data[offset:offset+4]
            size = struct.unpack_from('<I', data, offset+4)[0]
            block_size = size + 8  # 4 bytes FourCC + 4 bytes size + size bytes content

            if offset + block_size > total_len:
                raise ValueError(f"Model block at offset {offset} exceeds file size.")

            block = data[offset:offset+block_size]
            models.append((block_size, block))
            offset += block_size

        return models


if __name__ == '__main__':
    root = tk.Tk()
    app = ColReorganizerApp(root)
    root.mainloop()
