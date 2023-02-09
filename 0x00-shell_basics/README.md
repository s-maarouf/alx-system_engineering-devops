# About these scripts

## 1) 0-current_working_directory
	This script prints the absolute path name of the current working directory.

## 2) 1-listit
	This script displays the contents list of your current directory.

## 3) 2-bring_me_home
	This script changes the working directory to the user’s home directory.

## 4) 3-listfiles
	This script Display current directory contents in a long format.

## 5) 4-listmorefiles
	This script displays the current directory's contents:
		-including hidden files.
		-using the long format.

## 6) 5-listfilesdigitonly
	This script displays the current directory's contents:
		-using long format.
		-with user and group IDs displayed numerically.
		-including hidden files.

## 7) 6-firstdirectory
	This script creates a directory named `my_first_directory` in the `/tmp/` directory.

## 8) 7-movethatfile
	This script moves the file **betty** from `/tmp/` to `/tmp/my_first_directory`.

## 9) 8-firstdelete
	This script deletes the file **betty** from `/tmp/my_first_directory`.

## 10) 9-firstdirdeletion
	This script deletes the directory `my_first_directory` that is in the `/tmp` directory.

## 11) 10-back
	This script changes the working directory to the previous one.

## 12) 11-lists
	This script prints the type of the file named **iamafile** that is in the `/tmp` directory.

## 13) 13-symbolic_link
	This script creates a symbolic link to `/bin/ls`, **named __ls__**.

## 14) 14-copy_html
	This script copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.

## 15) 100-lets_move
	This script moves all files beginning with an uppercase letter to the directory `/tmp/u`.

## 16) 101-clean_emacs
	This script deletes all files in the current working directory that end with the character **~**.

## 17) 102-tree
	This script creates the directories `welcome/`, `welcome/to/` and `welcome/to/school` in the current directory. But onlu using two spaces in the script.

## 18) 103-commas
	This script lists all the files and directories of the current directory, separated by commas **,**.
		-Directory names should end with a slash **/**
		-Files and directories starting with a dot **.** should be listed
		-The listing should be alpha ordered, except for the directories . and .. which should be listed at the very beginning


## 19) school.mgc
	This file can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0.
