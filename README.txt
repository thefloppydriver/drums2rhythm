What it does:
drums2rhythm re-charts the 4-lane drum section of a .chart file into the rhythm guitar section without messing with ANYTHING other than the rhythm guitar section.

Why it does it:
drums2rhythm is essentially a workaround for Clone Hero that enables you to play the drum charts.

How it does it:
If you want to know exactly how it works, look at the script (python 3 is fairly close to english and the script is mostly for loops and simple math.) but in short, drums2rhythm replaces the open (purple) note with the 5th (orange) note.

What to do?:
Put drums2rhythm.exe (or .py) into the folder with the .chart (the file MUST be named "notes.chart" or the program won't work.) file that you want to have re-charted and double-click the file.
That's it :]

What drums2rhythm DOESN'T do:
drums2rhythm does NOT chart songs to 4-lane drums. The .chart file must ALREADY HAVE the drums charted.
drums2rhythm does NOT work with .mid files (yet.) To convert a .mid file to a .chart file, download moonscraper, open the .mid file, click "File" in the top left corner, click "Export", then put the .chart file into the folder that had the .mid file that you just exported.
drums2rhythm does NOT add drum support to Clone Hero. drums2rhythm is a WORKAROUND that charts the drums to the already supported rhythm guitar.
drums2rhythm does NOT corrupt your files. The VERY first thing that drums2rhythm does (after setting up global variables and importing the needed modules) is to copy the original .chart file, rename it to "notes.chartbackup", and paste it in the folder with the original .chart file.


MR. PROGRAMMER SIR, I HAVE AN IIIIIISSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSUUUUUUUUUUUUUUUUEEEEEEEEEEEEEEEEEEEEEEE!!!!!!!!!!!!!:
You can report a bug via github, email me at thefloppydriver@gmail.com, or message me (thefloppydriver#9210) on the drums2rhythm discord server at https://discord.gg/Fm7DQv3