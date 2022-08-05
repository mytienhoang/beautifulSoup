import _json
import requests

#Didn't need to import beautifulsoup since it's already in the folder

#function to get job list from url f'https://www.talent.com/jobs?k={role}&l={location}'

def getJobList(role,location):
    url = f'https://www.talent.com/jobs?k={role}&l={location}'
    # Complete the missing part of this function here

#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    print("Saving data to JSON")

#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    # ask for the job location
    print("Enter the desired job location")
    location = input()
    print('So you want a job in ' + location + ', with the occupation title being "' + role + '". ')
    
if __name__ == '__main__':
    main()
