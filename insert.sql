
DELETE FROM classes;

DELETE FROM races;


INSERT INTO races 
  (rname, feat, skills, stats)
VALUES 
  ("Human", 1, "3-Any", NULL),
  ("Dwarf", 0, "2-Rock_Working", "+2_Con, -2_Cha"),
  ("Elf", 0, "2-Prancing", "+2_Dex, -2_Con"),
  ("Gnome", 0, "2-Tinkering", "+2_Con, -2_Str"),
  ("Half-elf", 1, "2-Diplomacy", NULL),
  ("Half-orc", 0, "2-Bullying", "+2_Str, -2_Int, -2_Cha"),
  ("Halfling", 0, "2-Partying", "+2_Dex, -2_Str");

INSERT INTO classes
VALUES
  ("Fighter", 10, 2, "good", "fort", "bonus feats", 0),
  ("Rogue", 6, 8, "average", "ref", "sneak attack", 0),
  ("Wizard", 4, 2, "poor", "will", "spell book", 1),
  ("Cleric", 8, 2, "average", "fort will", "turn undead", 1),
  ("Monk", 8, 4, "average", "fort ref will", "self improvement", 0);