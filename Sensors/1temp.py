                # Read data from THUM_34
                THUM_34.write("OPEN 34\r\n")
                THUM_34.flush()
                print("34 is opened")
                sleep(3)

                THUM_34.write("SEND\r\n")
                THUM_34.flush()
                print("send")
                sleep(3)
        
                data_34 = THUM_34.readlines()
                # Extract RH and Ta from the data
                rh_match = re.search(r'RH= (\d+\.\d+)', data_34[-1])
                ta_match = re.search(r'Ta= (\d+\.\d+)', data_34[-1])

                if rh_match and ta_match:
                    rh_value = rh_match.group(1)
                    ta_value = ta_match.group(1)

                    # Get current date and time
                    now = datetime.now()
                    current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

                    # Print the data
                    writer.writerow({'Date': date, 'Time': time, 'Zone' : "B", 'Subzone': "1", 'Ambient temperature': ta_value, 'Relative humidity': rh_value})
                    sleep(3)

                    THUM_34.write("CLOSE\r\n")
                    print("closed")
                    sleep(3)