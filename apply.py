from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os  # to get the resume file
import time  # to sleep
import getlinks

# sample application links if we don't want to run get_links.py
URL_g1 = 'https://boards.greenhouse.io/cdbaby/jobs/4030259003?gh_src=6aa9332a3'
URL_l2 = 'https://boards.greenhouse.io/memsql/jobs/2060074?gh_src=c2cf63b91'
# URL_l3 = 'https://jobs.lever.co/fleetsmith/eb6648a6-7ad9-4f4a-9918-8b124e10c525/apply?lever-source=Glassdoor'
# URL_l4 = 'https://jobs.lever.co/stellar/0e5a506b-1964-40b4-93ab-31a1ee4e4f90/apply?lever-source=Glassdoor'
# URL_l6 = 'https://jobs.lever.co/verkada/29c66147-82ef-4293-9a6a-aeed7e6d619e/apply?lever-source=Glassdoor'
# URL_l8 = 'https://jobs.lever.co/rimeto/bdca896f-e7e7-4f27-a894-41b47c729c63/apply?lever-source=Glassdoor'
# URL_l9 = 'https://jobs.lever.co/color/20ea56b8-fed2-413c-982d-6173e336d51c/apply?lever-source=Glassdoor'


# there's probably a prettier way to do all of this
# test URLs so we don't have to call get_links
# URLS = [URL_g1, URL_l4, URL_l3, URL_l6, URL_l8, URL_l9]
URLS = [URL_g1]

# Fill in this dictionary with your personal details!
JOB_APP = {
    "first_name": "Anandha",
    "last_name": "Rajendran",
    "email": "ranandh87@gmail.com",
    "phone": "503-383-9048",
    "org": "eBay",
    "resume": "resume.pdf",
    "resume_textfile": "resume_short.txt",
    "linkedin": "https://www.linkedin.com/in/ranandha/",
    "website": "",
    "github": "",
    "twitter": "",
    "location": "Portland, Oregon, United States",
    "grad_month": '06',
    "grad_year": '2014',
    "university": "San Jose State University"  # if only o.O
}


# Greenhouse has a different application form structure than Lever, and thus must be parsed differently
def greenhouse(driver):
    # basic info
    driver.find_element_by_id('first_name').send_keys(JOB_APP['first_name'])
    driver.find_element_by_id('last_name').send_keys(JOB_APP['last_name'])
    driver.find_element_by_id('email').send_keys(JOB_APP['email'])
    driver.find_element_by_id('phone').send_keys(JOB_APP['phone'])

    # This doesn't exactly work, so a pause was added for the user to complete the action
    try:
        loc = driver.find_element_by_id('job_application_location')
        loc.send_keys(JOB_APP['location'])
        #loc.send_keys(Keys.DOWN)  # manipulate a dropdown menu
        # loc.send_keys(Keys.DOWN)
        loc.send_keys(Keys.RETURN)
        # time.sleep(2) # give user time to manually input if this fails

    except NoSuchElementException:
        pass

    # Upload Resume as a Text File
    driver.find_element_by_css_selector("[data-source='paste']").click()
    resume_zone = driver.find_element_by_id('resume_text')
    resume_zone.click()
    with open(JOB_APP['resume_textfile']) as f:
        lines = f.readlines()  # add each line of resume to the text area
        for line in lines:
            resume_zone.send_keys(line)
            time.sleep(2)

            # Upload coverletter as a Text File
        driver.find_element_by_xpath("//*[@id='main_fields']/div[9]/div/div[3]/a[3]").click()
        cover_letter_zone = driver.find_element_by_id('cover_letter_text')
        cover_letter_zone.click()
        with open(JOB_APP['resume_textfile']) as f:
            lines = f.readlines()  # add each line of resume to the text area
            for line in lines:
                cover_letter_zone.send_keys(line)
                time.sleep(2)

    # add linkedin
    try:
        driver.find_element_by_xpath("//label[contains(.,'LinkedIn')]").send_keys(JOB_APP['linkedin'])
    except NoSuchElementException:
        try:
            driver.find_element_by_xpath("//label[contains(.,'Linkedin')]").send_keys(JOB_APP['linkedin'])
        except NoSuchElementException:
            pass

    # #school details
    # try:
    #   school = driver.find_element_by_xpath("//*[@id='s2id_education_school_name_0']/a/span[1]").send_keys(JOB_APP['university'])
    #   school.send_keys(Keys.DOWN)
    #   school.send_keys(Keys.RETURN)
    # except NoSuchElementException:
    #     pass

    # where do you live
    try:
        driver.find_element_by_css_selector("#job_application_answers_attributes_2_text_value").send_keys("Portland,Oregon,USA")
    except NoSuchElementException:
        pass

    # Age 18
    try:
     DropDownSelection = driver.find_element_by_css_selector("#s2id_job_application_answers_attributes_5_boolean_value > a")
     driver.find_element_by_xpath("//*[@id='s2id_job_application_answers_attributes_5_boolean_value']/a/span[2]").click()
     DropDownSelection.send_keys(Keys.ARROW_DOWN)
     DropDownSelection.send_keys(Keys.RETURN)
    except NoSuchElementException:
        pass

    # can you relocate
    try:
        driver.find_element_by_xpath("//*[@id='job_application_answers_attributes_3_text_value']").send_keys("Yes")
    except NoSuchElementException:
        pass



    # add graduation year
    try:
        driver.find_element_by_xpath("//select/option[text()='2021']").click()
    except NoSuchElementException:
        pass

    # add university
    try:
        driver.find_element_by_xpath("//select/option[contains(.,'Harvard')]").click()
    except NoSuchElementException:
        pass

    # add degree
    try:
        driver.find_element_by_xpath("//select/option[contains(.,'Bachelor')]").click()
    except NoSuchElementException:
        pass

    # add major
    try:
        driver.find_element_by_xpath("//select/option[contains(.,'Computer Science')]").click()
    except NoSuchElementException:
        pass

    # add website
    try:
        driver.find_element_by_xpath("//label[contains(.,'Website')]").send_keys(JOB_APP['website'])
    except NoSuchElementException:
        pass

    # add work authorization
    try:
        driver.find_element_by_xpath("//select/option[contains(.,'any employer')]").click()
    except NoSuchElementException:
        pass

    driver.find_element_by_id("submit_app").click()


