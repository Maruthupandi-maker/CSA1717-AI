% Backward chaining: Prolog proves a goal from rules and facts
fact(fever). fact(cough).
possible_infection :- fact(fever), fact(cough).
recommend_checkup :- possible_infection.
% Query: ?- recommend_checkup.
