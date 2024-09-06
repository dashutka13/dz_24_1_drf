Docker

Клонируйте содержимое данного репозитория к себе: https://github.com/dashutka13/dz_24_1_drf.git

.env добавьте данные из env.sample.

Поднять и собрать проект командой: docker-compose up -d --build.

Для создания superuser: docker-compose exec python manage.py csu.

Для остановки проекта, удаления всех контейнеров, сетей и томов: docker-compose down -v.