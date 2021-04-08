import os
#import pyttsx3 as px
import pyautogui as pt
import datetime
import speech_recognition as sr

#*******************************************************
# defineing real time

print("\n\t\t*********** Mark1 Here ***********\n")

#*******************************************************
# taking Command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)

    try:
        print("recognizing...")
        x = r.recognize_google(audio)
        print(x)

    except Exception as ep:
        print(ep)
        px.speak("I didn't understand, say that againg please")
        print("I didn't understand, say that again please")
        return "None"

    return x

#*******************************************************
# Time
def time():

    Time = datetime.datetime.now().strftime("%I:%M")
    px.speak("The time is")
    px.speak(Time)

#********************************************************
# defining current date

def date():

    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    px.speak("The date is")
    px.speak(day)
    px.speak(month)
    px.speak(year)

#********************************************************
# taking screenshot

def screenshot():

    img = pt.screenshot()
    img.save(r'C:\Users\Hemendra chaudhary\Pictures\Screenshots\\screenshot.png')
    px.speak("Screenshot Taken")
    
#*******************************************************
# WelCome Greetings 
def greetings() :
    px.speak("Hello sir, welcome back...")
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12:
        px.speak("Good Morning")
    elif hour>=12 and hour<18:
        px.speak("Good Afternoon")
    elif hour>=18 and hour<24:
        px.speak("Good Evening")
    else:
        px.speak("Good Night")
    px.speak("I'm Mark1 here...")
    
    


#********************************************************
# configurig hadoop cluster

def hadoop():

    print("----------------------------------------------------------------------------\n")


# creating templates for hdfs configuration file of hadoop

    file_1 = open("template.xml","w")
    file_1.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->')
    file_1.close()

    print("Template Created For hdfs Configuration File Of Hadoop")
    #px.speak("template created for hdfs configuration file of hadoop")

# creating templates for core configuration file of hadoop

#    file_2 = open("core-site.xml","w")
#    file_2.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->')
#    file_2.close()
#    
#    print("Template Created For core Configuration File Of Hadoop")
    #px.speak("Template created for core configuration file of hadoop")

#*********************************************************
# configuring hadoop master node

    def hadoop_master():
    
        #px.speak("Enter The IP Of Your Master Node")
        nn_ip = input("Enter The IP Of Your Master Node: ")
        #px.speak("Enter The Port No For Master Node")
        nn_port = input("Enter The Port No For Master Node: ")
        #px.speak("Enter The Directory For Master Node")
        nn_dir = input("Enter The Directory For Master Node: ")
        
# sending softwares that requires for configurig hadoop setup

        #px.speak("sending JDK software")
        os.system("scp jdk-8u281-linux-x64.rpm  root@{}:/root/".format(nn_ip))
        #px.speak("JDK software send Successfully!!")
        
        #px.speak("sending Hadoop Software")
        os.system("scp hadoop-1.2.1-1.x86_64.rpm root@{}:/root/".format(nn_ip))
        #px.speak("Hadoop software send successfully!!")
        
# installing Java and Hadoop software

        #px.speak("Installing java jdk")
        os.system("ssh root@{} rpm -ivh /root/jdk-8u281-linux-x64.rpm".format(nn_ip))
        #px.speak("Java installed Successfully!!")
        
        #px.speak("Installing hadoop")
        os.system("ssh root@{} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force".format(nn_ip))
        #px.speak("Hadoop installed Successfully!!")


# creating directory 

        #px.speak("Creating Directory")
        os.system("ssh root@{} mkdir /root/{}".format(nn_ip, nn_dir))
        print("Directory Created\n")
        #px.speak("Directory Created")


        file = open("template.xml", "r")
        lines = file.readlines()
        file.close()
        new = "".join(lines)


# configuration of hdfs-site.xml

        hdfs = open("hdfs-site.xml", "w")
        hdfs.write(new + '\n\n<configuration>\n' + '<property>\n' + '<name>dfs.name.dir</name>\n' + '<value>/{}</value>\n'.format(nn_dir) + '</property>\n' + '</configuration>\n')
        hdfs.close()


