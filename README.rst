**signup**

*URL*
/auth/signup/

*Method*
``POST``

*Data Params*
.. code-block:: JSON
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

**login**

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

**get post data**

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
