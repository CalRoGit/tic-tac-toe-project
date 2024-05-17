## Imports ##
import random
import stddraw
import stdarray
import DrawXO

## Global variables ##
gameRunning = True
menu = True

## Setting default canvas ##
stddraw.setXscale(0, 10)
stddraw.setYscale(0, 10)
stddraw.clear(stddraw.DARK_GRAY)
stddraw.setPenColor(stddraw.WHITE)
stddraw.setPenRadius(0.03)


## Definitions ##
def button(x, y, t, w, h):
    """
    Create a button with stddraw
    Args:
    x (int): X position of button
    y (int): Y position of button
    t (str): Text in button
    w (int): Width of side of rectangle
    h (int): Height of side of rectangle
    """
    stddraw.line(x, y, (x + w), y)
    stddraw.line(x, y, x, (y + h))
    stddraw.line(x, (y + h), (x + w), (y + h))
    stddraw.line((x + w), (y + h), (x + w), y)
    stddraw.text((x + w/2), (y + h/2), t)

def TTTboard():
    """
    Create a regular sized tic-tac-toe board
    """
    stddraw.line(4, 8, 4, 2)
    stddraw.line(6, 8, 6, 2)
    stddraw.line(2, 4, 8, 4)
    stddraw.line(2, 6, 8, 6)

def storeBoard(array):
    """
    Function that stores the board and reprints the board after each turn
    Args:
    array (int array): Array of moves on the board
    """
    TTTboard()
    for col in range(9):
        if array[col] == 1:
            if col == 0:
                DrawXO.DrawX(2.25, 7.8)
            if col == 1:
                DrawXO.DrawX(4.25, 7.8)
            if col == 2:
                DrawXO.DrawX(6.25, 7.8)
            if col == 3:
                DrawXO.DrawX(2.25, 5.8)
            if col == 4:
                DrawXO.DrawX(4.25, 5.8)
            if col == 5:
                DrawXO.DrawX(6.25, 5.8)
            if col == 6:
                DrawXO.DrawX(2.25, 3.8)
            if col == 7:
                DrawXO.DrawX(4.25, 3.8)
            if col == 8:
                DrawXO.DrawX(6.25, 3.8)
        
        if array[col] == 2:
            if col == 0:
                stddraw.setPenRadius(0.005)
                DrawXO.DrawO(3, 7, 0.9)
                stddraw.setPenRadius(0.03)
            if col == 1:
                stddraw.setPenRadius(0.005)
                DrawXO.DrawO(5, 7, 0.9)
                stddraw.setPenRadius(0.03)
            if col == 2:
                stddraw.setPenRadius(0.005)
                DrawXO.DrawO(7, 7, 0.9)
                stddraw.setPenRadius(0.03)
            if col == 3:
                stddraw.setPenRadius(0.005)
                DrawXO.DrawO(3, 5, 0.9)
                stddraw.setPenRadius(0.03)
            if col == 4:
                stddraw.setPenRadius(0.005)
                DrawXO.DrawO(5, 5, 0.9)
                stddraw.setPenRadius(0.03)
            if col == 5:
                stddraw.setPenRadius(0.005)
                DrawXO.DrawO(7, 5, 0.9)
                stddraw.setPenRadius(0.03)
            if col == 6:
                stddraw.setPenRadius(0.005)
                DrawXO.DrawO(3, 3, 0.9)
                stddraw.setPenRadius(0.03)
            if col == 7:
                stddraw.setPenRadius(0.005)
                DrawXO.DrawO(5, 3, 0.9)
                stddraw.setPenRadius(0.03)
            if col == 8:
                stddraw.setPenRadius(0.005)
                DrawXO.DrawO(7, 3, 0.9)
                stddraw.setPenRadius(0.03)

