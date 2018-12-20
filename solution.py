import csv

"""
Open a .csv file with a given file name (must have a heading row that contains
the values "purpose" and "int_rate") and create a dictonary that maps each
unique purpose to a list containing the interest rates of every row that has
that specified purpose.
@param fileName {String}  the name of the csv file to process
@return  a dictionary mapping purposes to their matching interest rate
         e.g.:
         {
             'credit card': [12.3, 10.5],
             'car': [4.2, 3.5, 6.2]
         }
"""
def createPurposeToRateMapFromCsv(filename):
    # Create a dictionary to hold the one-to-many mapping of purposes to
    # interest rates that will be returned
    purposeToRateMap = {}
    
    # Load the specified .csv file
    try:
        with open(filename) as csvfile:
            # Iterate through every row in the file, add the interest
            # rate to the list of rates associated to the file's purpose
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Retrieve the data for this row
                purpose = row['purpose']
                intRate = float(row['int_rate'])

                # Check if this row's purpose already has an associated
                # list of interest rates in the map, and if so add this
                # row's interest rate to that list ...
                if purpose in purposeToRateMap:
                    purposeToRateMap[purpose].append(intRate)

                # ... but, if a list does not already exist then create
                # one and add this interest rate to it
                else:
                    purposeToRateMap[purpose] = [intRate]

        # Return the completed one-to-many mapping
        return purposeToRateMap
    
    except csv.Error:
        # Handle file errors
        print('Invalid file')

d = createPurposeToRateMapFromCsv('data.csv')
print(d)
