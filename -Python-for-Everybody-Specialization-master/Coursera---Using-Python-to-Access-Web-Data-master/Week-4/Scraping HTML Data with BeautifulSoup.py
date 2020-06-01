'''
Scraping Numbers from HTML using BeautifulSoup
In this assignment you will write a Python program
similar to http://www.pythonlearn.com/code/urllink2.py.
The program will use urllib to read the HTML from the data files below,
and parse the data, extracting numbers and compute the
sum of the numbers in the file.

We provide two files for this assignment.
One is a sample file where we give you the sum for your testing and
the other is the actual data you need to process for the assignment.

Sample data: http://python-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://python-data.dr-chuck.net/comments_353539.html (Sum ends with 63)
You do not need to save these files to your folder since your program
will read the data directly from the URL. Note: Each student will have a
distinct data url for the assignment - so only use your own data url for analysis.
'''
import time
#import socket
start  = time.time()
import urllib.request
from bs4 import BeautifulSoup

url = input('Enter - ')

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")
tag = soup("span")
count=0
sum=0
for i in tag:
	x=int(i.text)
	count+=1
	sum = sum + x
print ('Count = ',count)
print ('Sum =' ,sum)

end = time.time()

print("The total excecution Time for this code is sec", (end-start))


#Output: - 
#Enter - http://py4e-data.dr-chuck.net/comments_417435.html
#Count =  50
#Sum = 2434
#The total excecution Time for this code is sec 65.42838597297668
