# FiniteAutomaton
Deterministic Finite Automaton Simulator.

## Configuration
Set the automaton structure in the file: <b>automaton.txt</b>

### * statesT
This variable has the states with their transitions.<br>
Example:<br>
<pre>
S0 : { 'a' : 'S1', 'b' : S2 }
</pre>
### * start
The initial state of the automaton.<br>
Example:<br>
<pre>
start = ['S0']
</pre>
### * ends
Set of final states.<br>
<pre>
ends = ['S0', 'S2]
</pre>


(Code in Python 2.7)
