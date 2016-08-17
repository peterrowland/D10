#!/usr/bin/env python3# Exercise: Presidents# Author GitHub usernames:# #1:# #2:# Instructions:# Write a program to:# (1) Load the data from presidents.txt into a dictionary.# (2) Print the years the greatest and least number of presidents were alive.#     (between 1732 and 2016 (inclusive))#     Ex.#       'least = 2015'#       'John Doe'#       'most = 2015'#       'John Doe, Jane Doe, John Adams, and Jane Adams'# Bonus: Confirm there are no ties. If there is a tie print like so:#     Ex.#       'least = 1900, 2013-2015'#       'John Doe (1900)'#       'Jane Doe (2013-2015)'#       'most = 1900-1934, 2013'#       'John Doe, Jane Doe, John Adams, and Jane Adams (1900-1933)'#       'Sally Doe, Billy Doe, Mary Doe, and Cary Doe (1934)'#       'Alice Doe, Bob Doe, Zane Doe, and Yi Do (2013)'# (3) Write your print statements to a file (greatest_least.txt) as well.# Upload that file as well.############################################################################### Imports# Bodydef load_words():    with open('presidents.txt', 'r') as presidents:        dict_ = {}        data = presidents.readlines()        for line in data:            line_split = line.split(',')            dict_[line_split[0]] = [line_split[1],line_split[2].strip()] # would tuple be easier?    return dict_def check_alive(year, dict_):    ''' Takes year, checks against dictionary, returns all keys(names) where year in range'''    alive_list = []    ## THEY LIVE    # Loop through dictionary entries by key(name)    for name, span in dict_.items():        # print(name, span) # test iterate -- OK        #This handles cases with no death date -- better way to handle none value?        if span[1] == 'None':            span[1] = '2016'        # create range from val list        # check if year in range !! special case if d_date == none)        if year in range(int(span[0]),(int(span[1]) + 1)): # Check year in range, if no death date use 2016            # print(name) # test -- OK            # if yes, add to alive list            alive_list.append(name)    return alive_list# this is the main operationdef year_dict(dict_):    ''' Main operation. Loops through years range and calls check_alive'''    range_years = (1732, 2016)    year_dict = {}    for i in range(range_years[0], range_years[1] + 1):        year_dict[i] = check_alive(i, dict_)        # year_dict[i] = 'check_alive(i)' # expect dict of years -- OK    return year_dictdef get_len(dict_):    return len()##############################################################################def main():  # CALL YOUR FUNCTION BELOW    president_dict = load_words() # -- OK!    dict_Y = year_dict(president_dict) # -- OK!    sorted_years = sorted(dict_Y, key=lambda k: len(dict_Y[k]), reverse=True)    print("Most: {} \n {}".format(sorted_years[0], dict_Y[sorted_years[0]]))    print("Least: {} \n {}".format(sorted_years[-1], dict_Y[sorted_years[-1]]))    with open('greatest_least.txt', 'w') as output:        output.write("Most: {} \n {} \n".format(sorted_years[0], dict_Y[sorted_years[0]]))        output.write("Least: {} \n {} \n".format(sorted_years[-1], dict_Y[sorted_years[-1]]))    # print(min(dict_Y, key=dict_Y.keys)) # -- get min entries - FAIL    # print(max(sorted(dict_Y, key=dict_Y.get))) # -- prints years in order    # print(sorted(dict_Y, key=get_len(dict_Y.__getitem__))) # -- prints years randomly    # sort dictionary by len of value lists, using lambda    # for k in sorted(dict_Y, key=lambda k: len(dict_Y[k]), reverse=True):    #     print(k, str(dict_Y[k]))if __name__ == '__main__':    main()