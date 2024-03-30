import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import cv2
from PIL import Image, ImageTk


def select_image():
    path = filedialog.askopenfilename()
    if path:
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (11, 11), 0)
        canny = cv2.Canny(blur, 30, 100)
        dilated = cv2.dilate(canny, (1, 1), iterations=0)
        cnt, hierarchy = cv2.findContours(
            dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
        )
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        rgb_with_contours = cv2.drawContours(rgb.copy(), cnt, -1, (0, 255, 0), 2)

        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)

        rgb_with_contours = Image.fromarray(rgb_with_contours)
        rgb_with_contours = ImageTk.PhotoImage(rgb_with_contours)

        panelA.config(image=image)
        panelA.image = image

        panelB.config(image=rgb_with_contours)
        panelB.image = rgb_with_contours

        entry.delete(20, tk.END)
        entry.insert(20, len(cnt))


def about():
    messagebox.showinfo(
        "About",
        "This is a simple object detection application using tkinter and OpenCV.",
    )


window = tk.Tk()
window.title("Object Detection")

# Main frame
main_frame = ttk.Frame(window, padding=(20, 10))
main_frame.grid(row=0, column=0)

# Menu
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="About", command=about)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Image display frame
image_frame = ttk.Frame(main_frame)
image_frame.grid(row=0, column=0, padx=10, pady=10)

# Select image button
select_button = ttk.Button(main_frame, text="Select Image", command=select_image)
select_button.grid(row=1, column=0, pady=10)

# Panel A for original image
panelA = ttk.Label(image_frame)
panelA.grid(row=0, column=0)

# Panel B for image with contours
panelB = ttk.Label(image_frame)
panelB.grid(row=0, column=1, padx=20)

# Entry widget to display number of objects
entry = ttk.Entry(main_frame, width=30)
entry.grid(row=2, column=0, pady=10)
entry.insert(0, "Number of Objects: ")

window.mainloop()
