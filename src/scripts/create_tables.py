import mysql.connector
from mysql.connector import errorcode
import os
from dotenv import load_dotenv

load_dotenv()

# Define db name
DB_NAME = 'justtcg'

# Create table
TABLES = {}
TABLES['mtg_singles'] = (
    "CREATE TABLE `mtg_singles` ("
    " `idProduct` int(10) NOT NULL,"
    " `idMetaproduct` int(10),"
    " `countReprints` int(10),"
    " `enName` varchar(32) NOT NULL,"
    " `website` varchar(2083),"
    " `image` varchar(2083),"
    " `number` int(10),"
    " `rarity` varchar(32),"
    " `expansionName` varchar(32),"
    " `idExpansion` int(10),"
    " `idLocalization` int(10),"
    " PRIMARY KEY (`idProduct`)"
    ") ENGINE=InnoDB"
)

TABLES['mtg_localization'] = (
    "CREATE TABLE `mtg_localization` ("
    " `idLocalization` int(10) NOT NULL AUTO_INCREMENT,"
    " `idLanguage` int(10) NOT NULL,"
    " `languageName` int(10) NOT NULL,"
    " `productName` int(10),"
    " PRIMARY KEY (`idLocalization`)"
    ") ENGINE=InnoDB"
)

TABLES['mtg_expansion'] = (
    "CREATE TABLE `mtg_expansion` ("
    " `idExpansion` int(10) NOT NULL,"
    " `enName` int(10) NOT NULL,"
    " `expansionIcon` int(10) NOT NULL,"
    " PRIMARY KEY (`idExpansion`)"
    ") ENGINE=InnoDB"
)

"""TABLES['mtg_reprint'] = (
    "CREATE TABLE `mtg_reprint` ("
    " `idProduct` int(10) NOT NULL,"
    " `expansion` int(10) NOT NULL,"
    " `expansionIcon` int(10) NOT NULL,"
    " PRIMARY KEY (`idProduct`)"
    ") ENGINE=InnoDB"
)"""

"""TABLES['mtg_pricing'] = (
    "CREATE TABLE `mtg_localization` ("
    " `idLocalization` int(10) NOT NULL AUTO_INCREMENT,"
    " `idLanguage` int(10) NOT NULL,"
    " `languageName` int(10) NOT NULL,"
    " `productName` int(10),"
    " PRIMARY KEY (`idLocalization`)"
    ") ENGINE=InnoDB"
)"""

# https://api.cardmarket.com/ws/documentation/API_2.0:PriceGuide
TABLES['mtg_pricing_cardmarket'] = (
    "CREATE TABLE `mtg_pricing_cardmarket` ("
    " `idProduct` int(10) NOT NULL,"
    " `avg_sale_price` double(10,2) NOT NULL,"
    " `low_price` double(10,2) NOT NULL,"
    " `trend_price` double(10,2) NOT NULL,"
    " `foil_sell` double(10,2) NOT NULL,"
    " `foil_low` double(10,2) NOT NULL,"
    " `foil_trend` double(10,2) NOT NULL,"
    " `low_price_exp` double(10,2) NOT NULL,"
    " `avg_one` double(10,2) NOT NULL,"
    " `avg_seven` double(10,2) NOT NULL,"
    " `avg_thirty` double(10,2) NOT NULL,"
    " `foil_avg_one` double(10,2) NOT NULL,"
    " `foil_avg_seven` double(10,2) NOT NULL,"
    " `foil_avg_thirty` double(10,2) NOT NULL,"
    " PRIMARY KEY (`idProduct`)"
    ") ENGINE=InnoDB"
)

cnx = mysql.connector.connect(
    host=os.getenv("HOST"),
    user=os.getenv("USERNAME"),
    passwd=os.getenv("PASSWORD"))
cursor = cnx.cursor()


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)


for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()
