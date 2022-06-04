# Emails with Django

## Description

Currently following
[codewithmosh.com's](https://codewithmosh.com/p/the-ultimate-django-series)
ultimate Django series.

In part 3, we learn about advanced concepts regarding Django utilities. In
section two we dive into how to send and work with emails in Django.

This repository serves as a reference for how to work with emails in Django.

### Fake SMPT Server

We created a mock email server using Docker and the following library:
https://github.com/rnwood/smtp4dev

To run the locally with Docker, use the following command:
`docker run --rm -it -p 3000:80 -p 2525:25 rnwood/smtp4dev`

This will pull the image from DockerHub and create the email server on your
computer.

Once the build is complete, you can view the email server's admin panel at:
`http://localhost:3000`

### Email Backend Config

Django comes equipped with several email backends that suite various use cases.

The course only focused on the SMPT config, but its pretty straight forward to
swap it out in favor of another.

Here's a link for more: https://docs.djangoproject.com/en/4.0/topics/email/

### Sending an email

The project is configured to send an email when you visit
`localhost:8000/playground/hello/`.

Once the page loads, you can navigate to the SMPT admin where you should find an
email waiting.

**Note:** For the email to send make sure the SMPT server we started earlier and
the Django development server are both running! 🙃
