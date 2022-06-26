import string

#-----------------------------------------------------LEXICAL-----------------------------------------------------------------------------------

def lexical(sentence, check):

  #Initializations
  alphabet_list = list(string.ascii_lowercase)
  state_list = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 
                'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31']
  
  transition_table = {}

  for state in state_list:
    for alphabet in alphabet_list:
      transition_table[(state, alphabet)] = 'error'
    transition_table[(state, '#')] = 'error'
    transition_table[(state, ' ')] = 'error'

  #Start state
  transition_table['q0', ' ']='q0'

  #Finish state
  transition_table[('q4', '#')]= 'accept'
  transition_table[('q4', ' ')]= 'q5'

  transition_table[('q5', '#')]= 'accept'
  transition_table[('q5', ' ')]= 'q5'

  #Update the transition table for the following token : they
  transition_table[('q0', 't')]= 'q1'
  transition_table[('q1', 'h')]= 'q2'
  transition_table[('q2', 'e')]= 'q3'
  transition_table[('q3', 'y')]= 'q4'
  transition_table[('q4', ' ')]= 'q5'
  transition_table[('q5', 't')]= 'q1'

  #Update the transition table for the following token : he
  transition_table[('q0', 'h')]= 'q6'
  transition_table[('q6', 'e')]= 'q4'
  transition_table[('q4', ' ')]= 'q5'
  transition_table[('q5', 'h')]= 'q6'

  #Update the transition table for the following token : you
  transition_table[('q0', 'y')]= 'q7'
  transition_table[('q7', 'o')]= 'q8'
  transition_table[('q8', 'u')]= 'q4'
  transition_table[('q4', ' ')]= 'q5'
  transition_table[('q5', 'y')]= 'q7'

  #Update the transition table for the following token : eat
  transition_table[('q0', 'e')]= 'q9'
  transition_table[('q9', 'a')]= 'q10'
  transition_table[('q10', 't')]= 'q4'
  transition_table[('q4', ' ')]= 'q5'
  transition_table[('q5', 'e')]= 'q9'

  #Update the transition table for the following token : bring
  transition_table[('q0', 'b')]= 'q11'
  transition_table[('q11', 'r')]= 'q12'
  transition_table[('q12', 'i')]= 'q13'
  transition_table[('q13', 'n')]= 'q14'
  transition_table[('q14', 'g')]= 'q4'
  transition_table[('q4', ' ')]= 'q5'
  transition_table[('q5', 'b')]= 'q11'

  #Update the transition table for the following token : book
  transition_table[('q0', 'b')]= 'q11'
  transition_table[('q11', 'o')]= 'q15'
  transition_table[('q15', 'o')]= 'q16'
  transition_table[('q16', 'k')]= 'q4'
  transition_table[('q4', ' ')]= 'q5'
  transition_table[('q5', 'b')]= 'q11'

  #Update the transition table for the following token : bottle
  transition_table[('q0', 'b')]= 'q11'
  transition_table[('q11', 'o')]= 'q15'
  transition_table[('q15', 't')]= 'q17'
  transition_table[('q17', 't')]= 'q18'
  transition_table[('q18', 'l')]= 'q19'
  transition_table[('q19', 'e')]= 'q4'
  transition_table[('q4', ' ')]= 'q5'
  transition_table[('q5', 'b')]= 'q11'

  #Update the transition table for the following token : read
  transition_table[('q0', 'r')]= 'q20'
  transition_table[('q20', 'e')]= 'q21'
  transition_table[('q21', 'a')]= 'q22'
  transition_table[('q22', 'd')]= 'q4'
  transition_table[('q4', ' ')]= 'q5'
  transition_table[('q5', 'r')]= 'q20'

  #Update the transition table for the following token : play
  transition_table[('q0', 'p')]= 'q23'
  transition_table[('q23', 'l')]= 'q24'
  transition_table[('q24', 'a')]= 'q25'
  transition_table[('q25', 'y')]= 'q4'
  transition_table[('q4', ' ')]= 'q5'
  transition_table[('q5', 'p')]= 'q23'

  #Update the transition table for the following token : pancake
  transition_table[('q0', 'p')]= 'q23'
  transition_table[('q23', 'a')]= 'q26'
  transition_table[('q26', 'n')]= 'q27'
  transition_table[('q27', 'c')]= 'q28'
  transition_table[('q28', 'a')]= 'q29'
  transition_table[('q29', 'k')]= 'q30'
  transition_table[('q30', 'e')]= 'q4'
  transition_table[('q4', ' ')]= 'q5'
  transition_table[('q5', 'p')]= 'q23'

  #Update the transition table for the following token : piano
  transition_table[('q0', 'p')]= 'q23'
  transition_table[('q23', 'i')]= 'q31'
  transition_table[('q31', 'a')]= 'q26'
  transition_table[('q26', 'n')]= 'q27'
  transition_table[('q27', 'o')]= 'q4'
  transition_table[('q4', ' ')]= 'q5'
  transition_table[('q5', 'p')]= 'q23'

  #Lexical Analysis
  print()
  idx_char = 0
  state = 'q0'
  current_token = ' '
  while state != 'accept':
    current_char = input_string[idx_char]
    current_token += current_char
    state = transition_table[(state, current_char)]
    
    if state == 'q4':
      print('Current Token                  : ', current_token, ', valid')
      current_token = ' '
      check = True
    
    if state == 'error':
      print('Sorry, the word you entered is invalid')
      print('Please try again and re-check the words you entered!')
      check = False
      break
    idx_char = idx_char + 1

  #Conclusion
  if state == 'accept':
    print('\nAll tokens have been entered   : ', sentence, ', valid')
    check = True
  
  return check

