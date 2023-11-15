Python - Network #1
This undertaking focused on acquiring proficiency in employing the urllib and requests Python libraries for transmitting and receiving HTTP messages to URLs. The practice involved sending GET and POST requests, retrieving JSON resources, and engaging with APIs, specifically the Star Wars API, GitHub API, and Twitter API.

Tasks
0. What's my status? #0

0-hbtn_status.py: Python script that fetches https://intranet.hbtn.io/status.
Utilizes urllib.
1. Response header value #0

1-hbtn_header.py: Python script that displays the X-Request-Id response header variable of a request to a given URL.
Usage: ./1-hbtn_header.py <URL>.
Utilizes urllib.
2. POST an email #0

2-post_email.py: Python script that sends a POST request to a given URL with a specified email and displays the response body.
Usage: ./2-post_email.py <URL> <email>.
Utilizes urllib.
3. Error code #0

3-error_code.py: Python script that sends a request to a given URL and displays the response body, handling HTTP errors.
Utilizes urllib.
4. What's my status? #1

4-hbtn_status.py: Python script that fetches https://intranet.hbtn.io/status.
Utilizes requests.
5. Response header value #1

5-hbtn_header.py: Python script that displays the X-Request-Id response header variable of a request to a given URL.
Usage: ./5-hbtn_header.py <URL>.
Utilizes requests.
6. POST an email #1

6-post_email.py: Python script that sends a POST request to a given URL with a specified email and displays the response body.
Usage: ./6-post_email.py <URL> <email>.
Utilizes requests.
7. Error code #1

7-error_code.py: Python script that sends a request to a given URL and displays the response body, handling HTTP errors.
Utilizes requests.
8. Search API

8-json_api.py: Python script that sends a POST request to http://0.0.0.0:5000/search_user with a letter passed as a parameter.
Usage: ./8-json_api.py <letter>.
The letter is sent as the value of the variable q.
If no letter is given, sets q="".
If the response body is properly formatted and non-empty, displays it as [<id>] <name>.
Utilizes requests.
9. My Github!

10-my_github.py: Python script that takes GitHub credentials (username and password) and uses the Github API to display the corresponding ID.
Usage: ./10-my_github.py <username> <password>.
Utilizes requests.
10. Time for an interview!

100-github_commits.py: Python script that lists the 10 most recent comments of a given GitHub repository using the GitHub API.
Usage: ./100-github_commits.py <repository name> <owner name>.
Utilizes requests.



