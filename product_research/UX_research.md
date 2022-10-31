## Scenarios presented
- You already have a successful offer and want to see the changes after the offer in order to design a new offer.
- You want to learn more about a particular persona
- You want to further refine your predictions, catering to your own customers.
## Questions
### Dashboard page
- You already have a successful offer and want to see the changes after the offer in order to design a new offer.
    - Can you tell me what has changed recently and what’s the interesting change to you?
    - Can you tell me historical data on what change happened?

### Detailed trends page:
- Can you tell me more information about the groceries?
- What can you tell me regarding what is shown to you on the page?
- Were you able to navigate your way to a particular persona?

### Persona Page:
- Do you understand the data shown and the context behind them?
- Can you tell me more about this particular persona?
- Can you give me your opinion on whether this persona is interesting enough to pursue your offer formulation with?
- Are you able to make a decision on who and what offer to take on?

### At every page:
- How do you feel about the format of things being shown here?

## Overview of people interviewed
- Umar, UX designer. Collaborated with financial institutions in his ventures. Has some insights into the “bank’s mindset”.
- Julian, senior developer and instructor. Possess a lot of experience with UX and accessibility support.
## Raw Notes
### Umar
#### Dashboard

- Attention first drawn to the big numbers but don’t understand what context they are in
- Did not see the “Today” or “Sorting” dropdowns
- Looking for units / what its relative to
- The dropdown arrow is too small, didn’t realize it was a drop down until prompted
- Usually sites have a sorting and filter
- Assuming the Persona dropdown is the filter, unintuitive
- Hard to see that Dashboard card is clickable, suggests making it more obvious with a visual indicator (either animating/changing color/elevate/etc on hover)

#### Trends Page
- The labels “Graph” and “Persona” are not clear as to what they are. 
- Expected that the Persona tab would show cards.
- Understands that the bar below allows changing the time
- It is unclear what the “match” percentage means
- Misunderstanding the colour matching of the graph to the persona
- Through the workflow, Dashboard -> Trends -> Persona is unexpected, since the Persona page is an overview instead of being related to the Category. 

#### Persona Page
- Unclear exactly what the percentages are for
- Unclear what the bars for each category since they don’t reflect the percentages
- Confused about what “Compared to last view” means. Maybe add whenlast view was. 
- Don’t have a baseline to compare the numbers to. Which increases and decreases are significant? Doesn’t know the original value. 
- Doubts how useful the view is in general. Don’t know what it was before or the baseline. 
- The bars draw the most attention and are confusing what they are for. Possibly change the colour of the entire bar to be either green or red or just the segment that increased/decreased. 

#### Train Page
Think the order of “Upload data” and the “S3 Link” is wrong. It is confusing whether you should click “Upload” first or enter “S3 Link” first. 
It is not apparent what we are training.
No idea what “matches format” means.

#### General opinion
The “Today” view on the Dashboard is not significant to make the decision for the offer. Mainly looking at “Past month” and “Past year to date”. Everything else is kind of useless. The values for “Today” and “Past week” are subject to change that is not viable for promoting a product. If it was offering a prediction, it would be more applicable in shorter timespans. Don’t think spending habits have volatility. 
It is important to convey to the user whether a number is a statistic and what is a prediction from the machine learning model. 
If there was a prediction anywhere, would expect to be in the train tab or part of the trends tab

### Julian
#### Dashboard
- Want to see different things on the dashboard correlated to each other
- Didn’t realize that you could change the time frame
- It isn’t clear what the Persona is and why it is there
- Banks want to be able to segment their own market / customize their own persona
- 2% seems statistically insignificant to put on the dashboard (unnecessary information to have)
- It isn’t clear that the cards are clickable, intuitively thought that they were not. 

#### Trends Page
- Color of graphs could be hard to see so choose pallet carefully
- Graphs could be included with patterns to separate them
- Intuitive to change timeline
- It was unclear what the Persona tab meant
- He thought that the colors corresponded to each persona

#### Personas Page
- Again, the cards do not look like they are clickable
- Again, the numbers that are shown are insignificant, do not provide a lot of insights, and are not explainable. 
- Having a recommendation would be more interesting as opposed to displaying data that are insignificant
- No frame of reference
- Should make model do the work instead of the user

#### Training Page
- What is the format, Is there a way to validate prior to uploading or do you have to continuously upload the file to check. 
- It is unclear what the S3 link is for
- Most companies would not just give you a S3 link

## Summarizes Notes
- It was unclear which parts of the UI/UX were interactable, making them unintutive to use
- Oftentimes the user would attempt to make sense of the graph being shown and connect it to a particular meaning, as it had colors on them.
- The data presented lacks context and/or a baseline to compare to, making it unclear of its significance. 
- Some workflows should be more related as the user drills on to a particular flow.
- It was unclear that a machine learning model was involved, which should be conveyed much better and clearly separates real statistics from predictions. The only indicator of this was the “Train” tab/page, which the user would see much later and would be confused about what was being trained. 
- Generally, it was unclear exactly what the personas are for and what the percentages next to them meant. 
- In the Personas Page, the bars need to be changed: both interviewees thought the bars were supposed to be like bar graphs, changing based on the percentage next to it. 
- The most relevant data that banks would like to see is trends from the past month or year to date. In making an offer, considering just today’s or last week’s trends is too volatile. We should make sure the most important information is displayed first. 

## Copy of Prototype
[Figma](https://www.figma.com/file/0Zo52kMh5stWS6g2PQzL4q/Mango?node-id=0%3A1)

## Updated roadmap
[Roadmap](./roadmap.md)

What has changed:
Can put more research into accessibilities and being more intuitive as a whole. More UX interviews on a bi-weekly basis to continuously refine the UI.
Redesign Persona page. Adding tooltips for internal jargon would be helpful. 
More research into data models and formatting that builds the pre-trained model and provides a guideline for further training and refinement.
A service/way to validate customer data prior to refining the model.
A way to upload massive files for the model to train on that is effortless.

Explanation:
While our previous roadmap was focused alot on feature developments, we were lacking on the user experience side of things and especially frontend formulation. Our interviews with Umar and Julian clearly shown us that while the features might be fascinating to attain and use, if the website isn’t polished and intuitive it’s meaningless. 