# configuration of core-site.xml

        core = open("core-site.xml", "w")
        core.write(new + '\n\n<configuration>\n' + '<property>\n' + '<name>fs.default.name</name>\n' + '<value>hdfs://{}:{}</value>\n'.format(nn_ip, nn_port) + '</property>\n' + '</configuration>\n')
        core.close()

# copying configuration templates

        #px.speak("Configuring hdfs and core files of Hadoop")
        os.system("scp hdfs-site.xml root@{}:/etc/hadoop/hdfs-site.xml".format(nn_ip))
        os.system("scp core-site.xml root@{}:/etc/hadoop/core-site.xml".format(nn_ip))
        
        print("\nHadoop Configuration Done!!\n")
        #px.speak("Hadoop Configuration Done!!")

# formating directory and starting the service

        #px.speak("formatting and starting hadoop service")
        os.system("ssh root@{} hadoop namenode -format".format(nn_ip))
        os.system("ssh root@{} hadoop-daemon.sh start namenode".format(nn_ip))
        
        print("\nHadoop Service Started Successfully For Master Node!!\n")
        #px.speak("Hadoop Service Started Successfully For Master Node!!")        

        os.system("ssh root@{} jps".format(nn_ip))
        
#*********************************************************
# configuring hadoop master node

    def hadoop_worker():
        
        #px.speak("How many slaves you wanted to create")
        no_slaves = int(input("How many slaves you wanted to be created: "))
		
        for i in range(0,no_slaves):
            #px.speak("Enter the ip of master")
            ip_master = input("Enter the ip of master: ")
            
            #px.speak("enter the port number of master")
            port = input("Enter the port number of master : ")
            
            #px.speak("enter the ip of worker")
            ip_slave = input("Enter the ip of worker: ")
            
            #px.speak("enter the directory for worker node")
            dir = input("Enter the directory for worker node: ")
            
# sending softwares that requires for configurig hadoop setup

            #px.speak("sending JDK software")
            os.system("scp jdk-8u281-linux-x64.rpm  root@{}:/root/".format(ip_slave))
            #px.speak("JDK software send Successfully!!")
        
            #px.speak("sending Hadoop Software")
            os.system("scp hadoop-1.2.1-1.x86_64.rpm root@{}:/root/".format(ip_slave))
            #px.speak("Hadoop software send successfully!!")
        
# installing Java and Hadoop software

            #px.speak("Installing java jdk")
            os.system("ssh root@{} rpm -ivh /root/jdk-8u281-linux-x64.rpm".format(ip_slave))
            #px.speak("Java installed Successfully!!")
        
            #px.speak("Installing hadoop")
            os.system("ssh root@{} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force".format(ip_slave))
            #px.speak("Hadoop installed Successfully!!")            
            
            
            #px.speak("Creating Directory")
            os.system("ssh root@{} mkdir /root/{}".format(ip_slave,dir))
            #px.speak("Directory Created")

            
            file = open("template.xml", "r")
            lines = file.readlines()
            file.close()
            new = "".join(lines)
            
#Configuring hdfs-site for slave
            hdfs = open("hdfs-site.xml", "w")
            hdfs.write(new +"\n\n<configuration>\n" + "<property>\n" + "<name>dfs.data.dir</name>\n" + "<value>/{}</value>\n".format(dir) + "</property>\n" +"</configuration>\n") 
            hdfs.close()

#configuring core-site.xml for slave
            core = open("core-site.xml", "w")
            core.write(new+"\n\n<configuration>\n"+"<property>\n"+"<name>fs.default.name</name>\n"+"<value>hdfs://{}:{}</value>\n".format(ip_master,port) + "</property>\n"+"</configuration>\n")
            core.close()
            
#setting up datanode

            #px.speak("Configuring hdfs and core files of Hadoop")
            os.system("scp hdfs-site.xml root@{}:/etc/hadoop/hdfs-site.xml".format(ip_slave))
            os.system("scp core-site.xml root@{}:/etc/hadoop/core-site.xml".format(ip_slave))
            
            #px.speak("starting Hadoop service")
            os.system("ssh root@{} hadoop-daemon.sh start datanode".format(ip_slave))
            os.system("ssh root@{} hadoop dfsadmin -report".format(ip_master))
            
            print("\nHadoop Condiguration Done For Worker Node!!\n")
            #px.speak("Hadoop Condiguration Done For Worker Node!!")
            #px.speak("And conneted successfully to master!!")
        
