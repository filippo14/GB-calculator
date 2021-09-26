from datetime import datetime

first_time = str(input('Enter the first date in yyyy-mm-dd hh:mm format: '))
second_time = str(input('Enter the second date in yyyy-mm-dd hh:mm format: '))
avg_value_Grafana = float(input('Enter the numeric average value from Grafana in the time period of interest: '))
print("""Press: 
1 if the unit of measure of the previous average value is in Bytes 
2 if the unit of measure of the previous average value is in KiloBytes
3 if the unit of measure of the previous average value is in MegaBytes
4 if the unit of measure of the previous average value is in GigaBytes
""")
unit_measure = int(input("Tell me your option: "))

date_format_str = '%Y-%m-%d %H:%M'

date1 = datetime.strptime(first_time, date_format_str)
date2 = datetime.strptime(second_time, date_format_str)

# Get the interval between two datetimes as timedelta object
diff = date2 - date1
sec_in_day = 24 * 60 * 60
diff_in_sec = diff.days * sec_in_day + diff.seconds

def switch(option):

    def Bytes():
       value_in_GB = avg_value_Grafana * (1/1024) * (1/1024) * (1/1024)
       return value_in_GB

    def kiloBytes():
       value_in_GB = avg_value_Grafana * (1/1024) * (1/1024)
       return value_in_GB

    def megaBytes():
       value_in_GB = avg_value_Grafana * (1/1024)
       return value_in_GB
    
    def gigaBytes():
       value_in_GB = avg_value_Grafana
       return value_in_GB

    def default():
        return "Incorrect option"

    dict = {
        1: Bytes,
        2: kiloBytes,
        3: megaBytes,
        4: gigaBytes,
    }

    return dict.get(option,default)()
    

value_in_GB = switch(unit_measure)
result = float(value_in_GB) * float(diff_in_sec)
print( "The total of GigaBytes between " + first_time + " and " + second_time + " is: " + str(result) + " GB" )