from getdata.getdataframe import get_time_series_data

if __name__ == '__main__':
    start_secs = '17-06-2024 00:00:00'
    end_secs = '17-08-2024 00:00:00'
    ret = get_time_series_data(start_secs,end_secs,interval=5)
    my_data = ret.values.astype('f')
    print(my_data)
    print(ret)
