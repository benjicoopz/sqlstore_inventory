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
    print(split_date)
    month = int(months.index(split_date[0]) + 1)
    day = int(split_date[1].split(',')[0])
    year = int(split_date[2])
    return datetime.date(year, month, day)


def add_csv():
    with open('inventory.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            print(row)


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
    #add_csv()
    clean_date('October 25, 2017')
