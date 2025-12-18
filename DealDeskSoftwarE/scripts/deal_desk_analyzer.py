import pandas as pd
from datetime import datetime


def approval_logic(margin):
    try:
        margin = float(margin)
    except:
        return "INVALID DATA"

    if margin >= 30:
        return "AUTO APPROVE"
    elif margin >= 20:
        return "FINANCE REVIEW"
    else:
        return "REJECT"


def run_analysis(input_file_path):
    df = pd.read_excel(input_file_path)

    # Calculations
    df["Net_Revenue"] = df["Deal_Value"] * (1 - df["Discount_%"] / 100)
    df["Incentive_Cost"] = df["Deal_Value"] * (df["Incentive_%"] / 100)
    df["Profit"] = df["Net_Revenue"] - df["Cost"] - df["Incentive_Cost"]
    df["Margin_%"] = (df["Profit"] / df["Net_Revenue"]) * 100

    # Decision logic
    df["Decision"] = df["Margin_%"].apply(approval_logic)
    df["Margin_%"] = df["Margin_%"].round(2)

    # Save output
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"output/deal_analysis_{timestamp}.xlsx"
    df.to_excel(output_path, index=False)

    return output_path


if __name__ == "__main__":
    output = run_analysis("data/deal_input.xlsx")
    print(f"✅ Deal Desk analysis completed successfully.\n📁 Output saved at: {output}")
import tkinter as tk
from tkinter import filedialog, messagebox
from scripts.deal_desk_analyzer import run_analysis

def select_file():
    file_path = filedialog.askopenfilename(
        title="Select Deal Input File",
        filetypes=[("Excel files", "*.xlsx")]
    )
    if file_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)

def run_tool():
    input_path = entry_path.get()

    if not input_path:
        messagebox.showerror("Error", "Please select an input Excel file")
        return

    try:
        output_path = run_analysis(input_path)
        messagebox.showinfo(
            "Success",
            f"Deal Desk Analysis Completed!\n\nOutput saved at:\n{output_path}"
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------- UI ----------
root = tk.Tk()
root.title("Deal Desk Analyzer")
root.geometry("520x200")
root.resizable(False, False)

tk.Label(root, text="Deal Desk Analyzer", font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

entry_path = tk.Entry(frame, width=50)
entry_path.pack(side=tk.LEFT, padx=5)

tk.Button(frame, text="Browse", command=select_file).pack(side=tk.LEFT)

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
