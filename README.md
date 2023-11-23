# Apex Legends Tournaments Backend

Welcome to the backend repository for the Apex Legends Tournaments website! This Django Rest Framework (DRF) project serves as the backbone for managing and organizing tournaments for the popular game Apex Legends.

[Frontend](https://github.com/shiro47/tournament_website-frontend)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Introduction

This project aims to provide a robust backend system for organizing and managing Apex Legends tournaments. The use of Django Rest Framework ensures a scalable and efficient API for handling various tournament-related functionalities.

## Features

- **Tournament Management:** Create, update, and delete tournaments.
- **Team Registration:** Allow teams to register for upcoming tournaments.
- **User Authentication:** Secure user authentication for tournament organizers and participants.
- **API Documentation:** Detailed API documentation for easy integration with the frontend.

## Database
This project uses PostgreSQL as the database.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Pipenv (for managing Python virtual environment)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shiro47/tournament_website_backend.git
    ```
2. Navigate to the project directory:
    ```bash
   cd tournament_website_backend
    ```
3. Install dependencies using Pipenv:
    ```bash
   pipenv install
    ```
4. Activate the virtual environment:
    ```bash
   pipenv shell
    ```
5. Apply migrations:
    ```bash
    python manage.py migrate
    ```

### Usage

1. Start the development server:
    ```bash
    python manage.py runserver
    ```

The API will be accessible at http://127.0.0.1:8000/. You can explore the API using tools like [Postman](https://www.postman.com/) or integrate it into your frontend application.

## API Endpoints Documentation

### Login

- **Obtain Token**
  - Endpoint: `POST api-auth/login/`
  - Description: Obtain a JWT token for authentication.
  - Request Body:
    ```json
    {
      "username": "your_username",
      "password": "your_password"
    }
    ```
  - Response:
    ```json
    {
      "access": "your_access_token",
      "refresh": "your_refresh_token"
    }
    ```

- **Refresh Token**
  - Endpoint: `POST api-auth/login/refresh/`
  - Description: Refresh an expired JWT token.
  - Request Body:
    ```json
    {
      "refresh": "your_refresh_token"
    }
    ```
  - Response:
    ```json
    {
      "access": "your_new_access_token"
    }
    ```
### Registration

- **Register User**
  - Endpoint: `POST api-auth/register/`
  - Description: Register a new user account.
  - Request Body:
    ```json
    {
      "username": "new_username",
      "password": "new_password",
      "email": "user@example.com"
      // Additional fields as required by your RegisterSerializer
    }
    ```
  - Response:
    ```json
    {
      "id": "user_id",
      "username": "new_username",
      "email": "user@example.com",
      // Additional user details
    }
    ```


Note: Replace `"your_username"`, `"your_password"`, `"your_access_token"`, `"your_refresh_token"`, `"new_username"`, and `"new_password"` with actual values when making requests. Additionally, include any additional fields required by your `RegisterSerializer` in the registration request body.

### Players

- **List Players**
  - Endpoint: `GET /players/`
  - Description: Get a list of all players.

- **Create Player**
  - Endpoint: `POST /players/`
  - Description: Create a new player.
  - Request Body:
    ```json
    {
      "name": "Player Name",
      "platform": "PC",
      "discordID": 123456789,
      "discordName": "Player#123",
      "rank": "Gold III"
    }
    ```

- **Update Player**
  - Endpoint: `PUT /players/{player_id}/`
  - Description: Update an existing player.
  - Request Body:
    ```json
    {
      "name": "Updated Player Name",
      "platform": "PS4",
      "discordID": 987654321,
      "discordName": "UpdatedPlayer#987",
      "rank": "Platinum II"
    }
    ```

- **Partial Update Player**
  - Endpoint: `PATCH /players/{player_id}/`
  - Description: Partially update an existing player.
  - Request Body:
    ```json
    {
      "rank": "Diamond I"
    }
    ```

### Teams

- **List Teams**
  - Endpoint: `GET /teams/`
  - Description: Get a list of all teams.

- **Create Team**
  - Endpoint: `POST /teams/`
  - Description: Create a new team.
  - Request Body:
    ```json
    {
      "name": "Team Name",
      "player1": 1,  // Player ID
      "player2": 2,  // Player ID
      "player3": 3   // Player ID
    }
    ```

- **Update Team**
  - Endpoint: `PUT /teams/{team_id}/`
  - Description: Update an existing team.
  - Request Body:
    ```json
    {
      "name": "Updated Team Name",
      "player1": 4,  // Player ID
      "player2": 5,  // Player ID
      "player3": 6   // Player ID
    }
    ```

- **Partial Update Team**
  - Endpoint: `PATCH /teams/{team_id}/`
  - Description: Partially update an existing team.
  - Request Body:
    ```json
    {
      "name": "Updated Team Name"
    }
    ```

- **Delete Team**
  - Endpoint: `DELETE /teams/{team_id}/`
  - Description: Delete an existing team.

### Tournaments

- **List Tournaments**
  - Endpoint: `GET /tournaments/`
  - Description: Get a list of all tournaments.

- **Create Tournament**
  - Endpoint: `POST /tournaments/`
  - Description: Create a new tournament.
  - Request Body:
    ```json
    {
      "title": "Tournament Title",
      "description": "Tournament Description",
      "rewards": "Tournament Rewards",
      "rules": "Tournament Rules",
      "starting_at": "2023-01-01T00:00:00Z",  // ISO 8601 format
      "teams": [1, 2, 3]  // Team IDs
    }
    ```

- **Update Tournament**
  - Endpoint: `PUT /tournaments/{tournament_id}/`
  - Description: Update an existing tournament.
  - Request Body:
    ```json
    {
      "title": "Updated Tournament Title",
      "description": "Updated Tournament Description",
      "rewards": "Updated Tournament Rewards",
      "rules": "Updated Tournament Rules",
      "starting_at": "2023-02-01T00:00:00Z",  // ISO 8601 format
      "teams": [4, 5, 6]  // Updated Team IDs
    }
    ```

- **Add Team to Tournament**
  - Endpoint: `POST /tournaments/{tournament_id}/add_team/`
  - Description: Add a team to an existing tournament.
  - Request Body:
    ```json
    {
      "name": "New Team Name",
      "player1": 7,  // Player ID
      "player2": 8,  // Player ID
      "player3": 9   // Player ID
    }
    ```

- **Retrieve Tournament**
  - Endpoint: `GET /tournaments/{tournament_id}/`
  - Description: Retrieve details of a specific tournament.

- **Partial Update Tournament**
  - Endpoint: `PATCH /tournaments/{tournament_id}/`
  - Description: Partially update an existing tournament.
  - Request Body:
    ```json
    {
      "title": "Updated Tournament Title"
    }
    ```

- **Delete Tournament**
  - Endpoint: `DELETE /tournaments/{tournament_id}/`
  - Description: Delete an existing tournament.

- **Accept Team in Tournament**
  - Endpoint: `POST /tournaments/accept_team/{team_id}/`
  - Description: Accept a team into a tournament.

Note: Replace `{player_id}`, `{team_id}`, and `{tournament_id}` with the corresponding IDs in the URLs. The date format for `starting_at` is ISO 8601.


## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.
