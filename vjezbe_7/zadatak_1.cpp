#include <iostream>
#include <math.h>
#define _USE_MATH_DEFINES
#include <vector>
using namespace std;
#ifndef M_PI
    #define M_PI 3.14159265358979323846 
#endif

class Particle        
{
  public:                 
    double vo, alphao, xo, yo, dt;    
    double alpha; 
    double vx, vy;
    vector< double > xx;
    vector< double > yy;
    double r_o, t_o;

    Particle(double v_o_, double alphao_, double xo_, double yo_, double dt_)
    {
      alpha = (alphao_ * M_PI) / 180;
      vx = v_o_ * cos(alpha);    
      vy = v_o_ * sin(alpha);
      dt = dt_;
      r_o = xo_;
      t_o = 0.0;
      xo = xo_;
      yo = yo_;
    }
    
  private: 
    void move() 
    { 
      for(int i; i <= 10000; i++)
      { 
        xo = xo + vx * dt;
        vy = vy - 9.81 * dt;
        yo = yo + vy * dt;
        xx.push_back(xo);
        yy.push_back(yo);
        t_o = t_o + dt;
        if(yo <= 0)
        {
          break;
        }
      }
    }

  public:    
    void range()
    {
      move();  
      double r = xo - r_o;
      cout << "projektil 'range': " << r << " m" << endl;  
    }

      void totalTime()
      {        
        move();
        double t = t_o;
        cout << "ukupno vrijeme: " << t << " s" << endl;
      }
};


int main()
{
  Particle p1(100.0, 45.0, 0.0, 0.0, 0.01);
  p1.range();
  p1.totalTime();

  Particle p2(15.0, 40.0, 3.0, 3.0, 0.01);
  p2.range();
  p2.totalTime();

  return 0;
}