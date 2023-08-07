# Source Code for Case Study for Deterministic Pushdown Automata Implementation
Enrique Lejano and Patrick Leonida

## Definition of Machine via File Input
The source code will take file input as a text file in the following format:
ALL comma-separated inputs have no space in between.
1. First Line: States (comma-separated strings)
    - Example: A,B,C,D,E
2. Second Line: Input Alphabet (comma-separated strings)
    - Example: a,b
3. Third Line: Stack Symbols (comma-separated strings)
    - Example: Z,a,b
4. Fourth Line: Transition Functions (separated by semicolons)
    - Format (per transition): currentState,inputSymbol,nextState,popSymbol,pushSymbol
    - An empty string (λ) is inputted via an asterisk (*).
    - Example: A,a,B,\*,a;B,a,B,\*,a;B,b,C,\*,a;C,b,C,\*,a;C,c,D,a,\*;D,c,D,a,\*;D,\*,E,\*,\*;
5. Fifth Line: Start State (single string)
    - Example: A
6. Sixth Line: Final State/s (comma-separated strings)
    - Example: E,A
