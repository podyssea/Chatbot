# This file is going to go through the data in the csv file and take out all of the titles
import pprint	# Just used for looking at parts of the data array
import csv 	# Needed for the splitting of csv data
import json #to get requests
import re #regular expressions
from itertools import combinations #combinations for synonyms
import itertools #synonyms

# Input: data - a single column of the data (as in a table)
# Output: CSV format text that has to be copy pasted in raw mode of entities in DialogFlow

#Gets the file
def populate_entity(filename):
  # Open the csv file and ...
  dataFile = open(filename, encoding="utf8")
  dataRead = dataFile.read()
  # Split it into the individual bits of data
  dataRead = dataRead.splitlines()
  data = list(csv.reader(dataRead))
  return data
  
#Change the file name (needs to be of the same structure as the the first one)
archive = populate_entity('Short_Courses_Data.csv')

#Creates two empty temporary lists
subject = []
course = []

for entry in archive:
  subject.append(entry[0])
  course.append(entry[1])

subject.pop(0)
course.pop(0)

#This gives two lists one for subject and one for course that contain all the needed information
# that will be copy-pasted in the raw mode of the DIALOGFLOW entities
subject_list = list(dict.fromkeys(subject))
course_list = list(dict.fromkeys(course))

#--------------->>>>>>This is the important part<<<<<<---------------
for each in course_list:
      splitted = re.findall(r"[\w']+|[.,!?;]", each)

      for word in splitted:
          if (word in useless or word in sep):
              splitted.remove(word)
          elif len(word) == 1:
              splitted.remove(word)

      results = [' '.join(splitted[i:j]) for i, j in combinations(range(len(splitted) + 1), 2)]

      list_of_lists = [[i] for i in results]

      flattened = [val for sublist in list_of_lists for val in sublist]
      for entity in flattened:
        if entity == "and":
          flattened.remove(entity)
      flattened.insert(0,each)

      synonyms = (', '.join('"' + item + '"' for item in flattened))
      print(synonyms)


