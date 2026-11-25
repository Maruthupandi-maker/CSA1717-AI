% Sum integers from 1 to N
sum_to_n(0, 0).
sum_to_n(N, S) :- N > 0, N1 is N - 1, sum_to_n(N1, S1), S is N + S1.
% Query: ?- sum_to_n(5, S).
