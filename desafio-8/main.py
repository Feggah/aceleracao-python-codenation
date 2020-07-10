
doc = '''
#%RAML 1.0
title: api
version: 1
baseUri: http://localhost/api
mediaType:
  - application/json
protocols:
  - [HTTPS]
securitySchemes:
  JWT:
    description: JWT authentication
    type: x-JWT
    settings:
      signatures: ['HMAC-SHA256']
    describedBy:
      headers:
        Authorization:
          type: string
      responses:
        body:
          application/json:
            401:
              description: {"error": "Unauthorized"}

types:
  Auth:
    type: object
    discriminator: token
    properties:
      token: 
        required: true
        type: string

  Agent:
    type: object
    discriminator: agent_id
    properties:
      agent_id:
        required: true
        type: integer
      name:
        required: true
        type: string
        maxLength: 50
      status: 
        required: true
        type: boolean
      environment:
        required: true
        type: string
        maxLength: 20
      version:
        required: true
        type: string
        maxLength: 5
      address:
        required: true
        type: string
        maxLength: 39
      user_id: integer
    example:
      agent_id: 1
      name: Gabriel
      status: false
      environment: Windows
      version: 1.0
      address: 127.0.0.1
      user_id: 1

  User:
    type: object
    discriminator: user_id
    properties:
      user_id: 
        required: true
        type: integer
      name:
        required: true
        type: string
        maxLength: 50
      last_login: 
        required: true
        type: date
      email:
        required: true
        type: string
        maxLength: 254
      password:
        required: true
        type: string
        maxLength: 50
    example:
      user_id: 1
      name: Ricardo
      last_login: 2020-07-07
      email: ricardo@ricardo.com
      password: pass123


  Event:
    type: object
    discriminator: event_id
    properties:
      event_id: 
        required: true
        type: integer
      level:
        required: true
        type: string
        maxLength: 20
      payload:
        required: true
        type: string
      shelve: 
        required: true
        type: boolean
      date: 
        required: true
        type: datetime
      agent_id: integer
    example:
      event_id: 1
      level: DEBUG
      payload: payload
      shelve: true
      date: 2020-07-07T00:00:00
      agent_id: 1

  Group:
    type: object
    discriminator: group_id
    properties:
      group_id:
        required: true
        type: integer
      name:
        required: true
        type: string
        maxLength: 20
    example:
      group_id: 1
      name: Programmers

/auth/token:
  post:
    description: Create a JWT token
    body:
      application/json:
        username: string
        password: string
      responses:
        201:
          body:
            application/json:
              type: Auth
        400:
          body:
            application/json:
              description: {"error": "Bad request"}

/agents:
  get:
    description: Gets the agents list
    securedBy: JWT
    responses:
      200:
        body:
          application/json:
            type: Agent[]
      401:
        body:
          application/json:
            description: {"error": "Unauthorized"}
      403:
        body:
          application/json:
            description: {"error": "Forbidden"}
  post:
    description: Create a new agent
    securedBy: JWT
    body:
      application/json:
        type: Agent
    responses:
      201:
        body:
          application/json:
            description: {"message": "Created"}
      400:
        body:
          application/json:
            description: {"error": "Bad request"}
      401:
        body:
          application/json:
            description: {"error": "Unauthorized"}
      403:
        body:
          application/json:
            description: {"error": "Forbidden"}
  /{id}:
    get:
      description: Get a agent with the given ID
      securedBy: JWT
      responses:
        200:
          body:
            application/json:
              type: Agent
        401:
          body:
            application/json:
              description: {"error": "Unauthorized"}
        403:
          body:
            application/json:
              description: {"error": "Forbidden"}
        404:
          body:
            application/json:
              description: {"error": "Not found"}
    put:
      description: Update a agent with the given ID
      securedBy: JWT
      body:
        application/json:
          type: Agent
      responses:
        200:
          body:
            application/json:
              description: {"message": "OK"}
        400:
          body:
            application/json:
              description: {"error": "Bad request"}
        401:
          body:
            application/json:
              description: {"error": "Unauthorized"}
        403:
          body:
            application/json:
              description: {"error": "Forbidden"}
    delete:
      description: Delete a agent with the given ID
      securedBy: JWT
      responses:
        200:
          body:
            application/json:
              description: {"message": "OK"}
        401:
          body:
            application/json:
              description: {"error": "Unauthorized"}
        403:
          body:
            application/json:
              description: {"error": "Forbidden"}
        404:
          body:
            application/json:
              description: {"error": "Not found"}
  /{id}/events:
    get:
      description: Gets all events associated with the agent
      securedBy: JWT
      responses:
        200:
          body:
            application/json:
              type: Event[]
        401:
          body:
            application/json:
              description: {"error": "Unauthorized"}
        403:
          body:
            application/json:
              description: {"error": "Forbidden"}
    post:
      description: Creates a new event for the agent
      securedBy: JWT
      body:
        application/json:
          type: Event
      responses:
        201:
          body:
            application/json:
              description: {"message": "Created"}
        400:
          body:
            application/json:
              description: {"error": "Bad request"}
        401:
          body:
            application/json:
              description: {"error": "Unauthorized"}
        403:
          body:
            application/json:
              description: {"error": "Forbidden"}

    /{id}/events/{id}:
      get:
        description: Gets a specific event given event ID and agent ID
        securedBy: JWT
        responses:
          200:
            body:
              application/json:
                type: Event
          401:
            body:
              application/json:
                description: {"error": "Unauthorized"}
          403:
            body:
              application/json:
                description: {"error": "Forbidden"}
          404:
            body:
              application/json:
                description: {"error": "Not found"}
      put:
        description: Updates a specific event
        securedBy: JWT
        body:
          application/json:
            type: Event
        responses:
          200:
            body:
              application/json:
                description: {"message": "OK"}
          400:
            body:
              application/json:
                description: {"error": "Bad request"}
          401:
            body:
              application/json:
                description: {"error": "Unauthorized"}
          403:
            body:
              application/json:
                description: {"error": "Forbidden"}
          404:
            body:
              application/json:
                description: {"error": "Not found"}
      delete:
        description: Deletes a specific event
        securedBy: JWT
        responses:
          200:
            body:
              application/json:
                description: {"message": "OK"}
          401:
            body:
              application/json:
                description: {"error": "Unauthorized"}
          403:
            body:
              application/json:
                description: {"error": "Forbidden"}
          404:
            body:
              application/json:
                description: {"error": "Not found"}

/groups:
  get:
    description: Get the list of all groups
    securedBy: JWT
    responses:
      200:
        body:
          application/json:
            type: Group[]
      401:
        body:
          application/json:
            description: {"error": "Unauthorized"}
      403:
        body:
          application/json:
            description: {"error": "Forbidden"}

  post:
    description: Create a new group
    securedBy: JWT
    body:
      application/json:
        type: Group
    responses:
      201:
        body:
          application/json:
            description: {"message": "Created"}
      400:
        body:
          application/json:
            description: {"error": "Bad request"}
      401:
        body:
          application/json:
            description: {"error": "Unauthorized"}
      403:
        body:
          application/json:
            description: {"error": "Forbidden"}
  /{id}:
    get:
      description: Gets a specific group
      securedBy: JWT
      responses:
        200:
          body:
            application/json:
              type: Group
        401:
          body:
            application/json:
              description: {"error": "Unauthorized"}
        403:
          body:
            application/json:
              description: {"error": "Forbidden"}
        404:
          body:
            application/json:
              description: {"error": "Not found"}
    put:
      description: Updates a specific group
      securedBy: JWT
      body:
        application/json:
          type: Group
      responses:
        200:
          body:
            application/json:
              description: {"message": "OK"}
        400:
          body:
            application/json:
              description: {"error": "Bad request"}
        401:
          body:
            application/json:
              description: {"error": "Unauthorized"}
        403:
          body:
            application/json:
              description: {"error": "Forbidden"}
        404:
          body:
            application/json:
              description: {"error": "Not found"}
    delete:
      description: Deletes a specific group
      securedBy: JWT
      responses:
        200:
          body:
            application/json:
              description: {"message": "OK"}
        401:
          body:
            application/json:
              description: {"error": "Unauthorized"}
        403:
          body:
            application/json:
              description: {"error": "Forbidden"}
        404:
          body:
            application/json:
              description: {"error": "Not found"}
/users:
  get:
    description: Gets the list of all users
    securedBy: JWT
    responses:
      200:
        body:
          application/json:
            type: User[]
      401:
        body:
          application/json:
            description: {"error": "Unauthorized"}
      403:
        body:
          application/json:
            description: {"error": "Forbidden"}
  post:
    description: Create a new user
    securedBy: JWT
    body:
      application/json:
        type: User
    responses:
      201:
        body:
          application/json:
            description: {"message": "Created"}
      400:
        body:
          application/json:
            description: {"error": "Bad request"}
      401:
        body:
          application/json:
            description: {"error": "Unauthorized"}
      403:
        body:
          application/json:
            description: {"error": "Forbidden"}
  /{id}:
    get:
      description: Gets a specific user
      securedBy: JWT
      responses:
        200:
          body:
            application/json:
              type: User
        401:
          body:
            application/json:
              description: {"error": "Unauthorized"}
        403:
          body:
            application/json:
              description: {"error": "Forbidden"}
        404:
          body:
            application/json:
              description: {"error": "Not found"}
    put:
      description: Updates a specific user
      securedBy: JWT
      body:
        application/json:
          type: User
      responses:
        200:
          body:
            application/json:
              description: {"message": "OK"}
        400:
          body:
            application/json:
              description: {"error": "Bad request"}
        401:
          body:
            application/json:
              description: {"error": "Unauthorized"}
        403:
          body:
            application/json:
              description: {"error": "Forbidden"}
        404:
          body:
            application/json:
              description: {"error": "Not found"}
    delete:
      description: Deletes a specific user
      securedBy: JWT
      responses:
        200:
          body:
            application/json:
              description: {"message": "OK"}
        401:
          body:
            application/json:
              description: {"error": "Unauthorized"}
        403:
          body:
            application/json:
              description: {"error": "Forbidden"}
        404:
          body:
            application/json:
              description: {"error": "Not found"}

'''
