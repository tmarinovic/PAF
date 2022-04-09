#include <iostream>

void brojevi(float a1, float b1, float c1, float a2, float b2, float c2){

    float d = a1*b2 - b1*a2;                /*    a1/a2 = b1/b2 = c1/c2     */
    float x = (c1*b2 - b1*c2)/ d;
    float y = (a1*c2 - c1*a2)/ d;

    if(d != 0){
        std::cout << "x iznosi: " << x <<" \n y iznosi: "<< y;
        
    } else{
        printf("Jednadzba nema rjesenja.\n");
    }
}

int main() {
    brojevi(1,2,3,4,5,6);

    return 0;
}