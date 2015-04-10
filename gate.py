import random
import time


#funkcja losujaca z przedzialu intigerami
def randN( min, max ):
	temp_F = random.random() * (max-1) + min
	temp_N = temp_F - temp_F%1
	return int(temp_N)


###coin_acceptor -- wrzutnik monet
#	money_load - mozna zaladowac pieniedzmi
#	put_money - wrzut monet
#	accept - zwraca informacje o przepelnieniu
# 	reset - zeruje licznik wrzutnika

class COIN_ACCEPTOR:
	
	def __init__( self, h_many ):
		self.container2 = h_many
		self.counter = 0
		
	def put_money( self, cash ):
		if cash == 2:
			self.counter += 2
			print ">wrzucono 2"
			
	def accept( self ):
		if self.counter > 5:
			return True
		else:
			return False
			
	def reset( self ):
		self.counter = 0
		
	def load( self ):
		self.container2 = 10



###gate -- bramka
#	state - informuje o stanie czyli otwarta/zamknieta
#	try_pass - mozna sprobowac przez nia przejsc
#  coin_acceptor - posiada wrzutnik monet

class GATE:
	def __init__( self ):
		self.state = False
		self.coin_acceptor = COIN_ACCEPTOR( 10 )
	def try_pass( self ):
		if( self.state ):
			return True
		else:
			return False
	def check_state( self ):
		if self.coin_acceptor.accept():
			self.state = True


###Murphy_law -- you know
#	try - zwraca pech lub szczescie, parametrem jest prawdopodobienstwo

# pisze sie.. :)

###cash -- przechowuje walute, tylko jeden egzemplarz
#	value - jak wyzej

class CASH:
	def __init__(self, val ):
		self.value = val

###wallet -- przechowuje cash
#	pocket[] - przechowuje troche cash'u
#	put - mozna wlozyc cash
#	take - losuje lub wrzuca podany argument

class WALLET:
	def __init__(self, money):
		self.pocket = [ money ]
	def take ( self ):
		temp_id = randN( 0, len(self.pocket)-1 ) 
		return self.pocket[ temp_id ] #randomizacja soon
	def put ( self, put_money ):
		self.pocket.append( put_money )
	def count( self ):
		return "nie umiem liczyc"
		
###man -- istota czasami myslaca, (u)Boga w interfejs
#	tellabout() - mowi o czyms, jest 'przeciazona' wieloma typami parametrow//
#..				 		jak mowilem jest myslaca, bedzie probowala cos zrobic

class MAN:
	def __init__( self ):
		self.myWallet = WALLET( CASH( 2 ) )
	def tellabout( self, thing ):
		if	isinstance( thing, WALLET ):
			time.sleep(2)
			print thing.count()  
		elif isinstance( thing, GATE ):
			thing.check_state()
			time.sleep(2)
			if thing.state:
				print "bramka jest otwarta, yupiee..."
			else:
				print "moze wrzuce jeszcze pare monet, moze sie otworzy" 
	def dosth( self, thing, command ):
		if command == "przejdz" :
			time.sleep(2)
			thing.coin_acceptor.reset()
			print "przeszdlem bramke"




#koniec deklaracji - keep your fun


gate = GATE()
ziom = MAN()
while True:

	ziom.myWallet.put( CASH( 2 ) )
	ziom.myWallet.put( CASH( 2 ) )
	ziom.myWallet.put( CASH( "slon" ) )
	ziom.myWallet.put( CASH( 2 ) )
	ziom.myWallet.put( CASH( 2 ) )


	ziom.tellabout( ziom.myWallet )
	ziom.tellabout( gate )
	gate.coin_acceptor.put_money( ziom.myWallet.take().value )
	ziom.tellabout( gate )
	gate.coin_acceptor.put_money( ziom.myWallet.take().value )
	ziom.tellabout( gate )
	gate.coin_acceptor.put_money( ziom.myWallet.take().value )
	ziom.tellabout( gate )
	ziom.dosth( gate, "przejdz" )















