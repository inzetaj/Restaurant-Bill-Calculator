import tkinter as tk
from tkinter import messagebox
from datetime import datetime

#Create main window
window = tk.Tk()
window.title("Restaurant Bill Calculator")
window.geometry ("650x700")
window.configure(bg="black")

#title
title = tk.Label(
    window,
    text="RESTAURANT BILL CALCULATOR",
    fg="lime",
    bg="black",
    font=("Courier", 18, "bold"))
title.pack(pady=10)
            
#Global
subtotal = 0
item_number = 1

#Receipt Box add item function
def add_item():
    global subtotal, item_number

    try:
        # Get price from entry
        price = float(price_entry.get())

        # Add to subtotal
        subtotal += price

        # get item_name from entry
        item_name = item_entry_name.get()

        # Display item and name in receipt

        receipt_box.insert (tk.END, f"(")
        receipt_box.insert (tk.END, f"{item_name}")
        receipt_box.insert (tk.END, f") ")
        receipt_box.insert (tk.END, f"Item {item_number}: ${price:.2f}\n")
        
        #Increase item number
        item_number += 1

        # Clear entry box
        price_entry.delete(0, tk.END)
        item_entry_name.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

#Clear Receipt
def clear_receipt():
    receipt_box.delete("1.0", tk.END)

#Calculate Total Function
def calculate_total():
    tax = subtotal * 0.0675
    tip = subtotal * 0.20
    total = subtotal + tax + tip

    receipt_box.insert(tk.END, "----------------------\n")
    
    time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    receipt_box.insert(tk.END, f"{time}\n")
        
    receipt_box.insert(tk.END, f"Subtotal: ${subtotal:.2f}\n") 
    receipt_box.insert(tk.END, f"Tax: ${tax:.2f}\n") 
    receipt_box.insert(tk.END, f"Tip: ${tip:.2f}\n") 
    receipt_box.insert(tk.END, f"Final Total: ${total:.2f}\n")

    
#Part 3 - GUI LAYOUT
#Label
tk.Label(window, text="Enter Item Price").pack(pady=5)

#Entry Box
price_entry = tk.Entry(window)
price_entry.pack(pady=5)

#Item name label
tk.Label(window, text="Enter Item Name").pack(pady=5)

#Item name
item_entry_name = tk.Entry(window)
item_entry_name.pack(pady=5)

#Add item buttons
add_button = tk.Button(window, text="Add Item")
add_button.pack(pady=15)

calc_button = tk.Button(window, text="Calculate Total")
calc_button.pack(pady=10)

#receipt display
receipt_box = tk.Text(window, width=40, height=20)
receipt_box.pack(pady=10)

#clear receipt
clear_receipt_button = tk.Button(window, text="Clear Receipt")
clear_receipt_button.pack(pady=15)

#part 6 connect buttons
add_button.config(command=add_item)
calc_button.config(command=calculate_total)
clear_receipt_button.config(command=clear_receipt)
    
#Run window
window.mainloop()
