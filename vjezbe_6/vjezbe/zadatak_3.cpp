#include <iostream>
#include <list>
#include <iterator>
#include <algorithm>

using namespace std;

void polje(list <int> lista){

    list <int> :: iterator it;
    for(it = lista.begin(); it != lista.end(); ++it)
        cout << '\t' << *it;
    cout << '\n';
}

int main() {

    list<int> lista;
    lista.push_back(2);
    lista.push_back(-3);
    lista.push_back(4);
    lista.push_back(0);
    lista.push_back(-6);
    lista.push_back(5);

    cout << "\n pocetna lista : ";
    polje(lista);

    cout << "\n lista nakon okretanja redoslijeda : ";
    lista.reverse();
    polje(lista);

    cout << "\n lista nakon zamjene clanova : ";
    using std::swap;
    for (auto it = std::begin(lista); it != std::end(lista); it = std::adjacent_find(it, std::end(lista), std::less<int>{})) {
    swap(*it, *std::next(it));
    }
    polje(lista);

    cout << "\n lista nakon sortiranja clanova polja je : ";
    lista.sort();
    polje(lista);

    return 0;

}