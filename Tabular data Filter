
import csv
import os
from optparse import OptionParser


def process_input_file(input_file, target):
    input_csv = input_file
    # input_csv ='TK_DIV_HIST_RUSSELL_DVC_samples_2018-08-31T9-30-30_49319471.csv' \home\user\zcao\
    # output_direct =C:\Users\zcao\Desktop\Codes\Python\Utilities\

    #C:\Users\zcao\Desktop\TK_history_missing_events_US.csv



    output_csv = input_csv.strip('.csv') + '_output.csv'
    print(output_csv)


    load_file = open(input_csv, mode='r+')
    write_output = open(output_csv, mode='w', newline='')

    input_reader = csv.reader(load_file)
    output_writer = csv.writer(write_output)

    row_index = 0
    for row in input_reader:

        if len(row[0]) > 1:

            target_column = []
            comparied_column = []
            missing_from_target = ''
            missing_from_comparied = ''

            if '|' in row[int(target)-1] and row[int(target)]:
                for target_item in row[int(target)-1].split('|'):
                    target_column.append(target_item)


                for comparied_item in row[int(target)].split('|'):
                    comparied_column.append(comparied_item)


                for item in target_column:
                    if item in comparied_column:
                        continue
                    else:
                        missing_from_comparied = missing_from_comparied + '|' + item

                for item in comparied_column:
                    if item in target_column:
                        continue
                    else:
                        missing_from_target = missing_from_target + '|' + item

            elif 'NA' in row[int(target)-1] or 'NA' in row[int(target)]:
                missing_from_comparied = 'NA'
                missing_from_target = 'NA'

            elif row[int(target)-1] == row[int(target)] and row_index != 0:
                missing_from_target = ""
                missing_from_comparied = ""
            else:
                missing_from_target = 'missing_from_target: column' + str(int(target))
                missing_from_comparied = 'missing_from_comparied: column' + str((int(target) + 1))

            row_index += 1
            row.append(missing_from_comparied)
            row.append(missing_from_target)
            output_writer.writerow(row)

    write_output.close()
    load_file.close()

def main():
    parser = OptionParser()
    parser.add_option("-i", "--input_file", dest="filename")
    parser.add_option('-c', "--target", dest="column")
    #parser.add_option("-o", "--output_direct", dest="output_directory")
    (options, args) = parser.parse_args()


    input_file = options.filename
    target = options.column
    #output_direct = options.output_directory


    process_input_file(input_file,target) #, output_direct

if __name__ == '__main__':
    main()







