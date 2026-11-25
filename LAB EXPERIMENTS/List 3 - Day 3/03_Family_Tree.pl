% Family tree
parent(rajan, arun). parent(rajan, meena).
parent(arun, kavin). parent(meena, divya).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
% Queries: ?- parent(rajan, arun).  ?- grandparent(rajan, kavin).
