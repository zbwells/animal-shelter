# Wise County Animal Shelter Management Project

This is the public git repository for the Wise County ASMS (Animal Shelter Management System) project.

The project consists of multiple dynamic web applications (using the Django framework) which in tandem aim to provide a user-friendly web interface from which animal shelters can perform managerial tasks and provide information to the public.

## Purpose 

As of the beginning of the project (January 2023), the shelter in Wise County does most of its managerial tasks via paper, and a large portion of the volunteer workers' time is spent doing paperwork related to the adoption and intake of animals. The project aims to digitize forms which the shelter staff fill out regularly, and to store the data from these forms in a relational database which can be queried via the administrative component of the web interface, and simultaneously used to provide information to a front-facing website. Once this goal has been accomplished, this statement of purpose will be updated to suit a more broad set of goals.

## Details

The project was started in January 2023 as a Senior Capstone project by Computer Science and Management Information Systems students at the University of Virginia's College at Wise, who wanted to collaborate with the local animal shelter to decrease the amount of work involved in running the shelter, as well as help with outreach to the local and surrounding communities. See [CONTRIBUTORS](./CONTRIBUTORS) for information on the individuals involved with the development of the project.

While the system has been written with the Wise County Animal Shelter in mind, the intention is that the software be relatively easy to modify for usage with other shelter organizations. To this end, the project is released under the MIT License, which is a permissive free software license. See [LICENSE](./LICENSE) for details.

## Dependencies

* Python Imaging Library (Pillow 9.x)
* Django 4.x


The project utilizes the Django web application framework to generate dynamic content, and Pillow works in conjunction with Django to provide image processing support to the animal listing application. The exact versions which work with the project have not been thouroughly tested, but using the version branches listed above should result in everything functioning as intended. The dependencies of Django and Pillow respectively are not listed here.

## Hosting

Django applications rely on the WSGI or ASGI communication protocols to talk to fully functional web servers. For hosting this project, we recommned a combination of [nginx](https://nginx.org/en/) and [Gunicorn](https://gunicorn.org/). However, any other web server setup with WSGI or ASGI support should be sufficient. DigitalOcean has a tutorial and hosting Django projects using the aforementioned combination, which can be found [here](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-asgi-django-app-with-postgres-nginx-and-uvicorn-on-ubuntu-20-04).

See the User Manual (yet to be completed) for information on using an already working instance of the project.



