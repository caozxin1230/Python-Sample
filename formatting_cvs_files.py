import csv

with open ('US_MF_Divs_CAp_Gains_2017_long.csv') as long_gain_file,open('US_MF_Divs_CAp_Gains_2017_short.csv') as short_gain_file, open('Formatted_US_MF_Divs_CAp_Gains_2017.cvs',mode='w', newline='') as output_file:

    #read_from_short = short_gain_file.readlines()
    #read_from_long = long_gain_file.readlines()

    #output_writer = csv.writer(output_file) #,quotechar='|'
    long_gain_reader = csv.reader(long_gain_file, delimiter=',', quotechar='|')
    short_gain_reader = csv.reader(short_gain_file, delimiter=',', quotechar='|')
    output_writer = csv.writer(output_file, delimiter='|')
    mutual_fund_short =[]
    mutual_fund_long =[]
    ex_date_short = []
    ex_date_long = []
    amt_short =[]
    amt_long =[]
    identifier_short=[]
    identifier_long = []

    output_writer.writerow(['Ticker-ISO','Date','Short Capital Gain', 'Long Capital Gain'])

    for each_row in short_gain_reader:
        mutual_fund_short.append(each_row[0])
        ex_date_short.append(each_row[1])
        amt_short.append(each_row[3])
        identifier_short.append(each_row[0]+each_row[1])

    len_short = len(mutual_fund_short)

    for each_row in long_gain_reader:
        mutual_fund_long.append(each_row[0])
        ex_date_long.append(each_row[1])
        amt_long.append(each_row[3])
        identifier_long.append(each_row[0] + each_row[1])

    len_long = len(mutual_fund_long)

    for i in range(len_short):
        for j in range (len_long):
            if mutual_fund_short[i] == mutual_fund_long [j] and ex_date_short[i] == ex_date_long[j]:
                #print(mutual_fund_short[i], ex_date_short[i],amt_short[i],amt_long[j])
                output_writer.writerow([mutual_fund_short[i], ex_date_short[i],amt_short[i],amt_long[j]])

                #output_writer.writerow([mutual_fund_short[i], ex_date_short[i], amt_short[i]])
                #output_writer.writerow([mutual_fund_long[i], ex_date_long[i], ' ', amt_long[j]])

    for i in range(len_short):
        if identifier_short[i] not in identifier_long:
            output_writer.writerow([mutual_fund_short[i], ex_date_short[i],amt_short[i]])

    for j in range(len_long):
        if identifier_long[j] not in identifier_short:
            output_writer.writerow([mutual_fund_long[j], ex_date_long[j], ' ', amt_long[j]])
