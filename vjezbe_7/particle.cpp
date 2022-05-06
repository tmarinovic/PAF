#include <iostream>
#include <particle.h>
#include <math.h>
#include <vector>
using namespace std;
#ifndef M_PI
    #define M_PI 3.14159265358979323846 
#endif


Particle::Particle(double vo, double alphao, double xo, double yo, double step)
{ 
  alpha = (alphao * M_PI) / 180;
  v_x = vo * cos(alpha);    
  v_y = vo * sin(alpha);
  dt = step;
  r_o = xo;
  t_o = 0.0;
  x = xo;
  y = yo;
};

void Particle::evolve()
{
  while(y >= 0)
  {
    v_x += 0.;
    v_y += g*dt;
    x += v_x * dt;
    y += v_y * dt;
    t += dt;
  }
}

double Particle::range()
{
  evolve();  
  double r = x - r_o;
  cout << "Projektil 'range': " << r << " m" << endl;
  return 0;
}

double Particle::totalTime()
{
  evolve();
  double T = t;
  cout << "ukupno vrijeme: " << T << " s" << endl;
  return 0;
}