# FiniteAutomaton
Deterministic Finite Automaton Simulator.

## Configuration
Set the automaton structure in the file: <b>automaton.txt</b>

### * states
This variable has the states with their transitions.<br>
Example:<br>
<pre>
states = {
  'S0' : { 'a' : 'S1', 'b' : 'S2' },
  'S1' : { 'a' : 'S0', 'b' : 'S2' },
  'S2' : { 'a' : 'S2', 'b' : 'S2' }
}
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
