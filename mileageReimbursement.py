import csv


def calcReimburse(rate, begin, end):
    ''' formula for calculating reimbursement is
        reimbursement amount = mileage difference * rate of reimbursement
        returns the reimbursement rate in dollars per mile
    '''
    difference = end - begin
    return difference * rate


def read(filename):
    ''' reads the file filename and returns a tuple containing
        1. A list of the column titles
        2. A list of lists of each column
    '''
    fields = []
    rows = []
    with open("dataIn.csv", 'r') as csvfile:
        csvObject = csv.reader(csvfile)  # create a file object
        fields = next(csvObject)  # extracting field names from first row
        fields.append("Reimbursement")
        for row in csvObject:  # extracting each data row
            # extract elements from data row for calculation
            rate, begin, end = float(row[1]) / 100.0, float(row[2]), float(row[3])
            
            # perform reimbursement calculation
            reimbursement = "%.2f" % calcReimburse(rate, begin, end)

            # append the reimbursement value to the row
            row.append(reimbursement)

            # append the row to the row list
            rows.append(row)
    return fields, rows


def write(filename, fields, rows):
    ''' writes to the file filename
        fields is a list containing the column titles to write
        rows is a list of lists of each column to write
    '''
    with open("dataOut.csv", 'w') as csvfile:
        csvObject = csv.writer(csvfile)  # create a file object
        csvObject.writerow(fields) # write field names on first row
        for row in rows:
            csvObject.writerow(row)

        
def main():
    ''' reads data from "dataIn.csv",
        creates a new column for Reimbursements, and
        writes new modified data to "dataOut.csv"
    '''
    fields, rows = read("dataIn.csv")
    write("dataOut.csv", fields, rows)
