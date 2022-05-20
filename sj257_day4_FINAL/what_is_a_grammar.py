'''
New game (interpreter)
---------
1) You tell a story
2) I find a matching madlib (if I don't, I'll yell loudly, "No Way!" (SyntaxError)
3) I extract the placeholder values
4) Each madlib has a association action

Book of Madlibs (grammar)
---------------
M1. It was a <adj>, cold November day.  I woke up to the <adj>
smell of <bird> roasting in the <room> downstairs.
A1.  Goto <room>, Eat the <adj1> <adj2> bird.

M2. I <verb> down the stairs.
A2. Do <verb> at work.

Play game (programming)
---------
Amir: I verb:FLEW down down the stairs.
Me:  Do flying at work.

Anna: It was a <adj:RED>, cold November day.  I woke up to the <adj:ANGRY>
      smell of <bird:RAVEN>
Me:  Eat the RED ANGRY RAVEN.

Siva:  I like scary movies.
Me:    No way!



Grammar:
    Statements take actions  (exec)
    Expression return values (eval)

Statements
==========

NOP:
    "pass"                               Do nothing
    
ASSIGNMENT
    <varname> "=" <expr>                 globals()[varname] = eval(expr)

CONDITIONAL
    "if" <expr> ":" <stmt>              eval(expr); if true, exec(stmt)
    "elif" <expr> ":" <stmt>
    "else" "":" <stmt>

BOUNDED LOOP:
    "for" <varname> "in" <expr> ":" stmt
                                          a = eval(expr)
                                          it = a.__iter__()                 a: Iterable it: Iterator
                                          while True:
                                          try:
                                               <varname>  = it.__next__()         
                                          except StopIteration:
                                               break
                                          else:
                                               <stmt>
                                               
     "continue"                           go to the top of the "while" loop
     "break"                              get out of the while loop
'''
