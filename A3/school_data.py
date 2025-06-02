# school_data.py
# Barrett Sapunjis
#
# A terminal-based application for computing and printing statistics based on a given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import csv
import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here


# You may add your own additional classes, functions, variables, etc.

def readCSV(csvName):

    """
    Reads a csv to return an array of csv values, a map to the array, and a dictionary containing csv properties

    Parameters
    ----------

    schools : list -> strings for each school name. 
    rows: list -> contains all lines from csv
    csvProperties : dict -> contains information about csv (I.E. number of lines, number of schools seen etc...)
    array : float64 -> numpy array to be stored with csv information 
    arrayMap : dict -> map to with key-values of school name and array location in master array. 
    
    ---
    
    args 
    ---
    none

    ---

    returns 
    -------
    array, 
    arrayMap,
    csvProperties 
    """
    schools = []
    seenSchools = set()
    seenYears = set()
    with open(csvName, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        for row in rows:
            if(row['School Code'] not in seenSchools):
                schools.append((row["School Name"], row['School Code']))
                seenSchools.add(row['School Code'])   
            if(row['ï»¿School Year'] not in seenYears):
                seenYears.add(row['ï»¿School Year'])
                schools
        
        csvProperties = {
            'numLines' : reader.line_num - 1,
            'numSchools' : len(schools),
            'years' : seenYears,
            'schools' : schools
        }
        
        array = createArray(csvProperties)
        arrayMap = createMap(csvProperties, seenYears)

        x : np.float64 = 1

        for row in rows:
            for i in range(10,13):
                try: 
                    int(row[f'Grade {i}'])
                except:
                    row[f'Grade {i}'] = np.nan
                    
            array[arrayMap[row['School Code']], 0, arrayMap[row['ï»¿School Year']]] = row['Grade 10']
            array[arrayMap[row['School Code']], 1, arrayMap[row['ï»¿School Year']]] = row['Grade 11']
            array[arrayMap[row['School Code']], 2, arrayMap[row['ï»¿School Year']]] = row['Grade 12']


        return array, arrayMap, csvProperties
    
def createMap(properties, years):
    """
    Takes in the csv properties, as well as the relevant years, to create a map for the parent array as a dictionary. 

    args
    ---
    properties : dict -> contains csv properties 
    years : int set -> contains a list of all  the ears seen in the csv 

    ---

    returns
    ---
    newDict : dict -> a dictionary representing a map to mask the array indexing 

    ---
    """

    newDict = {}
    i = 0
    for tup in properties['schools']:
        newDict[tup[0]] = i
        newDict[tup[1]] = i 
        i = i + 1
    yearsList = sorted(years)
    i = 0
    for year in yearsList: 
        newDict[year] = i
        i = i + 1
    return newDict
    
def stage2(schoolArray, arrayMap : dict, csvProperties : dict):
    """
    Prompts user for school name or code and returns the corresponding school data

    args
    ---
    schoolArray : float64 numpy array -> sub array containing information for an individual school
    arrayMap : dict -> mapping of school names/codes to array indices
    csvProperties : dict -> contains csv properties

    returns
    ---
    newArray : numpy array containing school-specific data
    schoolTuple : tuple containing school name and code
    """
    while(True):
        userIn = input("Please enter the high school name or school code: ")
        if userIn not in arrayMap.keys():
            print("The code or name you have entered is not in the data set, please try again")
            continue 
        else:
            newArray = schoolArray[arrayMap[userIn]][:][:]
            for tup in csvProperties['schools']:
                if userIn in tup:
                    schoolTuple = tup
            return newArray, schoolTuple

def createArray(properties):
    array = np.zeros((properties['numSchools'], 3, len(properties['years'])))
    return array


def main():


    print("\nENSF 692 School Enrollment Statistics")

    # Print Stage 1 requirements here
    AllSchoolsArray, arrayMap, csvProperties = readCSV("Assignment3Data.csv")
    print(f"\nThe shape of the array is {AllSchoolsArray.shape}")
    print(f"the depth of the array is {AllSchoolsArray.shape[0]}, with each layer having dimensions of {AllSchoolsArray.shape[1]} x {AllSchoolsArray.shape[2]}")
    
    # Prompt for user input
    schoolArray, school = stage2(AllSchoolsArray, arrayMap, csvProperties)
    print(schoolArray)
    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")
    print(f"The selected school is: {school[0]} (Code: {school[1]})")
    print(f"The mean Enrollment for Grade 10 in all years is: {int(np.nanmean(schoolArray[0][:]))}")
    print(f"The mean Enrollment for Grade 11 in all years is: {int(np.nanmean(schoolArray[1][:]))}")
    print(f"The mean Enrollment for Grade 12 in all years is: {int(np.nanmean(schoolArray[2][:]))}")
   
    print(f"The highest enrollment for any grade in any year was: {int(np.nanmax(schoolArray))}")
    print(f"The lowest enrollment for any grade in any year was: {int(np.nanmin(schoolArray))}")

    totalSchoolEnrollments = []
    sum = 0
    for year in sorted(csvProperties['years']):
        totalSchoolEnrollments.append((year,int(np.sum(schoolArray[:,arrayMap[year]]))))

    sum = int(sum + np.sum(schoolArray[:,:]))
    

    print(f"The total enrollment for all years can be found in the below list: ")
    print(totalSchoolEnrollments)
    print(f"The total enrollment in all 10 years was: {sum}")
    print(f"the mean yearly enrollment over the 10 years is: {sum//10}")

    if np.max(schoolArray) < 500: 
        print("No enrollments over 500")
    else:
        over_500 = schoolArray[schoolArray > 500]
        mean = int(np.nanmean(over_500))

        print(f"The median value of the >500 enrollments is {mean}")            
                    
        


    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")
    
    print(f"\nThe mean enrollment for all schools in 2013 was: {int(np.nanmean(AllSchoolsArray[:,:, arrayMap['2013']]))}")
    print(f"The mean enrollment for all schools in 2022 was: {int(np.nanmean(AllSchoolsArray[:,:, arrayMap['2022']]))}")

    print(f"\nThe total graduating class of 2022 was: {int(np.nansum(AllSchoolsArray[:,2, arrayMap['2022']]))}")
    
    print(f"the highest enrollment for a single grade within the entire time period was: {int(np.nanmax(AllSchoolsArray))}")
    print(f"the lowest enrollment for a single grade within the entire time period was: {int(np.nanmin(AllSchoolsArray))}")
    #csvString, dictThing = readCSV("Assignment3Data.csv")



if __name__ == '__main__':
    main()

