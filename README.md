# Fashion-Recommendation

The Clothing Item Recommender is a machine learning model that takes text descriptions of clothing items as input and provides a ranked list of links to similar items from various websites. This repository contains the necessary code and instructions to train and deploy the recommender model.

Model Overview

The recommender model is built using natural language processing (NLP) techniques and employs a combination of text embeddings and similarity matching to find similar clothing items. It leverages a pre-trained language model to encode the text descriptions into high-dimensional representations. These representations are then compared using a similarity measure to rank the similarity between items.

Getting Started

To get started with the Clothing Item Recommender, follow the instructions below.

Pre-requisites

Python 3.7 or higher
pip package manager

Prepare the Dataset

The Dataset can be prepared by web scraping. I have used parsehub web scraping tool to scrap data from amazon . I have also manually scrapped limeroad data using requests and beautiful soup.After gathering data organize your clothing item dataset into a CSV file with two columns: description and url. The description column should contain text descriptions of the clothing items, and the url column should contain the corresponding URLs to the items' websites. Ensure that the dataset has a sufficient number of examples for accurate recommendations.

