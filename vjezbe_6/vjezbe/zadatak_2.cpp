#include <iostream>

using namespace std;

void kruznica(float x, float y, float p, float q, float r){
    float d =  (x-p)*(x-p) + (y-q)*(y-q);
    float R = r*r;
    
    if (d==R) {
        cout << "tocka se nalazi na kruznici.";
    } else if (d<R) {
        cout << "tocka se nalazi unutar kruznice.";
    } else {
        cout << "tocka se nalazi van kruznice.";
    }

}


int main() {

    kruznica(2,3,6,7,9);

    return 0;
}