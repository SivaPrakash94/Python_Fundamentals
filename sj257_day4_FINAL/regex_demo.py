''' Regex is short for Regular Expressions.

Q. What are regular expressions for?
A. Search text for a pattern.

Q. Is there simpler way?
A. Yes, but only for simple patterns:
          'a' in seq
          'act' in seq
          seq.index('act')

Q. What do we need regexes?
A. Regexes help for complex patterns, used for data extraction        

An expression is "regular" is it can be expressed
it term of four tools:

    1) atoms/alphabet:                A  G  C  T
    2) concatenation                  GATTACA
    3) alternation                    ATT|GAG
    4) kleene star                    A*            zero of more occurences

This is ALL that can searched, but it is a pain
to write it out sometimes, so we have shortcuts:

    Quantifiers
    -----------
    r+           rr*                    one or more
    r?           ()|r                   zero or one
    r{2,4}       rrrr|rrr|rr            at least two, no more than four
    r{2,4}?      rr|rrr|rrrr            non-greedy (pick the shortest match)
 
    [ag]         (a|g)                  character groups
    [^ag]        (c|t)                  inverted character group

    Character Specifications
    ------------------------
    [0123456789] (0|1|2|3|4|5|6|7|8|9)
    [0-9]        (0|1|2|3|4|5|6|7|8|9)  character ranges
    \d           (0|1|2|3|4|5|6|7|8|9)  digits
    \D           [^0-9]
    \w           [A-Za-z_0-9]           word
    \W           [^A-Za-z_0-9]
    \s           ( |\t|\f|\r|\n)        space
    \S           [^ \t\f\r\n]           non-space
    .            [AGCT0-9 \t]           any one character but not a newline
    \b                                  boundary between \w\W \W\w

    Capturing Groups
    ----------------
    abc(def)ghi(jkl)mno                 group 0: abcdefghijklmno
                                        group 1: def
                                        group 2: jkl

    How to NOT capture
    ------------------
    abc(?:def)ghi(jkl)mno               group 0: abcdefghijklmno
                                        group 1:  jkl

'''

##import re
##
##seq = 'gttatatgataagtcgaaccggactggacgactccgatcatgcgacgaagactagaggta'
##
##print(re.findall(r'act|gag', seq))
##print(re.findall(r'aa*', seq))
##print(re.findall(r'(?:cag)', seq))

from statistics import mean, median, stdev
import re

with open('data/team_history.txt') as f:
    hist = f.read()

scores = list(map(int, re.findall(r'(\d+) (?:point|goal)s?', hist)))
dates = re.findall(r'\d{1,2}/\d{1,2}/\d{4}', hist)
record = re.findall(r'won|lost', hist)

print(f'In 2013, we played {len(dates)} games from {dates[0]} to {dates[-1]}.')
print(f'We scored {sum(scores)} goals in total for an average of {mean(scores)} per game.')
print(f'In at least half of the game we scored at least {median(scores)} times.')
print(f'Our lowest was {min(scores)} and our best was {max(scores)}.')
print(f'Our overall record was {record.count("won")}-{record.count("lost")}.')
print(f'We {record[0]} our first game and {record[-1]} our last game.')
