#This will be a search engine using csv, where you will be able to search porsche cars in the database depending on the year (File I/O)
import csv
#Here I am importing the csv library.

car_system = 'porsche.csv'
#Here I am assigning a variable to the csv file so I am able to use it in my function.

Porsche = [
    {'porsche': 'Porsche 718 Cayman GTS', 'year': 2017},
    {'porsche': 'Porsche 718 Boxter GTS', 'year': 2017},
    {'porsche': 'Porsche 992 Carrera S', 'year': 2019},
    {'porsche': 'Porsche 992 Turbo S', 'year': 2020},
    {'porsche': 'Porsche 992 GT3 Touring', 'year': 2021},
    {'porsche': 'Porsche 992 GT3 RS', 'year': 2022},
    {'porsche': 'Porsche Cayenne Turbo', 'year': 2018},
    {'porsche': 'Porsche Cayenne S', 'year': 2024},
    {'porsche': 'Porsche Taycan Turbo S', 'year': 2019}
]
#Here I have created database for my csv file, this will be the information that will be pulled into the definition below.

def main():
    Year = int(input("What year and newer would you like to search for?: "))
    #Here I have created a variable that will take the users input for the year and newer that they want to filter.

    with open(car_system,'w') as file:
        fieldnames = ['porsche', 'year']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(Porsche)
    """
    Here I have created a function that will be able to create and overwrite the csv file.
    The "with open" statement will open the file with the denotation w, meaning write.
    I have then followed this up with the variable writer, which will open the file using dictwriter, which opens the file as a dictionary.
    fieldnames is the paramaters that will be passed to the writerows function.
    The "writer.writeheader()", will create a header called 'porsche,year' in the file created, since the csv file ignores the first row, so it is a placement holder.
    Lastly, the "writer.writerows(porsche)" function will take the parameters that I have given it (fieldnames), and write them into the csv file, 
    and since I have put (porsche) into the function it will write in all of the data that is tied to that variable.
    """
    with open(car_system,'r') as file:
        reader = csv.DictReader(file)
        print(f"here are cars from {Year} and newer:")
        for row in reader:
            if int(row['year']) >= Year:
                print(f"{row['porsche']} {row['year']}")
    """
    Here I have created the search engine for the csv file.
    Here I have opened the file with the denotation r, meaning read.
    I have then followed this up with the variable reader, much like the write function, it will read the csv file as a dictionary.
    Now I have added a print function which will tell the user that it is displaying the year that they have input and newer, I have done this through a formatted string.
    I have also used a for statement which will look for rows in the variable reader.
    This then goes into an if statement, that will go through the rows and look for the ones that are equal to or bigger than the user input,
    this will then print out a formatted string which will print out the rows found.
    """
main()