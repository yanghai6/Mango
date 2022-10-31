URL: https://mango-app-prod.herokuapp.com/ 

*Note: Safari does not work since we require local storage to save authentication data*

**Key features:**

* **Authentication**: using Auth0

  * Login using Github or with: 
    * Username: admin@mangoapp.com
    * Password: Admin123456

  * Tabs should be hidden when not logged in
  * Protected endpoints will automatically require login. The user will be redirected to auth0 if not logged in. All endpoints other than the index (‘/’) are protected.
  
* **Use case 1**: Persona creation and prediction
  
  * Form with dropdowns to create a persona which is saved to the database
    
  * Leads to a prediction results page that predicts:
    Minimum offer value (first ML model)
    
  * Categories that the persona would be interested in (second ML model)
    Top 5 products that would be a good offer (derived from preferred categories)
    
* **Use case 2**: Dashboard
  
  * Displays the greatest changes of the categories (top 3 and bottom 3)
    
  * Lists the personas created before, links directly to the prediction results page
    
* **Use case 3**: Trends
  
  * Displays aggregate data for all information we have on transaction data on all categories
    
  * Graphs track both average amount spent and frequency of purchase
    
* **Data upload**
    
  * Allows for the upload of transaction data csv to improve the model training
    
  * Currently, this only uploads data to the database; training is not done on Heroku
