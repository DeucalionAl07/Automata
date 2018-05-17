from InfixToPostfix import InfixToPostfix
from RE2NFA import RE2NFA
from NFA2DFA import NFA2DFA
# Execution file for conversion
print 'Enter the regular expression'
exp = str(raw_input())
# Convert the RE to postfix form
conv = InfixToPostfix(exp)
exp = conv.doTrans() + "#"
# Comvert RE to NFA
eval = RE2NFA(exp)
table = eval.doTrans()
# Print NFA's transition table
print 'Initial State: ', table.head.val
print 'Final State: ', table.final(table.head).val
table.print_(table.head, eval.TOKENS)
# Convert the NFA to DFA
dfa = NFA2DFA(table, eval.TOKENS)
dfa.getLambdas(table.head)