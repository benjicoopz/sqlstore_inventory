from models import Base, session, Product, engine
import datetime
import csv
import time


def menu():
    while True:
        print('''
        \rStore Inventory
        \nv) View Details
        \ra) Add Product
        \rb) Make Backup
        \re) Exit''')
        fakechoice = input('\nPlease choose an option: ')
        realchoice = fakechoice.lower()
        if realchoice in ['v', 'a', 'b', 'e']:
            return realchoice
        else:
            input('''
            \rPlease choose one of the options above.
            \rOptions are the letters v, a, b, and e.
            \rPress enter to try again!
            ''')


def clean_date(date_str):
    split_date = date_str.split('/')
    try:
        month = int(split_date[0])
        day = int(split_date[1])
        year = int(split_date[2])
        return_date = datetime.date(year, month, day)
    except Exception:
        input('''
        \n***INVALID FORMAT***
        \rDate Format Should be: MM/DD/YYYY
        \rIf Single Digit for MM/DD, NO NEED FOR 0
        \rEx: 3/7/2018
        \rPress Enter to Try Again
        \r*********************''')
        return
    else:
        return return_date


def clean_price(price_str):
    try:
        split_price = price_str.split('$')
        nosignprice = split_price[1]
        price_float = float(nosignprice)
    except Exception:
        input('''
            \n***INVALID FORMAT***
            \rPrice Format Should be: $21.05
            \rBe Sure to Include the Dollar Sign!
            \rPress Enter to Try Again
            \r*********************''')
    else:
        return int(price_float * 100)


def clean_quan(quan_str):
    try:
        quan_int = int(quan_str)
    except Exception:
        input('''
        \n***INVALID ENTRY***
        \rProduct Quantity Should be a Whole Number
        \rEx: 87
        \rPress Enter to Try Again
        \r*********************''')
    else:
        return quan_int


def add_csv():
    with open('inventory.csv') as csvfile:
        data = csv.reader(csvfile)
        next(data)
        for row in data:
            product_in_db = session.query(Product).filter(Product.product_name == row[0]).one_or_none()
            if product_in_db is None:
                product = row[0]
                price = clean_price(row[1])
                quantity = clean_quan(row[2])
                date = clean_date(row[3])
                new_prod = Product(product_name=product, product_price=price,
                                   product_quantity=quantity, date_updated=date)
                session.add(new_prod)
        session.commit()


def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == 'v':
            pass
        elif choice == 'a':
            name = input('Product Name: ')
            amount_error = True
            while amount_error:
                amount = input('Product Quantity: ')
                amount_clean = clean_quan(amount)
                if type(amount_clean) == int:
                    amount_error = False
            price_error = True
            while price_error:
                price = input('Product Price (Ex:$5.70): ')
                price_clean = clean_price(price)
                if type(price_clean) == int:
                    price_error = False
            date_error = True
            while date_error:
                date = input('Date Updated (Ex: MM/DD/YYYY): ')
                date_clean = clean_date(date)
                if type(date_clean) == datetime.date:
                    date_error = False
            new_product = Product(product_name=name, product_quantity=amount_clean,
                                  product_price=price_clean, date_updated=date_clean)
            session.add(new_product)
            session.commit()
            print('Product Added!')
            time.sleep(2)
        elif choice == 'b':
            pass
        else:
            print('\nThanks for Checking out the Inventory!')
            app_running = False


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    add_csv()
    app()

    for prod in session.query(Product):
        print(prod)



