import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
import extractor
import replacer


def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")


def create_interface():
    root = tk.Tk()
    root.title("DF3D Modder")
    root.resizable(False, False)
    window_width, window_height = 500, 200
    center_window(root, window_width, window_height)

    # Grid config
    root.columnconfigure(1, weight=1)

    # Asset File Entry
    tk.Label(root, text="Asset File:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    asset_entry = tk.Entry(root, width=40)
    asset_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    tk.Button(root, text="Browse", command=lambda: browse_asset(asset_entry)).grid(row=0, column=2, padx=10, pady=10)

    # Audio Folder Entry
    tk.Label(root, text="Audio Folder:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    audio_entry = tk.Entry(root, width=40)
    audio_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
    tk.Button(root, text="Browse", command=lambda: browse_audio(audio_entry)).grid(row=1, column=2, padx=10, pady=10)

    # Progressbar
    progress = ttk.Progressbar(root, orient="horizontal", mode="determinate", length=400)
    progress.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    # Buttons
    button_frame = tk.Frame(root)
    button_frame.grid(row=3, column=0, columnspan=3, pady=10)

    extract_btn = tk.Button(button_frame, text="Extract Audio",
                            command=lambda: threading.Thread(target=extract_audio,
                                                             args=(asset_entry, audio_entry, progress),
                                                             daemon=True).start(),
                            width=20)
    extract_btn.pack(side="left", padx=10)

    replace_btn = tk.Button(button_frame, text="Replace Audio",
                            command=lambda: threading.Thread(target=replace_audio,
                                                             args=(asset_entry, audio_entry, progress),
                                                             daemon=True).start(),
                            width=20)
    replace_btn.pack(side="left", padx=10)

    return root


def browse_asset(asset_entry):
    file_path = filedialog.askopenfilename(filetypes=[("Asset files", "*.assets *.bundle")])
    if file_path:
        asset_entry.delete(0, tk.END)
        asset_entry.insert(0, file_path)


def browse_audio(audio_entry):
    folder_path = filedialog.askdirectory()
    if folder_path:
        audio_entry.delete(0, tk.END)
        audio_entry.insert(0, folder_path)


def extract_audio(asset_entry, audio_entry, progress):
    asset_file_path = asset_entry.get()
    audio_folder_path = audio_entry.get()

    if not asset_file_path or not audio_folder_path:
        messagebox.showerror("Error", "Please select both asset file and audio folder")
        return

    try:
        extractor.extract_audio(asset_file_path, audio_folder_path, progress)
        messagebox.showinfo("Success", "Audio extraction completed")
    except Exception as e:
        messagebox.showerror("Error", f"Extraction failed: {str(e)}")


def replace_audio(asset_entry, audio_entry, progress):
    asset_file_path = asset_entry.get()
    audio_folder = audio_entry.get()

    if not asset_file_path or not audio_folder:
        messagebox.showerror("Error", "Please select both asset file and audio folder")
        return

    try:
        replacer.replace_audio(asset_file_path, audio_folder, progress)
        messagebox.showinfo("Success", "Audio replacement completed")
    except Exception as e:
        messagebox.showerror("Error", f"Replacement failed: {str(e)}")


if __name__ == "__main__":
    root = create_interface()
    root.mainloop()
