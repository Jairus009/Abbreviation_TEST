V = ('LOL', 'OMG', 'RIP', 'TC', 'ILY', 'IDK', 'TBH', 'BTW', 'JK', 'GG', 'IMO', 'IRL', 'ICYMI', 'ROFL')
v_ANSWER = ('LAUGH OUT LOUD', 'OH MY GOD', 'REST IN PEACE', 'TAKE CARE', 'I LOVE YOU', "I DON'T KNOW", 'TO BE HONEST', 'BY THE WAY', 'JUST KIDDING', 'GOOD GAME', 'IN MY OPINION', 'IN REAL LIFE', 'IN CASE YOU MISSED IT', 'ROLLING ON THE FLOOR LAUGHING')
v_answer = ('laugh out loud', 'oh my god', 'rest in peace', 'take care', 'i love you', "i don't know", 'to be honest', 'by the way', 'just kidding', 'good game', 'in my opinion', 'in real life', 'in case you missed it', 'rolling on the floor laughing')

# Important NOTE FOR PROGRAMMERS :
#     -> IN THE ABBREVIATIONS TO BE ADDED OR EDITED IN ANSWER VARIABLES (V_ANSWER & v_answer).
#              1. DO NOT ADD SPACES IN THE BEGINNING, ENDING,
#              2. AND ONLY SINGLE SPACE SHOULD BE GIVEN BETWEEN WORDS.

MARKS = 0
Total_Marks = 7

# \\\\\\\\\\\\\\\\ ---> ALGORITHM  --->  /////////////// #
Q_num = 0
selection = '*#^*!'
SpaceBar = " "
TEST = "INTERESTED"
try:
    print('\nENTERING ONLINE TEST\n')
    print('When You Are READY, Press : ANY NUMBER')
    print("\nIf you don't want to, Press : ANY LETTER.\n")
    P = int(input('Press A Key: '))
except Exception:
    TEST = 'Not Interested'
    print('\nYOU CHOOSE NOT TO TAKE THE TEST.')
    print('\nHope You Would Comeback and Take The Test Once You Are Ready  :-(')

