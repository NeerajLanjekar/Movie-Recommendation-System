# Movie-Recommendation-System
This project report presents the design, implementation, and evaluation of a movie
recommendation system using collaborative filtering and content-based filtering techniques
with a search box. The goal of the system is to provide personalized movie
recommendations to users based on their preferences and selected movies. The project
incorporates a dataset of movies, collaborative filtering algorithms, and external APIs to fetch
additional movie details and posters. The experimental results demonstrate the effectiveness
of the system in generating accurate and diverse recommendations.

## Objective
The objective of the Movie Recommendation System is to provide personalized movie recommendations to users based on their preferences and selected movies with a good accuracy and efficiency. 

## Prerequisites
Python 3.7 or higher
pickle library
streamlit library
pandas library
requests library

All the prerequsites are provided in the "requirement.txt" file. Run following command to install mentioned versions of libraries in the machine (Provided the names and their respective required verisons in the "requirements.txt" file).

$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt 

## Usage
1. Download all the files provided in the drive link.
2. Run following command to install mentioned versions of libraries in the machine (Provided the names and their respective required verisons in the "requirements.txt" file).

	$ pip install -r requirements.txt 
	
3.Run the following command on the terminal opened in the same directory which is having the "app.py" file :
	
	$ streamlit run app.py
	
4. WebApp will be opened on your default browser.
5. There are 3 fields : 
	1st Recommends 5 movies based on Content Filtering
		1.Select/type the name of the Movie from the dropdown list which you like the most.
		2.Press the button "Show Recommendation".
		3.It will show the top 5 movie recommendation based on your selected movie.
	2nd Searches the movies 
		1. Type anything regarding a movie such as movie's title, genre, actors, directors, keywords, etc.
		2. Pressing enter will show you all the movies present in the dataset which matches to your searched query.
	3rd Recommends 20 top movies based on Collaborative Filtering
		1. Select any movies from the dropdown list or type the name of the movies.
		2. you can select many movies which you absolutly like. (those movies which you can give 5 stars ratings)
		3. Press the button "Show Recommendation".
		4. This will recommend 20 movies that you might like.
	All the movies will be shown with the title and their posters.	
   Like this You can interact with the movie recommendation system through the web interface.

## Challanges

Handling unknown users or cold start problem : how to deal with the new movies or users added in the datasets. Because we dont have enough information about the specific movie or users to recommend.
Data sparcity.
Scalability : In this project We have used few MBs of dataset, but in real world we might have few GBs of datasets to work with. So we should address this problem of scalability.
Dynamic Updates : We have already built this model, now if we want to add/remove some items then we have to rebuild this whole model


## Future work and Improvements

Incorporate User Feedback: Implement a mechanism to collect and incorporate user feedback on recommended movies. This can help improve the accuracy and relevance of future recommendations.

Hybrid Recommendation Approach: We can work on integration of collaborative filtering and content-based filtering techniques to create a hybrid recommendation approach. This can potentially provide more diverse and accurate recommendations by leveraging the strengths of both approaches.

Expand Movie Dataset: We can Continuously update and expand the movie dataset with more recent and diverse movies to ensure the system can recommend a wide range of options to users.

Social Integration: We can Integrate social media platforms to allow users to share their recommended movies or see recommendations from their friends. This can enhance the social aspect of the system and provide a more interactive experience.

Evaluate and Optimize Performance: We can Conduct rigorous performance evaluations of the recommendation system by collecting user feedback and measuring metrics like recommendation accuracy, diversity, and novelty.
