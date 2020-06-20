#Interactive code that takes in the city and timeline of interest of the user and
#displays key statistics on most frequent times of travel, popular stations and trip duration.
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
    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city_code = input("\nWould you like to see data for Chicago - 1, New York - 2, or Washington - 3? Please type the corresponding number\n").strip()
            city_map = {'1':'chicago','2':'new york city','3':'washington'}
            city = city_map[city_code]
            break
        except:
            print("\nIncorrect Input! Please enter as prompted by the question")
    while True:
        filter_data = input("\nWould you like to filter the data by month, day, both or not at all? (Type none for no time filter)\n").strip().lower()
        if filter_data in ['month','day','both','none']:
            month = 'all'
            day = 'all'
            if filter_data == 'month':
            # TO DO: get user input for month (all, january, february, ... , june)
                while True:
                    try:
                        month_code = input("\nWhich month - Jan, Feb, Mar, Apr, May, or June?\n").strip().title()
                        month_map = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'June':6}
                        month = month_map[month_code]
                        print("\nDisplaying statistics for ",city," during the month of ",month_code,"!!")
                        break
                    except:
                        print("\nIncorrect Input! Please enter as prompted by the question")
            elif filter_data == 'day':
                # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
                while True:
                    try:
                        day_code = input("\nWhich day - Mon, Tue, Wed, Thu, Fri, Sat, or Sun?\n").strip().title()
                        day_map = {'Mon':'Monday','Tue':'Tuesday','Wed':'Wednesday','Thu':'Thursday','Fri':'Friday','Sat':'Saturday','Sun':'Sunday'}
                        day = day_map[day_code]
                        print("\nDisplaying statistics for ",city," for all",day,"s!!")
                        break
                    except:
                        print("\nIncorrect Input! Please enter as prompted by the question")
            elif filter_data == 'both':
                # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
                while True:
                    try:
                        month_code = input("\nWhich month - Jan, Feb, Mar, Apr, May, or June?\n").strip().title()
                        month_map = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'June':6}
                        month = month_map[month_code]
                        day_code = input("\nWhich day - Mon, Tue, Wed, Thu, Fri, Sat, or Sun?\n").strip().title()
                        day_map = {'Mon':'Monday','Tue':'Tuesday','Wed':'Wednesday','Thu':'Thursday','Fri':'Friday','Sat':'Saturday','Sun':'Sunday'}
                        day = day_map[day_code]
                        print("\nDisplaying statistics for ",city," during the month of ",month_code," and all ",day,"(s)!!")
                        break
                    except:
                        print("\nIncorrect Input! Please enter as prompted by the question")
            else:
                print("\nThe data has not been filtered by either month or day. Statistics will be displayed for the city of ",city)
            break
        else:
            print("\nIncorrect Input! Please enter as prompted by the question")

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most popular month is: ",most_common_month)
    # TO DO: display the most common day of week
    most_common_weekday = df['day_of_week'].mode()[0]
    print("The most popular day of week is: ",most_common_weekday)
    # TO DO: display the most common start hour
    most_common_hour = df['Start Time'].dt.hour.mode()[0]
    print("The most popular hour is: ",most_common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    print("The most popular start station is: ",df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station

    print("The most popular end station is: ",df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip

    print("The most popular trip is: (",(df['Start Station'] + '  --->  ' + df['End Station']).mode()[0],")")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    print("The total travel time (in seconds) is : ",df['Trip Duration'].sum())

    # TO DO: display mean travel time

    print("The mean travel time (in seconds) is : ",df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    print("The distribution of user types is:")
    print(df['User Type'].value_counts().to_string())

    # TO DO: Display counts of gender

    if 'Gender' in df.columns:

        print("\nThe distribution of gender type is:")
        print(df['Gender'].value_counts().to_string())

    # TO DO: Display earliest, most recent, and most common year of birth

        print("\nThe earliest year of birth is: ",int(df['Birth Year'].min()))
        print("The most recent year of birth is: ",int(df['Birth Year'].max()))
        print("The most common year of birth is: ",int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        while True:
            dis = input("Before that! Do you want to see first few rows of filtered data?(Yes or No)").strip().title()
            if dis == "Yes":
                print("\nOkay! displaying the top few rows of the filtered data set\n")
                print(df.head())
                break
            elif dis == "No":
                print("Okay proceeding to show the statistics....")
                break
            else:
                print("Incorrect input! Please enter Yes or No to the question")
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
