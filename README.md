# Daemon_Monitor_enhance

1. Activate enviroment **"daemonEnv"**
   source daemonEnv/bin/activate

2. Start the mysql docker container and create a database and update the instance and database creadentials on .env file.
   **create a table**
   CREATE TABLE `DaemonDetails` (
  `daemon_name` varchar(255) DEFAULT NULL,
  `daemon_id` varchar(255) DEFAULT NULL,
  `daemon_status` varchar(255) DEFAULT NULL,
  `instance` int DEFAULT NULL
   );
   
   3. **Insert data into the table**'
      insert into DaemonDetails (daemon_name, daemon_id, daemon_status, instance) values ('filetransfer','4','UP',1);
  
4. python3 run.py
   It will host the application at "http://127.0.0.1:5000/"
