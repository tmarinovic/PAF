
import particle1 as prt

p1 = prt.Particle()

p1.init(10,60,0,0,0.01)   

print("Ukupno vrijeme trajanja gibanje iznosi: s", p1.total_time())
print("Najveca ostvarena brzina iznosi: m/s",p1.max_speed())

p1.velocity_to_hit_target(4,4,1)  

p1.reset()

p1.init(10,60,0,0,0.01)
p1.angle_to_hit_target(4,2,0.5)  
p1.reset()