import sqlite3
from Product import Product
import server


# connection=sqlite3.connect('sqlite3_aplication.db')
# cursor=connection.cursor()


def insertInUsers(name, email, password, birthDate, address):
    connection = sqlite3.connect('sqlite3_aplication.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (name,email,password,birthDate,address) VALUES (?,?,?,?,?)',
                   (name, email, password, birthDate, address))
    print('Inserted');
    connection.commit()
    connection.close()


def searcInUsersByEmail(email):
    connection = sqlite3.connect('sqlite3_aplication.db')
    cursor = connection.cursor()
    cursor.execute('Select * From Users Where email=?', (email,))
    user = cursor.fetchall()
    connection.close()
    return user


def checkEmalToBeValid(email):
    connection = sqlite3.connect('sqlite3_aplication.db')
    cursor = connection.cursor()
    cursor.execute('Select * From Users Where email=?', (email,))
    user = cursor.fetchone()
    print(user)
    connection.close()
    if (user == None):
        return True
    else:
        return False


def logInCheck(email, password):
    connection = sqlite3.connect('sqlite3_aplication.db')
    cursor = connection.cursor()
    cursor.execute('Select * From Users Where email=? AND password=?', (email, password))
    user = cursor.fetchone()
    connection.close()
    if user is None:
        return 'False'
    else:
        print(user)
        return 'True'


def checkForValidProduct(name):
    connection = sqlite3.connect('sqlite3_aplication.db')
    cursor = connection.cursor()
    cursor.execute('Select * From Products Where name=?', (name,))
    product = cursor.fetchone()
    print(product)
    connection.close()
    if product is None:
        return True
    else:
        return False


def insertProduct(name, price, stoc, description):  # check for no product with same name
    connection = sqlite3.connect('sqlite3_aplication.db')
    cursor = connection.cursor()
    if checkForValidProduct(name) is True:
        cursor.execute('INSERT INTO Products (name, price, stoc, description) VALUES (?,?,?,?)',
                       (name, price, stoc, description))
        print('Inserted');
        connection.commit()
        connection.close()
        return True
    else:
        return False


def serverRequest(message):
    firstWord = message.split()[0]
    if firstWord == 'Login':
        email = message.split()[1]
        password = message.split()[2]
        return logInCheck(email, password)
    elif firstWord == 'CreateUser':
        name = message.split()[1]
        email = message.split()[2]
        password = message.split()[3]
        birthDate = message.split()[4]
        address = message.split()[5]
        if checkEmalToBeValid(email):
            insertInUsers(name, email, password, birthDate, address)
            return 'True'
        else:
            return 'False'
    elif firstWord == 'getProducts':
        return sendProducts()
    elif firstWord == 'updateName':
        email = message.split()[1]
        name = message.split()[2]
        return updateUsername(email, name)
    elif firstWord == 'updatePassword':
        email = message.split()[1]
        password = message.split()[2]
        return updatePassword(email, password)
    elif firstWord == 'updateAge':
        email = message.split()[1]
        age = message.split()[2]
        return updateAge(email, age)
    elif firstWord == 'updateAddress':
        email = message.split()[1]
        address = message.split()[2]
        return updateUserAddress(email, address)
    elif firstWord == 'getUser':
        email = message.split()[1]
        return getUser(email)
    elif firstWord == 'getProduct':
        name = message.split()[1]
        return getProduct(name)
    elif firstWord == 'insertCommand':
        email = message.split()[1]
        products = message.split()[2]
        return insertCommand(email, products)
    elif firstWord == 'getCommands':
        email = message.split()[1]
        return getCommands(email)
    else:
        return 'False'


def getCommands(email):
    myString = "sendCommandsasf"
    connection = sqlite3.connect('sqlite3_aplication.db')
    cursor = connection.cursor()
    cursor.execute('SELECT products FROM Commands WHERE user=?',(email,))
    rows = cursor.fetchall()
    for row in rows:
        myString += row[0]+"&"
    connection.commit()
    connection.close()

    myString=myString[0:len(myString)-1]
    print(myString)
    return myString