def doMove(player, array, index):
    """
    Executes the move that the player has selected
    Args:
    player (int): Player 1 or 2
    array (int array): Array of moves on the board
    index (int): Space on board
    """
    if player == 1:
        # Top left
        if index == 0:
            array[index] = 1
            DrawXO.DrawXAnimation(2.25, 7.8)
        # Top middle
        if index == 1:
            array[index] = 1
            DrawXO.DrawXAnimation(4.25, 7.8)
        # Top right
        if index == 2:
            array[index] = 1
            DrawXO.DrawXAnimation(6.25, 7.8)
        # Middle left
        if index == 3:
            array[index] = 1
            DrawXO.DrawXAnimation(2.25, 5.8)
        # Middle middle
        if index == 4:
            array[index] = 1
            DrawXO.DrawXAnimation(4.25, 5.8)
        # Middle right
        if index == 5:
            array[index] = 1
            DrawXO.DrawXAnimation(6.25, 5.8)
        # Bottom left
        if index == 6:
            array[index] = 1
            DrawXO.DrawXAnimation(2.25, 3.8)
        # Bottom middle
        if index == 7:
            array[index] = 1
            DrawXO.DrawXAnimation(4.25, 3.8)
        # Bottom right
        if index == 8:
            array[index] = 1
            DrawXO.DrawXAnimation(6.25, 3.8)

    if player == 2:
        # Top left
        if index == 0:
            array[index] = 2
            stddraw.setPenRadius(0.005)
            DrawXO.DrawOAnimation(3, 7, 0.9)
            stddraw.setPenRadius(0.03)
        # Top middle
        if index == 1:
            array[index] = 2
            stddraw.setPenRadius(0.005)
            DrawXO.DrawOAnimation(5, 7, 0.9)
            stddraw.setPenRadius(0.03)
        # Top right
        if index == 2:
            array[index] = 2
            stddraw.setPenRadius(0.005)
            DrawXO.DrawOAnimation(7, 7, 0.9)
            stddraw.setPenRadius(0.03)
        # Middle left
        if index == 3:
            array[index] = 2
            stddraw.setPenRadius(0.005)
            DrawXO.DrawOAnimation(3, 5, 0.9)
            stddraw.setPenRadius(0.03)
        # Middle middle
        if index == 4:
            array[index] = 2
            stddraw.setPenRadius(0.005)
            DrawXO.DrawOAnimation(5, 5, 0.9)
            stddraw.setPenRadius(0.03)
        # Middle right
        if index == 5:
            array[index] = 2
            stddraw.setPenRadius(0.005)
            DrawXO.DrawOAnimation(7, 5, 0.9)
            stddraw.setPenRadius(0.03)
        # Bottom left
        if index == 6:
            array[index] = 2
            stddraw.setPenRadius(0.005)
            DrawXO.DrawOAnimation(3, 3, 0.9)
            stddraw.setPenRadius(0.03)
        # Bottom middle
        if index == 7:
            array[index] = 2
            stddraw.setPenRadius(0.005)
            DrawXO.DrawOAnimation(5, 3, 0.9)
            stddraw.setPenRadius(0.03)
        # Bottom right
        if index == 8:
            array[index] = 2
            stddraw.setPenRadius(0.005)
            DrawXO.DrawOAnimation(7, 3, 0.9)
            stddraw.setPenRadius(0.03)

