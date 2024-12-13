# Time Series

## Types
 - __Cross-sectional__ data or cross-section of a population is obtained by taking observations
from multiple individuals at the same point in time. It is noteworthy that analysis of cross-sectional data extends beyond
exploratory data analysis and visualization as shown in the preceding
example. Advanced methods such as cross-sectional regression fit a linear
regression model between several explanatory variables and a dependent
variable. For example, in case of customer churn analysis, the objective
could be to fit a logistic regression model between customer attributes and
customer behavior described by churned or not-churned. The logistic
regression model is a special case of generalized linear regression for
discrete and binary outcome. It explains the factors that make customers
churn and can predict the outcome for a new customer.


## Four main components 
    - long-term movement or trend
    - short-term movement or trend 
        - seasonal short-term movements
        - cyclic short-term movements
    - random or irregula fluctuations 

## Stationarity

__Augmented Dickey-Fuller (ADF)__ test for detecting stationarity
and describe the method of differencing for destationarizing non-stationary time series.
Differencing can remove trend and seasonal components. T


## Decomposition process
 Aimed to remove the component effects the data

_Basic properties_
    - distribution
    - mean
    - variance

_Stationarity_ means that statistical parameters of a time series do not change over time

_Basic properties_
    - distribution
    - mean
    - variance

Stationarity 
    - strong stationarity
    - weak stationarity (mean and auto-covariance function do not change over time)

Sample statistics
    - means
    - variance
    - correlation with other variables

## Importand aspects
<em>Granularity</em> level of your forecasting model. 

- The inputs and outputs of your forecasting model
- Granularity level of your forecasting model. 
> <em>Granularity</em> in time series forecasting represents the lowest detailed level of values captured for each time stamp. Granularity is related to the frequency at which time series values are collected
- Horizon of your forecasting model.
> <em>The horizon of your forecasting model</em> is the length of time into the future for which forecasts are to be prepared. These generally vary from short-term forecasting horizons (less than three months) to long-term horizons (more than two years). Short-term forecasting is usually used in short-term objectives such as material requirement planning, scheduling, and budgeting; on the other hand, long-term forecasting is usually used to predict the long-term objectives covering more than five years, such as product diversification, sales, and advertising.
- The endogenous and exogenous features of your forecasting model
> <em>Endogenous</em> and <em>exogenous</em> are economic terms to describe internal and external factors, respectively, affecting business production, efficiency, growth, and profitability. Endogenous features are input variables that have values that are determined by other variables in the system, and the output variable depends on them. <em>Exogenous</em> features are input variables that are not influenced by other variables in the system and on which the output variable depends.
<em>Exogenous</em> features:
  1. They are fixed when they enter the model.
  2. They are taken as a given in the model.
  3. They influence endogenous variables in the model.
  4. They are not determined by the model.
  5. They are not explained by the model.
- The structured or unstructured features of your forecasting model
- The univariate or multivariate nature of your forecasting model. 
> A _univariate_ data is characterized by a single variable. It does not deal with causes or relationships. Its descriptive properties can be identified in some estimates such as __central tendency__ (_mean_, _mode_, _median_), __dispersion__ (_range_, _variance_, _maximum_, _minimum_, _quartile_, and _standard deviation_), and the __frequency distributions__. The univariate data analysis is known for its limitation in the determination of relationship between two or more variables, correlations, comparisons, causes, explanations, and contingency between variables. Generally, it does not supply further information on the dependent and independent variables and, as such, is insufficient in any analysis involving more than one variable. To obtain results from such multiple indicator problems, data scientists usually use multivariate data analysis. This multivariate approach will not only help consider several characteristics in a model but will also bring to light the effect of the external variables.
- The univariate or multivariate forecasting.
> The term _univariate_ time series refers to one that consists of single observations recorded sequentially over equal time increments. Unlike other areas of statistics, the univariate time series model contains lag values of itself as independent variables. These lag variables can play the role of independent variables as in multiple regression. The _multivariate_ time series model is an extension of the univariate case and involves two or more input variables. It does not limit itself to its past information but also incorporates the past of other variables. Multivariate processes arise when several related time series are observed simultaneously over time instead of a single series being observed as in univariate case. 
- _Single-step_ or _multi-step_ structure of your forecasting model.
> Time series forecasting describes predicting the observation at the next time step. This is called a one-step forecast as only one time step is to be predicted. In contrast to the one-step forecast are the multiple-step or multi-step time series forecasting problems, where the goal is to predict a sequence of values in a time series. Many time series problems involve the task of predicting a sequence of values using only the values observed in the past.
  1. _Direct multi-step_ forecast. The direct method requires creating a separate model for each forecast time stamp. For example, in the case of predicting energy consumption for the next two hours, we would need to develop a model for forecasting energy consumption on the first hour and a separate model for forecasting energy consumption on the second hour.
  2. _Recursive multi-step_ forecast. Multi-step-ahead forecasting can be han-
dled recursively, where a single time series model is created to forecast next time stamp, and the following forecasts are then computed
using previous forecasts. 
  3. Direct-recursive hybrid multi-step forecast
  4. Mutliple output forecast.
- _Contiguous_ or _noncontiguous_ time series values of your forecasting model.
    1. Missing at random
    2. Missing completely at random
    3. Missing not at random

