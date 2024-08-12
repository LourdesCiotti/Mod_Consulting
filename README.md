## LINK TO SERVER: https://mod-consulting.onrender.com/ 


# Mod_Consulting

## Reflection Questions
## 1. Explain what you could have done better next time?
Next time, I would focus on implementing more robust checks on the code and testing it more thoroughly, ensuring that all edge cases are considered. Additionally, I would utilize more advanced Natural Language Processing (NLP) techniques to enhance the parsing of user queries, allowing for better interpretation and accuracy in the search functionality. My main focus on this task was that the whole setup, from the Backend to Frontend, to the hosting to work properly and answer the task sent over email. I would definitely improve the app.py itself.

## 2. What part of the application was the hardest to build?
The most challenging part of the application was implementing the search functionality that accurately interprets user queries and retrieves relevant movie data, I ended up with a mediocre search, given more time I would have worked with better algorithms or customized it better. Ensuring that the search algorithm can handle different input formats and expressions requires extensive testing and iteration to achieve the desired accuracy.

## 3. What part of the application was the easiest to build?
The easiest part of the application was setting up the HTML section, as I was able to find tutorials online and opted for a simple yet functional design. While this approach met my immediate needs, I recognize that further enhancements could improve the user experience and I may consider using libraries like Bootstrap in future projects to create a more polished interface with responsive design.

## 4. What took the most time to complete?
The task that took the most time was deploying the app. I decided in the first place to use PythonAnywhere, but after a few attempts I realized that for this job Render would work best, and that's what I finished using.  
Another thing that took considerable time when creating the app.py was deciding which "type of search" I wanted to focus on. I looked into: Regex, spaCy and NLTK, and pre-trained language such as GPT or BERT. I finally decided on a basic form of Natural Language Processing (NLP) by using regular expressions to parse user queries and extract key information such as release year, budget, Rotten Tomatoes score, and genre. This text parsing allows the application to interpret user intents and apply relevant filters to the movie dataset, enhancing the search functionality and demonstrating foundational NLP principles but up to a point. This can be WAY improved as it is the heart and soul of the app.
It is worth mentioning that the "sketching" of the searchable bar took also a considerable amount of time in the first place. I considered a few options such as: For Frontend: HTML/CSS and JavaScript, React, Vue.js, Angular, Bootstrap, Material UI. For Backend: Flask (Python), Express (Node.js), Django (Python). Finally, for server hosting: AWS (Elastic Beanstalk o EC2), PythonAnywhere, Vercel, Heroku, Railway, Google Cloud, Glitch.

## 5. What would you change about your application if you had more time?
If I had more time, as mentioned before I would improve the way the user prompt is ingested and analyzed. I would also enhance the user interface with better design and usability features, but in this case, I do not think is the main focus. 
