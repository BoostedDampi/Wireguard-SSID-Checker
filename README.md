# Wireguard-SSID-Checker
This two scripts when activated trough windows Task Scheduler can check if the Wifi is in a blacklist and if not will activate a wireguard VPN.

**How to Use:**
1. Put the two files in a folder somewere you don't forget.
2. You modify the two files adding into the bat file at the end the name of your Wireguard profile and changing the first two variables of the python file.
3. Open the window Task Scheduler and add a task, the trigger is an avent called *Microsoft-Windows-NetworkProfile/Operational* the surce is *NetworkProfile* and the Event ID is 10000, the action is starting the python script. Activate *Run with higher privilages* and *Run whether user is logged in or not* in the General tab and change the last option of the Settings tab to *Stop the existing Instance*. Change the settings of the Condition Tab to your preferences.
4. Do the same with the bat script changing the Event ID to 10001
5. Finish
