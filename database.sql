CREATE TABLE IF NOT EXISTS classes (
    cname TEXT PRIMARY KEY,
    bab TEXT NOT NULL,
    fsave BOOLEAN NOT NULL,
    rsave BOOLEAN NOT NULL,
    wsave BOOLEAN NOT NULL,
    abilities TEXT NOT NULL,
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