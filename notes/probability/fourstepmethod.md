# The Four Step Method

One of the most fundamental skills in probability is determining the likelihood of a particular outcome for a clearly specified sequence of events.

In many cases, we can rigorously calculate such probabilities by following a four step approach, whoch we have taken from the text book Mathematics for Computer Science....
We will follow the book and show how these apply in the "Let's make a deal" scenario.

For the TV show,  "Let's make a deal", the contestant would see three doors. One of which would contain a prize. The player would pick a door.
The host would open one of the other two doors, showing it didn't have a prize behind it and would then ask the contestant if they wanted to change their choice.
The question we have here is whether the contestant should change their choice.  We'll follow the four steps below to come to a decision, or you can read
the text which explains each of these three steps.

## Step 1: Find the Sample Space....
Our goal is to determine the likelihood of some particular event, so the first step is to find the set of all possible events of which our events are a subset.
These events will often be describe by a sequence of choices. 
In the "Let's make a deal" example, the sample space is all possible outcomes where the prize is placed behind a door, the user picks a door, and the host opens one of the doors that doesn't contain the prize, and the player either decides to stay with their choice or to change to the other door.

For more examples consider the following: being dealt five cards from a deck of 52 cards, or being given 1000 zip codes, or tracing a path
from the root of tree down to one of its leaves.... This first step is to use the definition of the events to create a set of all possible events, the sample space, 
and to define it mathematically in a way that we can analyze it.

## Step 2: Identify events of interest.
Once we've defined the sample space, we need to clearly specify which events we are interested in... what are the events whose likelihood we want to calculate.\
For the "Let's make a deal" example, the events of interest are when the u
This might be the five card hands containing a full house, or the zip codes from regions with a majority of senior citizens, or paths in a tree of a particular length.

## Step 3: Determine outcome probabilities
For each of the possible outcomes in the sample space we need to determine how likely that particular outcome is.  We usually use our understanding of the choice made
to get that outcome to calculate the probability.

## Step 4: Compute the Event Probabilities
Once we know the probability of each outcome and we know which outcomes we are interested in, we can simply add up those probabilities to get the overall probability for
our particular kind of event.

# Examples
We will work through these examples in class to make sure you understand the readings....
* The "Mathematics for Computer Science" text goes through these four steps in detail for the "Let's make a deal" problem.
* Card games provide many examples where calculating probabilities can be helpful. For example, suppose you have been dealt three cards
  the A,2,3 of hearts, what is the probability that after being dealt two more cards you will have a three of a kind? or a straight? or a flush?
  If someone else already has 3 fours, what is the probability that you will beat them with the next two cards?
* The MIT book also has an interesting example about dice games that is quite unintuitive.


  
