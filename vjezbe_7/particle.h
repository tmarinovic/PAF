class Particle 
  {  
    private:
        double t, x, y, v_x, v_y;  
        double dt;
        double g = -9.81;
        double r_o, t_o;
        double alpha;

        void evolve();

    public:
        Particle(double vo, double alpha, double xo, double yo, double step = 0.001);
        double range();
        double totalTime();
  };
  