#****************************************
#Configuring client

    def hadoop_client():
    
        #px.speak("enter the ip of master")
        ip_master = input("Enter the ip of Master: ")
        #px.speak("enter the port number of master")
        port = input("Enter the port number of Master: ")
        #px.speak("enter the ip of Client")
        ip_client = input("Enter the ip of Client: ")
        
# sending softwares that requires for configurig hadoop setup

        #px.speak("sending JDK software")
        os.system("scp jdk-8u281-linux-x64.rpm  root@{}:/root/".format(ip_client))
        #px.speak("JDK software send Successfully!!")
        
        #px.speak("sending Hadoop Software")
        os.system("scp hadoop-1.2.1-1.x86_64.rpm root@{}:/root/".format(ip_client))
        #px.speak("Hadoop software send successfully!!")
        
# installing Java and Hadoop software

        #px.speak("Installing java jdk")
        os.system("ssh root@{} rpm -ivh /root/jdk-8u281-linux-x64.rpm".format(ip_client))
        #px.speak("Java installed Successfully!!")
        
        #px.speak("Installing hadoop")
        os.system("ssh root@{} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force".format(ip_client))
        #px.speak("Hadoop installed Successfully!!")

        file = open("template.xml", "r")
        lines = file.readlines()
        file.close()
        new = "".join(lines)

#configuring core-site.xml for client
        core = open("core-site.xml", "w")
        core.write(new+"\n<configuration>\n"+"<property>\n"+"<name>fs.default.name</name>\n"+"<value>hdfs://{}:{}</value>\n".format(ip_master,port) + "</property>\n"+"</configuration>\n")
        core.close()

#setting up client

        #px.speak("Configuring core files of client")
        os.system("scp core-site.xml root@{}:/etc/hadoop/core-site.xml".format(ip_client))
        print("\nHadoop Condiguration Done For Client!!\n")
        #px.speak("Hadoop Condiguration Done For Client!!")
    
    while True:
    
        print("\n\t\t***********Which Node You Want To Configure**********\n\t\t\t1. Master Node\n\t\t\t2. Worker Node\n\t\t\t3. Client Node\n\t\t\t4. Main Menu\n\t\t\t5. EXIT")
        #px.speak("Which Node You Want To Configure")
        #px.speak("Master Node")
        #px.speak("Worker Node")
        #px.speak("Client Node")
        #px.speak("Or want to return main menu")
        #px.speak("Or else want to exit")
    
    
        #x = takeCommand().lower()
        
        x = input("Enter Your Choice : ")
    
        if (("master" in x)):
            hadoop_master()
        
        elif (("worker" in x)):
            hadoop_worker()
        
        elif (("client" in x)):
            hadoop_client()
        
        elif (("menu" in x) and ("main" in x)):
            #px.speak("returning to main menu")
            return 0
        
        elif (("exit" in x)):
            #px.speak("exiting")
            exit()
        
        
#--------------------------------------------------------------
#*******************LVM*******************
def lvm():\

    print("----------------------------------------------------------------------------\n")	
    print("\n\t\t*********Welcome to my LVM*********")
    #px.speak("Welcome to my LVM")
    
#*********************************
#Volume group creation
    def create_lvm():
    
        #px.speak("Enter the IP of System Where You Want LVM Partition")
        ip_lvm = input("Enter the IP of System Where You Want LVM Partition: ")

        #px.speak("Listing the Devices Mounted on This Host")
        os.system("ssh root@{} fdisk -l".format(ip_lvm))
        
        #px.speak("Enter Path of Storage Devices(Saperated By Space) i.e /dev/sda")
        storages=input("Enter Path of Storage Devices(Saperated By Space) i.e /dev/sda : ").split()
        print("\n")

        for i in storages:
            os.system("ssh root@{} pvcreate {}".format(ip_lvm, i))
            #px.speak("Physical Volume Created")
        print("\n")
        
        #px.speak("Enter Name of Volume Group")
        vg_name=input("Enter Name of Volume Group : ")
		
        cmd = ''
        for i in storages:
            cmd = cmd + ' ' + i 