def getProduct(name):
    connection = sqlite3.connect('sqlite3_aplication.db')
    cursor = connection.cursor()
    cursor.execute('SELECT name,price,stoc,description FROM Products WHERE name=?', (name,))
    rows = cursor.fetchone()
    myProduct = "getProduct^" + rows[0] + '^' + str(rows[1]) + '^' + str(rows[2]) + '^' + rows[3]
    connection.commit()
    connection.close()
    return myProduct


def getUser(email):
    connection = sqlite3.connect('sqlite3_aplication.db')
    cursor = connection.cursor()
    cursor.execute('SELECT name,email,password, birthDate,address FROM Users WHERE email=?', (email,))
    rows = cursor.fetchone()
    myUser = "getUser^" + rows[0] + '^' + rows[1] + '^' + rows[2] + '^' + rows[3] + '^' + rows[4]
    connection.commit()
    connection.close()
    return myUser


def sendProducts():
    myList = []
    connection = sqlite3.connect('sqlite3_aplication.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products')
    rows = cursor.fetchall()
    for row in rows:
        prod = Product(row[0], row[1], row[2], row[3], row[4])
        print(row)
        myList.append(prod)
    connection.commit()
    connection.close()
    # afisare
    # for b in myList:
    # print(b.id, b.name, b.price, b.stoc, b.description)
    return myList


def updateUsername(email, name):
    connection = sqlite3.connect('sqlite3_aplication.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE Users SET name=? WHERE email=?', (name, email))
    connection.commit()
    connection.close()
    return 'True'


def updatePassword(email, password):
    connection = sqlite3.connect('sqlite3_aplication.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE Users SET password=? WHERE email=?', (password, email))
    connection.commit()
    connection.close()
    return 'True'


def updateAge(email, age):
    connection = sqlite3.connect('sqlite3_aplication.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE Users SET birthDate=? WHERE email=?', (age, email))
    connection.commit()
    connection.close()
    return 'True'


def updateUserAddress(email, address):
    connection = sqlite3.connect('sqlite3_aplication.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE Users SET address=? WHERE email=?', (address, email))
    connection.commit()
    connection.close()
    return 'True'


def updateProductName(name, newName):
    connection = sqlite3.connect('sqlite3_aplication.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE Products SET name=? WHERE name=?', (newName, name))
    connection.commit()
    connection.close()


def insertCommand(user,producs):
    connection = sqlite3.connect('sqlite3_aplication.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Commands (user, products) VALUES (?,?)', (user, producs))

    connection.commit()
    connection.close()
    return 'True'


def createTable():
    connection = sqlite3.connect('sqlite3_aplication.db')
    cursor = connection.cursor()
    cursor.execute('Create Table Commands (id INTEGER  PRIMARY KEY AUTOINCREMENT, user TEXT, products TEXT)')
    connection.commit()
    connection.close()


#createTable()

#insertCommand('alin@gmail.com', 'Laptop-Hp, Smartphone-A32, Televizor-Led')
# cursor.execute('DROP TABLE Users')
# cursor.execute('Create Table Users (id INTEGER  PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, password TEXT, birthDate Text, address TEXT)') #tabel Users created
# cursor.execute('Create Table Products (id INTEGER  PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL, stoc INTEGER, description TEXT)')
# cursor.execute('INSERT INTO Products (name, price, stoc) VALUES (?,?,?)',('Scaun',4666.4,999))
# insertProduct("Cuie", 22, 33)
# cursor.execute('DELETE FROM Products WHERE id=17')
# connection.commit()
# connection.close()
# insertProduct("Smartphone A32", 1298.99,1000,"Smartphone Samsung Galaxy A32, Octa Core, 128GB, 4GB RAM, Dual SIM, 4G, 5-Camere, Baterie 5000 mAh, Awesome Blue")
# sendProducts()
#print(getUser('alin@gmail.com'))
#print(getProduct('Televizor Led'))
#print(getCommands('alin@gmail.com'))
#updateProductName('Xerox Hp', 'Xerox-Hp')

