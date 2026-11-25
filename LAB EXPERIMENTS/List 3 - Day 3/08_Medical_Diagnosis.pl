% Educational medical diagnosis rules only
symptom(fever). symptom(cough).
diagnosis(possible_respiratory_infection) :- symptom(fever), symptom(cough).
% Query: ?- diagnosis(Result).