#volume group created			
        os.system("ssh root@{} vgcreate {} {}".format(ip_lvm, vg_name, cmd))
        #px.speak("Volume Group Created")
        print("\n")
        
        #px.speak("Enter Size of Partition")
        size=input("Enter Size of Partition :")
        
        #px.speak("Enter the Name of Partition")
        name_lvm=input("Enter the Name of Partition :")
        print("\n")

#logical volume created
        os.system("ssh root@{} lvcreate --size {}G --name {} {}".format(ip_lvm, size, name_lvm, vg_name))
        #px.speak("Logical Volume Created")

#formated created volume
        os.system("ssh root@{} mkfs.ext4 /dev/{}/{}".format(ip_lvm, vg_name, name_lvm))
        #px.speak("Logical Volume Formated")
        print("\n")

#Mounting
        #px.speak("Ente the Mount Point Name")
        mount_point=input("Enter the Mount Point Name : ")
        print("\n")
        
        os.system("ssh root@{} mkdir /{}".format(ip_lvm, mount_point))
        #px.speak("Mount Point Directory Created")
        
        os.system("ssh root@{} mount /dev/{}/{} /{}".format(ip_lvm,vg_name,name_lvm,mount_point))
        #px.speak("Logical Volume Mounted Successfully")
        
        #px.speak("Bingo!! You Have Successfully Created LVM Partition")
        print("Bingo!! You Have Successfully Created LVM Partition")
        
#*****************************************
#Partition extension
    def extend_lv():
    
        #px.speak("Enter System IP Where You Want Extend Partition Size")
        ip_lvm = input("Enter System IP Where You Want Extend Partition Size: ")
        
        #px.speak("Enter the size")
        size = input("Enter the Size: ")
        
        #px.speak("Enter the name of volume group")
        vgname = input("Enter the name of Volume Group: ")
        
        #px.speak("Name of partition")
        name = input("Name of Partition: ")

#logical volume extended
        os.system("ssh root@{} lvextend --size +{}G /dev/{}/{}".format(ip_lvm, size,vgname,name))
        #px.speak("Logical Volume Extended")
        print("Logical Volume Extended\n\n")

#updating partition table
        os.system("ssh root@{} resize2fs /dev/{}/{}".format(ip_lvm, vgname,name))
        #px.speak("Logical Volume Formated")
        print("Logical Volume Formated\n\n")

#******************************************

#Volume group extension
    def extend_vg():
    
        #px.speak("Enter System IP Where You Want To Extend Volume Group")
        ip_lvm = input("Enter System IP Where You Want To Extend Volume Group: ")

        #px.speak("Listing of devices you have")
        os.system("ssh root@{} fdisk -l".format(ip_lvm))
        print("\n\n")
        
        
        #px.speak("Enter new Hard Disk device")
        new_hd=input("Enter new HD device (/dev/sdd.../dev/sdc) :# ")
        
        #px.speak("Enter the name of volume group")
        vg_name=input("Enter the name of Volume Group :# ")

#physical volume creation
        os.system("ssh root@{} pvcreate {}".format(ip_lvm, new_hd))
        #px.speak("Physical Volume Created")
        
#volume group extension
        os.system("ssh root@{} vgextend {} {}".format(ip_lvm, vg_name,new_hd))
        #px.speak("Volume Group Extended")
        
        #px.speak("Do you want to extend space of Logical Volume")
        choice=input("\nDo you want to extend space of LV(Y/N) :").capitalize()	
        if(choice=="Y"):
            #px.speak("Enter size to be extended for partition")
            size=int(input("Enter Size to be Extended for Partition :"))
            
            #px.speak("Enter Name of partition")
            name=input("Name of Partition :")
#logical volume size provision
            os.system("ssh root@{} lvextend --size +{}G /dev/{}/{}".format(ip_lvm, size,vg_name,name))
            #px.speak("Logical Volume Extended")

