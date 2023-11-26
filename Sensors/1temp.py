            try:
                THUM_34.write("OPEN 34\r\n")
                THUM_34.flush()
                print("34 is opened")
                sleep(1)

                THUM_34.write("SEND\r\n")
                THUM_34.flush()
                print("send")
                sleep(2)
                
                data_34 = THUM_34.readlines()

                last_line_34 = data_34[-1]
                rh_index_34 = last_line_34.find('RH=')
                temp_index_34 = last_line_34.find("Ta=")

                if rh_index_34 != -1 and temp_index_34 != -1:
                    rh_value_34 = float(last_line_34[rh_index_34 + 3:last_line_34.find('%RH')])
                    temp_value_34 = float(last_line_34[temp_index_34 + 3:last_line_34.find("'C")])
                    writer.writerow({'Date': date, 'Time': time, 'Zone': "B", 'Subzone': "1", 'Temp': temp_value_34, 'Humidity': rh_value_34})
                sleep(1)
                THUM_34.write("CLOSE\r\n")
                print("closed")
                sleep(1)
            except Exception as e:
                now = get_datetime()
                print(f"Error reading THUM_34 at {now[1]} on {now[0]}: {e}")
