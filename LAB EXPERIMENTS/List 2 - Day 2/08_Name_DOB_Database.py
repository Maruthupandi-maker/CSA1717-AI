# Python equivalent of a Name and Date-of-Birth database
people = [("Arun", "2004-05-12"), ("Meena", "2005-09-20"),
          ("Kavin", "2004-12-03")]
print("NAME AND DOB DATABASE")
for name, dob in people:
    print(f"{name} : {dob}")
search_name = "Meena"
match = next((dob for name, dob in people if name.lower() == search_name.lower()), None)
print(f"Search {search_name} -> {match if match else 'Not found'}")
