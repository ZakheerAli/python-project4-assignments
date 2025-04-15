import tkinter as tk  # Tkinter module import kar rahe hain GUI banane ke liye

# Constants (hamari values jo fixed hain)
CANVAS_WIDTH = 400     # Canvas ki width set kar rahe hain
CANVAS_HEIGHT = 400    # Canvas ki height set kar rahe hain
CELL_SIZE = 40         # Har blue box (cell) ka size 40x40 hoga
ERASER_SIZE = 30       # Eraser (pink box) ka size 30x30 hoga

# Main window
root = tk.Tk()  # Tkinter ki main window create kar rahe hain
root.title("Simple Eraser Canvas")  # Window ka title set kar rahe hain

# Create canvas
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)  # Canvas (drawing area) create kar rahe hain
canvas.pack()  # Canvas ko screen par show kar rahe hain

# Step 1: Create grid of blue boxes (cells)
cells = []  # Ek khaali list banayi jismein sab boxes (cells) ka reference store hoga
for row in range(0, CANVAS_HEIGHT, CELL_SIZE):  # Rows mein loop chala rahe hain
    for col in range(0, CANVAS_WIDTH, CELL_SIZE):  # Columns mein loop chala rahe hain
        rect = canvas.create_rectangle(
            col, row, col + CELL_SIZE, row + CELL_SIZE,  # Rectangle (box) ki position aur size
            fill='blue',  # Box ka colour blue set kar rahe hain
            outline='black'  # Box ke edges ka colour black
        )
        cells.append(rect)  # Har rectangle ko cells list mein add kar rahe hain

# Step 2: Create the eraser (pink box)
eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill='pink')  # Pink eraser box create kar rahe hain

# Step 3: Function to move eraser and erase blue cells
def move_eraser(event):  # Yeh function mouse move hone par eraser ko move karega
    x, y = event.x, event.y  # Mouse ki current position le rahe hain
    canvas.coords(eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)  # Eraser ki position update kar rahe hain

    # Check which cells are touching eraser
    overlapping = canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)  # Jo objects eraser se takra rahe hain unka list le rahe hain

    for obj in overlapping:  # Har overlapping object ke liye
        if obj in cells:  # Agar wo object blue boxes (cells) mein se hai
            canvas.itemconfig(obj, fill='white')  # To us box ka color white kar do (jaise erase ho gaya)

# Step 4: Bind mouse motion to move_eraser
canvas.bind('<B1-Motion>', move_eraser)  # Jab left mouse button ke sath mouse move ho, to move_eraser function call karo

# Run the program
root.mainloop()  # Program ko continuously chalaye rakho (GUI on rakhta hai)
