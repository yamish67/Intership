# TASK 4 - Setup and Use a Firewall on Windows/Linux

# Tools Used 
Windows - Netsh
Linux   - ufw

# Steps from Windows 

1) - Open Firewall Configuration Tool
     Command Used - Open 'Windows Defender Firewall with Advanced Security
     ![Screenshot 2025-05-30 101244](https://github.com/user-attachments/assets/2fcb8f17-0c69-4b84-b803-822e471e26d0)

2) - List Current Firewall Rules
     Command Used - netsh advfirewall firewall show rule name=all
     ![Screenshot 2025-05-30 101616](https://github.com/user-attachments/assets/9e7df024-bdc8-462f-b5bf-5469416fb98f)


3) - Add Rule to Block Port 23 (Telnet)
     Command Used - netsh advfirewall firewall add rule name="Block Telnet" dir=in action=block protocol=TCP localport=23
     ![Screenshot 2025-05-30 101710](https://github.com/user-attachments/assets/61762119-6af6-4f75-969c-e55d43243882)

     

4) - Test the Block Rule
     Command Used - Telnet 127.0.0.1 23
     ![Screenshot 2025-05-30 102038](https://github.com/user-attachments/assets/d2872620-f839-4cd9-9b4f-cf9818bf988c)

5) - Add Rule to Allow SSH (Port 22)
     Command Used - netsh advfirewall firewall add rule name="Allow SSH" dir=in action=allow protocol=TCP localport=22
     ![Screenshot 2025-05-30 101813](https://github.com/user-attachments/assets/022faf52-378b-4aa6-bf28-f9215b1b2012)

6) - Remove Block Rule
     Command Used - netsh advfirewall firewall delete rule name="Block Telnet
     ![Screenshot 2025-05-30 101842](https://github.com/user-attachments/assets/16a0445b-2521-4c2c-8efb-d891369b09d1)

# Detailed Report for Firewall configuration

[Task_4_Firewall_Report.pdf](https://github.com/user-attachments/files/20515372/Task_4_Firewall_Report.pdf)

