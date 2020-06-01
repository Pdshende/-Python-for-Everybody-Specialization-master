'''
In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://python-data.dr-chuck.net/comments_353540.json (Sum ends with 71)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
'''
import time
start = time.time()
import urllib.request, urllib.parse, urllib.error
import json

#Data collection
link = input('Enter location: ')
print('Retrieving', link)

html = urllib.request.urlopen(link).read().decode()
print('Retrieved', len(html), 'characters')

try:
    js = json.loads(html)
except:
    js = None

cn = 0
sm = 0
for item in js['comments']:
    cn += 1
    sm += int(item['count'])

print('Count:', cn)
print('Sum:', sm)
end = time.time()

print("The total excecution Time for this code is sec", (end-start))

'''
Output: - 
Enter location: http://py4e-data.dr-chuck.net/comments_417438.json
Retrieving http://py4e-data.dr-chuck.net/comments_417438.json
Retrieved 2717 characters
Count: 50
Sum: 2178
The total excecution Time for this code is sec 2.7438461780548096

'''
