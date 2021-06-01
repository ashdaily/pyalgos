"""
# Task: Bracket Parser

Write a bracket parser that checks for correct number of bracket pairs of type
* '(' and ')'
* '{' and '}'

for a given input string. It should display "ok" if the given string or expression has a correct bracket pair configuration, and display "failed" otherwise.

### Strings to test
1) `(defun avg (n1 n2 n3 n4)(/ (+ n1 n2 n3 n4) 4))(write(avg 10 20 30 40))` &rarr; ok
2) `({(1 + x)**2 + x} + 1)*(1 + x)` &rarr; ok
3) `(a + b*(c + d} / {a - d)*3)` &rarr; failed
4) `(x + q)^3 + 3*{x - q} + {(x-q)*q} + ({x-q}*x)^2` &rarr; ok
5) `(x + q)^3 + 3*{x - q + ({(x-q)*q} + ({x-q}*x)^2})` &rarr; failed

Hints:
- `({})` is matching, because the outer and inner brackets form pairs
- `((){}` is not matching, because the first `)` has no partner
- `(){})` is not matching, because the last `)` has no partner
- `({)}` is also not matching, because pairs must be either entirely inside or outside other pairs
"""


def bracket_parser(s):
    # ensure even number of occurences
    # add to the stack if it's left bracket ( {
    # pop from the stack if current bracket is the right match of the TOS
    brackets = []
    bracket_pairs = {
        "{": "}",
        "(": ")"
    }

    for curr_bracket in s:
        if curr_bracket in bracket_pairs.keys():
            brackets.append(curr_bracket)
            print("+", brackets)
        else:
            if brackets:
                if bracket_pairs[brackets[-1]] == curr_bracket:
                    print("-", brackets)
                    popped = brackets.pop()
                    print(popped)
                    continue
            return False

    return True if brackets else False
                

if __name__ == "__main__":
    result = bracket_parser("()")
    print(result)

                
    