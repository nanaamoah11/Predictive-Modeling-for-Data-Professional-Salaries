# Predictive-Modeling-for-Data-Professional-Salaries
### Overview:
This project aims to develop a machine learning model for predicting salaries of data professionals. As the demand for data-related roles continues to grow, understanding salary trends and factors influencing compensation is essential for both job seekers and employers. By leveraging machine learning techniques, we can build a predictive model that analyzes various factors such as job title, experience level, employment type, and company characteristics  to estimate salary ranges for data-related jobs.

### Data Collection: 
The project utilizes a dataset containing information on work year, job titles, experience levels, employment type, locations, remote ratio, company sizes, and corresponding salaries of data professionals.

work_year: The year the salary was paid.
experience_level: The experience level in the job during the year

employment_type: The type of employment for the role

job_title: The role worked in during the year.

salary: The total gross salary amount paid.

salary_currency: The currency of the salary paid as an ISO 4217 currency code.

salaryinusd: The salary in USD

employee_residence: Employee's primary country of residence in during the work year as an ISO 3166 country code.

remote_ratio: The overall amount of work done remotely

company_location: The country of the employer's main office or contracting branch

company_size: The scale or magnitude of the companies where the employees are employed.

### Data Preprocessing: 
The dataset is preprocessed to handle outliers, encode categorical variables, and normalize numerical features.
### Model Development: 
The project involves training and evaluating machine learning algorithms, among them decision tree regressor, to construct a precise prediction model.
### Evaluation Metrics: 
The model's performance is assessed using metrics such as mean absolute error (MAE), mean squared error (MSE).
### Deployment: 
The final trained model is deployed within a user-friendly Streamlit interface, enabling users to input their job-related information and obtain salary predictions seamlessly.

The final deployed model can be accessed via the following link : https://huggingface.co/spaces/amissah1/CareerCompensaPro

#### Contributing
Contributions to the project are welcome! Feel free to submit pull requests, suggest improvements, or report any issues you encounter.


### Contact Information
For questions or collaboration opportunities, please contact [Nana Amoah](mailto:nanaamoah776@gmail.com).

### Acknowledgements
Special thanks to [kaggle.com] for providing the dataset used in this project.


