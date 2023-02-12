import tkinter as tk
import random

def roll_dice(num_dice, num_sides, keep_dice):
    results = []
    for i in range(num_dice):
        roll = random.randint(1, num_sides)
        results.append(roll)
    results.sort()
    if keep_dice < num_dice:
        results = results[-keep_dice:]
    return sum(results)

def main():
    root = tk.Tk()
    tk.Label(root, text="How many dice would you like to roll?").grid(row=0, column=0)
    tk.Label(root, text="How many sides do each dice have?").grid(row=1, column=0)
    tk.Label(root, text="How many dice do you want to keep?").grid(row=2, column=0)

    num_dice = tk.Entry(root)
    num_sides = tk.Entry(root)
    keep_dice = tk.Entry(root)

    num_dice.grid(row=0, column=1)
    num_sides.grid(row=1, column=1)
    keep_dice.grid(row=2, column=1)

    result_label = tk.Label(root, text="")
    result_label.grid(row=4, column=0)

    def roll():
        num_dice_val = int(num_dice.get())
        num_sides_val = int(num_sides.get())
        keep_dice_val = int(keep_dice.get())
        result_label.config(text=str(roll_dice(num_dice_val, num_sides_val, keep_dice_val)))

    tk.Button(root, text="Roll!", command=roll).grid(row=3, column=1, sticky="E")

    root.mainloop()

if __name__ == "__main__":
    main()
