.. note:: python 3.8.5, all other dependencies in requirements.txt. Use virtual environments
.. note:: ADD ENVIRONMENT VARIABLES

.. note:: SECRET_KEY="django secret key"
.. note:: DEBUG=True
.. note:: PY_HUNTER_KEY="YOUR PY_HUNTER API KEY"
.. note:: CLEARBIT_KEY="YOUR CLEARBIT API KEY"

.. note:: Bot config file config.json at BASE_DIR

.. rubric:: **signup**

*URL*
/auth/signup/

*Method*
``POST``

*Data Params*
.. code:: json
{
"username": "string",
"password": "string",
"password2": "string(must be the same as password)",
"email": "string",
"first_name": "string",
"last_name": "string"
}

*Success Response*
- Code: 201
*Error Response*
- Code: 400

.. rubric:: **login**

*URL*
/auth/login/

*Method*
``POST``

*Data Params*
.. code-block:: JSON
{
"username": "string",
"password": "string"
}

*Success Response*
- Code: 200
Tokens:
.. code-block:: JSON
{
"refresh": "string",
"access": "string"
}
*Error Response*
- Code: 400

.. rubric:: **get post data**

*URL*
/api/posts/

*Methods*
``GET`` ``POST``

*Data GET Params*
Headers:
Content-Type: application/json
Authorization: Bearer <your access token here>

*Data POST Params*
Headers:
Content-Type: application/json
Authorization: Bearer <your access token here>
.. code-block:: JSON
{
"title": "string",
"content": "string",
"like": number,
"dislike": number,
"user": number <user.id>
}
*Success Response*
- Code: 200
.. code-block:: JSON
[
{
"id": 1,
"title": "string",
"content": "string",
"like": number,
"dislike": number,
"created": "2021-02-16T16:24:06.407516Z",
"user": 1
}
]
*Error Response*
- Code: 401

.. rubric:: **update data**

*URL*
/api/posts/<id>/

*Methods*
``PUT``

*Data PUT Params*
Headers:
Content-Type: application/json
Authorization: Bearer <your access token here>
.. code-block:: JSON
{
"id": number,
"like": 10
}
*Success Response*
- Code: 200
.. code-block:: JSON
[
{
"id": 1,
"title": "string",
"content": "string",
"like": number,
"dislike": number,
"created": "2021-02-16T16:24:06.407516Z",
"user": 1
}
]
*Error Response*
- Code: 401
