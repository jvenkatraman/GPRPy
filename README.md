## FOR UCLA EPSS 136C
Spring 2022

Jaahnavee Venkatraman (jaahnavee96@ucla.edu)

----------------------------------------------------------------------------------------------------------------------------------

I don't have a Mac so I don't have Terminal. What do I do?

You can either install Terminal for Windows here (https://docs.microsoft.com/en-us/windows/terminal/install) or use your Powershell Prompt in Anaconda Navigator.

----------------------------------------------------------------------------------------------------------------------------------

How do I install the software?

- Go to https://github.com/Jsci96/GPRPy, and download the Code (green button) as a zip folder.

- Extract the files from the folder.

- In terminal cd into the folder you just unzipped. I installed mine on my Desktop so in terminal I will type

  `cd /Users/jaahnavee/Desktop/GPRPy-master`

- Type the following to install the software (wait for the first process to finish before typing the next)

  `python installMigration.py`
   
   `pip install .`

  Note: GPRPy needs to be installed on Python3.8 or less. The installation will not work if you are in a Python12 environment.

- After installation you should be able to run the program by typing

  `gprpy p` [for fixed survey]
  
  `gprpy c` [for CMP/WARR surveys]
   
  in terminal.

----------------------------------------------------------------------------------------------------------------------------------

How do I run the gprpy application?

- Open terminal and type

  `gprpy p`
  
- More information on installation is available below (taken from the source README).

----------------------------------------------------------------------------------------------------------------------------------

How do I change my python environment from 3.12 to 3.8?

You have to have 'Conda' installed on your device for this to work. To check if it's installed type

`which conda`

Once Conda is installed, you can check which environment is activated by typing

`conda info --envs`

The asterisk (*) indicates the environment you're currently in. To change the environment type

`conda activate (environment name)`

Retype

`conda info --envs`

and the asterisk (*) should now be next to the new (environment name).

----------------------------------------------------------------------------------------------------------------------------------

I want to access and change the root code for the application. How do I do this?

 - In order to edit the code yourself, you will need to locate the root folder of your Anaconda application, and go to lib > python3.8 > site-packages > gprpy. Here, you will find all the python scripts used by GPRPy. Note that changing the code or replacing files on your Desktop gprpy folder will not make direct changes to the application.
 
 - If you are looking to switch out the files to add the 'custom' color option, replace gprpy > gprpyGUI.py with the corresponding file in my git repository above.
 
----------------------------------------------------------------------------------------------------------------------------------

How do I view the GPS tracks on Google Earth?

- In the folder GPRPy-master > gprpy is a script called txt_to_kml.py. Open it in Spyder.
- Follow the instructions in the code header to produce a .kml file from your MALA GPS tracks (.cor.txt files).
- Go to Google Earh, click on the 'Projects' tab > Open > Import KML file from computer.

----------------------------------------------------------------------------------------------------------------------------------

And you're all set- enjoy!
Feel free to email me / drop by Dave's office if you have any questions. Below this begins the source README.

# GPRPy
Open-source Ground Penetrating Radar processing and visualization software. Supported by the National Science Foundation under grant [EAR-1550732](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1550732).

![Profile GUI](profileGUI.png)

![CMP/WARR GUI](CWGUI.png)

## Simplemost installation

**In the following instructions, if you use Windows, use the comands `python` and `pip`. If you use Mac or Linux, use the commands `python3` and `pip3` instead.**

1) Download the GPRPy software from 
   [https://github.com/NSGeophysics/GPRPy/archive/master.zip](https://github.com/NSGeophysics/GPRPy/archive/master.zip). <br/>
   Save the file somewhere on your computer and extract the zip folder. <br/>
   As an **alternative**, you can install git from [https://git-scm.com/](https://git-scm.com/), then run in a command prompt:<br/>
   `git clone https://github.com/NSGeophysics/GPRPy.git`<br/>
   The advantage of the latter is that you can easily update your software by running from the GPRPy folder in a command prompt:<br/>
   `git pull origin master`

2) Install Python 3.7 or higher. You can obtain it for example from [https://conda.io/miniconda.html](https://conda.io/miniconda.html)

3) Once the installation finished, open a command prompt that can run Python <br/>
   On Windows: click on Start, then enter "Anaconda Prompt", without the quotation marks into the "Search programs and files" field. On Mac or Linux, open the regular terminal.

4) In the command prompt, change to the directory  where you downloaded the GPRPy files.
   This is usually through a command like for example<br/>
   `cd Desktop\GPRPy`<br/>
   if you downloaded GPRPy directly onto your desktop. Then type the following and press enter afterward:<br/>
   `python installMigration.py`<br/>
   Then type the following and press enter afterward:<br/>
   `pip install .`<br/>
   **don't forget the period "." at the end of the `pip install` command**


## Running the software
After installation, you can run the script from the Anaconda Prompt (or your Python-enabled prompt) by running either<br/>
`gprpy`<br/>
or<br/>
`python -m gprpy`

The first time you run GPRPy it could take a while to initialize. GPRPy will ask you if you want to run the profile [p] or WARR / CMP [c] user interface. Type<br/>
`p`<br/>
and then enter for profile, or<br/>
`c`<br/>
and then enter for CMP / WARR.

You can also directly select one by running either<br/>
`gprpy p`<br/>
or<br/>
`gprpy c`<br/>
or<br/>
`python -m gprpy p`<br/>
or<br/>
`python -m gprpy c`


## Running automatically generated scripts
To run automatically generated scripts, open the command prompt that can run python (for example Anaconda Prompt), switch to the folder with the automatically generated script and run<br/>
`python myscriptname.py`<br/>
where myscriptname.py is the name of your automatically generated script.  


## In case of trouble
If you have several versions of python installed, for example on a Mac or Linux system, replace, in the commands shown earlier,
`python` with `python3`<br/>
and<br/>
`pip` with `pip3`

If you have any troubles getting the software running, please send me an email or open an issue on GitHub and I will help you getting it running.


## Uninstalling GPRPy
To uninstall GPRPy, simply run, in the (Anaconda) command prompt<br/>
`pip uninstall gprpy`

## News
Follow [@GPRPySoftware](https://twitter.com/GPRPySoftware) on twitter to hear about news and updates.
Recent tweets:

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Fixed small issue that led to multiples when picking points in profile. Thanks Marcus Pacheco for pointing it out! If you use picking in profile mode, please update to version 1.0.3 (uninstall the old version before).</p>&mdash; GPRPy (@GPRPySoftware) <a href="https://twitter.com/GPRPySoftware/status/1139243564469313536?ref_src=twsrc%5Etfw">June 13, 2019</a></blockquote>

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">I will post updates, changes, and GPRPy news here.</p>&mdash; GPRPy (@GPRPySoftware) <a href="https://twitter.com/GPRPySoftware/status/1089246592786485251?ref_src=twsrc%5Etfw">January 26, 2019</a></blockquote>

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">GPRPy is a free ground penetrating radar processing and visualization software developed at the University of Alabama. You can download it and install it following the instructions here: <a href="https://nsgeophysics.github.io/GPRPy/">nsgeophysics.github.io/GPRPy/</a></p>&mdash; GPRPy (@GPRPySoftware) <a href="https://twitter.com/GPRPySoftware/status/1088806792191197188?ref_src=twsrc%5Etfw">January 25, 2019</a></blockquote>