def checkWin(player, array):
    """
    Check whether a 3 in a row occurs
    Args:
    player (int): Player 1 or 2
    array (int array): Array of moves on the board
    Returns:
    True if win, "Draw" if draw and false otherwise
    """
    # Check rows
    if player == 1:
        if array[0] == 1 and array[1] == 1 and array[2] == 1:
            stddraw.line(2, 7.05, 8, 7.05)
            return True
        if array[3] == 1 and array[4] == 1 and array[5] == 1:
            stddraw.line(2, 5.05, 8, 5.05)
            return True
        if array[6] == 1 and array[7] == 1 and array[8] == 1:
            stddraw.line(2, 3.05, 8, 3.05)
            return True
    
        # Check columns
        if array[0] == 1 and array[3] == 1 and array[6] == 1:
            stddraw.line(3, 8, 3, 2)
            return True
        if array[1] == 1 and array[4] == 1 and array[7] == 1:
            stddraw.line(5, 8, 5, 2)
            return True
        if array[2] == 1 and array[5] == 1 and array[8] == 1:
            stddraw.line(7, 8, 7, 2)
            return True
        
        # Check diagonal
        if array[0] == 1 and array[4] == 1 and array[8] == 1:
            stddraw.line(2.05, 8, 8, 2.05)
            return True
        if array[6] == 1 and array[4] == 1 and array[2] == 1:
            stddraw.line(2.05, 2.1, 8, 8.05)
            return True
        
    if player == 2:
        # Check rows
        if array[0] == 2 and array[1] == 2 and array[2] == 2:
            stddraw.line(2, 7.05, 8, 7.05)
            return True
        if array[3] == 2 and array[4] == 2 and array[5] == 2:
            stddraw.line(2, 5.05, 8, 5.05)
            return True
        if array[6] == 2 and array[7] == 2 and array[8] == 2:
            stddraw.line(2, 3.05, 8, 3.05)
            return True
    
        # Check columns
        if array[0] == 2 and array[3] == 2 and array[6] == 2:
            stddraw.line(3, 8, 3, 2)
            return True
        if array[1] == 2 and array[4] == 2 and array[7] == 2:
            stddraw.line(5, 8, 5, 2)
            return True
        if array[2] == 2 and array[5] == 2 and array[8] == 2:
            stddraw.line(7, 8, 7, 2)
            return True
        
        # Check diagonal
        if array[0] == 2 and array[4] == 2 and array[8] == 2:
            stddraw.line(2.05, 8, 8, 2.05)
            return True
        if array[6] == 2 and array[4] == 2 and array[2] == 2:
            stddraw.line(2.05, 2.1, 8, 8.05)
            return True
        
    # Check draw
    isDraw = True
    for col in range(9):
        if array[col] == 0:
            isDraw = False
            break
    if isDraw:
        return "Draw"
    else:
        return False

def compMove(player, array):
    """
    Perform computers moves
    Args:
    player (int): Player 1 or 2
    array (int array): Array of moves on the board 
    """
    doneMove = False

    while doneMove != True:
        index = random.randrange(9)

        if array[index] == 0:
            doneMove = True
            doMove(player, array, index)

def menuFunc(menu):
    while menu:
        stddraw.setFontSize(50)
        stddraw.text(5, 6, "Tic - Tac - Toe")
        stddraw.line(2.5, 5.5, 7.5, 5.5)
        stddraw.setFontSize(20)
        button(1, 2, "Multi-Player", 3, 1)
        button(6, 2, "Computer", 3, 1)
        
        if stddraw.mousePressed():
            # Multi_Player mode
            if (1 <= stddraw.mouseX() <= 4) and (2 <= stddraw.mouseY() <= 3):
                menu = False
                return 1
            # Computer mode
            if (6 <= stddraw.mouseX() <= 9) and (2 <= stddraw.mouseY() <= 3):
                menu = False
                return 2
        stddraw.show(10)

