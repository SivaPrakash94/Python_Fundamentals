try:
    print(38 / 5)                       # In the try-block
    print(38 // 5)                      # top to bottom  
    {}['missing']                       # longjump to a matching handler 
    print(38 // -1)
except IndexError:                      # handler ONLY runs with IndexError
    print('I indexed too far!')
except ZeroDivisionError:               # handler ONLY runs with zero division
    print('Hmm, not all integers have a multiplicative inverse')
except RuntimeError:                    # first match wins
    print('The CPU is on fire')
else:                                   # executes when there is NO exception at all
    print('No problem. Nothing to see here. Move along')
finally:                                # always runs, but after everything else
    print("That's all folks")

'''    
7.6
7
That's all folks
Traceback (most recent call last):
  File "<pyshell#955>", line 4, in <module>
    {}['missing']                       # longjump to a matching handler
KeyError: 'missing'
#  ^--- If an exception doesn't match ANY handler, the finally clause runs, and it continues looking for a handler.
#  ^--- The default handler prints a traceback and stops the problems.
'''

'''
There is a builin class called BaseException.
New exceptions subclass from existing exceptions.
Many standard exceptions have been written for you.
The person raising the exception gets to choose which one.
Ideally, they should either document it or it should guessable.


SyntaxError          As program loads before it executes.
NameError            Variable not defined in the namespace   

LookupError
  |-- IndexError     bad index into a sequence
  |-- KeyError       bad key in a dict or set
TypeError            type mismatch  
ValueError           value doesn't make sense
FileNotFoundError    missing file
OSError
  |-- FileNotFoundError
  |-- FileExistsError
ZeroDivisionError    division by zero
OverflowError        internal implementation limits
RuntimeError         generic error, doesn't fit anywhere else

'''