#updating partition table
            os.system("ssh root@{} resize2fs /dev/{}/{}".format(ip_lvm, vg_name,name))
            #px.speak("Logical Volume Formated")
            print("\n")
            print("Size of LV increased! by {}".format(size))
            #px.speak("Size of Logical Volume Increased! by {} Successfully!!".format(size))
        else:
            print("Volume Group extended successfully")
            #px.speak("Volume group extended successfully")
            exit()	        
    
    while True:
    
        print("\n\t***************What You Want To Do With LVM***************\n\t\t\t1. Create New LVM\n\t\t\t2. Extend Partition Size\n\t\t\t3. Add More Device to Volume Group\n\t\t\t4. Main Menu\n\t\t\t5. EXIT")
        #px.speak("What Do Want To Do With LVM")
        #px.speak("Create New LVM")
        #px.speak("Extend Partition Size")
        #px.speak("Add More Device to Volume Group")
        #px.speak("Or want to go to main menu")
        #px.speak("Or else Want To Exit")
    
    
    
        #x = takeCommand().lower()
        
        x = input("Enter Your Choice : ")

        
        if (("create" in x) and ("lvm" in x)):
            create_lvm()
        
        elif (("partition" in x) and ("size" in x)):
            extend_lv()
        
        elif (("volume" in x) and ("group") in x):
            extend_vg()
        
        elif (("menu" in x) and ("main" in x)):
            #px.speak("returning to main menu")
            return 0
        
        elif (("exit" in x)):
            #px.speak("exiting")
            exit()
            
            
#--------------------------------------------------------------

#************AWS************
def aws():
    print("----------------------------------------------------------------------------\n")
    print("\t\t***********WELCOME TO AWS CLI***********\n\n")
    #px.speak("WelCome To AWS CLI")

#configuring AWS CLI
    #px.speak("Configure Your AWS in CLI by Entering Credentials")
    os.system("aws configure")


#EC2 service
    def ec2_service():
        while True:

            print("\n\t***************What You Want To Do With EC2 Service***************\n\t\t\t1. Launch Instance\n\t\t\t2. Create Volume\n\t\t\t3. Attach Volume\n\t\t\t4. Privious Menu\n\t\t\t5. EXIT")
            #px.speak("What You Want To Do With EC2 Service")
            #px.speak("Launch Instance")
            #px.speak("Create Volume")
            #px.speak("Attach Volume")
            #px.speak("Or want to return to previous menu")
            #px.speak("Or else Want To Exit")

            #x = takeCommand().lower()
            
            x = input("Enter Your Choice : ")

            if (("launch" in x) and ("instance" in x)):
                print("\n")
            
                #px.speak("Enter Image ID")
                image_id = input("Enter Image ID(ami-id) : ")
            
                #px.speak("How Many Instance You Want")
                count = input("How Many Instance You Want : ")
            
                #px.speak("Enter your instance type")
                instance_type = input("Enter Your Instance Type : ")
            
                #px.speak("Enter key-name")
                key_name = input("Enter Key Name : ")
            
                #px.speak("ENter security-group-id")
                security_grp = input("Enter Security Group ID : ")
            
                #px.speak("Enter Subnet ID")
                subnet_id = input("Enter Subnet ID : ")
            
            
#Launching instance
                os.system("aws ec2 run-instances --image-id {} --count {} --instance-type {} --key-name {} --security-group-ids {} --subnet-id {}".format(image_id,count,instance_type,key_name,security_grp,subnet_id))
	
                #px.speak("Bingo!! EC2 instance Launch successfully!!")
                print("Bingo!! EC2 instance Launch successfully!!") 
 
#Creating volume
            elif (("create" in x) and ("volume" in x)):
                print("\n")
            
                #px.speak("Enter Image volume type")
                voluem_type = input("Enter Image Volume Type : ")
            
                #px.speak("Enter Size of Volume(in GiB)")
                size = input("Enter Size Of Volume(in GiB) : ")
            
                #px.speak("Enter Availability Zone")
                avl_zone = input("Enter Availability Zone ID : ")
            
                os.system("aws ec2 create-volume --volume-type {} --size {} --availability-zone {}".format(voluem_type,size,avl_zone))
            
                #px.speak("EBS  Volume Created Successfully")
                print("EBS  Volume Created Successfully")
            
