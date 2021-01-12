
import serial 
printer=serial.Serial("/dev/ttyAMA0",baudrate=9600,timeout=1)

def feedTicket():
	for i in range(0,7):
		printer.write("\n")

#printing

def printSeatNumber(seat) :
	seatNumber=[4, 4, 28, 4, 28, 20, 28, 4, 92, 20, 92, 4, 254, 10, 14, 0, 252, 0, 0, 7, 8, 14, 10, 14, 4, 2, 186, 42, 188, 1, 18, 12]
	seatNumberLength=32
	zoomTo(1)
	printer.write("Seat Number:   %2i   :" % seat)
	printPoints(seatNumber,seatNumberLength)
	printer.write("\n")


def printSeatNumber(seat1,seat2):
	seatNumber=[4, 4, 28, 4, 28, 20, 28, 4, 92, 20, 92, 4, 254, 10, 14, 0, 252, 0, 0, 7, 8, 14, 10, 14, 4, 2, 186, 42, 188, 1, 18, 12]
	seatNumberLength=32
	zoomTo(1)
	printer.write("Seat Number:   %2i, %2i  :" % (seat1,seat2))
	printPoints(seatNumber,seatNumberLength)
	printer.write("\n")

def printSeatNumber( seat1, seat2, seat3):
	seatNumber=[4, 4, 28, 4, 28, 20, 28, 4, 92, 20, 92, 4, 254, 10, 14, 0, 252, 0, 0, 7, 8, 14, 10, 14, 4, 2, 186, 42, 188, 1, 18, 12]
	seatNumberLength=32
	zoomTo(1)
	printer.write("Seat Number:   %2i,%2i,%2i  :" % (seat1,seat2,seat3))
	printPoints(seatNumber,seatNumberLength)
	printer.write("\n")

def printSeatNumber(seat1, seat2, seat3, seat4):
	seatNumber=[4, 4, 28, 4, 28, 20, 28, 4, 92, 20, 92, 4, 254, 10, 14, 0, 252, 0, 0, 7, 8, 14, 10, 14, 4, 2, 186, 42, 188, 1, 18, 12]
	seatNumberLength=32
	zoomTo(1)
	printer.write("Seat Number: %2i,%2i,%2i,%2i  :" % (seat1,seat2,seat3,seat4))
	printPoints(seatNumber,seatNumberLength)
	printer.write("\n")



def printBusNumber(bus):
	busNumber=[14, 2, 2, 14, 4, 12, 4, 12, 4, 5, 5, 12, 5, 28, 0, 29, 21, 31, 68, 92, 0, 2, 62, 2, 126, 0, 127, 0, 0, 7, 8, 14, 10, 14, 4, 2, 186, 42, 188, 1, 18, 12]
	busNumberLength=42
	zoomTo(1)
	printer.write("Bus Number :   %2i  : " % bus)
	printPoints(busNumber,busNumberLength)
	printer.write("\n")


def printDate( d):
	date=[54, 43, 169, 57, 40, 10, 10, 56, 2, 20, 24, 0, 248, 8, 72, 88, 8, 248, 0, 248]
	dateLength=20
	zoomTo(1)
	printer.write("Date :     %s   : " % d)
	printPoints(date,dateLength)
	printer.write("\n")

def printTime( t):
	time=[14, 34, 2, 34, 6, 2, 186, 42, 190, 0, 29, 21, 31, 4, 252, 0, 252]
	timeLength=17
	zoomTo(1)
	printer.write("Time :      %s    :  " % t)
	printPoints(time,timeLength)
	printer.write("\n")

def printFrom(station):
	fro=[28, 68, 4, 60, 16, 16, 56, 40, 56]
	froLength=9
	zoomTo(1)
	printer.write("From :        %s     :   " % station)
	printPoints(fro,froLength)
	printer.write("\n")


def printTo(station):
	to=[30, 2, 10, 250, 14, 0, 252]
	toLength=7
	zoomTo(1)
	printer.write("To   :        %s     :   " % station)
	printPoints(to,toLength)
	printer.write("\n")


def printCost( c):
    cost=[184, 168, 60, 4, 28, 84, 28, 4, 252, 4, 68, 188, 132, 132, 44, 36, 4, 252, 0, 252]
    costLength=0x14
    zoomTo(1)
    printer.write("Cost :       %2.2f      : " % c)
    printPoints(cost,costLength)
    printer.write("\n")



def printPoints( msg, lenght):
	zoomTo(3)
	printer.write(serial.to_bytes([0x1b,0x4b,lenght,0x00])) #ESC K Command
	for i in range(lenght):
		printer.write(serial.to_bytes([msg[i]]))
  


def printTicket1( busNum, seat1,fromStation, toStation,cost, line, date,time):
    printTime(time)
    printDate(date)
    printCost(cost/100.0)
    printTo("Nazla")
    printFrom("Ma7ta")
    printSeatNumber(seat1)
    printBusNumber(busNum)
    feedTicket()


def printTicket2( busNum, seat1, seat2,fromStation, toStation,cost, line, date, time):
    printTime(time)
    printDate(date)
    printCost(cost/100.0)
    printTo("Nazla")
    printFrom("Ma7ta")
    printSeatNumber(seat1,seat2)
    printBusNumber(busNum)
    feedTicket()


def printTicket3( busNum, seat1, seat2, seat3,fromStation, toStation,cost, line, date, time):
    printTime(time)
    printDate(date)
    printCost(cost/100.0)
    printTo("Nazla")
    printFrom("Ma7ta")
    printSeatNumber(seat1,seat2,seat3)
    printBusNumber(busNum)
    feedTicket()


def printTicket4( busNum, seat1, seat2, seat3, seat4,fromStation, toStation,cost, line, date, time):
	printDate(date)
	printTime(time)
	printCost(cost/100.0)
	printTo("Ma7ta")
	printFrom("seed")
	printSeatNumber(seat1,seat2,seat3,seat4)
	printBusNumber(busNum)
	feedTicket()


#Formating
#Spacing
def setLineSpacing( n):
	printer.write(serial.to_bytes([0x1b,0x31,n]))

#Magnification
#Change font size
#values between 1 and 8
def verZoomTo(n):
	printer.write(serial.to_bytes([0x1b,0x56,n]))
	

def horZoomTo( n):
	printer.write(serial.to_bytes([0x1b,0x57,n]))
	


def zoomTo( n):
	verZoomTo(n)
	horZoomTo(n)


def zoomTo2( w, h):
	printer.write(serial.to_bytes([0x1B,0x58,w,h]))
	

###################

#UnderLine
def allowUnderline():
	printer.write(serial.to_bytes([0x1B,0x2D,1]))
	


def disableUnderline():
	printer.write(serial.to_bytes([0x1B,0x2D,0]))
	



#rotation
#All rotation is CCW (CounterClockWise)
def rotate0():
	printer.write(serial.to_bytes([0x1C,0x49,0]))


def rotate90():
	printer.write(serial.to_bytes([0x1C,0x49,1]))
	

def rotate180():
	printer.write(serial.to_bytes([0x1C,0x49,2]))
	

def rotate270():
	printer.write(serial.to_bytes([0x1C,0x49,3]))
	

setLineSpacing(3)
printTicket4(10,1,2,3,4,"xz","zx",550,2,"09-04-2018","10:59AM")
#printDate( "09-04-2018")