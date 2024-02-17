# How to migrate from an existing Django project to a tailwind-hot-reload projetc


Copy project template from https://github.com/timonweb/django-tailwind/tree/master/example


1. Use the exisiting Dockerfile and docker-compose.yml (adjust only if needed, based on existing project)

2. delete folder 'project'

3. requirements.txt: add 'django-tailwind[reload]'

4. copy over 'manage.py' from existing project

5. copy over 'project' folder from existing project (sometimes called 'core')

6. project/settings.py: 
    - INSTALLED_APPS : add "django_browser_reload", "tailwind", "theme"
    - MIDDLEWARE: add "django_browser_reload.middleware.BrowserReloadMiddleware"
    - add TAILWIND_APP_NAME = "theme"
    - add TAILWIND_DEV_MODE = DEBUG

7. project/urls.py:
    - urlpatterns : add path("__reload__/", include("django_browser_reload.urls"))

8. copy folders like home, static, templates from existing project

9. copy files from root folder (yamls, configs, scripts...) from existing project
