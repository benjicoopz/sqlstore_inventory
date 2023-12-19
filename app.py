from models import Base, session, Product, engine
import datetime
import csv


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
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October',
              'November', 'December']
    split_date = date_str.split(' ')
    month = int(months.index(split_date[0]) + 1)
    day = int(split_date[1].split(',')[0])
    year = int(split_date[2])
    return datetime.date(year, month, day)


def clean_price(price_str):
    split_price = price_str.split('$')
    if len(split_price) < 2:
        return None
    nosignprice = split_price[1]
    price_float = float(nosignprice)
    return int(price_float * 100)


def clean_quan(quan_str):
    quan_int = int(quan_str)
    return quan_int


def add_csv():
    with open('inventory.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            print(row)
            product = row[0]
            price = clean_price(row[1])
            quantity = clean_quan(row[2])
            date = clean_date(row[3])
            new_prod = Product(product_name=product, product_price=price, product_quantity=quantity, date_updated=date)
            session.add(new_prod)
        session.commit()


def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == 'v':
            pass
        elif choice == 'a':
            pass
        elif choice == 'b':
            pass
        else:
            print('\nThanks for Checking out the Inventory!')
            app_running = False


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    # app()
    add_csv()

    for prod in session.query(Product):
        print(prod)
