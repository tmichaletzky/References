#include <iostream>
#include <map>
#include <vector>


using namespace std;

// A küldetés, hogy a lázadók megsemmisítő csapást mérjenek a Halálcsillagra.
// A Halálcsillag erejét egy részfeladat megoldásával lehet csökkenteni.

class Jedi{
    string name;
    string rang;
    int power;
    friend bool operator== (const Jedi& left, const Jedi& right);
public:
    string get_name(){return name;}
    string get_rang() {return rang;}
    int get_power() {return power;}
    Jedi(const string& j_name, const string& j_rang, const int& j_power){
        name=j_name;
        rang=j_rang;
        power=j_power;
    }
    void power_up(const int& force){
        power+=force;
    }

};

bool operator==(const Jedi& left, const Jedi& right){
    return left.name==right.name && left.rang==right.rang && left.power==right.power;
}

class JediCouncil{
    map<string, vector<Jedi> >  my_council;
public:
    void add(Jedi& new_jedi) {
        if(new_jedi.get_name() == "Anakin"){
            new_jedi.power_up(5);
        }else{
            new_jedi.power_up(10);
	}
        my_council[new_jedi.get_rang()].push_back(new_jedi);
    }

    int member_number(const string& rang){
        int counter=0;
        for(map<string, vector<Jedi> >::iterator i = my_council.begin(); i != my_council.end(); ++i){
            for(vector<Jedi>::iterator j = (i->second).begin(); j != (i->second).end(); ++j){
                if(j->get_rang() == rang){
                    counter++;
                }
            }
        }
        return counter;
    }

    void print(){
        for(map<string, vector<Jedi> >::iterator i = my_council.begin(); i != my_council.end(); ++i){
            for(vector<Jedi>::iterator j = (i->second).begin(); j != (i->second).end(); ++j){
                cout << j->get_name() << endl;
            }
        }
    }

    bool is_member(const Jedi& my_jedi){
       for(map<string, vector<Jedi> >::iterator i = my_council.begin(); i != my_council.end(); ++i){
            for(vector<Jedi>::iterator j = (i->second).begin(); j != (i->second).end(); ++j){
                if(my_jedi == *j){
                    return true;
                }
            }
        }
        return false;
    }


    string strongest(const string& rang){
        Jedi first_jedi = *my_council[rang].begin();
        for(vector<Jedi>:: iterator j = my_council[rang].begin(); j != my_council[rang].end(); ++j){
            if(j->get_power() > first_jedi.get_power()){
                first_jedi = *j;
            }
        }
        return first_jedi.get_name();
    }


};



int main()
{
  int death_star_power = 4;


  // - Készítsünk egy Jedi osztályt, ami egy jedi nevét, rangját és erejét
  // tárolja el (std::string name, std::string rank, int power). Készítsünk
  // lekérdező műveleteket is az adattagokhoz (get_name(), get_rank(),
  // get_power()).

  Jedi j1("Anakin", "Knight", 15);
  Jedi j2("Obiwan", "Knight", 14);
  Jedi j3("Ashoka", "Padawan", 10);
  Jedi j4("Yoda", "Master", 25);

  if (j1.get_power() == 15)
  {
    death_star_power -= j1.get_power() - j2.get_power();
  }



  // - Készítsünk egy JediCouncil osztályt, ami a jedi tanácsot reprezentálja.
  // Ebben tároljuk el a jedi tagokat rangjuk szerint. Egy ranghoz több jedi
  // is tartozhat.
  // - Készítsünk műveletet, amivel a jedi tanácshoz hozzárendelhetünk újabb
  // jediket (add). Ekkor a jedi ereje 10-zel megnő.
  // - Készítsünk egy member_number() függvényt, ami megadja, hogy hány adott
  // rangú jedi van a tanácsban.

  JediCouncil council;
  council.add(j1);
  council.add(j2);
  council.add(j3);
  council.add(j4);

  if (j2.get_power() == 24)
  {
    death_star_power -= council.member_number("Padawan");
  }



  // - Készítsünk egy tagfüggvényt a jedi tanács osztályhoz, amivel kiírhatjuk
  // a képernyőre a tanács tagjait.
  // - Készítsünk egy is_member() tagfüggvényt, amivel eldönthetjük, hogy egy
  // adott jedi tagja-e a tanácsnak.
  // - Módosítsuk az add() függvényt úgy, hogy amikor Anakin nevű jedit adunk
  // hozzá, akkor kerüljön be a tanácsba, de a rangja csak 5-tel emelkedjen.

  council.print();
  if (council.is_member(j1) && j1.get_power() == 20 &&
      council.is_member(j2) && j2.get_power() == 24)
  {
    death_star_power -= 1;
  }



  // - Készítsünk egy tagfüggvényt a jedi tanás osztályhoz, ami megadja a
  // legerősebb, adott rangú jedi nevét.

  if (council.strongest("Knight") == "Obiwan")
  {
    death_star_power -= 1;
  }


  std::cout
    << "Az eddig elért érdemjegy: "
    << 5 - death_star_power
    << std::endl;

  return 0;
}