#Attach volume to existing instance
            elif (("attach" in x) and ("volume" in x)):
                print("\n")
            
                #px.speak("Enter Volume ID")
                volume_id = input("Enter Volume ID : ")
            
                #px.speak("Enter instance id where you want to attach the volume")
                instance_id = input("Enter Instance ID : ")
            
                #px.speak("Enter Device  name which you want to attach")
                device_name = input("Enter Device Name : ")
            
                os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device {}".format(volume_id,instance_id,device_name))
            
                #px.speak("EBS volume Attached Successfully")
                print("EBS volume Attached Successfully")

            elif (("menu" in x) and ("previous" in x)):
              #px.speak("returning to main menu")
              return 0

            elif ("exit" in x):
                #px.speak("exiting")
                exit()
             
            
    while True:
            
        print("----Service List----\n")
        #px.speak("Right Now I only access EC2 Service Of AWS")
        print("1.EC2\n")
     
        #px.speak("Do you want me to proceed with EC2(yes/no)")
        print("Do you want me to proceed with EC2(yes/no)")
        
        #x = takeCommand().lower()
 
        x = input("Ente Your Choice : ") 
 
        if ("yes" in x):
            ec2_service()
        
        elif ("no" in x):
            #px.speak("Returning to main menu")
            return 0
            
            

#--------------------------------------------------------------
#**********DOCKER***************
def docker():
		
    print("----------------------------------------------------------------------------\n")
    print("\t\t***********WELCOME TO DOCKER WORLD!!***********\n\n")
    #px.speak("Welcome to Docker world")
    
    while True:
	
        print("\n\t***************What You Want To Do***************\n\t\t\t1. Install The Docker\n\t\t\t2. Go With The Same\n\t\t\t3. Main Menu\n\t\t\t4. EXIT")
            
        #px.speak("What You Want To Do")
        #px.speak("Install The Docker")
        #px.speak("Go With The Same")
        #px.speak("Or want to go to main menu")
        #px.speak("Or else Want To Exit")
    
        #x = takeCommand().lower()
    
        x = input("Enter Your Choice : ")
    
        if (("install" in x) and ("docker" in x)):
    
            #px.speak("Enter System IP Where You Want To Configure Docker")
            ip = input("Enter System IP Where You Want To Configure Docker : ")
            
   
            #os.chdir("/etc/yum.repos.d")
            #os.system("touch docker-ce.repo")
    
            os.system("scp docker.repo root@{}:/etc/yum.repos.d/docker.repo".format(ip))
            #px.speak("Yum configuration for docker is successfully complete!!")
    
            os.system("ssh root@{} yum install docker-ce --nobest -y".format(ip))
            #px.speak("Docker-ce Installed Successfully!!")
    
            os.system("ssh root@{} systemctl enable docker --now".format(ip))
            #px.speak("Docker service started and enabled successfully!!")
    
            #px.speak("Docker Info")
            os.system("ssh root@{} docker info".format(ip))

            #print("Visiting website..........")
            #webbrowser.open("https://hub.docker.com/search?q=&type=image")

        elif (("go" in x) and ("same" in x)):
        
            #px.speak("Enter System IP Where You Want To Docker Operations")
            ip = input("Enter System IP Where You Want To Docker Operations : ")
		
            while True:
    
                print("\n\t***************What You Want To Do With Docker***************\n\t\t\t1. Pull An Docker Image\n\t\t\t2. Install A Container\n\t\t\t3. Check Running Container\n\t\t\t4. Shutdown A Container\n\t\t\t5. Start A Container\n\t\t\t6. Privious Menu\n\t\t\t7. EXIT")
            
                #px.speak("What You Want To Do With Docker")
                #px.speak("Pull An Docker Image")
                #px.speak("Install An Container")
                #px.speak("Check Running Container")
                #px.speak("Shutdown A Container")
                #px.speak("Start A Container")
                #px.speak("or want to return to previous menu")
                #px.speak("Or else Want To Exit")
            
            
            
                #x = takeCommand().lower()
              
                x = input("Enter Your Choice : ")
            
                #iso_image pull	
                if (("pull" in x) and ("image" in x)):
                    #px.speak("Enter Docker Image Name i.e (image_name:version)")
                    image_name = input("Enter Docker Image Name i.e (image_name:version) : ")          
                    os.system("ssh root@{} docker pull {}".format(ip,image_name))
                
                    #px.speak("{} Image Pulled Successfully!!".format(image_name))

                #installing os
                elif (("install" in x) and ("container" in x)):
                    #px.speak("Enter Docker Image Name i.e (image_name:version)")
                    image_name = input("Enter Docker Image Name i.e (image_name:version) : ")
                    os.system("ssh root@{} docker run -dit {}".format(ip,image_name))
               
                    #px.speak("Container Installed successfully with the {} image".format(image_name))
                
                #Checking running os
                elif (("running" in x)  and ("container" in x)):
                    #px.speak("Checking OS running status on docker")
                    print("Checking OS running on docker")
                    os.system("ssh root@{} docker ps".format(ip))
                 
                
			
                #Shutdown OS
                elif (("shutdown" in x) and ("container" in x)):
                    #px.speak("Showing all the Running Docker Container ID")
                    print("\nShowing all the Running Docker Container ID\n")
                    os.system("ssh root@{} docker ps -q".format(ip))

                    #px.speak("Enter OS name which you want to stop")                
                    os_name=input("Enter OS name : ") 
                    os.system("ssh root@{} docker stop {}".format(ip,os_name))
 
                    #px.speak("Docker container stopped successfully!!")
 
                #Starting os
                elif (("start" in x) and ("container" in x)):
            
                    #px.speak("Showing all containers ID")
                    os.system("ssh root@{} docker ps -a -q".format(ip))
             
                    #px.speak("Enter OS name which you want to start")	
                    os_name=input("Enter OS name : ")
                    os.system("ssh root@{} docker start {}".format(ip,os_name))
                    os.system("ssh root@{} docker attach {}".format(ip,os_name))
            
                elif (("previous" in x) and ("menu" in x)):
                    #px.speak("returning to previous menu")
                    return 0
            
            
                elif ("exit" in x):
                    #px.speak("exiting")
                    exit()
        
        elif (("menu" in x) and ("main" in x)):
            #px.speak("returning to main menu")
            return 0
        
        elif (("exit" in x)):
            #px.speak("exiting")
            exit()
            
            
