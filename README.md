# Is Art a Good Reflection of its Times?

------

## By analyzing trends in the lyrics of the top 100 songs of each year since 2006, we can try to chart the fluctuations in popularity of different topics of interest.

------

### Background

I have been an avid lover of music for as long as I can remember, and looking back I can remember that in each era of music there have been several distinct events, people, and occurrences -- all of which become associated with that time. (For example, the OJ Simpson would likely be most associated with the dates of the trial in 1995 and not for his football career.)

Also, going back and watching some of my favorite old TV Shows like Friends and Fresh Prince of Bel-Air, I noticed that the each era had its own style, mood, and jokes. While, for the most part, every TV show has had staying power thanks to its relatability, there would always be one or two jokes or references per season that I just simply did not understand. 

This project has emerged from being a consumer of the arts as well as a programmer by trade. As the landscapes shifted, I realized that I could quantitatively see just how much I was missing out. Were the topics in those jokes really as popular as they seemed? (See: https://www.buzzfeed.com/jenniferabidor/friends-references-that-taught-people-some-brand-new)

To start with, I wanted to see if the references made in the top 100 song lyrics of each year would match up with the overall trends of the internet.

### Data

Lyrics: Using Beautiful Soup, I scraped all the available year-end hot 100 lists for song titles and artist information. Then I used the LyricsGenius package for Python to query the songs on genius.com (Note: Before I found the LyricsGenius client, I tried a more crude method of querying the Genius API using the `module`. This method can be found in `thrutheyears-web-genius-scrape.ipynb`)

Trends: To check whether the data I got matches 'true' popularity metrics, I will likely use Google Trends data. Graphing the top references from the lyrics and their usage rates in time alongside that on google trends should give effective for comparison.

### Preparation

I used SpaCy to prepare and evaluate the tokens in the data. Mainly, for this project, I focused on the Entities. After much transformation and data cleaning, some graphs of the frequency of the top terms in each category (nouns, adverbs, entities, verbs, words) data can be seen.

### Further Exploration

Indeed, my analysis of popular references in song lyrics is not yet done, however, I have some ideas on where this exploration could continue to. 

With each era in time, I hypothesize that there are resounding themes in music. For example, the themes in the music of the 50s may be different to the themes of the music in the 1960s and 70s when the Apollo Missions were inspiring the nation. Sentiment analysis through time could be graphed along side the economic or cultural movements to see if there is any correlation. 





