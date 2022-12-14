"""Dobrý den, aplikace je propojená s databází, kód sql: CREATE TABLE `pojistenci`.`pojistenci` (`ID` INT(10) NOT NULL AUTO_INCREMENT , `Jmeno` VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_czech_ci NOT NULL , `Prijmeni` VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_czech_ci NOT NULL , `Vek` VARCHAR(10) NOT NULL , `Tel` VARCHAR(15) NOT NULL , `Bydliste` VARCHAR(30) CHARACTER SET utf8 COLLATE utf8_czech_ci NOT NULL , PRIMARY KEY (`ID`)) ENGINE = InnoDB;
, pro lokální server a databázi jsem použil XAMPP Apache + MySQL, do PyCharm jsem nainstaloval mysql.connector"""
import mysql.connector

def vlozit(con,cur):
    pid=input("Zadejte ID pojištěnce:")
    pjm=input("Zadejte jméno:")
    ppr=input("Zadejte příjmení:")
    pve=input("Zadejte věk:")
    pte=input("Zadejte telefon:")
    pby=input("Zadejte bydliště:")
    sql = "INSERT INTO Pojistenci (ID, Jmeno, Prijmeni, Vek, Tel, Bydliste) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (pid,pjm,ppr,pve,pte,pby)
    cur.execute(sql, val)
    con.commit()
    print(cur.rowcount, "Záznam byl uložen")

def seznam(cur):
    cur.execute("SELECT * FROM pojistenci")
    res = cur.fetchall()
    print("------------------------------------------------------------------------")
    print("ID   Jméno   Příjmení    Věk     Tel    Bydliště")
    print("------------------------------------------------------------------------")
    for x in res:
            print(str(x[0])+"   "+x[1]+"    "+x[2]+"    "+x[3]+"    "+x[4]+"    "+x[5])
    print("------------------------------------------------------------------------")
def upravit(con,cur):
    pid = input("Zadejte ID pojištěnce:")
    pjm = input("Zadejte jméno:")
    ppr = input("Zadejte příjmení:")
    pve = input("Zadejte věk:")
    pte = input("Zadejte telefon:")
    pby = input("Zadejte bydliště:")
    sql = "update pojistenci set Jmeno='"+pjm+"', Prijmeni='"+ppr+"',Vek='"+pve+"', Tel='"+pte+"', Bydliste='" +pby+"' where ID="+pid
    cur.execute(sql)
    con.commit()
    print(cur.rowcount, "Záznam byl upraven.")
def vymazat(con,cur):
    pid=input("Zadejte ID pojištěnce:")
    sql = "delete FROM pojistenci where ID = '"+pid+"'"
    cur.execute(sql)
    con.commit()
    print(cur.rowcount, "Záznam byl vymazán.")
def main():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="Pojistenci"
    )
    cur = con.cursor()
    ch = 0
    print("")
    print("Vítejte v aplikaci pro správu pojištěnců.")
    print("-----------------------------------------")
    print("")
    while (ch <= 4):
        print("1. Vložit pojištěnce")
        print("2. Zobrazit seznam pojištěných")
        print("3. Upravit pojištěnce")
        print("4. Vymazat pojištěnce")
        print("5. Konec")
        ch = int(input("Vyber požadovanou akci:"))
        if (ch == 1):
            vlozit(con, cur)
        if (ch == 2):
            seznam(cur)
        if (ch == 3):
            upravit(con, cur)
        if (ch == 4):
            vymazat(con, cur)
    else: print("Aplikace byla ukončena.")

main()