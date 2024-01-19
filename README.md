# **Word Block:** a 2-dimensional square acrostic generator

Description
------
**Word Block** is a program which takes inspiration from *Wordle* and the *Sator Square*. Given an input word, the program uses a recursive  
function to find all possible two-dimensional acrostics containing the input word, where each side is the length of the input word, and prints  
them to the terminal. Currently, the program selects from a dictionary containing all English words, [found here](https://www.bragitoff.com/2016/03/english-dictionary-in-csv-format/).
This has proven to be a limitation on the program's usability, not only are the vast majority of output word blocks full of esoteric and archaic words,  
but this dictionary also contains non-alphabetic characters that are known to cause crashes in some circumstances. In the future, I plan to  
reimplement the dictionary search with [MIT's 10,000 most common English words](https://www.mit.edu/~ecprice/wordlist.10000).  

Given the starting word "beer", [here's an example of terminal output.](images/driver_output.jpg)  

Personally, my favorite find so far has been this:  

b &nbsp; a &nbsp; b &nbsp; y  
e &nbsp; y &nbsp; &nbsp;l &nbsp; e  
e &nbsp; l &nbsp; &nbsp;u &nbsp; l  
r &nbsp; e &nbsp; e &nbsp; k  

beer: grain-based fermented alcohol  
ayle: archaic term for grandfather  
blue: color  
yelk: archaic form of 'yolk'  

baby: everyone knows what a baby is  
eyle: archaic form of 'ail'  
elul: month in the Hebrew calendar corresponding to August - September  
reek: state of smelling badly  

The program is actually run on 'driver.py', but if you want a look under the hood, most of the interesting stuff is happening in 'wordblock.py'.

Background
------
When I started writing this program, I was just wrapping up Al Sweigart's excellent introduction to Python, [Automate the Boring Stuff](https://automatetheboringstuff.com),  
and like many of my friends I was swept up in the *Wordle* craze. Word puzzles like this were a novel concept to me, and I needed a project to  
synthesize what I'd learned so far, so I started researching potential game ideas, with "Sudoku, but words" as a jumping-off point. Almost  
immediately I found out Wordoku already exists, so that idea was bunk, but I'd also stumbled upon an ancient curio called the *Sator Square*. 

[Example of a Sator Square found in  Oppède-le-Vieux, France, dating from the Medieval period](images/sator_square.jpg)

Believed to have originated in the Roman Empire, and later adopted into Christian iconography, the Sator Square is a type of acrostic,  
traditionally containing five latin words: Sator, Rotas, Arepo, Opera, and Tenet, arranged so that the square can be read from any direction.  
Though the palindromic nature of the Sator Square and similar acrostics non-viable for a Wordle-like game due to the repetition of  
characters, the concept of a square of interlacing words adds an interesting level of complexity to the puzzle, and increases the number of  
possible word combinations for replayability's sake.  

As of now, the program's sole function is to generate word blocks, which has been interesting enough for me as I'm simply not clever enough to come up with them without the brute force of a computer.


Installation & Use
------
All program files should be installed under the same parent folder in order to preserve relative file paths called on in the code.

Using the program is simple, just run 'driver.py' and it will begin printing to the terminal all possible word blocks containing the word "beer".  
Feel free to try different starting words! Open 'driver.py' in your favorite text editor, and change the value of the variable any word of your  
choice, or any combination of letters, really. The program isn't dependent on the starting word existing in the dictionary, so you can use your  
name, your pet's name, your favorite place, or some gobbledigook, and it'll still work. However, I recommend using 5-letter words or less. In my  
experience, there appears to be some optimization issues with longer words.  

**NOTE: Only use lower-case, the program is case-sensitive!**  


Future Plans
------
Listed in order of priority:
1. Migrate the dictionary on which this program is based to the simplified MIT dictionary of the 10,000 most common English words.
2. Develop a simple UI to accept and validate input words, and to allow the user to prematurely stop the generation of word blocks without aborting the program entirely.
3. Write new code to generate and write **all** possible word blocks of a given side-length. This only makes sense once the new dictionary is implemented, as the number of possible words will be an order of magnitude smaller. It takes an unreasonably long time to generate all possible word blocks *with* a starting word under the current dictionary. A list of all word blocks would form the basis for a Wordle-clone.
