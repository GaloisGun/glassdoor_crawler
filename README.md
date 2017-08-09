# Job Crawler for Glassdoor
The crawler was designed to extract job information from the glassdoor.

## Installation
- Python 2.7
- Scrapy

## Usage
1. Download
````
git clone git@github.com:GaloisGun/glassdoor_crawler.git
````

2. Open Glassdoor.com 
- Do not login in
- search the job you want to crawl
- copy the result link as start_url

3. Change the start_urls
Open glassdoor.py and change the start_urls

4. Run
```````
scrapy crawl glassdoor -o jobs.json
```````
The program will automatically create a json file to store the results

## Sample Result
``````
[
  {
    "location": "McLean, VA",
    "jobID": "2381389441",
    "title": "Software Engineer",
    "company_name": " Booz Allen Hamilton Inc.",
    "details": [
      "2+ years of experience with developing Web applications in ASP .NET, C#, .NET 4.0, Java, or Python",
      "2+ years of experience with software engineering concepts and the software development life cycle",
      "Knowledge of database concepts, Web server maintenance, error log analysis, and code performance analysis",
      "Ability to obtain a security clearance",
      "BA or BS degree"
    ]
  },
  {
    "location": "San Mateo, CA",
    "jobID": "2450373135",
    "title": "Software Engineer",
    "company_name": " Jobvite",
    "details": [
      "Rewrite, refactor, and re-architecture and scale applications;",
      "Define scalable platform vision and strategy, present to management team and work with world-class engineers and product managers to implement vision and strategy;",
      "Innovate products, designs, technologies, and deliver product launches in rapid creative environment; and,",
      "Work with Product Management on requirements definition and design"
    ]
  },
  {
    "location": "Minnetonka, MN",
    "jobID": "2469102085",
    "title": "Software Engineer",
    "company_name": " Peoplenet Communications",
    "details": [
      "Stay on top of new and up-and-coming technologies",
      "Be an educator and a mentor for junior engineers",
      "Possess intellectual humility - Be able to make mistakes and learn from them",
      "Design and build sophisticated and highly-scalable systems",
      "Challenge everything - Push yourself and others by asking how we can be better in all aspects of our work",
      "Ensure the team\u2019s work is of high quality through the use of best practices such as continuous integration, unit and integration testing, and code reviews",
      "Take ownership and lead development of team objectives",
      "Collaborate in a culture that promotes passion in technology",
      "Hack away at the bleeding edge of technology during our epic Hack-a-thons (and win a cool prize like a Super Star Destroyer Lego set!)"
    ]
  },
  {
    "location": "Purchase, NY",
    "jobID": "2473726474",
    "title": "Software Engineer",
    "company_name": " ASG Technologies",
    "details": [
      "Develop web-based user interface elements and/or Web Components for presenting and interacting with Enterprise Content. Participate in the full SDLC: requirements analysis, design, coding, testing, debugging, problem resolution. Work in an agile environment with a cross-functional team."
    ]
  }
  ]
  ``````
  


