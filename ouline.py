import _json
import requests
import json
from bs4 import BeautifulSoup

#Didn't need to import beautifulsoup since it's already in the folder

#function to get job list from url 
#f'https://www.talent.com/jobs?k={role}&l={location}'

def getJobList(role,location):
    url = f'https://www.talent.com/jobs?k={role}&l={location}'
    #function to get job list from url #f'https://www.talent.com/jobs?k={role}&l={location}'
    response = requests.get(url)
    # print the status code here!
    print(response.status_code)
    soup =   BeautifulSoup(response.text, "html.parser")
    JobDetails = soup.find_all('div', class_='card card__job')
    # Create an array Here
    jobDetailsjson = {}
    for job in JobDetails:
        jobTitle = job.find('h2', class_='card__job-title').text.strip()
        company = job.find('div', class_='card__job-empname-label').text.strip()
        description = job.find('p', class_='card__job-snippet').text.replace('\n', '').replace("'", "").strip()
        jobDetailsjson['Title'] = jobTitle
        jobDetailsjson['Company'] = company
        jobDetailsjson['Description'] = description
        # Add jobDetailsjson to that array
    return jobDetailsjson



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
    getJobList(role, location)
    print('So you want a job in ' + location + ', with the occupation title being "' + role + '". ')
    
if __name__ == '__main__':
    main()