#-----------------------------------------------------PARSER------------------------------------------------------------------------------------

def parser(sentence, check):
  if check:
    print('=====================================================================================================')
    print('||                    A word validation check with a lexical analyzer has been completed           ||')                      
    print('||                         Next, the grammar rules will be checked                                 ||')
    print('=====================================================================================================')

    #Input Example
    tokens = sentence.lower().split()
    tokens.append('EOS')

    #Symbols Definition
    non_terminals = ['S', 'SB', 'VB', 'OB']
    terminals = ['he', 'you', 'they', 'eat', 'bring', 'play', 'read', 'pancake', 'bottle', 'piano', 'book']

    #Parse Table Definition
    parse_table = {}

    parse_table[('S', 'he')] = ['SB', 'VB', 'OB']
    parse_table[('S', 'you')] = ['SB', 'VB', 'OB']
    parse_table[('S', 'they')] = ['SB', 'VB', 'OB']
    parse_table[('S', 'eat')] = ['error']
    parse_table[('S', 'bring')] = ['error']
    parse_table[('S', 'play')] = ['error']
    parse_table[('S', 'read')] = ['error']
    parse_table[('S', 'pancake')] = ['SB', 'OB']
    parse_table[('S', 'bottle')] = ['SB',  'OB']
    parse_table[('S', 'piano')] = ['SB', 'OB']
    parse_table[('S', 'book')] = ['SB', 'OB']
    parse_table[('S', 'EOS')] = ['error']

    parse_table[('SB', 'he')] = ['he']
    parse_table[('SB', 'you')] = ['you']
    parse_table[('SB', 'they')] = ['they']
    parse_table[('SB', 'eat')] = ['error']
    parse_table[('SB', 'bring')] = ['error']
    parse_table[('SB', 'play')] = ['error']
    parse_table[('SB', 'read')] = ['error']
    parse_table[('SB', 'pancake')] = ['error']
    parse_table[('SB', 'bottle')] = ['error']
    parse_table[('SB', 'piano')] = ['error']
    parse_table[('SB', 'book')] = ['error']
    parse_table[('SB', 'EOS')] = ['error']

    parse_table[('VB', 'he')] = ['error']
    parse_table[('VB', 'you')] = ['error']
    parse_table[('VB', 'they')] = ['error']
    parse_table[('VB', 'eat')] = ['eat']
    parse_table[('VB', 'bring')] = ['bring']
    parse_table[('VB', 'play')] = ['play']
    parse_table[('VB', 'read')] = ['read']
    parse_table[('VB', 'pancake')] = ['error']
    parse_table[('VB', 'bottle')] = ['error']
    parse_table[('VB', 'piano')] = ['error']
    parse_table[('VB', 'book')] = ['error']
    parse_table[('VB', 'EOS')] = ['error']

    parse_table[('OB', 'he')] = ['error']
    parse_table[('OB', 'you')] = ['error']
    parse_table[('OB', 'they')] = ['error']
    parse_table[('OB', 'eat')] = ['error']
    parse_table[('OB', 'bring')] = ['error']
    parse_table[('OB', 'play')] = ['error']
    parse_table[('OB', 'read')] = ['error']
    parse_table[('OB', 'pancake')] = ['pancake']
    parse_table[('OB', 'bottle')] = ['bottle']
    parse_table[('OB', 'piano')] = ['piano']
    parse_table[('OB', 'book')] = ['book']
    parse_table[('OB', 'EOS')] = ['error']

    #Stack Initialization
    stack = []
    stack.append('#')
    stack.append('S')

    #Input reading initialization
    idx_token = 0
    symbol = tokens[idx_token]

    #Parsing Process
    try :

      while (len(stack) > 0):
        top = stack[len(stack)-1]
        print('Top                   = ', top)
        print('Symbol                = ', symbol)

        if top in terminals:
          print('Top is a terminal symbol')

          if top == symbol:
            stack.pop()
            idx_token = idx_token + 1
            symbol = tokens[idx_token]

            if symbol == 'EOS':
              print('Stack Contents  : ', stack)
              stack.pop()

          else:
            print('Error')
            break;

        elif top in non_terminals:
          print('Top is a non-terminal symbol')

          if parse_table[(top, symbol)][0] != 'error':
            stack.pop()
            symbols_to_be_pushed = parse_table[(top, symbol)]

            for i in range(len(symbols_to_be_pushed)-1,-1,-1):
              stack.append(symbols_to_be_pushed[i])

          else:
            print('Error')
            break;

        else:
          print('Error')
          break;

        print('Stack Contents : ', stack)
        print('-----------------------------------------------------------------------------------------------------')
       
    except KeyError :
      print('The word was not found in the system')

    #Conclusion
    print()
    if symbol == 'EOS' and len(stack) == 0:
      print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
      print('|| Input String : ', sentence,"                                                      ||")
      print('||--------------------------------------------------------------------------------------||')
      print('||                                   Congratulations!                                   ||')
      print('||      The sentence you input is accepted because it is in accordance with grammar     ||')
      print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    else :
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('| Error, Input String : ', sentence,"                                              |")
      print('|---------------------------------------------------------------------------------------|')              
      print('|                                             Sorry,                                    |')
      print('|     The sentence you input is not accepted because it does not match the grammar      |')
      print('|                                   or there is an invalid word                         |')
      print('|                      Please re-check the sentence you entered. Thank you              |')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      
  else :
    pass

  return parser
#--------------------------------------------------MAIN PROGRAM---------------------------------------------------------------------------------
check = False
print('\n  TUGAS BESAR TEORI BAHASA DAN AUTOMATA | KELOMPOK 15 | IF-44-01')

while check != True:
  print('=================================================================')
  print('||       Welcome, Please do a word check in English            ||')
  print('||   Here are the words in English that have been studied      ||')
  print('||=============================================================||')
  print('|| SB  : he, you, they                                         ||')
  print('|| VB  : eat, bring, play, read                                ||')
  print('|| OB  : pancake, bottle, piano, book                          ||')
  print('=================================================================')
  sentence = input('Input                          : ')
  
  input_string = sentence.lower() + '#'
  check = lexical(sentence, check)

parser(sentence, check)