<h1>Github-Scraper</h1>
Simple automated reconnaissance tool created with Selenium in Python.

<h2>Tables of Content</h2>
<ul>
  <li><a href = "#generalInfo">General Info</a></li>
  <li><a href = "#technologies">Technologies</a></li>
  <li><a href = "#setup">Setup</a></li>
  <li><a href = "#status">Status</a></li>  
  <li><a href = "#inspiration">Inspiration</a></li>
</ul>

<h2 id="generalInfo">General info</h2>
This GitHub scraper tool is a Python script that automatically scans through all repositorys within a targeted GitHub Profil, including all subfolders, to check for specific file extensions and search for certain terms. The tool is fully customizable to search for specific file extensions and terms. This project was intended for training purposes to learn the basics of Python, web development, and web automation using Selenium. Additionally, it can be used as a reconnaissance tool for penetration testing purposes.

<h2 id="technologies">Technologies</h2>
<ul>
  <li>Python 3.11.2</li>
  <li>Selenium 4.8.2</li>
  <li>Urllib 3.11.2</li>
</ul>

<h2 id="setup">Setup</h2>
1. To run this tool clone or download the "main.py" file from this repository.<br></br>
2. Install Python3 and the required dependencies: Selenium, Webdriver Manager, and urllib.
<p align="center">
  <img class= "center" src="/images/dependencies_setup.PNG">
</p>
3. Run the script using Python
<p align="center">
  <img class= "center" src="/images/run_main.PNG">
</p>
4. The script will ask for the URL of the GitHub Profil you want to scrape. Enter the URL and press enter.<br></br>
5. The script will start running and will print out the URLs of all the files that match the specified file extensions and terms.<br></br>
6. You can customize the file extensions and terms to search for by modifying the code of the script. The relevant lines are:
<br></br>
<p align="center">
  <img class= "center" src="/images/relevant_lines_for_customization.PNG">
</p>
<h2 id="status">Status</h2>

For training purposes, the project is now complete. If you'd like to try out the tool, you can scan my Github profile where you'll find a repository named "TestRepo". It contains various files and subfolders with fake passwords and user information that can be used for testing purposes.

<h2 id= "inspiration">Inspiration</h2>
This project idea was inspired by Phd Security's 'Python Program That Can Scrape Github For Hackers'(https://www.youtube.com/watch?v=6UsdsC0B-vE), with changes made to the depth of the search, URL generation, and error handling.
