# Dynamic Snakes & Ladders
Python program to create and play Snakes and Ladders with any board width.


### To Play:
````
python3 main.py
```````
### To Run tests: 
````
python3 -m unittest discover tests
````

## Game Modes
1. Auto :- The quickest game. Die is rolled automatically, directly see the results of the game.
2. Auto-Slowed :- The game goes on like auto mode but each turn is slowed down so that output is each turn is readable.
3. Manual :- Player must press enter to roll the die for each turn. 

## Game Rules:
1. Players roll die and move the given number of steps.
2. They land on a snake head, ladder start or empty space.
3. On landing on snake head the player is swallowed and stops at the snake tail.
4. On landing on ladder start the player climbs the ladder and stop at ladder end.
5. On landing on empty space nothing happens.
6. Players get an extra chnace on rolling 6.
7. Player reaching the End wins.

## Components:
1. Board
2. Snakes (Long, Short)
3. Ladders (Long, Short)
4. Players

## Steps:
1. Make Board. => validate
2. Add Snakes. => validate
3. Add Ladders. => validate
4. Select number of players.
5. Start Game.
6. Roll die.
7. Move the given number of steps.
8. Check for Snake/Ladder.
9. Perform required action.
10. Repeat step 6 to 9 till all players reach the end.
11. Show stats.
12. End

## Validation for Components
1. Board (N x N)
    1. Must be Square
    2. N >= 10.
    3. Total Snakes/Ladders = (N/2 + 1) (Short = 60%, Long = 40%).
    4. (Snakes or Ladders) per row/column < 20% of Total Snakes & Ladders

2. Snakes.
    1. Head > Tail
    2. Head and Tail not in same/adjacent row
    3. Head/Tail not at Start/End of Board
    4. Head/Tail not in same postion as Ladder Start/End.
    5. Short Snake should not span more than (20% of N) rows and less than 1 row.
    6. Long Snakes should not span more than (60% of N) rows and less than (20% of N) rows.
    7. No Head in first row.

3. Ladders.  
    1. Start < End.
    2. Start and End not in same/adjacent row.
    3. Start/End not at Start/End of Board
    4. Start/End not in same postion as Snake Head/Tail.
    5. Short Ladder should not span more than (20% of N) rows and less than 1 row.
    6. Long Ladder should not span more than (60% of N) rows and less than (20% of N) rows.
    7. No Start in Last Row.
    