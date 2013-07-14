PostE - Post Extensible
=======================

A extensible post system for Django, where you can build you own Post 
system in few minutes, with several kind of post, like Video Post, Text post, 
Audio Post, Quote Post and your own custom Post.

How to install, for now
-----------------------

Using pip+git:

    pip install git+https://github.com/hersonls/poste.git

How to use
----------

1. Add "poste" to your INSTALLED_APPS setting like this::

    ```Python
    INSTALLED_APPS = (
        ...
        'poste',
    )
    ```

2. Include the poste URLconf in your project urls.py like this::

    ```Python
    url(r'^blog/', include('poste.urls')),
    ```

3. Run `python manage.py syncdb` to create the poste models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a post (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/blog/ to see your posts.


Contribute
----------

Here is a several things what we need implement:

- Tags
- Feed RSS