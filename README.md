# World War BATTLES!

World War Battles is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

It is a single player game, where a player is playing against the computer to find its hidden ships. All ships have to be sunk to win the game.

[Here is the live version of my project](https://world-war-battles-c242ecc67e54.herokuapp.com/)


![Responsive screens](README.md.docs/image.png)

## How To Play Game

The game uses Legends which help a player know when a hit or miss takes place. A `X` is used to mark a hit, so when a ship is hit, the plaaceholder will be replaced by and `X`. A `&` marks the position in whic the ship is located. `O` is used as a placeholder. The `-` is used when a player missed the ship, and that means a loss.

The player as well as the computer take turns in guessing where the ship of the other is located in order to win. Once an oponent makes a correct guess, then they win. 

## Features
### Existing Features
- Player's and computer's initial structure of the board.
    - A player will insert their their name as well as their desired board size.
    - No guesses take place on this section

![alt text](image-8.png) 

- This is the initial board. This is where a player sees where their ships are located. 

![Initial board](image-10.png)

- This feature checks if the a valid number has been inserted or not.

![Number validation](image-11.png)

- When everything has been added accordingly, the game will continue running.

![Running game](image-12.png)

- A player will be prompted to guess the computer's ship location by inserting coordinates of the location.
- The computer will guess the locataion of the Player's ship.
- Ships will be invisible 

![alt text](image-9.png)

- When the game ends, or player turns are over, the below message with appear:

![End game](image-13.png)

## Testing
* I have manually tested my code using PEP8 Python Validator.
* The results given: too many blank line, my code has many missing spaces after the ',' especially inside parenthesis's, and some lines are too long.

## Bugs
A board could not be created as it was not defined properly. It was not set properly
![alt text](image.png)

![alt text](image-1.png)

![alt text](image-2.png)

![alt text](image-3.png)

In order to check if the game is running, I had used a list as seen on the below screen shot to tell if the ships have been hit or not. I used ‘!’ exclamation marks as placeholders, however my Mentor advised I use a different legend for good user experience. Please see below for previous matrix:

![Old matrix](image-4.png)

![alt text](image-5.png)

![alt text](image-6.png)

![invalid int](image-16.png)

![Reeated guess](image-15.png)

## Deployment
This project was deployed using Code Insitutte's mock terminal for Heroku.

- Steps for deployment:
    - Fork or clone this repository
    - Create a new Heroku App
    - Set the buildbacks to Python and NodeJS in that order
    - Link the Heroku app to the repository
    - Click on Deploy


## Credits
* For a better understanding of creating a Battleships game [Knowledge Mavens](https://www.google.com/search?q=how+to+make+a+simple+battleship+game+in+python&sca_esv=8c3f90bc5e947fd3&ei=eBfoZq3IDoy0hbIPvszCkQU&oq=how+to+create+battleship+game+in+python&gs_lp=Egxnd3Mtd2l6LXNlcnAiJ2hvdyB0byBjcmVhdGUgYmF0dGxlc2hpcCBnYW1lIGluIHB5dGhvbioCCAEyBhAAGBYYHjIGEAAYFhgeMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCBAAGIAEGKIEMggQABiABBiiBDIIEAAYgAQYogQyCBAAGIAEGKIESLNjUOUGWJ8VcAF4AJABAJgBlwOgAaghqgEGMy0xMC4yuAEByAEA-AEBmAICoAKuA8ICChAAGLADGNYEGEeYAwCIBgGQBgiSBwUxLjQtMaAHpTs&sclient=gws-wiz-serp#fpstate=ive&vld=cid:3353d00c,vid:tF1WRCrd_HQ,st:0)
* Code Institute for the deployment terminal.
* Matt Rudge's Ultimate Battleships walkthrough for the structure of the game.
