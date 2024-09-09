# Maze Solver

![maze-solver](https://github.com/user-attachments/assets/2b0c27da-e1ca-4c7e-b059-73c2f085c780)

## Description

This application creates a maze and solves it. That's it. It's quite simple 🤷🏻‍♂️.

## Getting Started

### Dependencies

* Python3
* tkinter

### Installing

1. Install [dependencies](#dependencies) mentioned above.
2. Clone this repository.
```
git clone https://github.com/peshala-prabhapoorna/maze-solver.git
```

### Executing program

* Run the following command from inside the cloned repository (`cd maze-solver`).
```
./run
```

## Help

### Denial of permission for `run` script
If the terminal spits out an error like `-bash: ./run: Permission denied` when you try to run the application with `./run`. Give the script file execute permission by running the following command.
```
chmod +x run
```

### Working with tkinter
Let's start by just making sure that your tkinter installation is working. Tkinter is a Python library that allows us to create graphical user interfaces (GUIs) for our programs.

For most systems, `tkinter` will work out of the box. Run the following command in your terminal to see if it's installed:
```
python -m tkinter
```
You should see a little window pop up with some buttons inside. If you do, great! You can close that window, you're done with this step.
If you do have issues, read on.

#### Problems with Tkinter? Install missing dependencies
If you're seeing an error like this you may need to install some dependencies: `ModuleNotFoundError: No module named '_tkinter'`. First, check to see which version of python you are using:
```
python --version
```
You should be on 3.10 or higher. If you're not, update your Python version.

Next, it's important to understand that `tkinter` depends on the `Tcl/Tk` library. I've found that the installing the `tk-dev` or `python-tk` packages are usually the easiest way to install and link it to your Python version. On Ubuntu (Linux), run:
```
sudo apt-get install python3-tk
```
On Mac OS, make sure you have Homebrew installed, and then run:
```
brew install python-tk
```
**Your versions of python-tk and python should match!**

Now, if `python -m tkinter` still isn't working, you may need to uninstall and reinstall Python so that it links to the now-available `Tcl/Tk` library.

## Authors

[Peshala Prabhapoorna](https://www.linkedin.com/in/peshala-prabhapoorna/)

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

This project was built as a part of the Boot.dev backend developer program.
* [Boot.dev - Build a Maze Solver](https://www.boot.dev/courses/build-maze-solver-python)
