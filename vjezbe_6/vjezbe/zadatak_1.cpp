#include <iostream>

using namespace std;
void pravac(float x, float y, float p, float q){
    float result = (p-x)/(q-y);
    cout << "Jednadzba pravca je y - " << y <<" = "<< result << " * x - "<< x;
}

int main(){
    pravac(4,8,3,3);
    return 0;
}
