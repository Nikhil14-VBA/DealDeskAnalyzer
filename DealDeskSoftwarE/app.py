import tkinter as tk
from tkinter import filedialog, messagebox

# Correct import (because scripts is now a package)
from scripts.deal_desk_analyzer import run_analysis


def browse_file():
    file_path = filedialog.askopenfilename(
        title="Select Deal Input File",
        filetypes=[("Excel Files", "*.xlsx")]
    )
    entry_path.delete(0, tk.END)
    entry_path.insert(0, file_path)


def run_tool():
    input_file = entry_path.get()

    if not input_file:
        messagebox.showerror("Error", "Please select an input Excel file")
        return

    try:
        output_file = run_analysis(input_file)
        messagebox.showinfo(
            "Success",
            f"Deal Desk analysis completed!\n\nOutput saved at:\n{output_file}"
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- UI ---------------- #

root = tk.Tk()
root.title("Deal Desk Analyzer")
root.geometry("600x200")

frame = tk.Frame(root)
frame.pack(pady=20)

entry_path = tk.Entry(frame, width=50)
entry_path.pack(side=tk.LEFT, padx=5)

tk.Button(frame, text="Browse", command=browse_file).pack(side=tk.LEFT)

tk.Button(
    root,
    text="Run Analysis",
    command=run_tool,
    bg="#1f7a1f",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20
).pack(pady=20)

root.mainloop()
