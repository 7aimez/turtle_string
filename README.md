<div align="center">
   <h1>Turtle String</h1>
   <b>Converts a string into a turtle drawing</b>
   
   <br /><br />

   <img src="https://img.shields.io/github/languages/count/7aimez/turtle_string" />
   <img src="https://img.shields.io/github/languages/top/7aimez/turtle_string?logo=python" />
   <img src="https://img.shields.io/github/stars/7aimez/turtle_string" />
   <img src="https://img.shields.io/github/forks/7aimez/turtle_string" />
</div>

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

Run [auto.sh](install/auto.sh) (for raw, use https://github.com/7aimez/turtle_string/raw/refs/heads/main/install/auto.sh), to automatically install Turtle String. Then, edit the setup dictionary just inside the `main()` function to your preferences. Finally, run the program in _python_:

```sh
python main.py
```

## Contents

- [`src`](src/) - Contains source files and python code
- [`install`](install/) - Install _Turtle String_
- [`key`](key/) - Contains the key for lettering and the text arguments
- [`src/examples`](src/examples/) - Contains example of the code being used

## License

_Turtle String_ is under the MIT Licesnse. Read [LICENSE](LICENSE) to find out more.
