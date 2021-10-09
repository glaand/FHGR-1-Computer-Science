import sqlite3

conn = sqlite3.connect('data.db')
conn.execute('''
    CREATE TABLE temp_and_humi
    (
        year            VARCHAR(10) NOT NULL,
        month           VARCHAR(10) NOT NULL,
        day             VARCHAR(10) NOT NULL,
        hour            VARCHAR(10) NOT NULL,
        minutes         VARCHAR(10) NOT NULL,
        seconds         VARCHAR(10) NOT NULL,
        temperature     VARCHAR(10) NOT NULL,
        humidity        VARCHAR(10) NOT NULL
    );
'''
)
conn.execute('''
    CREATE UNIQUE INDEX idx_th ON temp_and_humi (year, month, day, minutes, seconds);
'''
)
conn.execute('''
    CREATE TABLE sound
    (
        year            VARCHAR(10) NOT NULL,
        month           VARCHAR(10) NOT NULL,
        day             VARCHAR(10) NOT NULL,
        hour            VARCHAR(10) NOT NULL,
        minutes         VARCHAR(10) NOT NULL,
        sound_cnt       INT NOT NULL
    );
'''
)
conn.execute('''
    CREATE UNIQUE INDEX idx_s ON sound (year, month, day, minutes);
'''
)
conn.close()
