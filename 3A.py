#Magician
import time
# nastavy senzor zjistovani barvy
dType.SetColorSensor(api, 0, 1, version=1)

color = ""
while True:
	# zjistuje barvu kostky v loopu
	while color not in ("R","G","B",):
		dType.SetColorSensor(api, 0, 1, version=2)
		if(dType.GetColorSensor(api)[0]==1):
			color = "R"
			new_x = 273 
			new_y = -60
			new_z = -40 
		if(dType.GetColorSensor(api)[1]==1):
			color = "G"
			new_x = 172 
			new_y = -124
			new_z = -40
		if(dType.GetColorSensor(api)[2]==1):
			color = "B"
			new_x = 238
			new_y = -87
			new_z = -40
		dType.SetColorSensor(api, 1, 1, version=1)
		print(color)
	
	# polozi kostku dle barvy
	dType.SetPTPCmd(api, 2, 64, 266, 50, 0, 1)
	dType.SetPTPCmd(api, 2, 64, 266, 19, 0, 1)
	dType.SetEndEffectorSuctionCup(api, 1,  1, isQueued=1)
	time.sleep(1)
	dType.SetPTPCmd(api, 2, 64, 266, 50, 0, 1)
	# place
	dType.SetPTPCmd(api, 2, new_x, new_y, 50, 0, 1)
	dType.SetPTPCmd(api, 2, new_x, new_y, new_z, 0, 1)
	dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)
	time.sleep(1)
	dType.SetPTPCmd(api, 2, new_x, new_y, 50, 0, 1)
	# place
	dType.SetPTPCmd(api, 2, 64, 266, 50, 0, 1)
	color = ""
	
	
	
