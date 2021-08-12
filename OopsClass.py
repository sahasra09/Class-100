class Car(object):
    def __init__(self,color,model,company,speed_limit):
        self.color=color
        self.model=model
        self.company=company
        self.speed_limit=speed_limit
    
    def start(self):
        print('The car has started')

    def stop(self):
        print('The car has stopped')

    def accelerate(self):
        print('accelerating...')

    def change_gear(self,gear_type):
        print('The gear switched to ',gear_type)

bugattiChiron=Car('black','bugatti Chiron','Bugatti','480')
print(bugattiChiron.color)
bugattiChiron.start()
bugattiChiron.accelerate()
bugattiChiron.change_gear('5')
bugattiChiron.stop()

