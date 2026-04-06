# Python Sandbox

## Project Overview
A simple Python sandbox designed for educational purposes, particularly for beginners. It provides a menu-driven console interface to explore and run various basic Python scripts.

## How It Works
- `main.py` is the entry point — it scans the directory for `.py` files and presents a numbered menu
- The user selects a script by number, and it runs that script in a subprocess
- New scripts can be added simply by dropping `.py` files into the project root

## Project Structure
- `main.py` — Main launcher with menu-driven interface
- `hello_world_console.py` — Basic "Hello World" console example
- `hello_world_turtle.py` — Graphical "Hello World" using the `turtle` library
- `input_print.py` — Simple user input and output demonstration
- `README.md` — Documentation in Ukrainian

## Running the Project
The app runs as a console application:
```
python main.py
```

## Dependencies
- Python 3.11 (standard library only)
- `tkinter` — Required by the `turtle` module for graphics

## Architecture Notes
- No external packages required
- Uses `subprocess` to isolate each script execution
- Flat file structure — all scripts live in the project root
