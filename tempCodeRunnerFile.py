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
  st.write()
  idx_char = 0
  state = 'q0'
  current_token = ' '
  while state != 'accept':
    current_char = input_string[idx_char]
    current_token += current_char
    state = transition_table[(state, current_char)]
    
    if state == 'q4':
      st.write('Current Token                  : ', current_token, ', valid')
      current_token = ' '
      check = True
    
    if state == 'error':
      st.write('Sorry, the word you entered is invalid')
      st.write('Please try again and re-check the words you entered!')
      check = False
      break
    idx_char = idx_char + 1

  #Conclusion
  if state == 'accept':
    st.write('\nAll tokens have been entered   : ', sentence, ', valid')
    check = True
  
  return check

#--------------------------------------------------MAIN PROGRAM---------------------------------------------------------------------------------
check = False
count = 0
set('\n  TUGAS BESAR TEORI BAHASA DAN AUTOMATA | KELOMPOK 15 | IF-44-01')

while check != True and count < 1:
  st.write('=================================================================')
  st.write('||       Welcome, Please do a word check in English            ||')
  st.write('||   Here are the words in English that have been studied      ||')
  st.write('||=============================================================||')
  st.write('|| SB  : he, you, they                                         ||')
  st.write('|| VB  : eat, bring, play, read                                ||')
  st.write('|| OB  : pancake, bottle, piano, book                          ||')
  st.write('=================================================================')
  sentence = st.text_input('Input                          : ', key = count)
  count += 1
  
  input_string = sentence.lower() + '#'
  check = lexical(sentence, check)