% Fruit colors; Prolog backtracking can find alternatives
fruit_color(apple, red). fruit_color(apple, green).
fruit_color(banana, yellow).
fruit_color(grapes, green). fruit_color(grapes, purple).
% Queries: ?- fruit_color(apple, C).  ?- fruit_color(Fruit, Color).
