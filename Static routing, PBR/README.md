Static routes

Настроены статические маршруты между маршрутизаторами ZL-R1, LP-R5, DP-R9 и OV-R13;

![Иллюстрация к проекту](https://github.com/vladimirvolfovich93/Part1/blob/main/Static%20routing%2C%20PBR/Static%20routes.png)

PBR

На PF-R19 настроена политика маршрутизации так, что пакеты до OV-R13 ходят через PG-R18, PF-R20;

На PF-R19 настроена политика маршрутизации так, что пакеты до LP-R5 ходят через PG-R18, PG-R17;

![Иллюстрация к проекту](https://github.com/vladimirvolfovich93/Part1/blob/main/Static%20routing%2C%20PBR/PBR.png)
