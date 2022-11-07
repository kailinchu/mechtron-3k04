import sqlite3
import Patient as P

def createDB():
    connection = sqlite3.connect('userdata.db')
    cursor = connection.cursor()

    # create database table
    cursor.execute('''CREATE TABLE IF NOT EXISTS accounts (
                        username TEXT,
                        password TEXT,
                        pacingMode TEXT,
                        lrl INTEGER,
                        url INTEGER,
                        apw REAL,
                        vpw REAL,
                        aamp REAL,
                        vamp REAL,
                        asens REAL,
                        vsens REAL,
                        arp INTEGER,
                        vrp INTEGER,
                        pvarp INTEGER,
                        actThr TEXT,
                        reactTime INTEGER,
                        respFactor INTEGER,
                        recoveryTime INTEGER,
                        maxSensRate INTEGER,
                        fixedAVdelay INTEGER
                )
                ''')
    connection.commit()