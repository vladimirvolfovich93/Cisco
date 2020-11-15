OSPF Filter-Lists

Настроен OSPF на R3, зоне 42 известен только маршрут по-умолчанию. Назначен stub на R3, R14, R8 в зоне 42(totaly stub);

В зону 10 не попадают маршруты из зоны 42. Из зоны 0 все маршруты известны. На R2 и R24 отфильтрованы приходящие LSA type 3:

conf t
 ip prefix-list FILTER-area42to10 deny 35.10.64.0/24
 ip prefix-list FILTER-area42to10 deny 35.10.65.0/25
 ip prefix-list FILTER-area42to10 deny 35.10.65.128/27
 ip prefix-list FILTER-area42to10 permit 0.0.0.0/0 le 32
 router ospf 10
  area 10 filter-list prefix FILTER-area42to10 in
  exit
 exit;

Все маршрутизаторы в OSPF доступны между собой, на ZL-R1(OSPF 10: default-iformation originate) распространяется маршрут по умолчанию;

![Иллюстрация к проекту](https://github.com/vladimirvolfovich93/Part1/blob/main/OSPF%20Filter-Lists/OSPF%20filter-lists.png)
