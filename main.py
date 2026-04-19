import tkinter as tk
from tkinter import messagebox


def calculate_tip():
    try:
        bill = float(entry_bill.get())
        tip_percent = float(entry_tip.get())
        people = int(entry_people.get())

        if bill < 0 or tip_percent < 0 or people <= 0:
            messagebox.showerror("Error", "Please enter valid positive values.")
            return

        tip_amount = bill * (tip_percent / 100)
        total = bill + tip_amount

        bill_per_person = bill / people
        tip_per_person = tip_amount / people
        total_per_person = total / people

        result_text.set(
            f"Total Tip: ${tip_amount:.2f}\n"
            f"Bill Per Person: ${bill_per_person:.2f}\n"
            f"Tip Per Person: ${tip_per_person:.2f}\n"
            f"Total Per Person: ${total_per_person:.2f}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")


root = tk.Tk()
root.title("Tip Calculator")
root.geometry("320x340")

tk.Label(root, text="Bill Amount ($)", font=("Arial", 11)).pack(pady=5)
entry_bill = tk.Entry(root)
entry_bill.pack()

tk.Label(root, text="Tip Percentage (%)", font=("Arial", 11)).pack(pady=5)
entry_tip = tk.Entry(root)
entry_tip.pack()

tk.Label(root, text="Number of People", font=("Arial", 11)).pack(pady=5)
entry_people = tk.Entry(root)
entry_people.pack()

tk.Button(root, text="Calculate", command=calculate_tip).pack(pady=12)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, justify="center", font=("Arial", 11)).pack(pady=10)

root.mainloop()