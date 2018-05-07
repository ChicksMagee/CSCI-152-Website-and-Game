import time
click("1525157664106.png")
wait(12)
click("1525157713709.png")
wait(5)
doubleClick("1525158941766.png")

wait(5)
if(exists("1525676846339.png")):popup("Transfer test passed")
else: popup("transfer failed")        

