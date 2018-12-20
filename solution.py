import csv
import matplotlib.pyplot as plt

"""
Open a .csv file with a given file name (must have a heading row that
contains the values "purpose" and "int_rate") and create a dictonary that
maps each unique purpose to a list containing the interest rates of every
row that has that specified purpose.
@param fileName {String}  the name of the csv file to process
@returns  a dictionary mapping purposes to their matching interest rate
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


"""
Takes a dictionary of miscellaneous keys mapped to lists of numbers
and returns a dictionary of the same keys mapped to the average value
of the list of numbers they were previously mapped to.
@param ogMap {Dict}  a dictionary with keys of any type mapped to lists
                     of numbers (e.g. floats, ints - any object that can
                     be summed and divided)
@returns {Dict}  a dictionary with keys of any type mapped to a singular
                 number: the average of the list from the inputted
                 dictionary
"""
def averageOfOneToManyMapping(ogMap):
    # Create a dictionary to hold return value of this function: the
    # original keys mapped to the averaged value
    averagedMap = {}

    # Iterate through every key in the original mapping and add the
    # averaged equivalent to the averageMap
    for key in ogMap:
        averagedMap[key] = sum(ogMap[key]) / float(len(ogMap[key]))

    # Return the mapping that now contains the averaged values
    return averagedMap

if __name__ == "__main__":
    # Calculate mapping of purposes to average interest rates from file
    purposesToAvgRateMap = averageOfOneToManyMapping(
        createPurposeToRateMapFromCsv('data.csv')
    )

    # Depack mapping into two aligned lists (i.e. the i-th element of
    # purposes is mapped to the i-th element of intRates)
    purposes = []
    intRates = []
    for k, v in purposesToAvgRateMap.items():
        purposes.append(k)
        intRates.append(v)

    # Initialize graph
    plt.rcdefaults()

    # Create bar graph of values
    plt.bar(range(len(intRates)), intRates, width = 0.6)
    plt.xticks(range(len(intRates)), purposes, fontsize = 'small', rotation = 90)
    plt.title('Purpose vs Mean Interest Rate')
    plt.xlabel('purpose')
    plt.ylabel('mean interest rates (%)')
    plt.tight_layout()

    # Render and display the chart to the user
    plt.show()
