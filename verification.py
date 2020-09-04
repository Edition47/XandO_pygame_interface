def verify_win_condition(buttons):
    for button in buttons:
        if button[0] == 1:
            topl = button[1]
        if button[0] == 2:
            top = button[1]
        if button[0] == 3:
            topr = button[1]
        if button[0] == 4:
            midl = button[1]
        if button[0] == 5:
            mid = button[1]
        if button[0] == 6:
            midr = button[1]
        if button[0] == 7:
            lowl = button[1]
        if button[0] == 8:
            low = button[1]
        if button[0] == 9:
            lowr = button[1]
    if topl == "X" and top == "X" and topr == "X":
        return "Player X has won"
    elif topl == "O" and top == "O" and topr == "O":
        return "Player O has won"
    #
    elif midl == "X" and mid == "X" and midr == "X":
        return "Player X has won"
    elif midl == "O" and mid == "O" and midr == "O":
        return "Player O has won"
    #
    elif lowl == "X" and low == "X" and lowr == "X":
        return "Player X has won"
    elif lowl == "O" and low == "O" and lowr == "O":
        return "Player O has won"
    #
    elif topl == "X" and midl == "X" and lowl == "X":
        return "Player X has won"
    elif topl == "O" and midl == "O" and topr == "O":
        return "Player O has won"
    #
    elif top == "X" and mid == "X" and low == "X":
        return "Player X has won"
    elif top == "O" and mid == "O" and low == "O":
        return "Player O has won"
    #
    elif topr == "X" and midr == "X" and lowr == "X":
        return "Player X has won"
    elif topr == "O" and midr == "O" and lowr == "O":
        return "Player O has won"
    #
    elif topl == "X" and mid == "X" and lowr == "X":
        return "Player X has won"
    elif topl == "O" and mid == "O" and lowr == "O":
        return "Player O has won"
    #
    elif lowl == "X" and mid == "X" and topr == "X":
        return "Player X has won"
    elif lowl == "O" and mid == "O" and topr == "O":
        return "Player O has won"
    else:
        return 0


def modify_state(buttons, m_x, m_y, player):
    turn = player
    if player % 2 is 0:
        player = "X"
    else:
        player = "O"
    for button in buttons:
        if m_x < 80 and m_y < 80 and button[0] == 1:
            if button[2] is False:
                button[1] = player
                button[2] = True
                turn += 1
        elif 80 < m_x < 160 and m_y < 80 and button[0] == 2:
            if button[2] is False:
                button[1] = player
                button[2] = True
                turn += 1
        elif 160 < m_x < 240 and m_y < 80 and button[0] == 3:
            if button[2] is False:
                button[1] = player
                button[2] = True
                turn += 1
        elif m_x < 80 and 80 < m_y < 160 and button[0] == 4:
            if button[2] is False:
                button[1] = player
                button[2] = True
                turn += 1
        elif 80 < m_x < 160 and 80 < m_y < 160 and button[0] == 5:
            if button[2] is False:
                button[1] = player
                button[2] = True
                turn += 1
        elif 160 < m_x < 240 and 80 < m_y < 160 and button[0] == 6:
            if button[2] is False:
                button[1] = player
                button[2] = True
                turn += 1
        elif m_x < 80 and 160 < m_y < 240 and button[0] == 7:
            if button[2] is False:
                button[1] = player
                button[2] = True
                turn += 1
        elif 80 < m_x < 160 and 160 < m_y < 240 and button[0] == 8:
            if button[2] is False:
                button[1] = player
                button[2] = True
                turn += 1
        elif 160 < m_x < 240 and 160 < m_y < 240 and button[0] == 9:
            if button[2] is False:
                button[1] = player
                button[2] = True
                turn += 1
    return button, button[0], turn
