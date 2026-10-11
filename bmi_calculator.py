import tkinter as tk
from tkinter import ttk, messagebox


def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        # Validate user input
        if weight <= 0 or height <= 0:
            messagebox.showerror(
                "Invalid Input",
                "Height and weight must be greater than zero."
            )
            return

        # Convert height from centimetres to metres
        height_m = height / 100

        # Calculate BMI
        bmi = weight / (height_m ** 2)

        # Determine BMI category for adults
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Healthy weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obesity"

        # Display result
        result_label.config(
            text=f"Your BMI: {bmi:.2f}",
            foreground="#2563eb"
        )

        category_label.config(
            text=f"Category: {category}"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numbers for height and weight."
        )


def clear_fields():
    height_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)

    result_label.config(text="Your BMI: --")
    category_label.config(text="Category: --")


# Create the main application window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("420x460")
root.resizable(False, False)
root.configure(bg="#f1f5f9")

# Main heading
title_label = tk.Label(
    root,
    text="BMI CALCULATOR",
    font=("Arial", 22, "bold"),
    bg="#f1f5f9",
    fg="#1e293b"
)
title_label.pack(pady=20)

# Input frame
input_frame = tk.Frame(root, bg="#f1f5f9")
input_frame.pack(pady=10)

# Height input
height_label = tk.Label(
    input_frame,
    text="Height (cm):",
    font=("Arial", 12),
    bg="#f1f5f9"
)
height_label.grid(row=0, column=0, padx=10, pady=12, sticky="w")

height_entry = ttk.Entry(input_frame, width=20, font=("Arial", 12))
height_entry.grid(row=0, column=1, padx=10, pady=12)

# Weight input
weight_label = tk.Label(
    input_frame,
    text="Weight (kg):",
    font=("Arial", 12),
    bg="#f1f5f9"
)
weight_label.grid(row=1, column=0, padx=10, pady=12, sticky="w")

weight_entry = ttk.Entry(input_frame, width=20, font=("Arial", 12))
weight_entry.grid(row=1, column=1, padx=10, pady=12)

# Calculate button
calculate_button = tk.Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi,
    font=("Arial", 12, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    relief="flat",
    padx=15,
    pady=8,
    cursor="hand2"
)
calculate_button.pack(pady=15)

# Result display
result_label = tk.Label(
    root,
    text="Your BMI: --",
    font=("Arial", 17, "bold"),
    bg="#f1f5f9",
    fg="#2563eb"
)
result_label.pack(pady=10)

category_label = tk.Label(
    root,
    text="Category: --",
    font=("Arial", 13),
    bg="#f1f5f9",
    fg="#334155"
)
category_label.pack(pady=5)

# Clear button
clear_button = tk.Button(
    root,
    text="Clear",
    command=clear_fields,
    font=("Arial", 11),
    padx=15,
    pady=5,
    cursor="hand2"
)
clear_button.pack(pady=10)

# Disclaimer
disclaimer_label = tk.Label(
    root,
    text="BMI is a screening tool, not a medical diagnosis.",
    font=("Arial", 8),
    bg="#f1f5f9",
    fg="#64748b"
)
disclaimer_label.pack(side="bottom", pady=12)

# Start the application
root.mainloop()