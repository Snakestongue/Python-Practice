
#len(). length of string in chars(spaces too)

#(use name.xyz for following methods)(or varname.method)

#name.find(" "): Will return first position of given character. EX: 12344, 4 is in spot 3 so prints 3
#name.rfind(" "): Will return last position of given character. EX: 42345, 4 is in spot 3 so prints 3
#for find/rfind any characters not shown(like q in 12345) returns -1
#name.capitalize(): Returns first letter in a string(abc def returns Abc def)
#name.upper(): Returns all capitalized letters(aBc Def returns ABC DEF)
#name.lower(): Returns all lowercased letters(aBc Def returns abc def)
#name.isdigit(): Returns true/false based on numbers/strings(ABC123/ABCDEF returns false while 123456 returns true)
#name.isalpha(): Returns true/false if only aphabet used(SM AA and SM123= false(space, number), SMAA = true)
#name.count(" "): Counts how many specfic characters and returns that((A)  ABCABCABC will return 3 for A)
#name.replace("x ", ""): Replaces any x with y(or any chars)(empty string deletes that(2))
