"""Custom Turtle Shape Creator."""

import tkinter as tk 


#Program settings
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
CENTRE_X = CANVAS_WIDTH // 2
CENTRE_Y = CANVAS_HEIGHT // 2

points = []


def add_point(event):
  """Record a point clicked by the user."""
  x = event.x  - CENTRE_X
  y = CENTRE_Y - event.y

  points.append((x, y))

  canvas.create_oval(
      event.x - 3,
      event.y - 3,
      event.x + 3, 
      event.y + 3,
      fill="black"
  )

  if len(points) >= 2:
    previous = points[-2]

    canvas.create_line(
            previous[0] + CENTRE_X,
            CENTRE_Y - previous[1],
            event.x,
            event.y
        )

  coordinate_label.config(
      text=f"Coordinates: {tuple(points)}"
  )

  print("Coordinates:", tuple(points))


def create_shape():
    """Show the completed shape."""
    if len(points) < 3:
        status_label.config(
            text="Please add at least 3 points."
        )
        return

    canvas.create_polygon(
        [
            (x + CENTRE_X, CENTRE_Y - y)
            for x, y in points
        ],
        fill="lightblue",
        outline="black"
    )

    status_label.config(
        text="Shape created successfully."
    )


def clear_shape():
    """Clear the current drawing."""
    points.clear()
    canvas.delete("all")

    coordinate_label.config(
        text="Coordinates: ()"
    )

    status_label.config(
        text="Drawing cleared."
    )


def save_code():
    """Generate and save a Turtle Python program."""
    if len(points) < 3:
        status_label.config(
            text="Create a shape before saving."
        )
        return

    code = f'''"""Generated Custom Turtle Shape."""

import turtle


screen = turtle.Screen()
screen.title("My custom turtle shape")

shape = turtle.Shape("compound")

shape_points = {tuple(points)}

shape.addcomponent(
    shape_points,
    "lightblue",
    "black"
)

screen.register_shape(
    "custom_shape",
    shape
)

my_turtle = turtle.Turtle()
my_turtle.shape("custom_shape")

turtle.done()
... 

    with open(
        "custom_turtle_shape.py",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(code)

    status_label.config(
        text="Python Turtle code saved!"
    )


def start_program():
    """Open the drawing interface."""
    welcome.destroy()

    title_label = tk.Label(
        window,
        text="Custom Turtle Shape Creator",
        font=("Arial", 18, "bold")
    )
    title_label.pack(pady=10)

    instructions = tk.Label(
        window,
        text="Click around the canvas to draw your shape."
    )
    instructions.pack()

    global canvas
    canvas = tk.Canvas(
        window,
        width=CANVAS_WIDTH,
        height=CANVAS_HEIGHT,
        bg="white"
    )
    canvas.pack(pady=10)

    canvas.bind(
        "<Button-1>",
        add_point
    )

    global coordinate_label
    coordinate_label = tk.Label(
        window,
        text="Coordinates: ()",
        font=("Arial", 10)
    )
    coordinate_label.pack(pady=5)

    button_frame = tk.Frame(window)
    button_frame.pack(pady=5)

    create_button = tk.Button(
        button_frame,
        text="Create Shape",
        command=create_shape
    )
    create_button.grid(
        row=0,
        column=0,
        padx=5
    )

    clear_button = tk.Button(
        button_frame,
        text="Clear",
        command=clear_shape
    )
    clear_button.grid(
        row=0,
        column=1,
        padx=5
    )

    save_button = tk.Button(
        button_frame,
        text="Save Python Code",
        command=save_code
    )
    save_button.grid(
        row=0,
        column=2,
        padx=5
    )

    global status_label
    status_label = tk.Label(
        window,
        text="Ready to draw."
    )
    status_label.pack(pady=5)









  
