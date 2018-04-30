import time
import pandas as pd
import numpy as np
import calendar
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
    #Variable Intialization
    city_name=' '
    city=' '
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_name=input('Enter your city Name::chicago, or new york city or washington:\n')
    #Checking whether right city is entered or not
    while (city_name.strip()!='chicago' and city_name!='new york city' and city_name!='washington'):
        print('Please enter correct cityname:\n')
        city_name=input('Enter your city Name::chicago, or new york city or washington:\n')
    city=city_name
           
    # get user input for month (all, january, february, ... , june)
    month=input('Enter month to display statistics::all,January,February,....June:\n' )
    while(month!='all' and month!='January' and month!='February' and month!='March'and \
           month!='April' and month!='May' and month!='June' ):
       print('Enter Month in Text in CamelCase only between January and June')
       month=input('Enter month to display statistics::all,January,February,....June:\n' )
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('Enter day of week ::all,Monday,Tuesday,.....Sunday:\n')
    while(day!='all' and day!='Sunday' and day!='Monday' and day!='Tuesday' and day!='Wednesday'\
         and day!='Thursday' and day!='Friday' and day!='Saturday'):
       print('Enter Day in Text in CamelCase only between Sunday and Saturday:Example like::Sunday or Monday')
       day=input('Enter day of week ::all,Monday,Tuesday,.....Sunday:\n')
    print('-'*40)
    return city, month, day


def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])
    #converting starttime endtime into DateTimeFormat
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['End Time']=pd.to_datetime(df['End Time'])
    #Adding New Columns Month,Day,hour , StartStation && EndStation by time package
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.weekday_name
    df['hour']=df['Start Time'].dt.hour
    df['Start Station && End Station']=df['Start Station']+' and '+df['End Station']
    #Converting Column Month  Number into Month in text by apply by calendar package
    df['month']=df['month'].apply(lambda x: calendar.month_name[x])
    #returning dataframe based on month and Day values entered
    if month=='all' and  day=='all':
        return df
    elif month=='all' and day!='all':
        return df.loc[(df['day']==day)]
    elif month!='all' and day=='all':
        return df.loc[(df['month']==month)]
    elif month!='all' and day!='all':
        return df.loc[(df['month']==month) & (df['day']==day)]
    else:
        return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    #Variable Intialization
    com_month=' '
    com_dow=' '
    com_sh=0
    # display the most common month
    com_month=df['month'].mode()[0]
    print('most Common Month:{}\n'.format(com_month))
    # display the most common day of week
    com_dow=df['day'].mode()[0]
    print('most Common day of week:{}\n'.format(com_dow))
    # display the most common start hour
    com_sh=df['hour'].mode()[0]
    print('most Common day of start hour:{}\n'.format(com_sh))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    #Variable Intialization
    start_SS=' '
    end_SS=' '
    freq_start_end_SS=' '
    # display most commonly used start station
    start_SS=df['Start Station'].mode()[0]
    # display most commonly used end station
    print('most Common Start Station:{}\n'.format(start_SS))
    end_SS=df['End Station'].mode()[0]
    print('most Common end Station:{}\n'.format(end_SS))
    # display most frequent combination of start station and end station trip
    freq_start_end_SS=df['Start Station && End Station'].mode()[0]
    print('most Common Start Station and End Station:{}\n'.format(freq_start_end_SS))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    #Variable Intialization
    totaltraveltime=0
    meantraveltime=0
    # display total travel time
    totaltraveltime=df['Trip Duration'].sum()
    print('Total Travel Time:{}\n:'.format(totaltraveltime))

    # display mean travel time
    meantraveltime=df['Trip Duration'].mean()
    print('Total Travel Time:{}\n:'.format(meantraveltime))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    #Variable Intialization
    user_types=0
    gender_count=0
    earliest_DOB=0
    most_recent=0
    most_common=0
    # Display counts of user types
    user_types=df['User Type'].value_counts()[0]
    print('User Type Counts:{}\n:'.format(user_types))
    #print(df)
    #checking if Gender Column Exists in Dataframe
    if 'Gender' in df:
        gender_count=df['Gender'].value_counts()[0]
        # Display counts of gender
        print('Gender Type Counts:{}\n:'.format(gender_count))

    # Display earliest, most recent, and most common year of birth
    #checking if Birthyear Column Exists in Dataframe
    if 'Birth Year' in df:
        earliest_DOB=df['Birth Year'].max()
        print('Earliest DOB:{}\n:'.format(earliest_DOB))
    if 'Birth Year' in df:
        most_recent=df['Birth Year'].iloc[-1]
        print('Most Recent DOB:{}\n:'.format(most_recent))
    if 'Birth Year' in df:
        most_common=df['Birth Year'].mode()[0]
        print('Most common DOB:{}\n:'.format(most_common))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
