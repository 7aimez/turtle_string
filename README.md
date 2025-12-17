# Turtle String

**Converts a string into a turtle drawing**

---

## About

This python script splits up the text, uses the letter functions to draw the letter using `t.goto(x, y)`, reletive to the bottom left corner of the letter, e.g. `t.goto(x+10, y+20)`.

## Features

- All letters (a-z)
- Special characters (`.`, `,`, `!`, `?`, `'`)
- Background colour
- Letter spacing
- Line spacing
- Text line width ('boldness')

## Requirements

- Python 2.5 or later
- Turtle libs


## Get Started

**Follow these steps to use _Turtle String_:**

### Manually

1. Clone the repo
   
   ```sh
   git clone https://github.com/7aimez/turtle_string.git
   ```
3. Move into the source folder
   
   ```sh
   cd turtle_string/src
   ```

4. Edit the setup dictionary just inside the `main()` function to your preferences
5. Run the program in _python_

   ```sh
   python main.py
   ```

6. **Done!** Watch your text appear on the screen

### Automatically

Run [auto.sh](install/auto.sh) to automatically install Turtle String. Then, edit the setup dictionary just inside the `main()` function to your preferences. Finally, run the program in _python_:

```sh
python main.py
```

## Contents

- [`src`](src/) - Contains source files and python code
- [`key`](key/) - Contains the key for lettering and the text arguments
- [`src/examples`](src/examples/) - Contains example of the code being used
