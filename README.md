### Executive Summary
A significant challenge for people with disabilities is the lack of awareness around accessible 
employers, programs, and opportunities within the community. Additionally, the information they 
seek on inclusive hiring practices, benefits, accommodations, and company culture is scattered 
across multiple sources. Our application uses data mining techniques on company blogs, Twitter, 
Glassdoor, YouTube, etc., to aggregate such information, and, in doing so, empowers the underserved
disabled community to make more informed job-search decisions. The application also aims to help
employers identify gaps in the information they provide, thus bringing them closer to diverse 
candidates' needs.
--------
### The Opportunity
* Inclusive employers are open to hiring candidates who identify as disabled, & offer dedicated accomodations and benefits.
* While searching for inclusive employers, these candidates look up information online.
* The information they seek on accommodations, benefits and overall company culture is hard to find and scattered across multiple sources (such as official company web pages, blog posts, Twitter, company review websites, YouTube videos, etc.).
* Our web application aims to decrease friction for disabled job seekers by centralizing information on inclusive employers. 
* The goal of our product is to empower disabled candidates to make better decisions during their job search.
--------
### Scope
* As a starting point for the project, we focused on companies specifically in the technology industry. 
* Amongst these, we did a quick check of the publicly available data for each, on the basis of which we selected three companies (Microsoft, Cisco, and Intel) for our MVP (Minimum Viable Product).
* To extract information about inclusive hiring practices, we limited ourselves to official company websites and chose to leave out third-party news websites or blogs.
* We added sources like Twitter, YouTube, and official company DEI reports to increase the diversity of our data sources.
--------
### Project Information 
[Project Poster](https://projectinclusion.netlify.app/)

[Project Walk-through and Demo](https://www.youtube.com/watch?v=R6R0PL0jpKg&t=2s)

--------
### File Structure on the repository

    ├── Articles                                  
    │   └── employee-community-articles.ipynb    <- Juptyer notebook that extracts employee community articles.
    │   └── extract-paras.ipynb                  <- Juptyer notebook that extracts paras from articles.
    │   └── extract-paras-output.csv             <- Extracted paras into a csv file.
    │   └── inclusive-hiring-articles.ipynb      <- Juptyer notebook that extracts inclusive hiring articles.
    │   └── paras-to-pages.xlsx                  <- Converted paras to pages into a csv flie.
    │   └── relevance-filter.ipynb               <- Juptyer notebook used for filtering relevant articles.
    │   └── relevance-filter-output.xlsx         <- Extracted filtered articles into a csv file.
    │
    ├── Bing-Search                              
    │   ├── cleaning-search-output.ipynb         <- Jupyter notebook that cleans search outputs.
    │   ├── search-output-python-first.csv       <- CSV output of the first search version.
    │   ├── search-output-python-second.csv      <- CSV output of the second search version.
    │   ├── search-output-with-news.csv          <- CSV output of search with news articles.
    │   ├── search-output-with-tldextract.csv    <- CSV output of search with tldextract applied.
    │   ├── search-output-without-news.csv       <- CSV output of search without news articles.
    │   ├── search-python-first.py               <- First version of search implementation.
    │   └── search-python-second.py              <- Second version of search implementation.
    │
    ├── Glassdoor                                
    │   ├── cisco-reviews-output.xlsx            <- CSV output of cisco reviews.
    │   ├── glassdoor-cons-output.xlsx           <- CSV output of the cons.
    │   ├── glassdoor-filtration.ipynb           <- Jupyter notebook for filtering glassdoor comments.
    │   ├── glassdoor-pros-output.xlsx           <- CSV output of the pros.
    │   ├── intel-reviews-output.xlsx            <- CSV output of intel reviews.
    │   ├── microsoft-reviews-output.xlsx        <- CSV output of microsoft reviews.
    │   ├── relevant-glassdoor-results.xlsx      <- CSV output of relevant glassdoor results.
    │   └── extract-reviews.py                   <- Python file used to extract reviews.
    │
    ├── Ratings                                  
    │   └── valuable500-disabilityin.ipynb       <- Jupyter notebook for extracting valuable500 and disabilityIn ratings.
    │
    ├── Twitter                                  
    │   └── employee-community-tweets.xlsx       <- Extracted employee community tweets into a CSV file. 
    │   └── extract-tweets.ipynb                 <- Jupyter notebook to extract tweets.   
    │   └── inclusive-hiring-tweets.xlsx         <- Extracted employee community tweets into a CSV file.     
    │   └── leadership-tweets.xlsx               <- Extracted leadership tweets into a CSV file.     
    │   └── unfiltered-tweets.xlsx               <- Extracted all tweets (unfiltered) into a CSV file.     
    │
    ├── Website                                  
    │   └── static                               
    │       └── secondary-pages                       
    │           └── assets                           
    │               └── css                      <- All css files for the website.
    │               └── img                      <- All images used on the website.
    │               └── js                       <- Javascript files used on the website.
    │               └── vendor                   <- All vendor related files.
    │   └── templates                            
    │       └── cisco_tabs                       
    │           └── employee.html                <- HTML file for the Employee Comments tab.
    │           └── erg.html                     <- HTML file for the Employee Community tab.
    │           └── hiring.html                  <- HTML file for the Inclusive Hiring tab.
    │           └── mission.html                 <- HTML file for the Mission and Vision tab.
    │           └── questions.html               <- HTML file for the Submit a Question tab.
    │           └── ratings.html                 <- HTML file for the Rating and Reviews tab.
    │       └── intel_tabs 
    │           └── employee.html                <- HTML file for the Employee Comments tab.
    │           └── erg.html                     <- HTML file for the Employee Community tab.
    │           └── hiring.html                  <- HTML file for the Inclusive Hiring tab.
    │           └── mission.html                 <- HTML file for the Mission and Vision tab.
    │           └── questions.html               <- HTML file for the Submit a Question tab.
    │           └── ratings.html                 <- HTML file for the Rating and Reviews tab.
    │       └── microsoft_tabs 
    │           └── employee.html                <- HTML file for the Employee Comments tab.
    │           └── erg.html                     <- HTML file for the Employee Community tab.
    │           └── hiring.html                  <- HTML file for the Inclusive Hiring tab.
    │           └── mission.html                 <- HTML file for the Mission and Vision tab.
    │           └── questions.html               <- HTML file for the Submit a Question tab.
    │           └── ratings.html                 <- HTML file for the Rating and Reviews tab.
    │       └── welcome.html                     <- HTML file for the homepage.
    │   └── main.py                              <- Main python file for the flask app.
    │   └── Procfile                             <- Procfile required for flask.
    │   └── README.md                            <- README for developers to use this website on a local machine.
    │   └── requirements.txt                     <- All the libraries required for deploying this app.
    │    
    ├── README.md                                <- The top-level README for developers using this project (aka this file).

--------