# online-assessment-server

## Description
Example server using Python, Django, and Django Rest Framework. Currently deployed on Render and using an external PostgreSQL database hosted on Supabase.

You can view an example of its usage on this [deployed site.](https://warm-blancmange-a405eb.netlify.app/)

## Details
Has two endpoints:
* /recipes/
* /recipes/:id/

The Recipe model is as follows:
* id
* title
* description
* image_url*
* view_count*

*Image_url and view_count are placeholders in this example. Image_url is a randomly generated integer that references a random image hosted on the client.
