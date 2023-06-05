
#write class dec


#write function dec



class lasergun:

    isToy = False


    def __init__(self, damage, ammoSize, ammo):
        self._damage = damage
        self._ammoSize = ammoSize
        self._ammo = ammo
    
    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        self._damage = value

    
    def shoot(self, value=1):

        if self._ammo > 0:
            self._ammo -= value               
            if self._ammo <= 0:
                self._ammo = 0
            print("Shooting!")            
        else:
            print("oh no, i have no ammo")

        
        print(f"You have {self._ammo} ammo left")

    def reload(self):
        print(f"ammo is {self._ammo}, I'm reloading")
        self._ammo = self._ammoSize
        print(f"ammo is {self._ammo}")



myLasergun = lasergun(100,20,20)

myLasergun.shoot()

myLasergun.reload()
