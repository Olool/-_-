"""
Системы конроля версий:
1. SUN - общий каталог, в который все умеют общий доступ.
Если ошибки попадают в общий репозиторий, то все получают эту ошибку.
2. Распределенная система контроля версий: git.
У каждого разработчика имеется свой локальный репозиторий. Все свои изменения они могут вносить в свой репозиторий (commit), могут перемещаться поистории (checkout). Также есть общий репозиторий (oiginal). Изменения из лок. реп. каждый разработчик может загрузить в общий репозиторий (push), а измения из общ. реп. может загрузить к себе в репозиторий (pull). 
