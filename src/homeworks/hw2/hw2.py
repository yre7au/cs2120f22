# Be sure you've done pip install z3-solver
from telnetlib import X3PAD
from z3 import *


# Here's a file you can often copy as a starting 
# point on a working program to solve some problem
# of interest. Here the problem is to compute and
# return a non-negative square root of argument, n 
def hw2():
    
    
    # Create z3 variable(s) representing the unknown
    # Here, the unknown, x, is the square root of n.
    X, Y, Z = Bools('X Y Z')
    
    s = Solver()
    
    # 1. X âˆ¨ Y, X âŠ¢ Â¬Y             -- affirming the disjunct
    # As proposition in PL: ((X \/ Y) /\ X) -> ~Y
    # If X or Y, and X is true, then it must be that Y is not true
    C1 = Implies(And(Or(X,Y),X),Not(Y))
    s.add(Not(C1))
    # I believe it's not valid
    r = s.check()
    # If there's a model/solution return it 
    if (r == unsat):
        print("C1 is valid")
    # otherwise return inconsistent value for error
    else :
        print("Here's a counter-example: ", s.model())
    # If X is true and Y is true, then X or Y is true. Furthermore, if X or Y is true, and X is true, then X or Y, and X is true.
    # However, Y is true, as stated above, meaning not Y is false. True does not imply false, which makes this rule not valid.
    s.reset()
    
    # 2. X, Y âŠ¢ X âˆ§ Y              -- and introduction
    # As proposition in PL: (X /\ Y) -> (X /\ Y)
    # If X and Y are true, then it must be that X and Y are true
    C2 = Implies(And(X,Y),And(X,Y))
    s.add(Not(C2))
    # I believe it's valid
    r = s.check()
    # If there's a model/solution return it 
    if (r == unsat):
        print("C2 is valid")
    # otherwise return inconsistent value for error
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    # 3. X âˆ§ Y âŠ¢ X                 -- and elimination left
    # As proposition in PL: (X /\ Y) -> X
    # If X and Y are true, then it must be that X is true
    C3 = Implies(And(X,Y),X)
    s.add(Not(C3))
    # I believe it's valid
    r = s.check()
    # If there's a model/solution return it 
    if (r == unsat):
        print("C3 is valid")
    # otherwise return inconsistent value for error
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    # 4. X âˆ§ Y âŠ¢ Y                 -- and elimination right
    # As proposition in PL: (X /\ Y) -> Y
    # If X and Y are true, then it must be that Y is true
    C4 = Implies(And(X,Y),Y)
    s.add(Not(C4))
    # I believe it's valid
    r = s.check()
    # If there's a model/solution return it 
    if (r == unsat):
        print("C4 is valid")
    # otherwise return inconsistent value for error
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    # 5. Â¬Â¬X âŠ¢ X                   -- negation elimination 
    # As proposition in PL: ~(~X) -> X
    # If not, not X is true, then it must be that X is true
    C5 = Implies(Not(Not(X)),X)
    s.add(Not(C5))
    # I believe it's valid
    r = s.check()
    # If there's a model/solution return it 
    if (r == unsat):
        print("C5 is valid")
    # otherwise return inconsistent value for error
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    # 6. Â¬(X âˆ§ Â¬X)                 -- no contradiction
    # As proposition in PL: ~(X /\ (~X))
    # Not, X and not X
    C6 = Not(And(X,Not(X)))
    s.add(Not(C6))
    # I believe it's valid
    r = s.check()
    # If there's a model/solution return it 
    if (r == unsat):
        print("C6 is valid")
    # otherwise return inconsistent value for error
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    # 7. X âŠ¢ X âˆ¨ Y                 -- or introduction left
    # As proposition in PL: X -> (X \/ Y)
    # If X is true, then it must be that X or Y is true
    C7 = Implies(X,Or(X,Y))
    s.add(Not(C7))
    # I believe it's valid
    r = s.check()
    # If there's a model/solution return it 
    if (r == unsat):
        print("C7 is valid")
    # otherwise return inconsistent value for error
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    # 8. Y âŠ¢ X âˆ¨ Y                 -- or introduction right
    # As proposition in PL: Y -> (X \/ Y)
    # If Y is true, then it must be that X or Y is true
    C8 = Implies(Y,Or(X,Y))
    s.add(Not(C8))
    # I believe it's valid
    r = s.check()
    # If there's a model/solution return it 
    if (r == unsat):
        print("C8 is valid")
    # otherwise return inconsistent value for error
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    # 9. X â†’ Y, Â¬X âŠ¢ Â¬ Y           -- denying the antecedent
    # As proposition in PL: ((X -> Y) /\ (~X)) -> ~Y
    # If X implies Y is true, and not X is true, then it must be that Y is true
    C9 = Implies(And(Implies(X,Y),Not(X)),Not(Y))
    s.add(Not(C9))
    # I believe it's not valid
    r = s.check()
    # If there's a model/solution return it 
    if (r == unsat):
        print("C9 is valid")
    # otherwise return inconsistent value for error
    else :
        print("Here's a counter-example: ", s.model())
    # If X is false and Y is true, then X implies Y is true because false implies anything is true. Furthermore, if X is false, then
    # not X is true. Therefore, X implies Y and not X is true. However, since Y is true, not Y is false. True cannot imply false, 
    # meaning this rule is not valid.
    s.reset()
    
    # 10. X â†’ Y, Y â†’ X âŠ¢ X â†” Y      -- iff introduction
    # As proposition in PL: ((X -> Y) /\ (Y -> X)) -> X <-> Y
    # If X implies Y is true, and Y implies X is true, then is must be that X and Y imply each other
    C10 = Implies(And(Implies(X,Y),Implies(Y,X)),And(Implies(X,Y),Implies(Y,X)))
    s.add(Not(C10))
    # I believe it's valid
    r = s.check()
    # If there's a model/solution return it 
    if (r == unsat):
        print("C10 is valid")
    # otherwise return inconsistent value for error
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    # 11. X â†” Y âŠ¢ X â†’ Y            -- iff elimination left
    # As proposition in PL: (X <-> Y) -> (X -> Y)
    # If X and Y impy each other, then it must be that X implies Y
    C11 = Implies(And(Implies(X,Y),Implies(Y,X)),Implies(X,Y))
    s.add(Not(C11))
    # I believe it's valid
    r = s.check()
    # If there's a model/solution return it 
    if (r == unsat):
        print("C11 is valid")
    # otherwise return inconsistent value for error
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    # 12. X â†” Y âŠ¢ Y â†’ X            -- iff elimination right
    # As proposition in PL: (X <-> Y) -> (Y -> X)
    # If X and Y imply each other, then it must be that Y implies X
    C12 = Implies(And(Implies(X,Y),Implies(Y,X)),Implies(Y,X))
    s.add(Not(C12))
    # I believe it's valid
    r = s.check()
    # If there's a model/solution return it 
    if (r == unsat):
        print("C12 is valid")
    # otherwise return inconsistent value for error
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    # 13. X âˆ¨ Y, X â†’ Z, Y â†’ Z âŠ¢ Z  -- or elimination
    # As proposition in PL: (((X \/ Y) /\ (X -> Z)) /\ (Y -> Z)) -> Z
    # If X or Y is true, and X implies Z is true, and Y implies Z is true, then it must be that Z is true
    C13 = Implies(And(And(Or(X,Y),Implies(X,Z)),Implies(Y,Z)),Z)
    s.add(Not(C13))
    # I believe it's valid
    r = s.check()
    # If there's a model/solution return it 
    if (r == unsat):
        print("C13 is valid")
    # otherwise return inconsistent value for error
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    # 14. X â†’ Y, Y âŠ¢ X             -- affirming the conclusion
    # As proposition in PL: ((X -> Y) /\ Y) -> X
    # If X implies Y is true, and Y is true, then it must be that X is true
    C14 = Implies(And(Implies(X,Y),Y),X)
    s.add(Not(C14))
    # I believe it's not valid
    r = s.check()
    # If there's a model/solution return it 
    if (r == unsat):
        print("C14 is valid")
    # otherwise return inconsistent value for error
    else :
        print("Here's a counter-example: ", s.model())
    # If X is false and Y is true, then X implies Y is true because false impies anything is true. If X implies Y is true and Y is true,
    # then X implies Y, and Y is true. However, X is false, and true cannot imply false, thus, this rule is not valid.
    s.reset()
    
    # 15. X â†’ Y, X âŠ¢ Y             -- arrow elimination
    # As proposition in PL: ((X -> Y) /\ X) -> Y
    # If X implies Y is true, and X is true, then it must be that Y is true
    C15 = Implies(And(Implies(X,Y),X),Y)
    s.add(Not(C15))
    # I believe it's valid
    r = s.check()
    # If there's a model/solution return it 
    if (r == unsat):
        print("C15 is valid")
    # otherwise return inconsistent value for error
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    # 16. X â†’ Y, Y â†’ Z âŠ¢ X â†’ Z     -- transitivity of â†’ 
    # As proposition in PL: ((X -> Y) /\ (Y -> Z)) -> (X -> Z)
    # If X implies Y is true, and Y implies X is true, then it must be that X implies Z is true
    C16 = Implies(And(Implies(X,Y),Implies(Y,Z)),Implies(X,Z))
    s.add(Not(C16))
    # I believe it's valid
    r = s.check()
    # If there's a model/solution return it 
    if (r == unsat):
        print("C16 is valid")
    # otherwise return inconsistent value for error
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    # 17. X â†’ Y âŠ¢ Y â†’ X            -- converse
    # As proposition in PL: (X -> Y) -> (Y -> X)
    # If X implies Y is true, then it must be that Y implies X is true
    C17 = Implies(Implies(X,Y),Implies(Y,X))
    s.add(Not(C17))
    # I believe it's not valid
    r = s.check()
    # If there's a model/solution return it 
    if (r == unsat):
        print("C17 is valid")
    # otherwise return inconsistent value for error
    else :
        print("Here's a counter-example: ", s.model())
    # If X is false and Y is true, then X implies Y is true because false implies anything is true. However, Y implies X is false 
    # because true cannot imply false. Therefore, X implies Y, implies, Y implies X, is false because this statement is equivalent to 
    # false implies true, which mentioned above is false. Therefore this rule is not valid.
    s.reset()
    
    # 18. X â†’ Y âŠ¢ Â¬Y â†’ Â¬X          -- contrapositive
    # As proposition in PL: (X -> Y) -> ((~Y) -> (~X))
    # If X implies Y is true, then it must be that not Y implies not X
    C18 = Implies(Implies(X,Y),Implies(Not(Y),Not(X)))
    s.add(Not(C18))
    # I believe it's valid
    r = s.check()
    # If there's a model/solution return it 
    if (r == unsat):
        print("C18 is valid")
    # otherwise return inconsistent value for error
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    # 19. Â¬(X âˆ¨ Y) â†” Â¬X âˆ§ Â¬Y       -- DeMorgan #1 (Â¬ distributes over âˆ¨)
    # As proposition in PL: (~(X \/ Y)) <-> ((~X) /\ (~Y))
    # Not, X or Y, and not x, and not y imply each other
    C19 = And(Implies(Not(Or(X,Y)),And(Not(X),Not(Y))),Implies(And(Not(X),Not(Y)),Not(Or(X,Y))))
    s.add(Not(C19))
    # I believe it's valid
    r = s.check()
    # If there's a model/solution return it 
    if (r == unsat):
        print("C19 is valid")
    # otherwise return inconsistent value for error
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    # 20. Â¬(X âˆ§ Y) â†” Â¬X âˆ¨ Â¬Y       -- Demorgan #2 (Â¬ distributes over âˆ§)
    # As proposition in PL: (~(X /\ Y)) <-> ((~X) \/ (~Y))
    # Not, X and Y, and not x, or not y imply each other
    C20 = And(Implies(Not(And(X,Y)),Or(Not(X),Not(Y))),Implies(Or(Not(X),Not(Y)),Not(And(X,Y))))
    s.add(Not(C20))
    # I believe it's valid
    r = s.check()
    # If there's a model/solution return it 
    if (r == unsat):
        print("C20 is valid")
    # otherwise return inconsistent value for error
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()


hw2()