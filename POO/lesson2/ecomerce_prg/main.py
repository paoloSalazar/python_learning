from ecomerce.database import Database as DB
from ecomerce.database import Formatter
def main():
    # database = DB()
    # database.connect()
    formatter = Formatter()
    formattedString = formatter.format_string("this is my formatted string.")
    print(formattedString)



if __name__ == "__main__":
    main()