            try:
                # Read data from IR_5
                command_5 = "5M!\r"
                IR_5.write(command_5)
                IR_5.flush()
                time.sleep(5)
                # read bit
                data_str_5 ="5D0!\r"
                IR_5.write(data_str_5)
                data_5 = IR_5.readline()
                IR_5.flush()
                time.sleep(5)
                if len(data_5.split('+'))> 1:
                    writer.writerow({'Date': date, 'Time': time, 'Surface Temp Zone C (3)': data_5})
            except Exception as e:
                now = get_datetime()
                print(f"Error reading IR_5 at {now[0]} on {now[1]}: {e}")