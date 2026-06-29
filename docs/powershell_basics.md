# Basic PowerShell Commands

## Navigation

- `cd <folder>`  
  Change directory (move into a folder)

- `cd ..`  
  Move one directory up

- `ls` or `dir`  
  List files and folders in the current directory

---

## Current Location

- `pwd`  
  Show the current directory path

---

## Files and Folders

- `type <file>`  
  Display the contents of a file

- `echo <text>`  
  Print text to the console

- `mkdir <name>`  
  Create a new folder

- `ni <name>`  
  Create a new file (New-Item shortcut)

---

## Deleting

- `rm <file>`  
  Remove a file

- `rm -r <folder>`  
  Remove a folder and its contents

---

## Help and Console

- `help <command>`  
  Show help for a command

- `clear`  
  Clear the console screen

---

## Examples

```powershell
cd Downloads
ls
mkdir test
ni file.txt
rm file.txt