# Game loop multi-player
def gameLoopMulti():
    tictacArray = stdarray.create1D(9, 0) # Array of moves (1 = X) (2 = O)
    player = 1 # Player turn (1 = X) (2 = O)
    index = 0 # Index of spaces (eg. 0 = top left, 1 = top middle...)
    p1Score = 0 # Player 1 score
    p2Score = 0 # Player 2 score
    loopTimes = 1 # Amount of loops of game. (Chooses who plays first)
    while gameRunning:
        if checkWin(player, tictacArray) == "Draw":
            stddraw.setFontSize(40)
            stddraw.text(5, 5, "Game ends in a draw!")
            stddraw.show(2000)
            stddraw.setFontSize(20)
            tictacArray = stdarray.create1D(9, 0)
            loopTimes += 1
            if loopTimes % 2 == 0:
                player = 2
            else:
                player = 1
        
        stddraw.clear(stddraw.DARK_GRAY)
        storeBoard(tictacArray)
        stddraw.text(1, 9, "Player " + str(player) + "'s turn")
        stddraw.text(8, 9, "Player 1 score: " + str(p1Score))
        stddraw.text(8, 8.5, "Player 2 score: " + str(p2Score))
        
        if stddraw.mousePressed():
            
            # Top left
            if (2 < stddraw.mouseX() < 4) and (6 < stddraw.mouseY() < 8):
                if tictacArray[0] == 0:
                    index = 0
                    doMove(player, tictacArray, index)
                    if checkWin(player, tictacArray) == True:
                        stddraw.setFontSize(40)
                        stddraw.text(5, 5, "Player " + str(player) + " wins!")
                        stddraw.show(2000)
                        stddraw.setFontSize(20)
                        if player == 1:
                            p1Score += 1
                        if player == 2:
                            p2Score += 1

                        tictacArray = stdarray.create1D(9, 0)
                        loopTimes += 1
                        if loopTimes % 2 == 0:
                            player = 1
                        else:
                            player = 2
                        
                    player += 1

            # Top middle
            if (4 < stddraw.mouseX() < 6) and (6 < stddraw.mouseY() < 8):
                if tictacArray[1] == 0:
                    index = 1
                    doMove(player, tictacArray, index)
                    if checkWin(player, tictacArray) == True:
                        stddraw.setFontSize(40)
                        stddraw.text(5, 5, "Player " + str(player) + " wins!")
                        stddraw.show(2000)
                        stddraw.setFontSize(20)
                        if player == 1:
                            p1Score += 1
                        if player == 2:
                            p2Score += 1

                        tictacArray = stdarray.create1D(9, 0)
                        loopTimes += 1
                        if loopTimes % 2 == 0:
                            player = 1
                        else:
                            player = 2
                        
                    player += 1

            # Top right
            if (6 < stddraw.mouseX() < 8) and (6 < stddraw.mouseY() < 8):
                if tictacArray[2] == 0:
                    index = 2
                    doMove(player, tictacArray, index)
                    if checkWin(player, tictacArray) == True:
                        stddraw.setFontSize(40)
                        stddraw.text(5, 5, "Player " + str(player) + " wins!")
                        stddraw.show(2000)
                        stddraw.setFontSize(20)
                        if player == 1:
                            p1Score += 1
                        if player == 2:
                            p2Score += 1

                        tictacArray = stdarray.create1D(9, 0)
                        loopTimes += 1
                        if loopTimes % 2 == 0:
                            player = 1
                        else:
                            player = 2
                        
                    player += 1

            # Middle left
            if (2 < stddraw.mouseX() < 4) and (4 < stddraw.mouseY() < 6):
                if tictacArray[3] == 0:
                    index = 3
                    doMove(player, tictacArray, index)
                    if checkWin(player, tictacArray) == True:
                        stddraw.setFontSize(40)
                        stddraw.text(5, 5, "Player " + str(player) + " wins!")
                        stddraw.show(2000)
                        stddraw.setFontSize(20)
                        if player == 1:
                            p1Score += 1
                        if player == 2:
                            p2Score += 1

                        tictacArray = stdarray.create1D(9, 0)
                        loopTimes += 1
                        if loopTimes % 2 == 0:
                            player = 1
                        else:
                            player = 2
                        
                    player += 1

            # Middle middle
            if (4 < stddraw.mouseX() < 6) and (4 < stddraw.mouseY() < 6):
                if tictacArray[4] == 0:
                    index = 4
                    doMove(player, tictacArray, index)
                    if checkWin(player, tictacArray) == True:
                        stddraw.setFontSize(40)
                        stddraw.text(5, 5, "Player " + str(player) + " wins!")
                        stddraw.show(2000)
                        stddraw.setFontSize(20)
                        if player == 1:
                            p1Score += 1
                        if player == 2:
                            p2Score += 1

                        tictacArray = stdarray.create1D(9, 0)
                        loopTimes += 1
                        if loopTimes % 2 == 0:
                            player = 1
                        else:
                            player = 2
                    
                    player += 1

            # Middle right
            if (6 < stddraw.mouseX() < 8) and (4 < stddraw.mouseY() < 6):
                if tictacArray[5] == 0:
                    index = 5
                    doMove(player, tictacArray, index)
                    if checkWin(player, tictacArray) == True:
                        stddraw.setFontSize(40)
                        stddraw.text(5, 5, "Player " + str(player) + " wins!")
                        stddraw.show(2000)
                        stddraw.setFontSize(20)
                        if player == 1:
                            p1Score += 1
                        if player == 2:
                            p2Score += 1

                        tictacArray = stdarray.create1D(9, 0)
                        loopTimes += 1
                        if loopTimes % 2 == 0:
                            player = 1
                        else:
                            player = 2
                        
                    player += 1

            # Bottom left
            if (2 < stddraw.mouseX() < 4) and (2 < stddraw.mouseY() < 4):
                if tictacArray[6] == 0:
                    index = 6
                    doMove(player, tictacArray, index)
                    if checkWin(player, tictacArray) == True:
                        stddraw.setFontSize(40)
                        stddraw.text(5, 5, "Player " + str(player) + " wins!")
                        stddraw.show(2000)
                        stddraw.setFontSize(20)
                        if player == 1:
                            p1Score += 1
                        if player == 2:
                            p2Score += 1

                        tictacArray = stdarray.create1D(9, 0)
                        loopTimes += 1
                        if loopTimes % 2 == 0:
                            player = 1
                        else:
                            player = 2
                    
                    player += 1

            # Bottom middle
            if (4 < stddraw.mouseX() < 6) and (2 < stddraw.mouseY() < 4):
                if tictacArray[7] == 0:
                    index = 7
                    doMove(player, tictacArray, index)
                    if checkWin(player, tictacArray) == True:
                        stddraw.setFontSize(40)
                        stddraw.text(5, 5, "Player " + str(player) + " wins!")
                        stddraw.show(2000)
                        stddraw.setFontSize(20)
                        if player == 1:
                            p1Score += 1
                        if player == 2:
                            p2Score += 1

                        tictacArray = stdarray.create1D(9, 0)
                        loopTimes += 1
                        if loopTimes % 2 == 0:
                            player = 1
                        else:
                            player = 2
                    
                    player += 1

            # Bottom right
            if (6 < stddraw.mouseX() < 8) and (2 < stddraw.mouseY() < 4):
                if tictacArray[8] == 0:
                    index = 8
                    doMove(player, tictacArray, index)
                    if checkWin(player, tictacArray) == True:
                        stddraw.setFontSize(40)
                        stddraw.text(5, 5, "Player " + str(player) + " wins!")
                        stddraw.show(2000)
                        stddraw.setFontSize(20)
                        if player == 1:
                            p1Score += 1
                        if player == 2:
                            p2Score += 1

                        tictacArray = stdarray.create1D(9, 0)
                        loopTimes += 1
                        if loopTimes % 2 == 0:
                            player = 1
                        else:
                            player = 2
                    
                    player += 1

        if player > 2:
            player = 1            
        stddraw.show(10)

