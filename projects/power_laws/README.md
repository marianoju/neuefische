# Power Laws: Cold Start Energy Forecasting

Hosted By DrivenData 

# Power Laws: Cold Start Energy Forecasting <small>Hosted By DrivenData</small>

*   [Home](/competitions/55/schneider-cold-start/page/110/)
*   [Problem Description](/competitions/55/schneider-cold-start/page/111/)

[Leaderboard](/competitions/55/schneider-cold-start/leaderboard/)  

[Data Download](/competitions/55/schneider-cold-start/data/) [Submissions](/competitions/55/schneider-cold-start/submissions/) [Team](/competitions/55/schneider-cold-start/team/)  

[Discussion <span class="badge" id="unread_forum_count"></span>](https://community.drivendata.org/c/cold-start-energy-forecast)[Official Rules](/competitions/55/schneider-cold-start/rules/)</div>

* * *

## Problem description

The objective of this competition is to forecast energy consumption from varying amounts of "cold start" data, and little other building information. That means that for each building in the test set you are given a small amount of data and then asked to predict into the future. Since this format of test data is a bit unusual, we'll give an overview here, with more detail below. Here is a visual represenation of the data setup for this problem:

![train test timing](https://s3.amazonaws.com/drivendata-public-assets/mlscheme.png)

The test data includes:

*   `cold_start_test.csv` - Cold start measurements of building consumption data (in watt-hours) and temperature. The cold start data is provided at an hourly time step over a period of anywhere from 1 day to 2 weeks. For example, if 2 days of cold start data are provided for `series_id` A, then you will have 24 * 2 = 48 consumption measurements to get your prediction started. If 2 weeks of cold start data is provided for `series_id` B, then you will have 24 * 7 * 2 = 336 consumption measurements to get your prediction started. Cold start data only comes in full days, e.g., there is no site with 2.5 days worth of cold start data, but there are sites with 1 day, 2 days, 3 days, etc., up to 14 days.
*   `submission_format.csv` - This provides the structure your predictions need to satisfy to be evaluated successfully. You will have `series_id` and `timestamp` columns to help you check that your predictions take place over the correct window. Note that the `series_id` is not a unique index, but `series_id` together with `timestamp` is unique (no timestamp appears twice in the same series). Additionally, there is the `consumption` column where your hourly, daily, or weekly predictions will go. The submission format also includes measured average temperatures for each prediction in the `temperature` column. Finally, we include a `prediction_window` column to help indicate what level of temporal aggregation we want you to predict.

As we'll cover below, limited additional meta data about each building in the test set is provided in `meta.csv`. Additionally, large amounts of consumption data for other sites is provided in `consumption_train.csv`.

*   **The Data**
*   [Overview](#features_list)
*   [Datasets](#datasets)


*   **Evaluation**
*   [Metric](#metric)
*   [Format](#format)


## Overview

* * *

Three time horizons for predictions are distinguished. The goal is either:

*   To forecast the consumption for each hour for a day (24 predictions).
*   To forecast the consumption for each day for a week (7 predictions).
*   To forecast the consumption for each week for two weeks (2 predictions).

In the test set, varying amounts of historical consumption and temperature data are given for each series, ranging from 1 day to 2 weeks. The temperature data may contain a small portion of wrong / missing values.

In the training set, 4 week series of hourly consumption and temperature data are provided. These series can be used to create different cold start regimes (varying amounts of provided data and prediction resolutions) for local training and testing.

Basic building information such as suface area, base temperature, and on/off days are given for each series in the training and test sets.


## Datasets

### Historical Consumption

Time series data of consumption and temperature data identified by their `series_id`.

`consumption_train.csv`

*   `series_id` - An ID number for the time series, matches across datasets
*   `timestamp` - The time of the measurement
*   `consumption` - Consumption (watt-hours) since the last measurement
*   `temperature` - Temperature (Celsius) during measurement, some values missing

### Building Metadata

Additional information about the included buildings in the train and test set.

`meta.csv`

*   `series_id` - An ID number for the time series, matches across datasets
*   `surface` - The surface area of the building (ordinal)
*   `base_temperature` - The base temperature for the building (ordinal)
*   `monday_is_day_off` - Whether or not the building is operational this day
*   `tuesday_is_day_off` - Whether or not the building is operational this day
*   `wednesday_is_day_off` - Whether or not the building is operational this day
*   `thursday_is_day_off` - Whether or not the building is operational this day
*   `friday_is_day_off` - Whether or not the building is operational this day
*   `saturday_is_day_off` - Whether or not the building is operational this day
*   `sunday_is_day_off` - Whether or not the building is operational this day

### Cold Start Test Data

Test data used to start a forecast. Includes metadata about prediction window as well as time series data on consumption.

`cold_start_test.csv`

*   `series_id` - An ID number for the time series, matches across datasets
*   `timestamp` - The time of the measurement
*   `consumption` - Consumption (watt-hours) since the last measurement
*   `temperature` - Temperature (Celsius) during measurement, some values missing


## Performance metric

* * *

The performance metric is a normalized version of mean absolute error. The normalization coefficient |$c_{i}$| for the |$i^{\text{th}}$| prediction is composed of a ratio of two numbers,

$ c_i = \frac{w_i}{m_i} $

where |$w_i$| is a weight that makes weekly (24 / 2), daily (24 / 7), and hourly (24 / 24) predictions equally important, and |$m_i$| is the true mean consumption over the prediction window under consideration (this mean is unknown to competitors). Multiplying predictions by **this coefficient makes each prediction equally important** and puts hourly, daily, and weekly predictions on the same scale.

Given the above definition, the metric |$NMAE$| is

$ NMAE = \frac{1}{N} \sum_{i=1}^{N}|\hat{y_i} - y_i|c_i $

*   |$N$| - The total number of consumption predictions submitted, including all hourly, daily, and weekly predictions
*   |$\hat{y}$| - The predicted consumption value
*   |$y$| - The actual consumption value
*   |$c$| - The normalization coefficient that weights and scales each prediction to have the same impact on the metric


## Submission format

* * *

The submission format is such that `series_id` together with `timestamp` is unique (no timestamp appears twice in the same series). We have provided the index `pred_id` for simplicity. Additionally, there is the `consumption` column where your hourly, daily, or weekly predictions will go. The `temperature` column reports the average temperature for that time period. The `prediction_window` column includes how often predictions need to be made (can be inferred from the timestamps).

<div class="well">For example, if you predicted...

<table class="table">

<thead>

<tr style="text-align: right;">

<th></th>

<th>series_id</th>

<th>timestamp</th>

<th>temperature</th>

<th>consumption</th>

<th>prediction_window</th>

</tr>

<tr>

<th>pred_id</th>

<th></th>

<th></th>

<th></th>

<th></th>

<th></th>

</tr>

</thead>

<tbody>

<tr>

<th>0</th>

<td>102781</td>

<td>2013-03-03 00:00:00</td>

<td>19.931250</td>

<td>0</td>

<td>daily</td>

</tr>

<tr>

<th>1</th>

<td>102781</td>

<td>2013-03-04 00:00:00</td>

<td>20.034375</td>

<td>0</td>

<td>daily</td>

</tr>

<tr>

<th>2</th>

<td>102781</td>

<td>2013-03-05 00:00:00</td>

<td>19.189583</td>

<td>0</td>

<td>daily</td>

</tr>

<tr>

<th>3</th>

<td>102781</td>

<td>2013-03-06 00:00:00</td>

<td>18.397917</td>

<td>0</td>

<td>daily</td>

</tr>

<tr>

<th>4</th>

<td>102781</td>

<td>2013-03-07 00:00:00</td>

<td>20.762500</td>

<td>0</td>

<td>daily</td>

</tr>

</tbody>

</table>

</div>

Your `.csv` file that you submit would look like:

    pred_id,series_id,timestamp,temperature,consumption,prediction_window
    0,102781,2013-03-03 00:00:00,19.931250000000002,0,daily
    1,102781,2013-03-04 00:00:00,20.034375,0,daily
    2,102781,2013-03-05 00:00:00,19.189583333333335,0,daily
    3,102781,2013-03-06 00:00:00,18.397916666666667,0,daily
    4,102781,2013-03-07 00:00:00,20.7625,0,daily


## Good luck!

* * *

Good luck and enjoy this problem! If you have any questions you can always visit the [user forum](http://community.drivendata.org/)!


## Data

File | Description
-----|------------
Cold Start Test Data | Cold start lead-in periods for the series that appear in the submission format.
Building Metadata | Information about the series that are available to competitors.
Training Data | Historical series that can be used as training data.
Submission Format | This is the format for submssions to the competition. Your submissions must match the columns and indices exactly.


