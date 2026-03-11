#importing the ui
from UI import GUI_main_window_login
import os
import csv

#Running the UI from the Main file
if __name__ == '__main__':
    with open("doctorCredentials.csv",'a',newline='') as f:
        writer = csv.writer(f)
        if os.stat("doctorCredentials.csv").st_size == 0:  # Check if file is empty
            writer.writerows([['Dr. Sanjay Gupta', 'sg'], ['Dr. Devi Shetty', 'ds'], ['Dr. Helen Rees', 'hr'], ['Dr. Paul Farmer', 'pf'], ['Dr. Atul Gawande', 'ag'], ['test', 't']])

    root = GUI_main_window_login()
    root.ui()
    root.mainloop()