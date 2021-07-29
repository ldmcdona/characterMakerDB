CREATE TABLE IF NOT EXISTS classes (
    cname TEXT PRIMARY KEY,
    hit_dice TINYINT NOT NULL,
    skill_points TINYINT NOT NULL,
    bab TEXT NOT NULL,
    good_saves TEXT,
    signature_ability TEXT,
    spells BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS feats (
    fname TEXT PRIMARY KEY,
    requirements TEXT,
    benefit TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS races (
    rname TEXT PRIMARY KEY,
    feat BOOLEAN NOT NULL,
    skills TEXT,
    stats TEXT
);

CREATE TABLE IF NOT EXISTS skills (
    sname TEXT PRIMARY KEY,
    prof_classes, TEXT NOT NULL
);

/*
CREATE TABLE IF NOT EXISTS classDisplay (
    cname, hit_dice, skill_points, bab, good_saves, signature_ability, spellcaster
    All but signature_ability are NOT NULL
    Only exists if there is a specific class table already.
);

CREATE TABLE IF NOT EXISTS wizard (
    level NN, bab NN, fsave NN, rsave NN, wsave NN, abilities, spells
)
*/