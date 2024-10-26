# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:39:03 2021

@author: sheet
"""

from subprocess import call
import tkinter as tk
import pandas as pd
from PIL import Image, ImageTk
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from joblib import load, dump

root = tk.Tk()
root.title("House Price Prediction")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

image2 = Image.open('4.jpg')
image2 = image2.resize((w, h), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

lbl = tk.Label(root, text="House Price Prediction System", font=('Times', 20, ' bold '), height=1, width=85, bg="Black", fg="white")
lbl.place(x=0, y=0)

def Model_Training():
    data = pd.read_csv("Book1.csv")
    labels = data['price']
    train1 = data.drop(['id', 'price'], axis=1)

    x_train, x_test, y_train, y_test = train_test_split(train1, labels, test_size=0.20, random_state=1)
    
    clf = GradientBoostingRegressor(n_estimators=400, max_depth=5, min_samples_split=2, learning_rate=0.1, loss='ls')
    clf.fit(x_train, y_train)
    
    # Save the model
    dump(clf, "House_Price_prediction_MODEL.joblib")
    print("Model saved successfully.")


def listToString(s): 
    return str(s[0])  # Assuming s is a single-value list

def call_file():
    bedrooms = tk.IntVar()
    sqft_living = tk.IntVar()
    floors = tk.IntVar()
    condition = tk.IntVar()
    yr_built = tk.IntVar()
    yr_renovated = tk.IntVar()
    zipcode = tk.IntVar()

    def Detect():
        e1 = bedrooms.get()
        e2 = sqft_living.get()
        e3 = floors.get()
        e4 = condition.get()
        e5 = yr_built.get()
        e6 = yr_renovated.get()
        e7 = zipcode.get()

        print(f"Inputs: {e1}, {e2}, {e3}, {e4}, {e5}, {e6}, {e7}")

        try:
            a1 = load('House_Price_prediction_MODEL.joblib')
            print("Model loaded successfully.")

            v = a1.predict([[e1, e2, e3, e4, e5, e6, e7]])
            print(f"Prediction result: {v}")

            predicted_price = listToString(v)
            print(f"Predicted Price: {predicted_price}")

            yes = tk.Label(root, text="Predicted House Price is \n " + str(predicted_price),
                            background="#7ec0ee", foreground="black",
                            font=('times', 20, ' bold '), width=20, height=5)
            yes.place(x=330, y=270)
            root.update()  # Force update of the GUI
        except Exception as e:
            print(f"Error during prediction: {e}")

    frame_display = tk.LabelFrame(root, text=" --Display-- ", width=500, height=550, bd=5, font=('times', 14, ' bold '), background="#660066")
    frame_display.grid(row=0, column=0, sticky='nw')
    frame_display.place(x=700, y=50)

    l1 = tk.Label(frame_display, text="Bedrooms", background="#ff66b3", font=('times', 20, ' bold '), width=10, fg='white')
    l1.place(x=90, y=50)
    bedrooms_entry = tk.Entry(frame_display, bd=2, width=5, font=("TkDefaultFont", 20), textvariable=bedrooms)
    bedrooms_entry.place(x=300, y=50)

    l2 = tk.Label(frame_display, text="Sqft Living", background="#ff66b3", font=('times', 20, ' bold '), width=10, fg='white')
    l2.place(x=90, y=100)
    sqft_living_entry = tk.Entry(frame_display, bd=2, width=5, font=("TkDefaultFont", 20), textvariable=sqft_living)
    sqft_living_entry.place(x=300, y=100)

    l3 = tk.Label(frame_display, text="Floors", background="#ff66b3", font=('times', 20, ' bold '), width=10, fg='white')
    l3.place(x=90, y=150)
    floors_entry = tk.Entry(frame_display, bd=2, width=5, font=("TkDefaultFont", 20), textvariable=floors)
    floors_entry.place(x=300, y=150)

    l4 = tk.Label(frame_display, text="Condition", background="#ff66b3", font=('times', 20, ' bold '), width=10, fg='white')
    l4.place(x=90, y=200)
    condition_entry = tk.Entry(frame_display, bd=2, width=5, font=("TkDefaultFont", 20), textvariable=condition)
    condition_entry.place(x=300, y=200)

    l5 = tk.Label(frame_display, text="Year Built", background="#ff66b3", font=('times', 20, ' bold '), width=10, fg='white')
    l5.place(x=90, y=250)
    yr_built_entry = tk.Entry(frame_display, bd=2, width=5, font=("TkDefaultFont", 20), textvariable=yr_built)
    yr_built_entry.place(x=300, y=250)

    l6 = tk.Label(frame_display, text="Year Renovated", background="#ff66b3", font=('times', 20, ' bold '), width=10, fg='white')
    l6.place(x=90, y=300)
    yr_renovated_entry = tk.Entry(frame_display, bd=2, width=5, font=("TkDefaultFont", 20), textvariable=yr_renovated)
    yr_renovated_entry.place(x=300, y=300)

    l7 = tk.Label(frame_display, text="Zipcode", background="#ff66b3", font=('times', 20, ' bold '), width=10, fg='white')
    l7.place(x=90, y=350)
    zipcode_entry = tk.Entry(frame_display, bd=2, width=5, font=("TkDefaultFont", 20), textvariable=zipcode)
    zipcode_entry.place(x=300, y=350)

    button1 = tk.Button(frame_display, text="Submit", command=Detect, font=('times', 20, ' bold '), width=10)
    button1.place(x=160, y=430)

def window():
    root.destroy()

button4 = tk.Button(root, foreground="white", background="black", font=("Times", 14, "bold"),
                    text="Price Prediction", command=call_file, width=20, height=2)
button4.place(x=100, y=100)

exit_button = tk.Button(root, text="Exit", command=window, width=10, height=1, font=('times', 15, ' bold '), bg="red", fg="white")
exit_button.place(x=150, y=220)

root.mainloop()
