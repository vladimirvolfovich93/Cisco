OSPF - NBMA networks

Настроен OSPF в DMVPN между ZL-R1, OV-R13, DP-R9, LP-R5;

Настроен OSPF для R22-R24;

Настроен Virtual Link для работы зоны 0 OSPF;

В зоне 0 broadcast для минимальной скорости обнаружения неполадок используется технология Fast Hello;

В остальных зонах таймеры оптимизированы до значений 3/12;

В зоне NBMA между ZL-R1, LP-R5 и OV-R13 таймеры 20/60, а на ZL-R1 ручное указание соседей и приоритет при выборах;

В зоне point-to-point между R1 и R9 таймеры 20/60;

Включена парольная аутентификация в режиме MD5;

Неиспользуемые сейчас интерфейсы переведены в режим Passive;


![Иллюстрация к проекту](https://github.com/vladimirvolfovich93/Part1/blob/main/OSPF%20-%20NBMA%20networks/OSPF%20with%20PtP%20%26%20NBMA.png)
