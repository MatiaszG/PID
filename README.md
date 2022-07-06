# PID
Projekt realizuje symulację sterowania członem całkującym przy pomocy dyskretnego regulatora PID. 
Nastawy regulatora jak i zadana wartość podawane są przez użytkownika.
Projekt uruchamia się przez uruchomienie skryptu PID_regulator.py.
Aby projekt się uruchomił, należy zainstalować moduły importowane na początku skryptu PID_regulator.py.
Okno wyświetlone po lewej stronie ekranu przedstawia animowany wykres obrazujący wartość zadaną oraz rzeczywistą.
Okno wyświetlone z prawej strony umożliwia dobranie parametrów regulatora oraz wartości zadanej.
Przycisk "Start\Stop" włącza lub wyłącza proces regulacji.
Warto pamiętać, że przy niewłaściwych nastawach regulatora, układ może utracić stabilność co poskutkuje nie dopasowaniem się wartości rzeczywistej do zadanej.
Zaleca się korzystanie z nastaw parametrów P, I oraz D w zakresie od 0 do 0.5 oraz wartości zadanej (Setpoint) w zakresie od 0 do 100.
