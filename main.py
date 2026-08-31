"""Custom Turtle Shape Creator."""

import tkinter as tk 


#Program settings
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
CENTRE_X = CANVAS_WIDTH // 2
CENTRE_Y = CANVAS HEIGHT // 2

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









  
