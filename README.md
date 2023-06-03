# DS_LAB_PROJECT


## **---    Execution of project.py   ---**


   .  Making Subprocess of Main Server which takes the Text File which Contains the HTTPS link for csv data.
   .  Second After that it Goes to Internal Server where it is sending the Text.txt File to each Individual process to Process the data and give        desired output.
   .  After Getting Desired Output it is Launching the Website "index.html" which shows the output in well structured manner.


### **---    Clients/Client.py    ---**


   .  It Sends the Text File to Main Server Through Dynamic Port.
   .  The Text File Contains the Https link of CSV data-collection.


### **---    Image Server (img_ser.py)   ---**
   
   
   .  Recieves Images From Image Client from Each Process.
   
   
### **---    Internal Server.py   ---**
   
   
   .  Sending the Text.txt File to Each Individual Process


### **---   P1.py , P2.py , p3.py , P4.py , P5.py , p6.py , p7.py , p8.py   ---**
   
   
   .  Run the Process Individually it will Process the Data and Form a Graphical Image of that Data.
   .  It also Calls a Subprocess "img_client.py" which sends the Image to "img_server.py".


### **---    After Executing All Processes.  ---**


   .  It Comes back to Main Process.
   .  And Lauches the Website.
