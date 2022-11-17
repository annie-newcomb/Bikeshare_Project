#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['washington', 'chicago', 'new york city']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        city = input("\nPlease enter city to analyze:").lower()
        if city in cities:
            break
        else:
            print("\n Please enter a valid city name")
    while True:
        month = input("Please enter month or enter all to see all months:").lower()
        if month in months:
            break
        else: 
            print("\n Please enter a valid month")
    while True:
        day = input("Please enter day of the week to select a day or enter all to see all data:").lower()
        if day in days:
            break
        else: print("\n Please enter a valid day")

    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('Most common month:', common_month)
    
    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    common_day = df['day_of_week'].mode()[0]
    print('Most common day:', common_day)

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    common_start_hour = df['start_hour'].mode()[0]
    print('Most common start hour:', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    df['start_station'] = df['Start Station']
    common_start_station = df['start_station'].mode()[0]
    print('Most common start station:', common_start_station)
    
    # TO DO: display most commonly used end station
    df['end_station'] = df['End Station']
    common_end_station = df['end_station'].mode()[0]
    print('Most common end station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_combo = df.groupby(['Start Station','End Station']).size().idxmax()
    print('Most frequent combination of start station and end station trip:', common_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time)
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print(user_types)
    print('\n')

    try:
        gender = df['Gender'].value_counts()
        print(gender)
        print('\n')
    except KeyError:
        print('\nThere is no gender information for this City')
    try:
        df['early_birth'] = df['Birth Year']
        early_birth = int(df['early_birth'].min())
        print('Earliest birth year:', early_birth)
    except KeyError:
        print('\n')
    try:
        df['recent_birth'] = df['Birth Year']
        recent_birth = int(df['recent_birth'].max())
        print('Most Recent birth year:', recent_birth)
    except KeyError:
        print('\n')
    try:
        df['common_birth'] = df['Birth Year']
        common_birth = int(df['common_birth'].mode()[0])
        print('Most common birth year:', common_birth)
    except KeyError:
        print('\nThere is no birth year information for this City')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
            
        
    
def raw(df):
    n = 5
    while n< (df.shape[0]):
        raw = input('\nWould you like to see raw data? Enter yes or no.\n').lower()
        if raw == 'yes':
            print(df.iloc[(n-5):n])
            n += 5
        else:
            break
        
#def raw(df):
    #i = 0
    #answ = input ('\nWould you like to see raw data? Enter yes or no.\n').lower()
    #while answ == 'yes':
    #print (df[i:].head())
    #i+=5
    #answ = input('\nWould you like more data?')
    
def main():
    #pd.set_option('display.max_columns', 25)
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw(df)   
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:




