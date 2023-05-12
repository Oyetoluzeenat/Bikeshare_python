import time
import datetime as dat
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

CITY_DATA={'chicago':'chicago.csv', 'new york city':'new_york_city.csv', 'washington':'washington.csv'}


def get_filters():
    """
    Greetings
    Ask user to specify a city, month and day to analyze
    Returns:
    (str) city - name of the city to analyze
    (str) month - name of the month to filter by, or "all" to apply no month filter
    (str) day -  name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nWelcome to ZIYTECHS Program')
    print('Let\'s explore some US bikeshare data! \n\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city_ref = int(input('What city would you like to get insight on? Available cities are chicago, new york city and washington.\n\npress 1  for chicago\npress 2 for new york city\npress 3 for washington\n\n'))

            city_list = ('chicago', 'new york city', 'washington')

        except Exception as e:
            print('\nPlease check your input!,\n Exception Occurred: {}, \n\n we don\'t have that city on our database\n\n'.format(e))

        else:
            city = city_list[(city_ref - 1)]
            break
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('\n\nWhat month would you be interested in, months available are:- January, February, March, April, May, June? \ninput "ALL" if you prefer to see for all available months: \n\n').lower()
            assert month in ('all', 'january', 'february', 'march', 'april', 'may', 'june')
            break

        except Exception as e:
            print('Please check your input!,\n Exception Occurred: {}, \n\n You could have misspelt something or no data for selected month\n\n'.format(e))

     # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('\n\nWhat day of the week are you interested in (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday)? \ninput "ALL" if you prefer to see for all days: \n\n').title()
            assert day in ('All', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
            break

        except Exception as e:
            print('Please check your input!,\n Exception Occurred: {}, \n\n You could have misspelt something\n\n'.format(e))

    print('-'*60 + '\n')
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
    print('\n' + '.'*20 + 'retrieving data\n')

    df = pd.read_csv(CITY_DATA[str(city)])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(str(month)) + 1

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == str(day)]

    print('\nData Retrieved!!!\n')
    # Ask if user would like to preview data
    while True:
        try:
            preview = input('\nWould you like to preview the raw data? Enter yes or no.\n').lower()
            break
        except:
            print('oops!!!, check your input and try again\n')

    if preview == 'yes':
        print('\n','.'*10 + "loading city data\n")
        print('\n\n', df.head(), '\n')

        # Ask if user would like to view more raw data and in how many steps
        while True:
            try:
                preview_more = input('\nWould you like to preview more raw data? Enter yes or no.\n').lower()
                start_index = 5
                break
            except:
                print('\noops!!!, check your input and try again\n')

        if preview_more == 'yes':
            while len(df)-1 >= start_index+10:
                while True:
                    try:
                        steps = int(input('How many more rows would you like to see? (number from 1 - 10): \n'))
                        assert steps in range(11)
                        break
                    except:
                        print('\noops!!!, check your input and try again\n')

                print('\n','.'*10 + "loading {} more rows of city data\n".format(steps))
                print('\n', df.iloc[(start_index + 1):(start_index + 1 +steps)], '\n')
                start_index += steps

                #ask if user would like to view more
                while True:
                    try:
                        see_more = input('\nWould you like to preview more raw data? Enter yes or no.\n').lower()
                        break
                    except:
                        print('\noops!!!, check your input and try again\n')

                if see_more != 'yes':
                    print('\n\nAlright then, let\'s have a fun experience exploring your selected data.\n')
                    break

    else:
        print('\n\nAlright then, let\'s have a fun experience exploring your selected data.\n')
    return df

def time_stats(df, city, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    if 'Start Time' and 'End Time' and 'month' and 'day_of_week' in set(df.columns):
        # TO DO: display the most common month
        if month == 'all':
            most_common_month = df['month'].mode()
            print('\nThe most common month(s) for City: {}, Month: {}, Day: {} is:\n'.format(city,month,day))
            for value in most_common_month.values:
                print(value)

        # TO DO: display the most common day of week
        if day == 'All':
            most_common_dow = df['day_of_week'].mode()
            print('\nThe most common day(s) of the week for City: {}, Month: {}, Day: {} is:\n'.format(city,month,day))
            for value in most_common_dow.values:
                print(value)

        # TO DO: display the most common start hour
        df['start hour'] = df['Start Time'].dt.hour
        most_common_start_hour = df['start hour'].mode()
        print('\nThe most common start hour(s) for City: {}, Month: {}, Day: {} is:\n'.format(city,month,day))
        for value in most_common_start_hour.values:
            print(value, '(00)hrs')

        # TO DO: display the most common end hour
        df['end hour'] = pd.to_datetime(df['End Time']).dt.hour
        most_common_end_hour = df['end hour'].mode()
        print('\nThe most common end hour(s) for City: {}, Month: {}, Day: {} is:\n'.format(city,month,day))
        for value in most_common_end_hour.values:
            print(value, '(00)hrs')

        # display a count for total number of completed trips
        trip_count = df['end hour'].count()
        print('\nThe total number of trips for City: {}, Month: {}, Day: {} is:\n{} {}'.format(city,month,day,trip_count,'Trip(s)'))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df, city, month, day):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    if 'Start Station' in set(df.columns):
        common_start_station = df['Start Station'].mode()
        print('\nThe most commonly used start station(s) for City: {}, Month: {}, Day: {} is:\n'.format(city,month,day))
        for value in  common_start_station.values:
            print(value)

    # TO DO: display most commonly used end station
    if 'End Station' in set(df.columns):
        common_end_station = df['End Station'].mode()
        print('\nThe most commonly used end station(s) for City: {}, Month: {}, Day: {} is:\n'.format(city,month,day))
        for value in common_end_station.values:
            print(value)

    # TO DO: display most frequent combination of start station and end station trip
    if 'Start Station' in set(df.columns) and 'End Station' in set(df.columns):
        df['Trip Combination'] = df['Start Station'] + ' ' + 'to' + ' ' + df['End Station']
        most_common_trip = df['Trip Combination'].mode()
        print('\nThe most frequent trip(s) for City: {}, Month: {}, Day: {} is:\n'.format(city,month,day))
        for value in most_common_trip.values:
            print(value)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df, city, month, day):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Trip Duration'] = df['Trip Duration'].astype(float)
    if 'Trip Duration' in set(df.columns):
        total_travel_time = df['Trip Duration'].sum()
        print('\nThe total travel time for City: {}, Month: {}, Day: {} is:\n{} {}'.format(city,month,day,total_travel_time,'Seconds'))

    # TO DO: display mean travel time
        mean_travel_time = np.mean(df['Trip Duration'])
        print('\nThe mean travel time for City: {}, Month: {}, Day: {} is:\n{} {}'.format(city,month,day,mean_travel_time,'Seconds'))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city, month, day):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in set(df.columns):

        #Fill the empty 'Birth Year' rows with the content of the cell above
        df['User Type'] = df['User Type'].fillna(method='ffill')

        user_type_count = df['User Type'].value_counts()
        print('\nThe User type Count for City: {}, Month: {}, Day: {} is:\n'.format(city,month,day),user_type_count)

    # TO DO: Display counts of gender
    if 'Gender' in set(df.columns):

        #Fill the empty 'Gender' rows with the content of the cell above
        df['Gender'] = df['Gender'].fillna(method='ffill')

        gender_count = df['Gender'].value_counts()
        print('\nThe Gender Count for City: {}, Month: {}, Day: {} is:\n'.format(city,month,day),gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in set(df.columns):

        #Fill the empty 'Birth Year' rows with the content of the cell above
        df['Birth Year'] = df['Birth Year'].fillna(method='ffill')

        earliest_yob = int(df['Birth Year'].min())
        print('\nThe earliest year of birth of users for City: {}, Month: {}, Day: {} is:\n'.format(city,month,day),earliest_yob)

        most_recent_yob = int(df['Birth Year'].max())
        print('\nThe most recent year of birth of users for City: {}, Month: {}, Day: {} is:\n'.format(city,month,day),most_recent_yob)

        most_common_yob = df['Birth Year'].mode()
        print('\nThe most common year(s) of birth of users for City: {}, Month: {}, Day: {} is:\n'.format(city,month,day))
        for value in most_common_yob.values:
            print(int(value))

    # Display age range distribution of users
    # The code block below was gotten from defltstack.com literature and modified to access current year
    current_DateTime = dat.datetime.now()
    current_date = current_DateTime.date()
    current_year = int(current_date.strftime("%Y"))

    # create new column to label age class distribution
    if 'Birth Year' in df.columns:
        #create a new column for age class
        df['Age Class'] = df['Birth Year'].copy()

        #create list of index where class is true
        #idx_Babies = (np.where(2019 <= df['Birth Year'].values() < 2022))
        #idx_Children = (np.where(2005 <= df['Birth Year'].values() < 2019))
        #idx_Young_Adults = (np.where(1991 <= df['Birth Year'].values() < 2005))
        #idx_Middle_aged_Adults = (np.where(1976 <= df['Birth Year'].values() < 1991))
        #idx_Old_Adults = np.where(df['Age Class'].values > 1976)[0]

        # create dictionary for age class. Age class as Key and list label as value
        #age_class_dict = {'Babies':idx_Babies, 'Children':idx_Children, 'Young_Adults':idx_Young_Adults, 'Middle_aged_Youths':idx_Middle_aged_Adults, 'Old_Adults':idx_Old_Adults}
        #age_class_dict = {'Old Adults':idx_Old_Adults}

        # modify age class column to labels for age class
        for row in df.itertuples():
            i = row.Index
            if (current_year-2)<=df.loc[i,'Birth Year'] and df.loc[i,'Birth Year']<(current_year + 1):
                df.loc[i, 'Age Class'] = 'Babies (0-2yrs)'
            elif (current_year - 16)<=df.loc[i,'Birth Year'] and df.loc[i,'Birth Year']<(current_year - 2):
                df.loc[i, 'Age Class'] = 'Children (3-16yrs)'
            elif (current_year - 30)<=df.loc[i,'Birth Year'] and df.loc[i,'Birth Year']<(current_year - 16):
                df.loc[i, 'Age Class'] = 'Young Adults (17-30yrs)'
            elif (current_year - 45)<=df.loc[i,'Birth Year'] and df.loc[i,'Birth Year']<(current_year - 30):
                df.loc[i, 'Age Class'] = 'Middle aged Adults (31-45yrs)'
            else:
                df.loc[i, 'Age Class'] = 'Old Adults (above 45yrs)'


        # get count of distinct values in age class column
        age_dist_count = df['Age Class'].value_counts()
        print('\nThe age demographic for City: {}, Month: {}, Day: {} is:\n'.format(city,month,day),age_dist_count)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def plot(df, rows=3, cols=2, dashboard_size=(20,10)):

    #Create figure and subplots for the Dasboard. The code below is a sample dashboard config that can take 6 plots in a 3 rows by 2 columns arrangement
    fig, axs = plt.subplots(4, 2, figsize=(20, 16), layout = 'constrained', facecolor='#fafafa')

    # set the dashboard default edge color 
    plt.rcParams['axes.edgecolor'] = 'none'

    # set the dashboard default color cycle 
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#e8cccc'])

    #Key Performance Indicators for overall performance
    df = df.assign(col=['KPI']*len(df), inplace=True)

    # create pivot tables
    pivot1 = pd.pivot_table(df, values='end hour', index=None, columns='col', aggfunc=len)
    pivot2 = pd.pivot_table(df, values='Trip Duration', index=None, columns='col', aggfunc=sum)
    pivot3 = pd.pivot_table(df, values='Trip Duration', index=None, columns='col', aggfunc=np.mean)
 

   # Key Performance Indicators
    kpis = [axs[0, 1].table(cellText=pivot1.values.round(), colLabels=['Total Trip count'], loc='left', cellLoc='center'),
        axs[0, 0].table(cellText=pivot2.values.round(),colLabels=['Total Trip Duration(sec)'], loc='center', cellLoc='center'),
        axs[0, 1].table(cellText=pivot3.values.round(), colLabels=['Avg Trip Duration (sec)'], loc='center', cellLoc='center'),
        ]

    #PLOT1 SUBSCRIBER VERSUS CUSTOMER
    
    #Plot 1 - Count of User Type and Gender
    if 'Gender' in set(df.columns):
        sb.countplot(data=df, x='User Type', hue = "Gender", ax=axs[1,0], palette = ["#8e0201", "#e8cccc"]).set(title = "User Type and Gender")
        #Plot 2 - Gender Distribution 
        gender_val = df["Gender"].value_counts()
        color = ["#8e0201", "#e8cccc"]
        axs[1,1].pie(gender_val, labels=gender_val.index, colors = color)
        axs[1,1].set_title("Gender Distribution")
        axs[1,1].set_facecolor = "red" 

    else:
        sb.countplot(data=df, x='User Type', ax=axs[1,0], palette = ["#8e0201", "#e8cccc"]).set(title = "User Type Distribution")
        user_val = df['User Type'].value_counts()
        #Plot 2 - User Type Distribution
        color = ["#8e0201", "#e8cccc"]
        axs[1,1].pie(user_val, labels=user_val.index, colors = color)
        axs[1,1].set_title("Gender Distribution")
        axs[1,1].set_facecolor = "red" 

    #Plot 3 - Chart of months by trip duration
    month_val = df.groupby('month')['Trip Duration'].sum().sort_values(ascending=True).head(6)
    plt3 = month_val.iloc[:5].plot(kind = "barh", legend = False, ax=axs[2,0])
    plt3.set_title("Month by Trip Duration")
    plt3.patches[3].set_facecolor("#8e0201")

    #Plot 4 - Chart of day_of_week by trip duration
    day_of_week_val = df.groupby('day_of_week')['Trip Duration'].sum().sort_values(ascending=True).head(6)
    plt4 =day_of_week_val.iloc[:5].plot(kind = "barh", legend = False, ax=axs[2,1])
    plt4.set_title("Day of Week by Trip Duration")
    plt4.patches[3].set_facecolor("#8e0201")

    #Plot 5 - Start and End Time
    plot5 = sb.regplot(data=df, x='start hour', y = 'end hour', ax=axs[3,0], scatter_kws={"color":"#8e0201"}, line_kws= {"color":"#e8cccc"} ).set(title = "Start and End Time")
     
    #Plot 6 - Most Common Start Station
    start_staion_val = df.groupby('Start Station')['Trip Duration'].sum().sort_values(ascending=True).head(6)
    plt6 = start_staion_val[:5].plot(kind = "barh", legend = False, ax=axs[3,1])
    plt6.set_title("Most Common Start Station")
    plt6.patches[4].set_facecolor('#8e0201')

    #Remove background colour for all rows, set font size and scaling of tables, remove table borders
    for kpi in kpis:
        kpi.set_fontsize (18)
        kpi.scale(0.3,3)
        for cell in kpi._cells:
            kpi._cells[cell].set_linewidth(0)
            kpi._cells[cell].set_color('none')
            if cell == (0,0):
                kpi._cells[cell].set_text_props(color='#8e0201')

    #Remove axis for first row
    axs[0,0].axis('off')
    axs[0,1].axis('off')

    #Add oversll title to the dashboard
    fig.suptitle('BIKESHARE COMPANY DASHBOARD', fontsize = 20)

    #Display dashboard
    plt.show()

def main():
     while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)    
        ''' 
        The next four lines of code does a quick statistical summary of the data.
        You should modify the print statements in their functions above to make the print happen inside the dashboard 
        You should also carry out your own exploratory data analysis to produce insightful charts that can be plotted in the dashboard
        '''
        while True:
            time_stats(df, city, month, day)
            station_stats(df, city, month, day)
            trip_duration_stats(df, city, month, day)
            user_stats(df, city, month, day)
            plot(df)

            see_another_stat = input('\nWould you like to see another statistics? Enter yes or no.\n')
            if see_another_stat.lower() != 'yes':
                break

        restart = input('\nWould you like to restart the program? Enter yes or no.\n\n') 
        if restart.lower() != 'yes':
            print('Thanks for using ZIYTECHS program.')
            break


if __name__ == "__main__":
    main()