# Teyematics-task

You have 2 csv files: posts.csv and comments.csv. Perform the following tasks:
1. Create a generic function that takes in the CSV file path and do the following:
	(i) Extracts the header and creates a schema
	(ii) Creates a postgres table, and 
	(iii) write the csv data into the created table.

2. Create endpoints to: 
	(i) Add to the comments
	(ii) Search posts based on comments text (paginated)

Notes:
1. write a test suite for your code testing all cases you can think of.
2. if possible, use chalice for your API
3. write a README detailing anything you deem might be interesting to know about your implementation.

<posts.csv>
<comments.csv>

To submit, create a GitHub repository and send in the GitHub url once done with the task via email.
If you have any question, do not hesitate to ask.


# Explanation

I worked sequentially according to the steps in the task. 
I extracted the header and created a schema.
I created a script to create a postgres table and inserted the csv data into the created table.

Lastly, I couldn't create the end point due to time constraint. 