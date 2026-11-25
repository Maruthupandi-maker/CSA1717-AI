% Monkey and banana planning facts/rules
at(monkey, door). at(box, window). banana_at(middle).
can_reach_banana :- at(monkey, middle), at(box, middle), banana_at(middle), write('Monkey climbs the box and gets the banana.').
% Conceptual query after moving monkey and box to middle: ?- can_reach_banana.
