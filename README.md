Data_Collection.py should be execeuted first. Face should be kept at a steady position so that clear images can be taken for dataset. The complete execution of Data_Collection.py is indicated only by "Data Collected---------"
written on terminal. After the excution of Data_Collection.py, Data_Train.py should be exceuted to train the recognizer
After the dataset training is complete, Recognition.py can be executed. Serial number should be given as 
in single digit integers as they represent list index. While executing Recognition.py if IndexError
is shown, before showing the list element in the window just reduce the serial value by 1
(new_serial = serial - 1) and the find the elements with the new_serial (names[new_serial]).
