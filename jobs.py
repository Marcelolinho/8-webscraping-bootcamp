from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
    print('Put some skill that you are not familiar with')
    unfamiliar_skill = input('>')
    print(f'Filtering out {unfamiliar_skill}')

    website = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation='
    response = requests.get(website).text
    soup = BeautifulSoup(response, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for i, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company = job.find('h3', class_='joblist-comp-name').text.strip()
            skills = job.find('span', class_='srp-skills').text.strip()
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                with open(f'posts/{i}.txt', 'w')as f:
                    f.write(f'Company Name: {company}')
                    f.write(f'Required Skills: {skills}')
                    f.write(f'More Info: {more_info}')
                print(f'File Saved {i}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} seconds...')
        time.sleep(time_wait * 60)