# Handle a Lever form
def lever(driver):
    # navigate to the application page
    driver.find_element_by_class_name('template-btn-submit').click()

    # basic info
    first_name = JOB_APP['first_name']
    last_name = JOB_APP['last_name']
    full_name = first_name + ' ' + last_name  # f string didn't work here, but that's the ideal thing to do
    driver.find_element_by_name('name').send_keys(full_name)
    driver.find_element_by_name('email').send_keys(JOB_APP['email'])
    driver.find_element_by_name('phone').send_keys(JOB_APP['phone'])
    driver.find_element_by_name('org').send_keys(JOB_APP['org'])

    # socials
    driver.find_element_by_name('urls[LinkedIn]').send_keys(JOB_APP['linkedin'])
    driver.find_element_by_name('urls[Twitter]').send_keys(JOB_APP['twitter'])
    try:  # try both versions
        driver.find_element_by_name('urls[Github]').send_keys(JOB_APP['github'])
    except NoSuchElementException:
        try:
            driver.find_element_by_name('urls[GitHub]').send_keys(JOB_APP['github'])
        except NoSuchElementException:
            pass
    driver.find_element_by_name('urls[Portfolio]').send_keys(JOB_APP['website'])

    # add university
    try:
        driver.find_element_by_class_name('application-university').click()
        search = driver.find_element_by_xpath("//*[@type='search']")
        search.send_keys(JOB_APP['university'])  # find university in dropdown
        search.send_keys(Keys.RETURN)
    except NoSuchElementException:
        pass

    # add how you found out about the company
    try:
        driver.find_element_by_class_name('application-dropdown').click()
        search = driver.find_element_by_xpath("//select/option[text()='Glassdoor']").click()
    except NoSuchElementException:
        pass

    # submit resume last so i   t doesn't auto-fill the rest of the form
    # since Lever has a clickable file-upload, it's easier to pass it into the webpage
    driver.find_element_by_name('resume').send_keys(os.getcwd() + "/resume.pdf")
    driver.find_element_by_class_name('template-btn-submit').click()


def aggregrate_urls():
    print(f'Job Listings: {aggregatedURLs}')
    print('\n')
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    for url in aggregatedURLs:
        print('\n')

        if 'greenhouse' in url:
            driver.get(url)
            try:
                greenhouse(driver)
                print(f'SUCCESS FOR: {url}')
            except Exception:
                # print(f"FAILED FOR {url}")
                continue

        elif 'lever' in url:
            driver.get(url)
            try:
                lever(driver)
                print(f'SUCCESS FOR: {url}')
            except Exception:
                # print(f"FAILED FOR {url}")
                continue
        # i dont think this else is needed
        else:
            # print(f"NOT A VALID APP LINK FOR {url}")
            continue

        time.sleep(1)  # can lengthen this as necessary (for captcha, for example)
    driver.close()


def defined_urls():
    print(f'Job Listings: {URLS}')
    print('\n')
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    for url in URLS:
        print('\n')

        if 'greenhouse' in url:
            driver.get(url)
            try:
                greenhouse(driver)
                print(f'SUCCESS FOR: {url}')
            except Exception:
                # print(f"FAILED FOR {url}")
                continue

        elif 'lever' in url:
            driver.get(url)
            try:
                lever(driver)
                print(f'SUCCESS FOR: {url}')
            except Exception:
                # print(f"FAILED FOR {url}")
                continue
        # i dont think this else is needed
        else:
            # print(f"NOT A VALID APP LINK FOR {url}")
            continue

        time.sleep(1)  # can lengthen this as necessary (for captcha, for example)
    driver.close()


if __name__ == '__main__':
    # call get_links to automatically scrape job listings from glassdoor
    # comment below line if you think need not collect one page links or 5 page links and apply for only defined Urls
    #  aggregatedURLs = getlinks.collectURLs()
    # aggregrate_urls()
    defined_urls()
