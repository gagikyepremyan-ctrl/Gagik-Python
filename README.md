1. The Initial Roll (The "Come-Out" Roll)
When you start the game, the script picks two random numbers between 1 and 6. Based on the sum of these numbers, one of three things happens:

Natural Win: If you roll a 7 or 11, you win immediately.

Craps (Loss): If you roll a 2, 3, or 12, the "house" wins immediately.

Setting the Point: If you roll any other number (4, 5, 6, 8, 9, or 10), that number becomes your "goal" (physically known as the "point").

2. The "Goal" Phase
If a goal is set, the script enters a while True loop. You must continue rolling the dice by pressing Enter until one of two things happens:

You hit your goal: You roll the same total you got on the first turn. You win!

You "Seven Out": You roll a 7 before hitting your goal. The casino wins.

3. A Hidden Logic Error (Recursion)
There is a specific function in your code called rotate_dice(). If you lose by rolling a 7 during the goal phase, the code calls rotate_dice(), which then calls roll_dice() all over again.

[!CAUTION]
Infinite Loop Risk: Because roll_dice calls rotate_dice and rotate_dice calls roll_dice, the game will automatically start a brand new round every time you lose in the second phase. This is called recursion. If you play for a very long time without stopping, the program could eventually crash due to a "stack overflow."
