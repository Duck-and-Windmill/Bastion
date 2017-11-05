# PROJECT: DESTROYED LOBSTER (aka Bastion)

## Inspiration
Pretty much every company that provides a free service (Google, Facebook, etc) does so because they make money off of their users' data. Despite the services rendered, we still believe that this arrangement heavily disfavors the users. That's where Bastion comes in.

## What it does
Bastion is a suite of microservices that allow users to profit off of their own data. With the Bastion proxy server, users can hide their internet traffic from their ISP, who would sell such information to advertisers. Users can then use the Bastion browser extension to monitor their web usage and store it on our servers, where we then process the data into an easily analyzable format before selling it to advertisers. The key difference here is that through Bastion, users get a cut of profit.

After getting this data, we process it, getting the top keywords of 9 general categories of industries, to determine which type of marketer we should sell this data to. Then, we pass this data into an SVM to get a very accurate classification of general industries. Lastly, we use this general categorical data and data from the chrome extension to gauge interest in that industry, offering more detailed data alongside this overall interest as well. 

## How we built it
The proxy server was built using simple Node.js. It fetches requests from clients as if they were its own requests, and forwards the responses back to the client. The chrome extension was made with just JavaScript, and most of it is saving the data into Firebase. The machine learning and data processing is all done in Python, BeautifulSoup is used to parse data from Google searches. SKLearn is used to do classification on data, outputting the final data we want to sell to marketers.

## Challenges we ran into
Testing the proxy was annoying as we had to use two computers (setting a computer as its own proxy would create an infinite loop). Even once we were able to test it, we quickly realized that making a proxy for HTTPS was a lot harder as SSL certificates are required. However, we didn't even get to the point where certificates were an issue as requests never seemed to be acknowledged by the proxy. 

We also were not expecting to make a chrome extension, it was a last minute decision when we realized the proxy would not be able to collect all the information we wanted. 

Lastly, there are always problems when working with data, and we had to deal with a lot of trouble when converting keyword data to something that could fit into a SVM. However, we found ways to get around this with BeautifulSoup and other parsers, allowing us to create meaningful data out of search history and other dimensions. 

## Accomplishments that we're proud of
Creating a chrome extension out of the blue when we hadn't made one before was a great success. Getting the proxy to work (at least for HTTP) also felt great.

## What we learned
Making a proxy server and creating an adblocker are both far more involved than we originally assumed (as evidenced by the fact we only made one of those two, and even then we still had issues). We still firmly believe in Bastion as an idea, but now we know there's a lot more work to do.

## What's next for Bastion
To make Bastion a full-featured product, we'd need to create more infrastructure, as well as improve the current services. The proxy would need to support HTTPS, and the chrome extension would need to act as an adblocker as well as collecting more information. Both the proxy and extension would need to authenticate to our server to keep track of user data. Once that's complete we'd have a better chance of selling the data to advertisers. 

Another feature we'd like to implement, assuming Bastion got off the ground, would be to include a marketplace where users could spend their money earned on products they'd buy anyways (games, gadgets, etc), but at discount. For example, instead of transferring their money to their bank account, a user could buy a new video game at a 10% discount through the Bastion marketplace, allowing us to avoid cashing out to every user all the time.