# This file is going to go through the data in the csv file and take out all of the titles
import pprint	# Just used for looking at parts of the data array
import csv 	# Needed for the splitting of csv data

global 
# Process: Create a dictionary of the entries and the synonyms of the given entity
# Input: data - a single column of the data (as in a table)
# Output: dictionary of {entries: synonyms}
def obtain_data(data):
  entity = {}
  for entry in data:
    synonyms = []
    

# ----------------------------------------- Populate specific entities ----------------------------------

# Process: Call the function obtain_data with the correct column and REST Api POST the data to the correct entity
# Input: data (as processed by 'populate_entry')
# Output: -1 if failed, 0 otherwise

def populate_Course(data):
  # Get the correct column (if for some reason the order changes at any point)
  column = -1
  for col in range(len(data[0])):
    if (data[0][col] == 'Title' or data[0][col] == 'Course'):
      column = col
      break
  if column == -1:
    return -1
  # Obtain the data from just the needed column
  colData = [row[col] for row in data[1:]]
  entries = obtain_data(colData)

  return 0


def populate_Subject_Area(data):
  # Get the correct column (if for some reason the order changes at any point)
  column = -1
  for col in range(len(data[0])):
    if (data[0][col] == 'Subject Area' or data[0][col] == 'Subject area'):
      column = col
      break
  if column == -1:
    return -1
  # Obtain the data from just the needed column
  colData = [row[col] for row in data[1:]]
  entries = obtain_data(colData)
  return 0

# Not sure if synonyms will be needed here - maybe just lower case version? Because some lecturers may share a surname so we would need to ask for the full name anyway. Unless we change that.
def populate_Lecturer(data):
  return -1


#------------------------------Get the data ready for population (and call the populators) --------------
# Process: Open the csv file (TEMPORARY SOLUTION - FIND A WAY TO USE THE DATABASE DIRECTLY)
# Input: filename
# Output: -1 if failed, 0 otherwise
def populate_entity(filename):
  # Open the csv file and ...
  dataFile = open(filename, 'r')
  dataRead = dataFile.read()
  # Split it into the individual bits of data
  dataRead = dataRead.splitlines()
  data = list(csv.reader(dataRead))
  
  # Populate the Course entity in Dialogflow
  populate_Course(data)
  

populate_entity('Short_Courses_Data.csv')