if TEST == "INTERESTED":
    for A in range(0, len(V), 2):
        Q = A
        Q_num = Q_num + 1
        Answer_is = "undefined"
        Entry = "k{b(o]i7="
        if selection != 'X':
            selection = '*#^*!'
        x = 0

        ###############################################################################
        while selection != 'X' and selection != '1' and selection != '2' and Entry == "k{b(o]i7=":

            # >>>>>>>>>>>>>>>>>>>>>>> A VERSION OF MAIN ALGORITHM USED BELOW >>>>>>>>>>>>>>>>>>> #
            if x == 0:
                print('\n', Q_num, 'Q. Select one from the following to answer.\n')
                print('    1. ', V[Q])
                print('    OR')
                print('    2. ', V[Q + 1])
            print('\n * NOTE :  TO EXIT FROM THE EXAMINATION, PRESS : "EXIT"')
            print('        : Your Inputs NEED NOT BE CASE SENSITIVE.')
            print('\nSelect the Abbreviation you want to answer, \n')
            selection = input('PRESS 1 or 2 : ')
            s = '1'
            T = 'EXIT'
            t = 'exit'
            x = 0
            for c in selection:
                if c == SpaceBar:
                    x = -1
                elif s != "Not Exit":
                    if x <= 0:
                        x = 1
                    if c == T[x - 1] or c == t[x - 1] and x != -1:
                        print('. ', end="")
                    else:
                        s = "Not Exit"
                    x = x + 1
            if s == '1' and selection != '1' and selection != '2':
                selection = 'X'
            # <<<<<<<<<<<<<<<<<<<<<<<<<<<    END    <<<<<<<<<<<<<<<<<<<<<<<<<<<<< #

            conformation = '~#@!'
            if selection == 'X':
                print('\nYou entered "Exit".')

            # +++++++++++++++++++++++++++++++++++++++++++++++++
            elif selection == '1' or selection == '2':
                if selection == '2':
                    Q = Q + 1
                while conformation != "321":
                    if conformation == '~#@!':
                        print('\nEnter the Abbreviation of the word "', V[Q], '" : ', end="")
                        Entry = input()
                    else:
                        print('Re-Enter the Abbreviation of"', V[Q], '": ', end="")
                        Entry = input()
                    print('\nYou have Entered :', Entry)
                    print('\nTO RE-ENTER YOU CAN PRESS ANY LETTER.')
                    print('TO CONFORM YOUR ANSWER PRESS, "321".')
                    print('\nPress a key: ', end="")
                    conformation = input()
                    print('')

                # \\\\\\\\\\\\\\\\\\\\\ ---> MAIN ALGORITHM ---> /////////////////// #
                # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                W = v_ANSWER[Q]
                w = v_answer[Q]
                V_len = len(W)
                E_len = len(Entry)
                # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                ANS_Ind_word_count = 0
                ANS_T_Sp = 0
                ANS_T_Char_COUNT = 0
                last_char = "NOTHING"
                for Y in range(0, V_len):
                    if Answer_is != "Incorrect":
                        if W[Y] == SpaceBar:
                            ANS_T_Char_COUNT += 1
                        else:
                            ANS_T_Char_COUNT += 1

                            if ANS_T_Char_COUNT == 1:
                                E_T_Sp = 0
                                E_T_Char_COUNT = 0

                        while ANS_T_Char_COUNT == E_T_Char_COUNT + 1:
                            for H in range(0, E_len):
                                if E_T_Sp + E_T_Char_COUNT == H and ANS_T_Char_COUNT == E_T_Char_COUNT + 1:
                                    if Entry[H] == SpaceBar:
                                        if last_char != SpaceBar and last_char != 'NOTHING':
                                            E_T_Char_COUNT += 1
                                        else:
                                            E_T_Sp += 1
                                        last_char = Entry[H]
                                    else:
                                        last_char = Entry[H]
                                        E_T_Char_COUNT += 1

                                    if E_T_Char_COUNT == ANS_T_Char_COUNT:
                                        E_I = Entry[E_T_Sp + E_T_Char_COUNT - 1]
                                        ANS_I = W[ANS_T_Char_COUNT + ANS_T_Sp - 1]
                                        ans_I = w[ANS_T_Char_COUNT + ANS_T_Sp - 1]
                                        if E_I == ANS_I or E_I == ans_I:
                                            Answer_is = 'Correct'
                                            if ANS_I != SpaceBar:
                                                print('               ', E_I,   '    ~    ', ANS_I)
                                            else:
                                                print('')
                                        else:
                                            Answer_is = 'Incorrect'
                                            print('\n       ''"', E_I, '"'  '     not same as     ''"', ANS_I, '"')

                # \\\\\\\\\\\\\\\\\\\\\ ---> END OF MAIN ALGORITHM ---> /////////////////// #

                if Answer_is != "undefined":
                    print()
                    print('                 : ', Answer_is, "\n")
                    if Answer_is == 'Correct':
                        MARKS = MARKS + 1
                    else:
                        print('   CORRECT ANSWER IS : ''"', W, '"')
            # ++++++++++++++++++++++++++++++++++++++++++++++++

            else:
                print('\nInvalid Entry !')
        ################################################################################
    # \\\\\\\\\\\\\\\\\\ ---> DONE DEAL --->  /////////////// #

    if selection == 'X':
        print('\nExamination Terminated')
    if Answer_is != "undefined":
        if A + 2 == len(V) and selection != 'X':
            print('\nTEST COMPLETED.')
    print('\nYOUR SCORE IS : ', end="")
    print(MARKS, '/', Total_Marks)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

    G = round(MARKS / Total_Marks * 100)
    print()
    if G < 30:
        print('Status : FAIL.\nPercentage = ', G, "%")
    else:
        print('Status : PASS.              With: ', end="")
        if G < 40:
            print('GRADE = D\nPercentage = ', G, "%")
        else:
            if G < 50:
                print('GRADE = C\nPercentage = ', G, "%")
            else:
                if G < 60:
                    print('GRADE = C+\nPercentage = ', G, "%")
                else:
                    if G < 70:
                        print('GRADE = B\nPercentage = ', G, "%")
                    else:
                        if G < 80:
                            print('GRADE = B+\nPercentage = ', G, "%")
                        else:
                            if G < 90:
                                print('GRADE = A\nPercentage = ', G, "%")
                            else:
                                print('GRADE = A+\nPercentage = ', G, "%")
