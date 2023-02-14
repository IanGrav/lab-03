# Lab 3
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Ian Gravallese

## Lab Question Answers

Question 1: Why are RESTful APIs scalable?

Answer for Question 1: 
One reason RESTful APIs are scalable is because they are "stateless" meaning that each request for resources from the client to the server contains all of the information necessary to complete the request, and is not reliant on any state of the client, server, or any other past requests. Another reason RESTful APIs are scalable is because they represent each resource with a unique HTTP URL identifier, meaning that resources cannot be confused, and they can easily be distributed among multiple servers, with each server holding a subset of resources. Another reason for RESTful APIs' scalability is their uniform interface, which allows for standardized interfacing between clients and servers, allowing both clients and servers to be developed independently of each other, and allowing clients to be added to a server without requiring any change to it. RESTful APIs are also scalable because they support cacheable responses, which can drastically reduce the number of requests actually made to the server, instead pulling the responses from the client-side cache.


Question 2: According to the definition of “resources” provided in the AWS article above, What are the resources the mail server is providing to clients?

Answer for Question 2:
The resources that the mail server is providing to the clients are the mail entries stored on the server, which hold strings which represent the recipient, sender, subject, body, and ID of individual emails sent to and stored on the server.


Question 3: What is one common REST Method not used in our mail server? How could
we extend our mail server to use this method?

Answer for Question 3:
One common REST method not used in our mail server is the PUT method, which would allow us to replace existing resources entirely, rather than for example DELETEing them and POSTing new ones. We could extend our mail server to use this method by defining a new function in the server to handle POST requests, which would use the provided email entry ID provided by the client (and parsed from the command line) to search for the correct email entry to replace (just like the frunction for DELETEing searches for the correct entry to delete), and then replace it with the information provided by the client (also parsed from the command line).


Question 4: Why are API keys used for many RESTful APIs? What purpose do they
serve? Make sure to cite any online resources you use to answer this question!

Answer for Question 4:
API keys are used for so many RESTful APIs to protect them from being accessed and/or abused by unauthorized users. API keys ensure that each user is authorized to be making requests of the server, and allow the server to track what users are making what requests. So basically, they are used as both a key and a tracking device for those accessing an API.

source:
https://cloud.ibm.com/docs/account?topic=account-manapikey#:~:text=An%20application%20programming%20interface%20key,or%20abuse%20of%20the%20API.