#greetings()
            
if __name__ == "__main__" :

    while True:
    
        print("\n\t\t\t***************MAIN MENU***************\n\t\t\t")

   
        #x = takeCommand().lower()
    

        #if (("you" in x) and ("how" in x)):
            #px.speak("I am very good")
            #print("I am very good")

            #px.speak("your help will help me some way")
            #print("your help will help me some way :)")

            #px.speak("what can I do for you, sir ?")
            #print("what can I do for you, sir ?")
            
        #elif (("what" in x) and ("can" in x) and ("do" in x)):

        
        print("\n\t***************What You Want Me To Do For You***************\n\t\t\t1. Hadoop Configuration\n\t\t\t2. LVM Partition\n\t\t\t3. AWS\n\t\t\t4. Docker\n\t\t\t5. EXIT\n")

            #px.speak("Today I can integrate four Technologies for you")
            #px.speak("which technology you want to configure")
            #px.speak("Hadoop")
            #px.speak("LVM Partition")
            #px.speak("AWS")
            #px.speak("And Docker")
            #px.speak("Or else you want me to exit")
        
        x = input("Enter Your Choice : ")        

        
        if ("hadoop" in x):
            #px.speak("configurig Hadoop Cluster")
            print("\n\t\t\t***************CONFIGURINING HADOOP CLUSTER***************\n\t\t\t")
            hadoop()
            
        elif (("lvm" in x) and ("partition" in x)):
            #px.speak("creating LVM Partition")
            print("\n\t\t\t***************LVM PARTITION***************\n\t\t\t")
            lvm()
            
        elif("aws" in x):
            #px.speak("opening AWS console")
            print("\n\t\t\t***************AWS***************\n\t\t\t")
            aws()
            
        elif ("docker" in x):
            #px.speak("configurig Docker")
            print("\n\t\t\t***************DOCKER***************\n\t\t\t")
            docker()
            
        elif ("exit" in x):
            #px.speak("exiting")
            exit()
            
            
        
        














