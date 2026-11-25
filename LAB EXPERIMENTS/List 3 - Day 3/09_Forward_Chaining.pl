% Forward chaining using a simple iterative rule process
fact(fever). fact(cough).
rule(possible_infection) :- fact(fever), fact(cough).
rule(recommend_checkup) :- rule(possible_infection).
% Query: ?- rule(possible_infection).
