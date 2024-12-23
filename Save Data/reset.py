import time

confirm = input("Are you sure you want to erase all saved data? (Type 'Y' or 'N') THIS ACTION CANNOT BE UNDONE!\n")

if confirm.upper() == "Y" or confirm.upper() == "YES" or confirm.upper() == "TRUE" or confirm.upper() == "'Y'":
    print("Erasing Data...")
    SAVEFILE = open("save.txt", "w")
    SAVEFILE.write("eyJjb2xsZWN0ZWRQb2ludHMiOiAwLCJoaWdoU2NvcmUiOiAwfQ==")
    SAVEFILE.close()
    print("Complete. All data has been reset.")

else:
    print("No Data has been changed.")

print("\nExiting now...")
time.sleep(3)
print(" ")