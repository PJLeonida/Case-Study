# Case Study
# Enrique Lejano, Patrick Leonida
# STALGCM - S12


# Deterministic Pushdown Automata
import tkinter as tk
from tkinter import simpledialog, messagebox


class DPDA:
    def __init__(self, states, alphabet, stack_symbols, transitions, start_state, final_state):
        self.States = states
        self.Alphabet = alphabet
        self.Stacksym = stack_symbols
        self.Transitions = transitions
        self.startState = start_state
        self.finalState = final_state

    def addTransition(self, currentState, read, popsym, nextState, pushsym):
        new_transition = (currentState, read, popsym)
        self.Transitions[new_transition] = (nextState, pushsym)

    def run(self, inputString):
        currState = self.startState
        stack = ['Z']
        if not inputString:
            if currState in self.finalState and (currState, '*') not in self.Transitions:
                return True
            inputString = '*'

        for index, char in enumerate(inputString):
            if (currState, char) in self.Transitions:
                print('currState: ', currState, char, stack)
                new_state, popS, pushS = self.Transitions[(currState, char)]
                currState = new_state

                if popS!= '*' and popS == stack[-1] and pushS == '*':  # Pop action
                    stack.pop()
                elif pushS != '*' and popS == '*':  # Push action
                    stack.extend(pushS)
                elif pushS == '*' and popS != stack[-1] and popS != '*':  # State calls for a pop action but top of stack != popsymbol
                    return False

                #if statement that catches if the program is done reading the last input
                if len(inputString)-1 == index and (currState, '*') in self.Transitions:
                    currState, popS, pushS = self.Transitions[currState, '*']
            else:
                return False

        print(currState, stack, char)
        print(currState in self.finalState)
        print(stack[-1])
        return currState in self.finalState and stack[-1] == 'Z'

    def step(self, currState, index, inputString, stack):
        if not inputString:
            if currState in self.finalState and (currState, '*') not in self.Transitions:
                return True
            inputString = '*'
        char = inputString[index]

        if (currState, char) in self.Transitions:
            print('currState: ', currState, char, stack)
            new_state, popS, pushS = self.Transitions[(currState, char)]
            currState = new_state

            if popS != '*' and popS == stack[-1] and pushS == '*':  # Pop action
                stack.pop()
            elif pushS != '*' and popS == '*':  # Push action
                stack.extend(pushS)
            elif pushS == '*' and popS != stack[-1] and popS != '*':  # State calls for a pop action but top of stack != popsymbol
                return False

            # if statement that catches if the program is done reading the last input
            if len(inputString) - 1 == index and (currState, '*') in self.Transitions:
                currState, popS, pushS = self.Transitions[currState, '*']
            return (currState, index+1, inputString[index+1], stack)
        else:
            return False


def run_dpda():
    input_string = input_entry.get()
    result = dpda.run(input_string)
    if result:
        messagebox.showinfo("Result", "Accepted")
    else:
        messagebox.showinfo("Result", "Rejected")

# Get user inputs for DPDA definition
states = simpledialog.askstring("Input", "Enter States (comma-separated):")
states = states.strip().split(',')

alphabet = simpledialog.askstring("Input", "Enter Alphabet (comma-separated):")
alphabet = alphabet.strip().split(',')

stack_symbols = simpledialog.askstring("Input", "Enter Stack Symbols (comma-separated):")
stack_symbols = stack_symbols.strip().split(',')

transitions_input = simpledialog.askstring("Input", "Enter Transitions (format: 'currentState,inputSymbol,nextState,pop Symbol,pushSymbol'; separate multiple transitions with ';'):")
transitions_input = transitions_input.strip().split(';')

transitions = {}
for transition_str in transitions_input:
    current_state, input_symbol, next_state, pop_symbol, push_symbol = transition_str.split(',')
    print(current_state, input_symbol, next_state, pop_symbol, push_symbol)
    transitions[(current_state, input_symbol)] = (next_state, pop_symbol, push_symbol)

start_state = simpledialog.askstring("Input", "Enter Start State:")
final_states = simpledialog.askstring("Input", "Enter Final States (comma-separated):")
final_states = final_states.strip().split(',')

window = tk.Tk()
window.title("DPDA Simulator")

dpda = DPDA(states, alphabet, stack_symbols, transitions, start_state, final_states)



# print(dpda.step('A', 0, 'aabccc', ['Z']))

# Create input label and entry widget
input_label = tk.Label(window, text="Input String:")
input_label.pack()
input_entry = tk.Entry(window)
input_entry.pack()

# Create a "Run DPDA" button
run_button = tk.Button(window, text="Run DPDA", command=run_dpda)
run_button.pack()

# Start the Tkinter event loop
window.mainloop()

# A,a,B,*,a;B,a,B,*,a;B,b,C,*,a;C,b,C,*,a;C,c,D,a,*;D,c,D,a,*;D,*,E,*,*;

# states = ['A', 'B', 'C']
# alphabet = ['0', '1', 'c']
# stack_symbols = ['Z', '0', '1']
# start_state = 'A'
# final_state = 'E', 'A'
# Transitions = {
#     # cState, input: nState, pop, push
#     ('A', 'a'): ('B', '*', 'a'),
#     ('B', 'a'): ('B', '*', 'a'),
#     ('B', 'b'): ('C', '*', 'a'),
#     ('C', 'b'): ('C', '*', 'a'),
#     ('C', 'c'): ('D', 'a', '*'),
#     ('D', 'c'): ('D', 'a', '*'),
#     ('D', '*'): ('E', '*', '*')
# }
# dpda = DPDA(states, alphabet, stack_symbols, Transitions, start_state, final_state)
# print(dpda.run('aabbcccc'))