# Game loop computer
def gameLoopComp():
    tictacArray = stdarray.create1D(9, 0) # Array of moves (1 = X) (2 = O)
    player = 1 # Player turn (1 = X) (2 = O)
    index = 0 # Index of spaces (eg. 0 = top left, 1 = top middle...)
    p1Score = 0 # Player 1 score
    compScore = 0 # Computer score
    loopTimes = 1 # Amount of loops of game. (Chooses who plays first)
    while gameRunning:
        if checkWin(player, tictacArray) == "Draw":
            stddraw.setFontSize(40)
            stddraw.text(5, 5, "Game ends in a draw!")
            stddraw.show(2000)
            stddraw.setFontSize(20)
            tictacArray = stdarray.create1D(9, 0)
            loopTimes += 1
            if loopTimes % 2 == 0:
                player = 2
            else:
                player = 1

        stddraw.clear(stddraw.DARK_GRAY)
        storeBoard(tictacArray)
        stddraw.text(1, 9, "Player " + str(player) + "'s turn")
        stddraw.text(8, 9, "Player 1 score: " + str(p1Score))
        stddraw.text(8, 8.5, "Computer score: " + str(compScore))
        
        if player == 2:
            compMove(player, tictacArray)
            if checkWin(player, tictacArray) == True:
                stddraw.setFontSize(40)
                stddraw.text(5, 5, "Computer wins!")
                stddraw.show(2000)
                stddraw.setFontSize(20)
                compScore += 1

                tictacArray = stdarray.create1D(9, 0)
                loopTimes += 1
                if loopTimes % 2 == 0:
                    player = 1
                else:
                    player = 2

            player += 1
        
        if player == 1:
            if stddraw.mousePressed():
                
                # Top left
                if (2 < stddraw.mouseX() < 4) and (6 < stddraw.mouseY() < 8):
                    if tictacArray[0] == 0:
                        index = 0
                        doMove(player, tictacArray, index)
                        if checkWin(player, tictacArray) == True:
                            stddraw.setFontSize(40)
                            stddraw.text(5, 5, "Player " + str(player) + " wins!")
                            stddraw.show(2000)
                            stddraw.setFontSize(20)
                            if player == 1:
                                p1Score += 1
                            if player == 2:
                                compScore += 1

                            tictacArray = stdarray.create1D(9, 0)
                            loopTimes += 1
                            if loopTimes % 2 == 0:
                                player = 1
                            else:
                                player = 2
                        player += 1

                # Top middle
                if (4 < stddraw.mouseX() < 6) and (6 < stddraw.mouseY() < 8):
                    if tictacArray[1] == 0:
                        index = 1
                        doMove(player, tictacArray, index)
                        if checkWin(player, tictacArray) == True:
                            stddraw.setFontSize(40)
                            stddraw.text(5, 5, "Player " + str(player) + " wins!")
                            stddraw.show(2000)
                            stddraw.setFontSize(20)
                            if player == 1:
                                p1Score += 1
                            if player == 2:
                                compScore += 1

                            tictacArray = stdarray.create1D(9, 0)
                            loopTimes += 1
                            if loopTimes % 2 == 0:
                                player = 1
                            else:
                                player = 2
                        player += 1

                # Top right
                if (6 < stddraw.mouseX() < 8) and (6 < stddraw.mouseY() < 8):
                    if tictacArray[2] == 0:
                        index = 2
                        doMove(player, tictacArray, index)
                        if checkWin(player, tictacArray) == True:
                            stddraw.setFontSize(40)
                            stddraw.text(5, 5, "Player " + str(player) + " wins!")
                            stddraw.show(2000)
                            stddraw.setFontSize(20)
                            if player == 1:
                                p1Score += 1
                            if player == 2:
                                compScore += 1

                            tictacArray = stdarray.create1D(9, 0)
                            loopTimes += 1
                            if loopTimes % 2 == 0:
                                player = 1
                            else:
                                player = 2
                        player += 1

                # Middle left
                if (2 < stddraw.mouseX() < 4) and (4 < stddraw.mouseY() < 6):
                    if tictacArray[3] == 0:
                        index = 3
                        doMove(player, tictacArray, index)
                        if checkWin(player, tictacArray) == True:
                            stddraw.setFontSize(40)
                            stddraw.text(5, 5, "Player " + str(player) + " wins!")
                            stddraw.show(2000)
                            stddraw.setFontSize(20)
                            if player == 1:
                                p1Score += 1
                            if player == 2:
                                compScore += 1

                            tictacArray = stdarray.create1D(9, 0)
                            loopTimes += 1
                            if loopTimes % 2 == 0:
                                player = 1
                            else:
                                player = 2
                        player += 1

                # Middle middle
                if (4 < stddraw.mouseX() < 6) and (4 < stddraw.mouseY() < 6):
                    if tictacArray[4] == 0:
                        index = 4
                        doMove(player, tictacArray, index)
                        if checkWin(player, tictacArray) == True:
                            stddraw.setFontSize(40)
                            stddraw.text(5, 5, "Player " + str(player) + " wins!")
                            stddraw.show(2000)
                            stddraw.setFontSize(20)
                            if player == 1:
                                p1Score += 1
                            if player == 2:
                                compScore += 1

                            tictacArray = stdarray.create1D(9, 0)
                            loopTimes += 1
                            if loopTimes % 2 == 0:
                                player = 1
                            else:
                                player = 2
                        player += 1

                # Middle right
                if (6 < stddraw.mouseX() < 8) and (4 < stddraw.mouseY() < 6):
                    if tictacArray[5] == 0:
                        index = 5
                        doMove(player, tictacArray, index)
                        if checkWin(player, tictacArray) == True:
                            stddraw.setFontSize(40)
                            stddraw.text(5, 5, "Player " + str(player) + " wins!")
                            stddraw.show(2000)
                            stddraw.setFontSize(20)
                            if player == 1:
                                p1Score += 1
                            if player == 2:
                                compScore += 1

                            tictacArray = stdarray.create1D(9, 0)
                            loopTimes += 1
                            if loopTimes % 2 == 0:
                                player = 1
                            else:
                                player = 2
                        player += 1

                # Bottom left
                if (2 < stddraw.mouseX() < 4) and (2 < stddraw.mouseY() < 4):
                    if tictacArray[6] == 0:
                        index = 6
                        doMove(player, tictacArray, index)
                        if checkWin(player, tictacArray) == True:
                            stddraw.setFontSize(40)
                            stddraw.text(5, 5, "Player " + str(player) + " wins!")
                            stddraw.show(2000)
                            stddraw.setFontSize(20)
                            if player == 1:
                                p1Score += 1
                            if player == 2:
                                compScore += 1

                            tictacArray = stdarray.create1D(9, 0)
                            loopTimes += 1
                            if loopTimes % 2 == 0:
                                player = 1
                            else:
                                player = 2
                        player += 1

                # Bottom middle
                if (4 < stddraw.mouseX() < 6) and (2 < stddraw.mouseY() < 4):
                    if tictacArray[7] == 0:
                        index = 7
                        doMove(player, tictacArray, index)
                        if checkWin(player, tictacArray) == True:
                            stddraw.setFontSize(40)
                            stddraw.text(5, 5, "Player " + str(player) + " wins!")
                            stddraw.show(2000)
                            stddraw.setFontSize(20)
                            if player == 1:
                                p1Score += 1
                            if player == 2:
                                compScore += 1

                            tictacArray = stdarray.create1D(9, 0)
                            loopTimes += 1
                            if loopTimes % 2 == 0:
                                player = 1
                            else:
                                player = 2
                        player += 1

                # Bottom right
                if (6 < stddraw.mouseX() < 8) and (2 < stddraw.mouseY() < 4):
                    if tictacArray[8] == 0:
                        index = 8
                        doMove(player, tictacArray, index)
                        if checkWin(player, tictacArray) == True:
                            stddraw.setFontSize(40)
                            stddraw.text(5, 5, "Player " + str(player) + " wins!")
                            stddraw.show(2000)
                            stddraw.setFontSize(20)
                            if player == 1:
                                p1Score += 1
                            if player == 2:
                                compScore += 1

                            tictacArray = stdarray.create1D(9, 0)
                            loopTimes += 1
                            if loopTimes % 2 == 0:
                                player = 1
                            else:
                                player = 2
                        player += 1

        if player > 2:
            player = 1  
        stddraw.show(10)
        
gameMode = menuFunc(menu)

if gameMode == 1:
    gameLoopMulti()
if gameMode == 2:
    gameLoopComp()