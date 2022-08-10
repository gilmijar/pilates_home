--
-- File generated with SQLiteStudio v3.3.3 on czw. sie 11 00:31:28 2022
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: allowed_user_group
DROP TABLE IF EXISTS allowed_user_group;

CREATE TABLE allowed_user_group (
    allowed_user_group_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id               INT,
    group_id              INT,
    allower_id            INT,
    created_date          TEXT    DEFAULT (date('now') ) 
);


-- Table: classes
DROP TABLE IF EXISTS classes;

CREATE TABLE classes (
    class_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    creation_code  TEXT,
    group_id       INT,
    class_date     TEXT,
    class_time     TEXT,
    class_duration INT,
    created_date   TEXT    DEFAULT (date('now') ),
    last_update    TEXT    DEFAULT (datetime('now') ) 
);


-- Table: entry_codes
DROP TABLE IF EXISTS entry_codes;

CREATE TABLE entry_codes (
    id           INTEGER NOT NULL
                         PRIMARY KEY AUTOINCREMENT,
    code         TEXT,
    created_date TEXT    DEFAULT (datetime('now') ) 
);


-- Table: groups
DROP TABLE IF EXISTS [groups];

CREATE TABLE [groups] (
    group_id           INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name         TEXT,
    group_teacher      INT,
    group_member_limit INT,
    created_date       TEXT    DEFAULT (date('now') ),
    last_update        TEXT    DEFAULT (datetime('now') ) 
);


-- Table: swaps
DROP TABLE IF EXISTS swaps;

CREATE TABLE swaps (
    swap_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    user_one     INT,
    class_one    INT,
    user_two     INT,
    class_two    INT,
    created_date TEXT    DEFAULT (date('now') ) 
);


-- Table: user_class
DROP TABLE IF EXISTS user_class;

CREATE TABLE user_class (
    user_class_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id       INT,
    class_id      INT,
    source        TEXT,
    swap_id       INT,
    creation_code TEXT,
    created_date  TEXT    DEFAULT (date('now') ),
    last_update   TEXT    DEFAULT (datetime('now') ) 
);


-- Table: user_group
DROP TABLE IF EXISTS user_group;

CREATE TABLE user_group (
    user_group_id INTEGER NOT NULL
                          PRIMARY KEY AUTOINCREMENT,
    user_id       INTEGER NOT NULL,
    group_id      INTEGER NOT NULL,
    created_date  TEXT    DEFAULT (datetime('now') ) 
                          NOT NULL
);


-- Table: users
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_id    INTEGER    NOT NULL
                          PRIMARY KEY AUTOINCREMENT,
    first_name TEXT (20)  NOT NULL,
    last_name  TEXT (100) NOT NULL,
    pass       TEXT (100) NOT NULL,
    email      TEXT (50)  UNIQUE,
    phone      INTEGER,
    role       TEXT (20) 
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
